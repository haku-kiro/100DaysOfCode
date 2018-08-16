using System;
using System.Collections;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Soap;
using System.Xml;


////
///
///NOTE, Beginning with the .NET Framework 2.0, this class is obsolete. Use BinaryFormatter instead. Instead of using the soap formatter (TODO, test this out)
///
///

/// <summary>
/// This is an example of serializing something with the Serializableattribute
/// using the soapformatter
/// Code from:
/// https://docs.microsoft.com/en-us/dotnet/api/system.serializableattribute?view=netframework-4.7.2
/// And
/// https://docs.microsoft.com/en-us/dotnet/api/system.runtime.serialization.formatters.soap.soapformatter?view=netframework-4.7.2
/// For an example of a binaryformatter, read the article
/// </summary>
namespace SerializationExample
{
    [Serializable()]
    public class TestSimpleObject
    {
        public int member1;
        public string member2;
        public string member3;
        public double member4;

        //A field that is not serialized
        [NonSerialized()]
        public string member5;
        public TestSimpleObject()
        {
            member1 = 11;
            member2 = "hello";
            member3 = "World";
            member4 = 3.14159265;
            member5 = "Hello, world!";
        }

        public void Print()
        {
            Console.WriteLine($"{nameof(member1)} = {member1}");
            Console.WriteLine($"{nameof(member2)} = {member2}");
            Console.WriteLine($"{nameof(member3)} = {member3}");
            Console.WriteLine($"{nameof(member4)} = {member4}");
            Console.WriteLine($"{nameof(member5)} = {member5}");

        }
    }

    
    class Program
    {
        public static void SerializeTestSimpleObject()
        {
            TestSimpleObject obj = new TestSimpleObject();

            //Before serialization the object:
            Console.WriteLine("This is before serialization:");
            obj.Print();

            //Opens a file and serializes the object into it in binary format
            Stream stream = File.Open("data.xml", FileMode.Create);
            SoapFormatter formatter = new SoapFormatter();

            formatter.Serialize(stream, obj);
            stream.Close();

            //Now we empty the obj
            obj = null;

            //Opens the data.xml file and deserializes the object from it
            stream = File.Open("data.xml", FileMode.Open);
            formatter = new SoapFormatter();

            //Deserialize into the obj (Has to be of the type TestSimpleObject)
            obj = (TestSimpleObject)formatter.Deserialize(stream);
            stream.Close();

            Console.WriteLine("\nAfter deserialization the object contains: ");
            obj.Print();

            //Just a quick reminder of what I did yesterday:
            //Not sure how the nodes work in this form, read up on parsing serialized data
            XmlDocument doc = new XmlDocument();
            doc.Load("data.xml");
            XmlNodeList listofnodes = doc.DocumentElement.SelectNodes("//SOAP-ENV/a1");
            foreach (XmlNode node in listofnodes)
            {
                Console.WriteLine(node.InnerText);
            }
        }


        //Soap serialize and deserialize methods:

        public static void Serialize()
        {
            //Creating a hashtable to be serialized
            Hashtable addresses = new Hashtable();
            addresses.Add("Jeff", "123 Main Steet, Redmond, WA 98052");
            addresses.Add("Fred", "987 Pine Road, Phila., PA 19116");
            addresses.Add("Mary", "PO Box 112233, Palo Alto, CA 94301");


            //Create a stream: 
            FileStream fs = new FileStream("DataFile.soap", FileMode.Create);

            SoapFormatter formatter = new SoapFormatter();
            try
            {
                formatter.Serialize(fs, addresses);
            }
            catch (SerializationException ex)
            {
                Console.WriteLine($"Failed to serialize. Reason: {ex.Message}");
                throw;
            }
            finally
            {
                fs.Close();
            }
        }

        public static void Deserialize()
        {
            //Create a hashtable to store the file:
            Hashtable table = null;

            //Open the soap file:
            FileStream fs = new FileStream("DataFile.soap", FileMode.Open);
            try
            {
                SoapFormatter formatter = new SoapFormatter();
                table = (Hashtable)formatter.Deserialize(fs);
            }
            catch (SerializationException ex)
            {
                Console.WriteLine($"Unable to deserialize. Reason: {ex.Message}");
            }
            finally
            {
                fs.Close();
            }

            //Loop over the address to show them:
            foreach (DictionaryEntry entry in table)
            {
                Console.WriteLine($"{entry.Key} Lives at {entry.Value}");
            }
        }

        static void Main(string[] args)
        {

            //SerializeTestSimpleObject();
            Serialize();
            Deserialize();


            //mrl
            Console.ReadLine();
        }
    }
}
