using System;
using System.Collections.Generic;
using System.Dynamic; //NB
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// This example creates a dictionary like datastructure that holds the dynamic type
/// </summary>
namespace WorkingWithDynamicTypesAndUnmanagedCode.Examples
{
    //Inherit the dynamic object class
    class DynamicDictionary : DynamicObject
    {
        Dictionary<string, object> dictionary = new Dictionary<string, object>();

        //This prop returns the number of elements in the inner dict
        public int Count
        {
            get
            {
                return dictionary.Count;
            }
        }

        //If you try to get the value of a prop not defined by the class, this method is called (Working with dynamic this is important)
        public override bool TryGetMember(GetMemberBinder binder, out object result)
        {
            // Converting the name to lowercase so that property names become case-insensitive
            string name = binder.Name.ToLower(); // binder being the prop you are accessing ? 

            // if the prop is found in the dict, set the result param to the prop value and return true
            //obv throws false if the value doesn't exist
            
            //Need to handle this better

            bool res = dictionary.TryGetValue(name, out result);

            //Using nameof would return name, not the content of the variable mike... 
            Console.WriteLine(res ? $"There was a member called: '{name}'": $"The member: '{name}' does not exist - try adding it :)");

            return res;
        }

        //You can handle the setting of a value as well
        public override bool TrySetMember(SetMemberBinder binder, object value) //sig is different, trying to set a `value` now not return a `result`
        {
            dictionary[binder.Name.ToLower()] = value; //setting the key (prop accessing) to the value passed

            //you can always add a value to a dict (Just keep in mind when not using a dict as the backing store/ or anything really - this overload would be important)
            return true;
        }

        /// <summary>
        /// Default for trying to  invoke a method of this class
        /// </summary>
        /// <param name="binder"></param>
        /// <param name="args"></param>
        /// <param name="result"></param>
        /// <returns></returns>
        public override bool TryInvokeMember(InvokeMemberBinder binder, object[] args, out object result)
        {
            //This would be really cool, look into
            Console.WriteLine("You called a method that doesn't exist");
            result = "Method called doesn't exist";
            return true; // based of this throws an error
        }

        //Using the above in the main of the conosle app
    }
}
