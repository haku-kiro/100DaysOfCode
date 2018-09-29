# Notes

## TSQL

- I already have some stuff on working with a tsql db somewhere
  - Snippet:

```Python

# Where the CONN_STRING =  "Driver={SQL Server Native Client 11.0};Server=server_address;Database=db_name;uid=SA;pwd=******"
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

# example use:
test = DAL()
result = test.Reader("SELECT TOP 1 * FROM dbo.opportunity WITH(NOLOCK)")

```

## other

- To work with postgress, mysql, or even sqllite, you could use SQLAlchemy

```Python

# to work with sqlalchemy, the db has to be hosted ? or running (I want it embeded - so I have to use sqlite )

# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

```

## Importing data from sqlite db, and storing in a dframe

```Python

# Note, you should do this in a with construct - just to make sure that you close the file afterwards

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection: con
con = engine.connect() # the with construct should go on the conn

# Perform query: rs
rs = con.execute('SELECT * FROM Album')

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys() # to give the df the correct columns

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())


##### An example of using the with construct is: 

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('SELECT LastName, Title FROM Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())


```

## Running queries using pandas

```Python

# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine) # note, doesn't take a connection, takes the engine

# The nice thing is that you don't have to add the columns to the df (df.columns = rs.keys())
# Print head of DataFrame
print(df.head())

```

