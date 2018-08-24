using System;
using Microsoft.Office.Interop.Word; //Look for the application (When adding the reference - like `word`)

namespace WorkingWithDynamicTypesAndUnmanagedCode.Examples
{
    static class WorkingWithWord
    {
        /// <summary>
        /// Takes the path of the doc file and reads it to the console.
        /// </summary>
        /// <param name="docPath"></param>
        public static void readDoc(string docPath)
        {
            //Opening a doc file
            Application thing = new Application();
            Document doc = thing.Documents.Open(docPath);

            //Loops through each word in the document
            int count = doc.Words.Count;
            for (var x = 1; x < count; x ++) // ms word starts the collection at 1 ... wtf ... (In future, debug these issues yourself)
            {
                Console.WriteLine(doc.Words[x].Text); //Also, you can't use the write method instead of the writeline
            }

            //Make sure to close resource:
            thing.Quit();
        }
    }
}
