import sqlite3

# A database named "NBA.db" is generated in the current directory
con = sqlite3.connect("NBA.db")

cur = con.cursor()
cur.execute("""
SELECT name FROM sqlite_master WHERE type='table' AND name='ESTADISTICAS';
""")

columnas = cur.fetchall()

for columna in columnas:
    print(columna[0])

con.close()