using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;

namespace ReflectionTests.Examples
{
    public static class FieldInfoExample
    {
        public static int Height;
        public static int Width;
        public static int Weight;
        public static string Name;

        public static void Write()
        {
            //Get the type pointer (Pretty important for basic reflection)
            Type type = typeof(FieldInfoExample);
            //Get all the fields in that type
            FieldInfo[] fields = type.GetFields();
            foreach (var field in fields)
            {
                string name = field.Name; //Return the name of the field
                object temp = field.GetValue(null); //Return the value of the field
                //type checking 
                if (temp is int)
                {
                    int value = (int)temp; //value conversions
                    Console.Write(name);
                    Console.Write($" Has the value of: {value}\n");
                }
                else if (temp is string)
                {
                    string value = temp as string; //ref conversion vs
                    Console.Write(name);
                    Console.Write( $" Has the value of: {value}\n");
                }
            }
        }
    }
}
