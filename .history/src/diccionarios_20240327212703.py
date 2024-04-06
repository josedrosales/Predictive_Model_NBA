import pandas as pd

players = pd.read_csv(r'C:\Users\sebas\Documents\Repositorio_DS\ProyectoDS\data\processed\data_complete_raw.csv')



#Se crean diccionarios para el nombre de los equipos y su abreviación, y para el nombre de los jugadores


team_name_dict = players.groupby('TEAM_ID')['TEAM_NAME'].first().to_dict()
team_abbre_dict = players.groupby('TEAM_ID')['TEAM_ABBREVIATION'].first().to_dict()
players_dict = players.groupby('PLAYER_ID')['PLAYER_NAME'].first().to_dict()

print(players_dict)