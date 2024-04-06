
import sqlite3
import pandas as pd


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cursor = con.cursor()
tabla = 'ESTADISTICAS'
query = f"SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tabla}'"

query = "PRAGMA table_info('ESTADISTICAS')"
cursor.execute(query)

# Recorrer las filas y mostrar la información
for row in cursor.fetchall():
    nombre_columna, tipo_dato, not_null, pk, dflt_value = row
    print(f"Nombre: {nombre_columna}")
    print(f"Tipo de dato: {tipo_dato}")
    print(f"No nulo: {'Si' if not_null else 'No'}")
    print(f"Clave primaria: {'Si' if pk else 'No'}")
    print(f"Valor por defecto: {dflt_value if dflt_value is not None else 'Ninguno'}")
    print("---")

cursor.close()
con.close()
#res = cur.execute("SELECT PLAYER_NAME, PTS FROM ESTADISTICAS;")

#PLAYER_NAME, PTS = res.fetchone()
#print(f'El jugador {PLAYER_NAME}, hizo {PTS} puntos')
