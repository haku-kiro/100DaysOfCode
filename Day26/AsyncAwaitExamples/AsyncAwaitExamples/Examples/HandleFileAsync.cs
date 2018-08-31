using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace AsyncAwaitExamples.Examples
{
    class HandleFileAsync
    {

        /// <summary>
        /// Just a test method to describe the process that occur through the life span of an async await method
        /// </summary>
        public static void FileCall()
        {

            //We call the method
            Task<int> task = FileAsync();

            //Control returns here before the above is done
            Console.WriteLine("Please wait while the file is processed...");

            //Other things can be done while the file is being read
            Console.Write("Enter text: ");
            string line = Console.ReadLine();
            Console.WriteLine($"You entered: {line}");

            //If you need to, you can wait for the task to end:
            task.Wait();
            //Assign the result of the task to a var
            int x = task.Result;
            Console.WriteLine($"The count variable: {x}");
        }

        static async Task<int> FileAsync()
        {
            string filePath = @"./testFile.txt";
            Console.WriteLine("In file async method");

            int Count = 0;

            //Reading the file, but using the async file reader
            using (StreamReader sr = new StreamReader(filePath))
            {
                //Read the data await (needs a matching async)
                string data = await sr.ReadToEndAsync(); //The method has to be awaitable to be used in async await

                //Process the file somehow
                Count += data.Length;

                //Slow running computation, some dummy code
                for (var x = 0; x < 10000; x++)
                {
                    int i = data.GetHashCode();
                    if (i == 0)
                    {
                        Count--; //waits to read the file?
                    }
                }
            }

            Console.WriteLine("The file has been read");
            return Count;
        }
    }
}
