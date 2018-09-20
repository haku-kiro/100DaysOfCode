using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ColCreation.DataObjects
{
    /// <summary>
    /// Data Class for each fields being added
    /// NOTE: Not being used at the moment (Dynamic types - find a way to parse to this at some point though) 
    /// </summary>
    public class FieldData
    {
        public string Fieldname { get; set; }
        public string FieldType { get; set; }
        public string Size { get; set; }
        public string Caption { get; set; }
        public string AllowNulls { get; set; }
    }
}
