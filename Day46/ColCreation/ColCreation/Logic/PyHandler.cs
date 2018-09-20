using IronPython.Hosting;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ColCreation.Extensions;
using Microsoft.Scripting.Hosting;

/// <summary>
/// Calls our python code
/// </summary>
namespace ColCreation.Logic
{
    /// <summary>
    /// TODO: Make generic
    /// </summary>
    class PyHandler
    {

        /// <summary>
        /// Returns a dynamic object with the field data
        /// </summary>
        /// <param name="csvPath"></param>
        /// <returns></returns>
        public dynamic ReturnFieldsData(string csvPath)
        {
            var engine = Python.CreateEngine();
            var scope = engine.CreateScope();

            scope.SetVariable("path", csvPath);

            var pythonFile = ScriptResource.ReadingData;
            string code = pythonFile.CodeFromArray();
            ScriptSource source = engine.CreateScriptSourceFromString(code); //Technically hardcoded - TODO: write a more generic method 

            Object result = source.Execute(scope); //No need to handle the result, make sure to add the scope to your execution

            return scope.GetVariable<dynamic>("colsToBeCreated");
        }
    }
}
