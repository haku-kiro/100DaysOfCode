from sqlalchemy import create_engine
import sqlite3

db_path = 'C:/Users/mdjco/Documents/Backups/DBBackups/chinook/chinook.db'

# this would be to use the sqlalchemy (should get this up and runnign actually)
# engine = create_engine(db_path)
# print(engine)

"""

This is how to use sqlalchemy

"""
# Connection to sqlite using sqlalchemy
# Import necessary module
# from sqlalchemy import create_engine

# # Create engine: engine
# engine = create_engine('sqlite:///Chinook.sqlite')
# print(engine)


# # Import necessary module
# from sqlalchemy import create_engine

# # Create engine: engine
# engine = create_engine('sqlite:///Chinook.sqlite')

# # Save the table names to a list: table_names
# table_names = engine.table_names()

# # Print the table names to the shell
# print(table_names)
# # This prints out: 
# """
# Just in case you need this, not sure how to list the tables with the sqlite3 module
# ['Album', 'Artist', 'Customer', 'Employee', 'Genre', 'Invoice', 'InvoiceLine', 'MediaType', 'Playlist', 'PlaylistTrack', 'Track']
# """


## ANYWAYS
# sql lite

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# can use pandas and what not here
# cursor.execute("query")

sql = "SELECT * FROM albums"
cursor.execute(sql)
print(cursor.fetchall())  # or use fetchone()