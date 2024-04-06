
import sqlite3
import pandas as pd


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cursor = con.cursor()
tabla = 'ESTADISTICAS'
query = f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabla}'"

# Obtener información de la tabla
tabla = con.cursor().execute("SELECT * FROM ESTADISTICAS").description

for columna in tabla:
    nombre_columna, tipo_dato = columna
    print(f"Nombre: {nombre_columna}")
    print(f"Tipo de dato: {tipo_dato}")
    print("---")

con.close()

cursor.close()
con.close()
#res = cur.execute("SELECT PLAYER_NAME, PTS FROM ESTADISTICAS;")

#PLAYER_NAME, PTS = res.fetchone()
#print(f'El jugador {PLAYER_NAME}, hizo {PTS} puntos')
