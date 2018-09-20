using ColCreation.Logic;
using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/// <summary>
/// Used for querying a db
/// </summary>
namespace ColCreation.GenericDAL
{
    /// <summary>
    /// Generic DAL,
    /// Doesn't/won't have record functionality
    /// </summary>
    class SQL
    {
        public string Connection { get; set; }

        public SQL()
        {
            Connection = ConfigurationManager.ConnectionStrings["Test"].ConnectionString;
        }


        /// <summary>
        /// Very basic implementation, no record functionality
        /// Do you need to have a dataset return type instead as your select my join multiple tables ?
        /// </summary>
        /// <param name="query"></param>
        public DataTable Reader(string query)
        {
            //Create Data Table
            DataTable table = new DataTable();

            try
            {
                using (SqlConnection conn = new SqlConnection(Connection))
                {
                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        conn.Open();
                        table.Load(cmd.ExecuteReader());
                        return table;
                    }
                }
            }
            catch (Exception ex)
            {
                Logging.LogMessage("Reader Failed!");
                Logging.LogMessage(ex.Message);
                Logging.LogMessage(ex.StackTrace);
                throw new Exception("Handle me"); //silent log other instances
            }
        }


        public int NonReader(string query)
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(Connection))
                {
                    using (SqlCommand cmd = new SqlCommand(query, conn))
                    {
                        conn.Open();
                        return cmd.ExecuteNonQuery();
                    }
                }
            }
            catch (Exception ex)
            {
                Logging.LogMessage("NonReader Failed!");
                Logging.LogMessage(ex.Message);
                Logging.LogMessage(ex.StackTrace);
                throw new Exception("Handle me"); //silent log other instances
            }
        }
    }

    public static class SQLExtensions
    {
        /// <summary>
        /// Extension method to return the value of the col passed
        /// </summary>
        /// <param name="dt"></param>
        /// <returns></returns>
        public static string FieldValue(this DataTable dt, string field)
        {
            var reader = dt.CreateDataReader();
            int ord = 0;

            try
            {
                //wow ms, wow
                ord = reader.GetOrdinal(field);
            }
            catch (Exception ex)
            {
                //Field does not exist
                Logging.LogMessage(ex.Message);
                Logging.LogMessage(ex.StackTrace);
                throw;
            }
            return reader.GetString(ord);
        }
    }
}
