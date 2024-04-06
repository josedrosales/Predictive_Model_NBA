
import sqlite3
import pandas as pd


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cur = con.cursor()

cur.execute("SELECT * FROM ESTADISTICAS;")

result = cur.fetchall()

for row in result:
    print (row)

