using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using SimpleWebServer.ServerMethods;

/// <summary>
/// Code taken from:
/// https://codehosting.net/blog/BlogEngine/post/Simple-C-Web-Server
/// 
/// TODO, check to see how to make a nancy module run off of this.
/// (Create your own rest api)
/// </summary>
namespace SimpleWebServer
{
    class Program
    {
        static void Main(string[] args)
        {
            string endpoint = "http://localhost:8080/test/";

            Webserver ws = new Webserver(SendResponse, endpoint);
            ws.Run();
            Console.WriteLine($"Simple WebServer, running at: {endpoint} - press any key to stop");
            Console.ReadKey();
            ws.Stop();

            //End goal is to pass method and endpoint here
            //PostServer ps = new PostServer();
            //Console.WriteLine($"Simple WebServer, running - press any key to stop");
            //Console.ReadKey();
        }

        public static string SendResponse(HttpListenerRequest request)
        {
            return string.Format("<HTML><BODY>My web page.<br>{0}</BODY></HTML>", DateTime.Now);
        }

        #region I know, just making neater
        //Just a cool side note, the params makes the array string able
        public static void thingTest(params string[] strings)
        {
            foreach (string s in strings)
                Console.WriteLine(s);
        } 
        #endregion
    }
}
