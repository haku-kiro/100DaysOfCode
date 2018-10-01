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

        One side note, would be to transactionilze this so that there are less issues
        """
        dal = DAL.DAL()

        for field in self._fields:
            try:
                # Get the prefix
                prefix = field._name[0: field._name.index('_')] # No real point now besides validation (entity changes)
                # Get nullable
                nullable = 'NULL' if field._nullable.upper() == 'Y' else 'NOT NULL'
                # Validate the size
                size = int(field._size)
                # validate entity exists
                tableQuery = f"SELECT Bord_Caption, Bord_tableid FROM dbo.Custom_Tables WHERE Bord_Prefix = '{field._entity}'"
                dal.Reader(tableQuery) # if throws error, continue # filth
            except:
                logger.InfoMessage(f"field error: {field._name}")
                continue
            # You kind of have to assume that the prefix will remain unique... this a problem ?
            try:
                tableQuery = f"SELECT Bord_Caption, Bord_tableid FROM dbo.Custom_Tables WHERE bord_caption = '{field._entity}'"
                dfTableName = dal.Reader(tableQuery)
                tableName = dfTableName.iloc[0,:][0]
                tableId = dfTableName.iloc[0,:][1]
            except:
                logger.ErrorMessage(f"The entity: ({field._entity}) does not exist");
                continue

            # Check to see if the field exists in the table already
            existsQuery = f"SELECT TOP 1 {field._name} FROM dbo.{tableName} WITH(NOLOCK)"
            existCheck = dal.Reader(existsQuery)
            if existCheck != None:
                logger.InfoMessage(f"This field exists already: {field._name}")
                continue
            
            # check the type, based on type create that field
            # Oh no, there is no switch/case in python...
            if field._type.upper() == 'TEXT': # just adds the most simple text field
                # alter the table, adding the field with the correct size and type
                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} NVARCHAR({size}) {nullable}"
                dal.NonReader(alterSQL)

                # Add the record to the custom_captions and custom_edits tables for this record... too tired... can't go on ... did other, more fun ,things ...
                # Should check if exists already and mark deleted, or ? 
                cusCaptionsQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')" 
                dal.NonReader(cusCaptionsQuery)
                # Note that the colp_datatype might change with each version of CRM, amongst other things
                cusEditsQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',10,0,NULL,NULL,NULL,N',',NULL,NULL,{size},NULL,NULL,4,{size},NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusEditsQuery)
            else:
                logger.InfoMessage(f"Field not added ({field._name})")


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