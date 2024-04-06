import sqlite3
import pandas as pd

players = pd.read_csv(r'C:\Users\sebas\Documents\Proyecto_DS\ProyectoDS\data\raw\data_complete_raw.csv', encoding='utf-8',dtype={'PLAYER_ID': int})
players_records = players.to_records(index=False)


# A database named "NBA.db" is generated in the current directory
con = sqlite3.connect("NBA.db")
con.execute("DROP TABLE IF EXISTS ESTADISTICAS;")

players.to_sql('ESTADISTICAS',con, index=True,if_exists='replace')

con.close()
