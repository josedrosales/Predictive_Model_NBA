
import sqlite3
import pandas as pd


players = pd.read_csv(r'C:\Users\sebas\Documents\Proyecto_DS\ProyectoDS\data\raw\data_complete_raw.csv')
players_records = players.to_records(index=False)
print(list(players_records.PLAYER_ID))
# A database named "NBA.db" is generated in the current directory

# con = sqlite3.connect("NBA.db")

# cursor = con.cursor()



# df_datos = pd.read_sql_query("SELECT * FROM ESTADISTICAS;", con)


# print(df_datos.PLAYER_ID)

#players_records = players.to_records(index=False)

#res = cur.execute("SELECT PLAYER_NAME, PTS FROM ESTADISTICAS;")

#PLAYER_NAME, PTS = res.fetchone()
#print(f'El jugador {PLAYER_NAME}, hizo {PTS} puntos')
