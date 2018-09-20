using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ColCreation.Logic;
using ColCreation.Extensions;
using ColCreation.DataObjects;
using ColCreation.GenericDAL;

namespace ColCreation
{
    class Program
    {
        static void Main(string[] args)
        {
            string pathToCsv = @"c:\Users\mdjco\Documents\Visual Studio 2017\Projects\IronPythonTest\IronPythonTest\RandomFiles\spreadsheetdata.csv";

            PyHandler handler = new PyHandler();
            var fieldData = handler.ReturnFieldsData(pathToCsv);

            foreach (var item in fieldData)
            {
                Console.WriteLine($"Test string: {item._name} {item._type} {item._size} {item._caption} {item._nullable}");
            }


            List<FieldData> concreteObjects = Extensions.Extensions.TryGetData(fieldData);

            foreach (var item in concreteObjects)
            {
                Console.WriteLine($"Concreate tests: {item.Fieldname} {item.FieldType} {item.Caption} {item.Size} {item.AllowNulls}");
            }

            SQL sql = new SQL();
            Console.WriteLine(sql.Connection);

            //Exists
            //sql.NonReader("CREATE TABLE NotTemp ( fieldname varchar(100))");


            var recData = sql.Reader($@"SELECT TOP 10 *
FROM dbo.Cases WITH(NOLOCK)
");

            Console.WriteLine(recData.FieldValue("Case_Description"));

            //MRL
            Console.ReadLine();
        }
    }
}
