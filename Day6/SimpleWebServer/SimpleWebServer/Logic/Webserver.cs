using System;
using System.Net;
using System.Threading;
using System.Linq;
using System.Text;

namespace SimpleWebServer.Logic
{
    class Webserver
    {
        private readonly HttpListener _listener = new HttpListener();
        private readonly Func<HttpListenerRequest, string> _responderMethod;

        public Webserver(string[] prefixes, Func<HttpListenerRequest, string> method)
        {
            if (!HttpListener.IsSupported)
                throw new NotSupportedException("Needs Windows XP SP2, Server 2003 or later.");

            //Method is required.
            _responderMethod = method ?? throw new ArgumentException("Method");

            //Url prefixes are required
            if (prefixes == null || prefixes.Length == 0)
                throw new ArgumentException("Prefixes");

            foreach (string s in prefixes)
                _listener.Prefixes.Add(s);

            
            _listener.Start();
        }

        public Webserver(Func<HttpListenerRequest, string> method, params string[] prefixes)
            : this(prefixes, method) { }

        public void Run()
        {
            ThreadPool.QueueUserWorkItem((o) =>
            {
                Console.WriteLine("Server is running");
                try
                {
                    while (_listener.IsListening)
                    {
                        ThreadPool.QueueUserWorkItem((c) =>
                        {
                            var ctx = c as HttpListenerContext;
                            try
                            {
                                string rstr = _responderMethod(ctx.Request);
                                byte[] buf = Encoding.UTF8.GetBytes(rstr);
                                ctx.Response.ContentLength64 = buf.Length;
                                ctx.Response.OutputStream.Write(buf, 0, buf.Length);
                            }
                            catch { } //Suppress any exceptions
                            finally
                            {
                                //Always close the stream
                                ctx.Response.OutputStream.Close();
                            }
                        }, _listener.GetContext());
                    }
                } catch { } //Suppress any exceptions
            });
        }

        public void Stop()
        {
            _listener.Stop();
            _listener.Close();
        }
    }
}
