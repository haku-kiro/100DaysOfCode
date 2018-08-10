using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Nancy;

namespace SimpleWebServer.API
{
    class BaseFile : Nancy.NancyModule
    {
        public BaseFile()
        {
            Get["/testpoint"] = data => getData(data);
        }

        private dynamic getData(dynamic data)
        {
            List<string> newList = new List<string>();
            newList.Add("Hello");
            newList.Add("World");
            return Response.AsJson(newList);
        }
    }
}
