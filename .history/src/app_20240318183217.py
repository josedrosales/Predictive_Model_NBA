
import sqlite3
import pandas as pd


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cursor = con.cursor()

# Obtener información de la tabla


for row in cursor.execute("SELECT PTS, MIN FROM ESTADISTICAS"):
    nombre_columna = row[0]
    tipo_dato = row[1]
    print(f"Nombre: {nombre_columna}")
    print(f"Tipo de dato: {tipo_dato}")
    print("---")

con.close()
#res = cur.execute("SELECT PLAYER_NAME, PTS FROM ESTADISTICAS;")

#PLAYER_NAME, PTS = res.fetchone()
#print(f'El jugador {PLAYER_NAME}, hizo {PTS} puntos')
