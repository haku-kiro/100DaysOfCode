using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Reflection;

namespace ReflectionTests.Examples
{
    public static class SettingAFieldWithReflection
    {
        public static int _field; // Has to be public ?

        public static void SettingField()
        {
            //Instead of:
            //_field = 123;

            FieldInfo info = typeof(SettingAFieldWithReflection).GetField("_field");

            //Set the value
            info.SetValue(null, 42);
            //Log output
            Console.WriteLine(_field);
        }

    }
}
