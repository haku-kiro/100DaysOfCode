using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WorkingWithDynamicTypesAndUnmanagedCode.Examples;

namespace WorkingWithDynamicTypesAndUnmanagedCode
{
    class Program
    {
        static void Main(string[] args)
        {
            //Part of the examples code:
            dynamic dict = new DynamicDictionary(); //Contains a dict

            //Adding a new prop, calls the TrySetMember method (Dict, returns a bool - so true)
            dict.FirstName = "Michael"; //Note, the definition has to be of dynamic type (Simply creating an instance of the class created will not work)
            dict.LastName = "Da Costa";

            //If we try to get a value, the TryGetMember method is called 
            Console.WriteLine(dict.FirsTNaMe); // note, doesn't check - dynamic - that is why it is a good idea to code for setting to lower on the TryGetMember override
            //Bec the above exists, prints the first name

            // the TryGetMemeber method returns a bool as well, so we can check on it (Well, sort of)
            try
            {
                Console.WriteLine(dict.FirstThing); // Still going to throw an error
            }
            catch 
            {
                //Silent surpress to check if valid
            }

            //We can call the the count prop bec it is defined in the class without it calling the TryGetMember method 
            Console.WriteLine($"The amount of props in the class: {dict.Count}"); //returns the amount of props in the dict

            //Calling a method that doesn't exist
            dict.methodThatDoesntExist(); //Note, if the TryInvokeMember returns false, this throws an error, otherwise you can use it to log method/member (for other overloads) not found

            ///
            ///The dynamic type is pretty cool, you can create an instance of the DynamicObject class in c# and then pass it to an IronPython function
            ///Should really read into this.
            ///

            //Read a docx file:
            string path = @"C:\Users\mdjco\Desktop\Work\testDoc.docx";
            WorkingWithWord.readDoc(path);

            //TODO: Iron python thing

            //MRL
            Console.ReadLine();
        }
    }
}
