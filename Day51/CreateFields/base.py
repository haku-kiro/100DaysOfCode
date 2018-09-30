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