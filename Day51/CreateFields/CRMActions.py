## Will be used to perform sage crm actions

import fileLoader # to get the fields
import logger
import DAL # for running queries

class SageActions:
    """
    Class to perform actions against the sage db, as well as configure and edit/customize certiain aspects
    """
    def __init__(self):
        """
        Create an instance of SageActions
        """
        self._fields = fileLoader.ColLoader()._cols # fields are instances of the colRow class

    def MetadataRefresh(self):
        """
        Method to perfom a views metadata refresh
        """
        dal = DAL.DAL()
        # Need to drop vSentinal
        dal.NonReader("DROP VIEW vSentinel")

        # Drop each view, and recreate them
        CreateViews = dal.Reader(
            """SELECT CuVi_ViewID, CuVi_ViewName, CuVi_ViewScript
FROM dbo.Custom_Views WITH(NOLOCK)
ORDER BY 1 """)

        DropViews = dal.Reader(
            """
            SELECT CuVi_ViewID, CuVi_ViewName, CuVi_ViewScript
FROM dbo.Custom_Views WITH(NOLOCK)
ORDER BY 1 DESC
            """
        )

        # dropping the views
        for view in range(len(DropViews)):
            # print(views.loc[view]["CuVi_ViewName"]) # I'm sure there's an easier way... but for now, this should be fine
            # drop each view
            viewName = DropViews.loc[view]["CuVi_ViewName"]
            dal.NonReader(f"DROP VIEW {viewName}") # Need to drop without dependencies...
        
        # Have to run this until there are no errors (Some views depened on other views ... Silly, I know - or just order by created date ?)
        for view in range(len(CreateViews)):
            viewScript = CreateViews.loc[view]["CuVi_ViewScript"]
            dal.NonReader(viewScript) 



# unit tests:

if __name__ == "__main__":
    actions = SageActions()
    for x in actions._fields:
        print(x._name)

    actions.MetadataRefresh()