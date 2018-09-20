using System;
using System.Collections.Generic;
using System.Text;
using ColCreation.DataObjects;
using ColCreation.Logic;

/// <summary>
/// Class file for Extension methods
/// </summary>
namespace ColCreation.Extensions
{
    public static class Extensions
    {
        /// <summary>
        /// takes in a pyfile byte array and returns the string value,
        /// NOTE: Have to remove the first 3 chars because of encoding - I think?
        /// </summary>
        /// <param name="pyfile"></param>
        /// <returns></returns>
        public static string CodeFromArray(this byte[] pyfile)
        {
            StringBuilder sbCodeBlock = new StringBuilder();
            foreach (var x in pyfile)
            {
                sbCodeBlock.Append(Convert.ToChar(x));
            }

            return sbCodeBlock.ToString().Substring(3); //removing the weird chars in the front
        }


        /// <summary>
        /// Method to convert the dynamic result from the py handler to a list of fields 
        /// NOTE: Any field changes need to be added here as well ... hence, point defeated
        /// Also, you can't have an extension method on a dynamic type - would be cool though
        /// </summary>
        /// <param name="pyResult"></param>
        /// <returns></returns>
        public static List<FieldData> TryGetData(dynamic pyResult)
        {

            List<FieldData> data = new List<FieldData>();
            //This kind of defeats the point
            try
            {
                foreach (var item in pyResult)
                {
                    if (item._name == "fieldname")
                        continue; // This would be header row (Assuming struct is kept)

                    var field = new FieldData()
                    {
                        Fieldname = item._name,
                        FieldType = item._type,
                        Size = item._size,
                        Caption = item._caption,
                        AllowNulls = item._nullable
                    };

                    data.Add(field);
                }
            }
            catch (Exception ex)
            {
                Logging.LogMessage("Error occured when trying to get dynamic data");
                Logging.LogMessage(ex.StackTrace);
                Logging.LogMessage(ex.Message);
            }

            return data;
        }
    }
}