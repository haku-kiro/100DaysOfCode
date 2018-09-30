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
        # Should create an instance of the dal in the ctor

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

    def AddFields(self):
        """
        Method to add the field to the entity
        Currently just adds all the fields in the self object
        """
        dal = DAL.DAL()

        for field in self._fields:
            try:
                prefix = field._name[0: field._name.index('_')]
            except:
                logger.InfoMessage(f"Could not create field: {field._name}")
                continue
            tableQuery = f"SELECT Bord_Caption FROM dbo.Custom_Tables WHERE Bord_Prefix = '{prefix}'"
            dfTableName = dal.Reader(tableQuery)
            tableName = dfTableName.iloc[0,:][0]

            # Check to see if the field exists in the table already
            existsQuery = f"SELECT TOP 1 {field._name} FROM dbo.{tableName} WITH(NOLOCK)"
            existCheck = dal.Reader(existsQuery)
            if existCheck != None:
                logger.InfoMessage(f"This field exists already: {field._name}")
                continue
            
            # check the type, based on type create that field
            # Oh no, there is no switch/case in python...
            if field._type.upper() == 'text':
                # alter the table, adding the field with the correct size and type

                # Add the record to the custom_captions and custom_edits tables for this record... too tired... can't go on ... did other, more fun ,things ...

            


    def ListFields(self):
        """
        Method to check what is going to be added
        """
        for field in self._fields:
            print(field._name)


# unit tests:

if __name__ == "__main__":
    actions = SageActions()
    for x in actions._fields:
        print(x._name)