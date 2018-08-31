using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AsyncAwaitExamples.Examples;

namespace AsyncAwaitExamples
{
    class Program
    {
        static void Main(string[] args)
        {
            HandleFileAsync.FileCall();

            //Mrl
            Console.WriteLine("Done");
            Console.ReadLine();
        }
    }
}
