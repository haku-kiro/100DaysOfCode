using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


/// <summary>
/// The code is taken from https://docs.microsoft.com/en-us/dotnet/standard/attributes/writing-custom-attributes#declaring-properties
/// The point is to add meta data to your class to show the developer for that item
/// </summary>
namespace AttributesTest.Attributes
{

    class DeveloperAttribute : Attribute
    {
        private string name;
        private string level;
        private bool reviewed;

        public DeveloperAttribute(string name, string level)
        {
            this.name = name;
            this.level = level;
            this.Reviewed = false;
        }

        //read only for the name
        public string Name
        {
            get
            {
                return name;
            }
        }

        //Read only for the level
        //btw, this is the same as the above
        public virtual string Level => level;


        //Make the reviewd read/write
        public virtual bool Reviewed
        {
            get
            {
                return reviewed;
            }
            set
            {
                reviewed = value;
            }
        }


    }
}
