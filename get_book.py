from conn_to_db import create_connection

conn = create_connection("database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM projects")
rows = cur.fetchall()
rows

def select_books_by_status(conn, status):
   """
   Query projects by priority
   :param conn: the Connection object
   :param status:
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM projects WHERE status=?", (status,))
   rows = cur.fetchall()
   return rows

def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :param table: table name
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()
   return rows

def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

if __name__ == "__main__":
   conn = create_connection("database.db")
   select_all(conn, "projects")