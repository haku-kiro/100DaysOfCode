using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


/// <summary>
/// This class shows how to create a custom attribute
/// </summary>
namespace AttributesTest.Attributes
{
    //Class needs to inherit the attribute class
    //Note, if using vs there is an attribute snippet

    [AttributeUsage(AttributeTargets.All)] // When set, allows your attrib to be applied to All (Mouse over for a better list)
    class CustomAttribute : Attribute
    {
        public string  SomeHelpText { get; set; }
    }
}
