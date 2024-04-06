
import sqlite3
import pandas as pd


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cur = con.cursor()

query = f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabla}'"

try:
    cur.execute(query)
    columnas = cur.fetchall()
except cur.connector.Error as e:
    print(f"Error al obtener información de las columnas: {e}")
    cur.close()
    exit()

con.close()
#res = cur.execute("SELECT PLAYER_NAME, PTS FROM ESTADISTICAS;")

#PLAYER_NAME, PTS = res.fetchone()
#print(f'El jugador {PLAYER_NAME}, hizo {PTS} puntos')
