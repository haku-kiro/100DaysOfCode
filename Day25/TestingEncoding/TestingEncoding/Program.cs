using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.RegularExpressions;

namespace TestingEncoding
{
    class Program
    {
        static void Main(string[] args)
        {
            //Converting a byte array to a string 
            var testVal = Convert.ToBase64String(Encoding.ASCII.GetBytes("TestUserName" + ":" + "testPassword"));
            //Just the bytes
            var encoding = Encoding.ASCII.GetBytes("TestUserName" + ":" + "testPassword");
            Console.WriteLine(testVal);
            
            StringBuilder sbByteData = new StringBuilder();
            StringBuilder sbTextData = new StringBuilder();

            //Should use a stringbuilder (x2)
            foreach (var x in encoding)
            {
                sbByteData.Append(x + " "); //Adding a space to make readable 
                sbTextData.Append(Convert.ToChar(x));
            }
            Console.WriteLine($"The byteString: {sbByteData.ToString()}");
            Console.WriteLine($"The text string: {sbTextData.ToString()}");


            //Path to an image: 
            string imageLoc = @"C:\Users\mdjco\Pictures\Hroni5I.jpg";
            byte[] imageData = File.ReadAllBytes(imageLoc);
            Console.WriteLine(imageData.Length);

            //Kind of makes the image look weird
            //for (var x = 0; x < imageData.Length; x++)
            //{
            //    if (imageData[x] == 101)
            //    {
            //        imageData[x] = 102;
            //    }
            //}

            //Creating a new array to hold the image and the username password
            byte[] bothArrays = new byte[encoding.Length + imageData.Length];

            //We copy from 0 to the length of the first array
            Array.Copy(imageData, bothArrays, imageData.Length);

            //Now we need to copy from the length of the first array to the end
            Array.Copy(encoding, 0, bothArrays, imageData.Length, encoding.Length);
            File.WriteAllBytes("testImage.jpg", bothArrays); //Image now has the password?

            byte[] newImageData = File.ReadAllBytes("./testImage.jpg");
            Console.WriteLine(newImageData.Length); // So we can see a size difference (25)

            //Try to brute force it ? 
            StringBuilder sbData = new StringBuilder();
            foreach (var x in newImageData)
            {
                sbData.Append(Convert.ToChar(x));
            }

            string resultingData = sbData.ToString();
            Console.WriteLine(resultingData);//This is going to be huge... lets see if we can see paterns as well :P (Like words)
            //We can kind of see the data at the bottom, but if it was inserted at a random point - how would we find it ?

            //Lets try regex
            Regex pattern = new Regex(@"[A-z]{4,}");
            var matches = pattern.Matches(resultingData);
            foreach (var x in matches)
            {
                Console.WriteLine(x.ToString());
            }

            Console.WriteLine(matches.Count); //Amount of potential 'words'

            //Reading in a text file of words - checking to see if any of the matches are a word:
            string dictFilePath = @"c:\Users\mdjco\Desktop\100DaysOfCode\Day25\list.txt";
            string[] dictData = File.ReadAllLines(dictFilePath);
            foreach (var x in matches) //Each word
            {
                if (dictData.Contains(x.ToString())) //if the match is in the dict:
                    Console.WriteLine($"A Match!! : {x.ToString()}"); //Doing it like this bec there is so much shit in the console... :D
            }

            //Holy shit, the word busy was in that image :/ Pretty cool stuff :P
            //I have added the 'words' 'TestUserName' and 'testPassword' to list.txt just to have more matches (And the point, really, is to find those 'words')

            //mrl
            Console.WriteLine("Done");
            Console.ReadLine();
        }
    }
}
