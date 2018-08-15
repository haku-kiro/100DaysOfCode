using System;
using System.Xml;


/// <summary>
/// Working with xml use the System.Xml namespace
/// There are two main methods used for reading xml
/// XmlDocument class - loads whole doc into mem, can query with xpath
/// and
/// XmlReader class - run through one elem at a time
/// </summary>
namespace WorkingWithXml
{
    class Program
    {
        /// <summary>
        /// You can use xml readers to read xml from an online source,
        /// using: http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml
        /// 
        /// This example uses the XmlReader class
        /// </summary>
        public static void ReadSomeXmlOnline()
        {
            XmlReader xmlReader = XmlReader.Create("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml");
            while (xmlReader.Read())
            {
                if ((xmlReader.NodeType == XmlNodeType.Element) && (xmlReader.Name == "Cube"))
                {

                    if (xmlReader.HasAttributes)
                    {
                        string time = xmlReader.GetAttribute("time");
                        if (time != null)
                        {
                            Console.WriteLine($"Date : {time}");
                            continue; //This line wont have currency details on it
                        }

                        Console.WriteLine($"{xmlReader.GetAttribute("currency")} : {xmlReader.GetAttribute("rate")}");
                    }
                }
            }
        }

        /// <summary>
        /// Same as before, just using the xmldocument class
        /// </summary>
        public static void ReadSomeXmlOnine2()
        {
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load("http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml");

            //Trying to get the time (Like the first example)
            XmlNode timeNode = xmlDoc.DocumentElement.ChildNodes[2].ChildNodes[0]; //Keep in mind that each "root" node is a container, and that the child nodes would be the first thing in that container 
            string time = timeNode.Attributes["time"].Value;
            Console.WriteLine($"Date : {time}");

            //ALWAYS be explicit in your foreach types
            foreach (XmlNode item in xmlDoc.DocumentElement.ChildNodes[2].ChildNodes[0].ChildNodes)
            {
                Console.WriteLine($"{item.Attributes["currency"].Value} : {item.Attributes["rate"].Value}");
            }
        }
        /// <summary>
        /// This method shows how the xml node class is used/works
        /// 
        /// The node class is used when you parse xml, it would hold each node (See above examples)
        /// There are more props to it though
        /// 
        /// Sorry for creating so many objects...
        /// </summary>
        public static void XmlNodeClass()
        {
            //Name prop
            XmlDocument xmlDocument = new XmlDocument();
            xmlDocument.LoadXml("<user name=\"John Doe\">A user node</user>");
            Console.WriteLine(xmlDocument.DocumentElement.Name); //Note, DocumentElement is the type XmlElement, which inherits from the XmlNode

            //Inner text prop
            XmlDocument xmlDocument2 = new XmlDocument();
            xmlDocument2.LoadXml("<test>InnerText is here</test>");
            Console.WriteLine(xmlDocument2.DocumentElement.InnerText);


            //Inner xml and inner text prop
            XmlDocument xmlDocument3 = new XmlDocument();
            xmlDocument3.LoadXml("<users><user>InnerText/InnerXml is here</user></users>");
            Console.WriteLine($"Inner text: {xmlDocument3.DocumentElement.InnerText}");
            Console.WriteLine($"Inner xml: {xmlDocument3.DocumentElement.InnerXml}");

            //Outer xml prop
            XmlDocument xmlDocument4 = new XmlDocument();
            xmlDocument4.LoadXml("<users><user>InnerText/InnerXml is here</user></users>");
            Console.WriteLine($"inner xml: {xmlDocument4.DocumentElement.InnerXml}");
            Console.WriteLine($"outer xml: {xmlDocument4.DocumentElement.OuterXml}");

            //Outer when outer is the only node
            XmlDocument xml = new XmlDocument();
            xml.LoadXml("<outerelem> This is a test, really</outerelem>");
            Console.WriteLine("Outer test: " + xml.DocumentElement.OuterXml);


            // Working with attributes
            XmlDocument xmlDocument5 = new XmlDocument();
            xmlDocument5.LoadXml("<user name=\"John Doe\" age=\"42\"></user>");
            //Do error checking for exists
            if (xmlDocument5.DocumentElement.Attributes["name"] != null)
            {
                Console.WriteLine(xmlDocument5.DocumentElement.Attributes["name"].Value);
            }
            if (xmlDocument5.DocumentElement.Attributes["age"] != null)
            {
                Console.WriteLine(xmlDocument5.DocumentElement.Attributes["age"].Value);
            }
        }

        //Learn more about xpath, the xml query language
        //XPATH ?


        /// <summary>
        /// The making of a news app, plus the ability to go through rss feeds - which is pretty cool
        /// </summary>
        public static void xpathMethods()
        {
            //Will be using the rss feed: http://rss.cnn.com/rss/edition_world.rss
            //To view the xml format of a rss site, view source... it's essentially xml

            //To go into (using this example) the name of the article: //rss/channel/title
            //This would be the xpath query


            //xpath method: SelectSingleNode
            //Selects the first node that matches the query
            XmlDocument xmlDoc = new XmlDocument();
            xmlDoc.Load("http://rss.cnn.com/rss/edition_world.rss");
            XmlNode titleNode = xmlDoc.SelectSingleNode("//rss/channel/title");
            if (titleNode != null)
                Console.WriteLine(titleNode.InnerText);

            //xpath method: SelectNodes
            //Returns a node list of all the nodes that match your xpath query
            XmlDocument xmlDocument = new XmlDocument();
            xmlDocument.Load("http://rss.cnn.com/rss/edition_world.rss");
            XmlNodeList xmlNodeList = xmlDocument.SelectNodes("//rss/channel/item");
            foreach (XmlNode node in xmlNodeList)
            {
                //Can use the SelectSingleNode to return the single node
                XmlNode aTitleNode = node.SelectSingleNode("title");
                XmlNode aDateNode = node.SelectSingleNode("pubDate");
                if ((aTitleNode != null) && (aDateNode != null))
                    Console.WriteLine($"{aDateNode.InnerText} : {aTitleNode.InnerText}");
                else if (aTitleNode != null)
                    Console.WriteLine($"No date: {aTitleNode.InnerText}"); //Less than ideal outcome
            }


            //If we wanted to use the SelectNodes to return a single node for each instance,
            XmlDocument xmlDocument2 = new XmlDocument();
            xmlDocument2.Load("http://rss.cnn.com/rss/edition_world.rss");
            XmlNodeList listofNodes = xmlDocument2.SelectNodes("//rss/channel/item/title");
            foreach (XmlNode x in listofNodes)
                Console.WriteLine($"Title only: {x.InnerText}");

        }


        static void Main(string[] args)
        {

            //Just an abstraction
            //ReadSomeXmlOnline();

            //ReadSomeXmlOnine2();

            //XmlNodeClass();

            xpathMethods();

            //mrl
            Console.ReadLine();
        }
    }
}
