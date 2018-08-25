using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;
using ReflectionTests.Examples;

namespace ReflectionTests
{
    class Program
    {
        static void Main(string[] args)
        {
            //Getting fields:
            FieldInfoExample.Height = 100;
            FieldInfoExample.Name = "Test name";
            FieldInfoExample.Width = 123;
            FieldInfoExample.Weight = 42;
            FieldInfoExample.Write();

            //Setting fields:
            SettingAFieldWithReflection.SettingField();

            //Calling methods:
            CallingMethods.MethodCaller();
            CallingMethods.Caller(); //Even picks up the inherited methods


            //Getting props:
            ReflectionOnProps.Proper();



            //MRL
            Console.ReadLine();
        }
    }
}
