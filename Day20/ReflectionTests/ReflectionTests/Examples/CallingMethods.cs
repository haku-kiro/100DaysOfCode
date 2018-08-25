using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;

namespace ReflectionTests.Examples
{
    class CallingMethods
    {
        //Define a list of params (For when calling)
        public static string[] parameters = new string[] { "Michael", "Not Michael" };

        public static void Inform(string param)
        {
            Console.WriteLine($"The value passed: {param}");
        }


        //reflection based methods
        public static void MethodCaller()
        {
            //Name of the method we want to call
            string name = "Inform";

            //Get the method info
            Type type = typeof(CallingMethods);
            MethodInfo info = type.GetMethod(name); //finds the method with the name passed

            //Loop over and call method with each param
            foreach (string parm in parameters)
            {
                //The first argument is null because the method is static (You don't have to create an instance of a class) so you pass null.
                info.Invoke(null, new object[] { parm });
            }
        }

        //Note, this method is not static (Have to create an instance - meaning when you invoke you have to pass an instance)
        public void Message(string parm)
        {
            Console.WriteLine($"You passed this value: {parm}");
        }

        //Making the caller static though
        public static void Caller()
        {
            //Create an instance
            CallingMethods methods = new CallingMethods();

            //Get the method info for all the methods in the class:
            MethodInfo[] info = typeof(CallingMethods).GetMethods();

            //The methods:
            foreach (var x in info)
            {
                Console.WriteLine(x.Name);

                if (x.Name == "Message")
                    foreach (var y in parameters)
                        x.Invoke(methods, new object[] { y }); // call the method with each string in parameters
            }
        }
    }
}
