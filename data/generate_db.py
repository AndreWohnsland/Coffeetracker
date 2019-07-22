import sqlite3

def create_new_db(DB):
    """ Creates a the new tables in the Database. """
    DB = sqlite3.connect(DB)
    c = DB.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL, amount INTEGER NOT NULL, money FLOAT(2) NOT NULL, enabled BOOL NOT NULL);")
    c.execute("CREATE TABLE IF NOT EXISTS tracks(Number INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, employee_ID INTEGER NOT NULL, time DATETIME)")