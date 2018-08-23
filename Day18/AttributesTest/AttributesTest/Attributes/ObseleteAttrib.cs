using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// This class file shows the use of the obsolete attrib
/// </summary>
namespace AttributesTest.Attributes
{
    class ObseleteAttrib
    {

        [Obsolete("Dont use me.", true)]
        public void OldDoThing()
        {
            Console.WriteLine("Welll... When someone tries to use me, I will break their code");
        }

        [Obsolete("This method is no longer supported, please use NewDoThing() instead")] 
        public void DoThing()
        {
            Console.WriteLine("Doing something");
        }

        public void NewDoThing()
        {
            Console.WriteLine("Doing something, new");
        }

    }
}
