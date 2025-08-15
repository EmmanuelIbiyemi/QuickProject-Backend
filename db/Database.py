import sqlite3 as sql

database = sql.connect('quickproject.db')
database.close()

if (database):
    print("DataBase have been created!")
else:
    print("Their was error while creating the database")