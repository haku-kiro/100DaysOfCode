using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;

namespace ReflectionTests.Examples
{
    class ReflectionOnProps
    {
        public int Awesome { get; set; }
        public string Perls { get; set; }

        public static void Proper()
        {
            //Creating an instance of the class
            ReflectionOnProps props = new ReflectionOnProps()
            {
                Awesome = 42,
                Perls = "fourty-two"
            };

            //Get the type
            Type type = typeof(ReflectionOnProps);

            //iterate over the props
            foreach (PropertyInfo propertyInfo in type.GetProperties())
            {
                //Get the name 
                string name = propertyInfo.Name;

                //Get the value 
                object value = propertyInfo.GetValue(props, null);

                //Check type 
                if (value is int)
                {
                    Console.WriteLine($"Int- {name} : {value}");
                }
                else if (value is string)
                {
                    Console.WriteLine($"String- {name} : {value}");
                }
            }
        }
    }
}
