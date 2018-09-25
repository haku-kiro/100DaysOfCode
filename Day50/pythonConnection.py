## connecting to a mssql server using python

import pyodbc
import pandas as pd

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};Server=41.180.14.74,64999;Database=CRMDEV;uid=SA;pwd=a$t3ch123")

df = pd.read_sql_query("SELECT CuVi_ViewScript FROM dbo.Custom_Views", cnxn)
print(df)

