import sqlite3

# A database named "NBA.db" is generated in the current directory
con = sqlite3.connect("NBA.db")

con.execute('''SELECT * FROM ESTADISTICAS;''')
print(con.fetchall())