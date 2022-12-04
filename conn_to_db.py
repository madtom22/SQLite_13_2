import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
       return conn
   except Error as e:
       print(e)

   return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
   except Error as e:
       print(e)

create_books_sql = """
   -- books table
   CREATE TABLE IF NOT EXISTS projects (
      id integer PRIMARY KEY,
      title text NOT NULL,
      autor text NOT NULL,
      year integer NOT NULL
   );
   """
if __name__ == "__main__":
   db_file = "database.db"
   conn = create_connection(db_file)
   if conn is not None:
       execute_sql(conn, create_books_sql)
       conn.close()
