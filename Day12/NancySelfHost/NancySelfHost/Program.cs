using System;
using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Nancy;
using Nancy.Hosting.Self;

namespace NancySelfHost
{
    public class Item
    {
        public int Key { get; set; }
        public string Data { get; set; }
        public string MoreData { get; set; }
    }

    public class ApiClassFile : NancyModule
    {
        public ApiClassFile()
        {

            //To allow cors
            After.AddItemToEndOfPipeline((ctx) =>
            {
                ctx.Response.WithHeader("Access-Control-Allow-Origin", "*")
                    .WithHeader("Access-Control-Allow-Methods", "POST,GET")
                    .WithHeader("Access-Control-Allow-Headers", "Accept, Origin, Content-type");

            });


            Get["/api/thing/{val}"] = x => method(x);
            Get["/api/thing"] = x => anotherMethod(x);

        }

        //return a list of things, as a json objec
        private dynamic anotherMethod(dynamic x)
        {
            List<Item> items = new List<Item>();
            int init = 1;

            Console.WriteLine("Request recieved");

            while (init <= 100)
            {
                items.Add(new Item() { Key = init, Data = $"someData {init * 3}", MoreData = $"just some more {123- init}"});
                init++;
            }

            return Response.AsJson(items);
        }

        dynamic method(dynamic x)
        {
            string valuePassed = x.val.ToString();
            Console.WriteLine(valuePassed);

            Hashtable hash = new Hashtable();
            hash.Add("Data", valuePassed);

            return Response.AsJson(new
                    {    data = valuePassed,
                         statusCode = HttpStatusCode.OK
                    }); //json like object
        }
    }


    /// <summary>
    /// Just to show how to self host with nancy
    /// </summary>
    class Program 
    {
        static void Main(string[] args)
        {
            using (var host = new NancyHost(new Uri("http://localhost:1020")))
            {
                host.Start();
                Console.WriteLine("Running on localhost:1020");
                Console.ReadLine();
            }

        }
    }
}
