using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using System.Threading.Tasks;

namespace SimpleWebServer.Callers
{
    /// <summary>
    /// //Need methods to do a GET call as well as a POST call
    /// </summary>
    public static class ApiCallers
    {
        /// <summary>
        /// Simple GET call, doesn't handle the response, just returns it
        /// </summary>
        /// <param name="endpoint"></param>
        /// <returns></returns>
        public static async Task<string> GetCall(string endpoint)
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    Task<string> CallTask = Task.Run(() =>
                    {
                        return client.GetStringAsync(endpoint);
                    });
                    return await CallTask;
                }
            }
            catch (Exception ex)
            {
                //TODO: Logging
                Debug.WriteLine(ex.Message);
                Debug.WriteLine(ex.StackTrace);
                throw;
            }
        }

        /// <summary>
        /// Simple post call, doesn't handle the response, just returns it.
        ///
        /// Note: The dictionary is a bit of a mess - Have to use string values for the keys
        /// and the values (Make sure to cast when creating post api endpoints)
        /// </summary>
        /// <param name="endpoint"></param>
        /// <param name="data"></param>
        public static async Task<string> PostCall(string endpoint, Dictionary<string, string> data)
        {
            try
            {
                using (HttpClient client = new HttpClient())
                {
                    var postContent = new FormUrlEncodedContent(data);
                    Task<string> CallTask = Task.Run(() =>
                    {
                        return client.PostAsync(endpoint, postContent)
                                     .Result
                                     .Content
                                     .ReadAsStringAsync();
                    });
                    return await CallTask;
                }
            }
            catch (Exception ex)
            {
                //TODO: Logging
                Debug.WriteLine(ex.Message);
                Debug.WriteLine(ex.StackTrace);
                throw;
            }
        }
    }
}

//Note: Need to look into how to handle cors (in case the browers need the response to perform an action)


///Other caller methods (Just as a reference):
///This is an example post call using jquery
///This would be a post call

///$.ajax({
///    type: "POST",
///  url: "http://localhost:8020",
///  data: { "someKey": "SomeValue"},
///  success: function(data) { alert(data); }
///});

/// Note the alert does not work bec of cors