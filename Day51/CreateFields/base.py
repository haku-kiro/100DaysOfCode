import logger 
import DAL
import pandas as pd
import fileLoader
import CRMActions as Actions

# Just showing how to use the logger
# logger.InfoMessage("This is a test message")

# can write queries (work on your naming ...) 
# dal = DAL.DAL()
# oppo_df = dal.Reader("SELECT TOP 100 * FROM dbo.opportunity WITH(NOLOCK)")

# rowcount = dal.NonReader("DROP TABLE #temp")

# print(rowcount)


# Creating an instance of the loader
# Example use of the loader
# loader = fileLoader.ColLoader()
# columns = loader._cols

# for x in columns:
#     print(x._name)

act = Actions.SageActions()
act.AddFields()

# dal = DAL.DAL()

# tableQuery = f"SELECT Bord_Caption, Bord_tableid FROM dbo.Custom_Tables WHERE bord_caption = 'cases'"
# dfTableName = dal.Reader(tableQuery)
# tableName = dfTableName.iloc[0,:][0]
# tableId = dfTableName.iloc[0,:][1]
# print(f"the table id is : {tableId}")
# print(f"the table name is : {tableName}")


# dfTables = dal.Reader("SELECT bord_caption, bord_prefix, bord_IdField FROM dbo.custom_tables")



# success = 0
# fail = 0

# print(dfTables.values[0][0])

# # for table, prefix, idfield in dfTables.values:
# #     try:
# #         dftemp = dal.Reader(f"SELECT TOP 1 {prefix}_description FROM dbo.{table}")
# #         thing = dftemp.iloc[0]
# #         success += 1
# #     except:
# #         fail += 1
# #         continue
# # print(f"Success: {success}")
# # print(f"Fail: {fail}")


