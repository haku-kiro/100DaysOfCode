using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// To write logfiles
/// </summary>
namespace ColCreation.Logic
{

    /// <summary>
    /// Maybe learn to use nlog/common.logging ...
    /// </summary>
    public static class Logging
    {
        /// <summary>
        /// Log a generic message, for now - going to use to write errors as well as info etc
        /// So Make sure to be explicit in message body
        /// </summary>
        public static void LogMessage(string message)
        {
            try
            {
                //Create the log file if it doesn't exist
                string logPath = AppDomain.CurrentDomain.BaseDirectory + "\\Logs";
                if (!File.Exists(logPath))
                    Directory.CreateDirectory(logPath);

                string path = AppDomain.CurrentDomain.BaseDirectory + "\\Logs\\" + DateTime.Now.ToShortDateString().Replace(" - ", "").Replace("/", "") + ".txt";

                using (StreamWriter sw = new StreamWriter(path, true))
                {
                    sw.WriteLine(message);
                }
            }
            catch 
            {
                Trace.Write("Well this is awkward...");
            }
        }

    }
}
