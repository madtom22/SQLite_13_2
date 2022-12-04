from conn_to_db import create_connection

def add_new_book(conn, projects):
   """
   Create a new project into the projects table
   :param conn: the Connection object
   :param projects:
   :return: project id
   """
   sql = '''INSERT INTO projects(title, autor, year)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, projects)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   projects = ("Kurs Python 3.10", "Roland Ziemek", "2022")
   conn = create_connection("database.db")
   pr_id = add_new_book(conn, projects)
   conn.commit()