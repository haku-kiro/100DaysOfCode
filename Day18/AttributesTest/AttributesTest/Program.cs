using AttributesTest.Attributes;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


/// <summary>
/// 
/// </summary>
namespace AttributesTest
{
    //Showing the developer attribute
    [Developer("Michael Da Costa", "42", Reviewed = true)]
    class Program
    {
        [DefaultValue(100)]
        public int ANumber { get; set; }

        [DefaultValue("Test value")]
        public string ThisIsATest { get; set; }

        static void Main(string[] args)
        {
            ObseleteAttrib thing1 = new ObseleteAttrib();

            //This shows that the method is deprecated, use instead: NewDoThing
            thing1.DoThing();

            thing1.NewDoThing();

            //The below wont work at all
            //thing1.OldDoThing();


            //For the Custom attribute example
            Method();
            Method2();


            //Showing how to use the default attrib
            Program program = new Program();
            program.ThisIsATest = "A value"; //Gets overwritten
            //Set the default values of each prop
            program.SetDefaults(); //Can run before and overwrite the values you "have", or you can get creative in the logic of the set defaults to check to see if the prop has a value

            program.ThisIsATest = "Newest value";

            Console.WriteLine(program.ToString());


            GetAttribte(typeof(Program)); //Prints the dev info for the Program class


            //MRL
            Console.ReadLine();
        }

        /// <summary>
        /// Use to show the value of the props after default init
        /// </summary>
        /// <returns></returns>
        public override string ToString()
        {
            return $"The value of ANumber: {this.ANumber} \nThe value of ThisIsATest: {this.ThisIsATest}";
        }

        public void SetDefaults()
        {

            //Made generic in that you could call this in any method and it would set anthing with a default value
            foreach (PropertyDescriptor prop in TypeDescriptor.GetProperties(this))
            {
                DefaultValueAttribute attr = (DefaultValueAttribute)prop.Attributes[typeof(DefaultValueAttribute)];
                if (attr != null)
                {
                    //Set the value of the attr to the value of the prop
                    prop.SetValue(this, attr.Value);
                }
            }
        }

        //Working with the custom attribute you've created
        [CustomAttribute(SomeHelpText = "This is some text to tell you what this method is for...")]
        public static void Method()
        {
            Console.WriteLine("Nothing");
        }

        //Note, you can use the shorthand version of an attribute name (For naming best practise is <Name>Attribute so you can use:)
        [Custom(SomeHelpText ="Some value")]
        public static void Method2()
        {
            Console.WriteLine("More nothing");
        }


        //Using the attribute data //Follow on from the developer class
        /// <summary>
        /// Prints the meta data by pulling the data in the attribute
        /// 
        /// TODO: Look into using the same attribute at multiple levels, accessing the info from it then:
        /// https://docs.microsoft.com/en-us/dotnet/standard/attributes/retrieving-information-stored-in-attributes#retrieving-multiple-instances-of-an-attribute-applied-to-the-same-scope
        /// </summary>
        public static void GetAttribte(Type t)
        {
            DeveloperAttribute attribute = (DeveloperAttribute)Attribute.GetCustomAttribute(t, typeof(DeveloperAttribute));
            if (attribute == null)
                Console.WriteLine("The attribute was not found");
            else
            {
                Console.WriteLine($"\nThe name of the developer: {attribute.Name}");
                Console.WriteLine($"The Developers level: {attribute.Level}");
                Console.WriteLine(attribute.Reviewed ? "This code has been reviewed" : "This code has not been reviewed");
            }
        }
    }
}
