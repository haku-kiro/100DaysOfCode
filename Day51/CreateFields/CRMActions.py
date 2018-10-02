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
            try:
                if not existCheck.empty:
                    logger.InfoMessage(f"This field exists already: {field._name}")
                    continue
            except:
                logger.InfoMessage(f"Creating field: {field._name}")
            
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
            elif field._type.upper() == 'INT':
                # Alter table (No size)
                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} INTEGER {nullable}"
                dal.NonReader(alterSQL)
                # cus_captions
                # Cus_edits
                cusCaptionIntQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')  "
                dal.NonReader(cusCaptionIntQuery) # should do a row count on this
                cusEditsIntQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',31,0,NULL,NULL,NULL,N',',NULL,NULL,20,NULL,NULL,5,20,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')" 
                dal.NonReader(cusEditsIntQuery) # Size, and the entry width same (for int)
            elif field._type.upper() == "DATETIME":
                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} DATETIME {nullable}"
                dal.NonReader(alterSQL)

                cusCaptionDateTimeQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusCaptionDateTimeQuery)
                cusEditsDateTimeQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',41,0,NULL,NULL,NULL,N',',NULL,NULL,20,NULL,NULL,2,20,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusEditsDateTimeQuery)

            elif field._type.upper() == 'CURRENCY':
                # Note that there are two fields created/added when you add a currency field
                # Also does an update on the field (After creating it)
                alterSQL1 = f"ALTER TABLE {tableName} ADD {field._name} NUMERIC(24, 6) NULL" # wont allow not null fields
                dal.NonReader(alterSQL1)
                # if you seperate your logic, it's one less call here ...
                alterSQL2 = f"ALTER TABLE {tableName} ADD {field._name}_CID INTEGER NULL"
                dal.NonReader(alterSQL2)

                updateSQL = f"UPDATE {tableName} SET {field._name}_CID=5" # could cause problems ... with the default currency (should do a lookup)
                dal.NonReader(updateSQL)

                ## Currency field 1 (Doesn't do a custom caption record for the CID field)
                cusCaptionCurrencyQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusCaptionCurrencyQuery)

                ## Two edits queries
                cusEditsCID = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_LookupFamily,ColP_System,ColP_DataType,ColP_CustomTableIDFK,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}_CID',N'{tableName}',21,N'CurrencySymbols',N'Y',5,{tableId},-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                cusEditsCurr = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',51,0,NULL,NULL,NULL,N',',NULL,NULL,20,NULL,NULL,6,24,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusEditsCID)
                dal.NonReader(cusEditsCurr)
            
            elif field._type.upper() == 'NUMERIC':
                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} NUMERIC(24, 6) {nullable}"
                dal.NonReader(alterSQL)

                cusCaptionNumericQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusCaptionNumericQuery)
                cusEditNumericQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field_name}',N'{tableName}',32,0,NULL,NULL,NULL,N',',NULL,NULL,20,NULL,NULL,6,24,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusEditNumericQuery)

            elif field._type.upper() == 'CHECKBOX':
                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} NCHAR(1) NULL"
                dal.NonReader(alterSQL)

                cusCaptionChckQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusCaptionChckQuery)
                cusEditChckQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',45,0,NULL,NULL,NULL,N',',NULL,NULL,20,NULL,NULL,4,1,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusEditChckQuery)

            elif field._type.upper() == "MULTI":
                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} NVARCHAR(MAX) {nullable}"
                dal.NonReader(alterSQL)

                cusCaptionMultiQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusCaptionMultiQuery)
                cusEditMultiQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',11,0,NULL,NULL,NULL,N',',NULL,NULL,20,NULL,NULL,4,20,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusEditMultiQuery)

            elif field._type.upper() == "SELECTION":
                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} NVARCHAR(40) NULL" # fun fact, selection fields are 40 chars wide
                dal.NonReader(alterSQL)

                # Adding the field, need to add the selection as well? (Naaah) 
                cusCaptionSelQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusCaptionSelQuery)

                lookup = ""
                if field._fieldInfo == "" or field._fieldInfo == field._name:
                    lookup = field._name

                else:
                    lookup = field._fieldInfo
                    # Check to see if that lookup exists
                    checkQuery = f"SELECT TOP 1 * FROM dbo.custom_captions WHERE capt_family = '{lookup}'"
                    dfCheck = dal.Reader(checkQuery)
                    if dfCheck.empty: 
                        lookup = field._name # if can't find, don't break just set to own field

                cusEditSelQueryCreateLookup = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',21,0,NULL,NULL,NULL,N',',NULL,NULL,1,N'{lookup}',NULL,4,40,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusEditSelQueryCreateLookup)

            elif field._type.upper() == "SSA":
                # Do ssa checks first (before creating field on the table)
                cusEditSSAQuery = ""
                try:
                    prefix = ""
                    dfCheck = dal.Reader(f"SELECT TOP 1 bord_prefix, bord_idField FROM dbo.custom_tables WITH(NOLOCK) WHERE bord_caption = '{field._fieldInfo}'")
                    if dfCheck.empty:
                        logger.InfoMessage(f"Could not link the ssa field ({field._name}) to the table passed: ({field._fieldInfo})");
                        continue
                    else:
                        prefix = dfCheck.values[0][0]
                        idField = dfCheck.values[0][1]
                        dfGetLink = dal.Reader(f"SELECT TOP 1 {prefix}_name FROM {tableName} WITH(NOLOCK)")
                        try:
                            if not dfGetLink.empty:
                                # Create edit with the link to the idfield
                                cusEditSSAQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',56,0,NULL,NULL,NULL,N',{idField},',NULL,NULL,20,N'{field._fieldInfo}',NULL,5,20,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed') "
                        except: # filth
                            # create edit with the link to the name field
                            cusEditSSAQuery = f"INSERT INTO Custom_Edits(ColP_ColName,ColP_Entity,ColP_EntryType,ColP_DefaultType,ColP_DefaultValue,ColP_SearchSql,ColP_LinkedField,ColP_SSViewField,ColP_StartTime,ColP_EndTime,ColP_EntrySize,ColP_LookupFamily,ColP_LookupWidth,ColP_DataType,ColP_DataSize,Colp_Restricted,ColP_Multiple,Colp_TiedFields,Colp_CanDelete,ColP_CustomTableIDFK,Colp_ExcludeFromIndexing,colp_CreatedBy,colp_CreatedDate,colp_UpdatedBy,colp_UpdatedDate,colp_TimeStamp,colp_Component)  VALUES (N'{field._name}',N'{tableName}',56,0,NULL,NULL,NULL,N',{prefix}_name,',NULL,NULL,20,N'{field._fieldInfo}',NULL,5,20,NULL,NULL,N',',N'Y',{tableId},NULL,-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed') "
                except:
                    logger.InfoMessage(f"An error occured when creating the SSA field: {field._name}");
                    continue

                alterSQL = f"ALTER TABLE {tableName} ADD {field._name} INTEGER NULL"
                dal.NonReader(alterSQL)

                cusCaptionSSAQuery = f"INSERT INTO Custom_Captions(Capt_FamilyType,Capt_Family,Capt_Code,Capt_DE,Capt_DU,Capt_ES,Capt_FR,Capt_UK,Capt_US,capt_CreatedBy,capt_CreatedDate,capt_UpdatedBy,capt_UpdatedDate,capt_TimeStamp,capt_Component)  VALUES (N'Tags',N'ColNames',N'{field._name}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',N'{field._caption}',-42,GETDATE(),-42,GETDATE(),GETDATE(),N'Changed')"
                dal.NonReader(cusCaptionSSAQuery)

                dal.NonReader(cusEditSSAQuery)
            else:
                logger.InfoMessage(f"Field not added !({field._name})!")


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