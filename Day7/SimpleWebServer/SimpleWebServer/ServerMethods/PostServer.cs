using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;
using System.Threading.Tasks;


/// <summary>
/// code from:
/// https://www.codeproject.com/Articles/599978/An-HttpListener-Server-for-Handling-AJAX-POST-Requ
/// </summary>
namespace SimpleWebServer.ServerMethods
{
    class PostServer
    {
        static HttpListener listener;
        private Thread listenThread;

        public PostServer()
        {
            listener = new HttpListener();
            listener.Prefixes.Add("http://localhost:8020/");
            listener.AuthenticationSchemes = AuthenticationSchemes.Anonymous;

            listener.Start();
            this.listenThread = new Thread(new ParameterizedThreadStart(startListener));
            listenThread.Start();
        }

        private void startListener(object obj)
        {
            while (true)
            {
                ProcessRequest();
            }
        }

        private void ProcessRequest()
        {
            var result = listener.BeginGetContext(listenerCallback, listener);
            result.AsyncWaitHandle.WaitOne();
        }

        private void listenerCallback(IAsyncResult result)
        {
            //dig into this context object, has http method and some other useful options

            HttpListener _listenHandler = (HttpListener)result.AsyncState;
            var context = _listenHandler.EndGetContext(result);
            var data_text = new StreamReader(context.Request.InputStream, context.Request.ContentEncoding).ReadToEnd();
            var cleaned_data = System.Web.HttpUtility.UrlDecode(data_text);

            context.Response.StatusCode = 200;
            context.Response.StatusDescription = "OK";

            //Look into CORS here


            Console.WriteLine(data_text);
            context.Response.Close();
        }
    }
}
