
import sqlite3
import pandas as pd


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cursor = con.cursor()

# Obtener información de la tabla

resultado = cursor.execute("SELECT PTS, MIN FROM ESTADISTICAS")
dat = resultado.fetchone()
data_deco = dat.decode("utf-8")
print(data_deco[0])
print(data_deco[1])



con.close()
#res = cur.execute("SELECT PLAYER_NAME, PTS FROM ESTADISTICAS;")

#PLAYER_NAME, PTS = res.fetchone()
#print(f'El jugador {PLAYER_NAME}, hizo {PTS} puntos')
