import sqlite3

# A database named "NBA.db" is generated in the current directory
con = sqlite3.connect("NBA.db")

cur = con.cursor()
cur.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='nombre_de_la_tabla';
""")
cur.fetchall()
print(cur.fetchall())

con.close()