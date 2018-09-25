import pyodbc
import pandas as pd
import Config as config
import logger

class DAL:
    """
    This class will act as the connection to the db,
    to run queries
    """
    def __init__(self):
        """
        Creating an instance pulls the config connection string and establishes a connection
        """
        self._connection = pyodbc.connect(config.CONN_STRING)

    def Reader(self, query):
        """
        Returns a pandas dataframe after being passed a query, this query is run on the connection that is created when you instantiate the DAL
        """
        try:
            return pd.read_sql_query(query, self._connection)
        except:
            logger.ErrorMessage(f"Failed to run query: {query}")

    def NonReader(self, query):
        """
        Runs non result querys on the connection string that is established when you create an instance
        Returns a row count?
        """
        try:
            cursor = self._connection.cursor()
            cursor.execute(query)
            cursor.commit()
            return cursor.rowcount
        except:
            logger.ErrorMessage(f"Failed to run query: {query}")

if __name__ == "__main__":
    # some random unit tests
    test = DAL()
    result = test.Reader("SELECT TOP 1 * FROM dbo.opportunity WITH(NOLOCK)")
    print(result)
    logger.InfoMessage(f"Creating an instance of DAL, using the connection string: {config.CONN_STRING}")