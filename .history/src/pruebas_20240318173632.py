import sqlite3

# A database named "NBA.db" is generated in the current directory
con = sqlite3.connect("NBA.db")

cur = con.cursor()
cur.execute("""
DESCRIBE ESTADISTICAS;
""")

columnas = cur.fe()

print(cur.fetchall())

con.close()