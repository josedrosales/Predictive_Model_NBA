import sqlite3
import pandas as pd

players = pd.read_csv(r'C:\Users\sebas\Documents\Proyecto_DS\ProyectoDS\data\raw\data_complete_raw.csv', encoding='utf-8',dtype={'PLAYER_ID': int})
players_records = players.to_records(index=False)


# A database named "NBA.db" is generated in the current directory
con = sqlite3.connect("NBA.db")
con.execute("DROP TABLE IF EXISTS ESTADISTICAS;")

players.to_sql('ESTADISTICAS',con, index=True,if_exists='replace')



# con.execute("""CREATE TABLE IF NOT EXISTS ESTADISTICAS
#     (SEASON_YEAR CHAR(7) NOT NULL,
#      PLAYER_ID INTEGER NOT NULL,
#      PLAYER_NAME TEXT,
#      NICKNAME VARCHAR(30),
#      TEAM_ID REAL NOT NULL,
#      TEAM_ABBREVIATION CHAR(5),
#      TEAM_NAME TEXT,
#      GAME_ID CHAR(10) NOT NULL,
#      GAME_DATE CHAR(10),
#      MATCHUP CHAR(12),
#      WL CHAR(1),
#      MIN REAL,
#      FGM REAL,
#      FGA REAL,
#      FG_PCT REAL,
#      FG3M INTEGER,
#      FG3A INTEGER,
#      FG3_PCT REAL,
#      FTM INTEGER,
#      FTA INTEGER,
#      FT_PCT REAL,
#      OREB INTEGER,
#      DREB INTEGER,
#      REB INTEGER,
#      AST INTEGER,
#      TOV INTEGER,
#      STL INTEGER,
#      BLK INTEGER,
#      BLKA INTEGER,
#      PF INTEGER,
#      PFD INTEGER,
#      PTS INTEGER,
#      PLUS_MINUS INTEGER,
#      AVAILABLE_FLAG INTEGER,
#      PTSRTeam INTEGER,
#      PTSTeam INTEGER,
#      W_PCTTeam REAL,
#      HOME_AWAY CHAR(1),
#      MIN_PROM REAL,
#      FGM_PROM REAL,
#      FGA_PROM REAL,
#      FG_PCT_PROM REAL,
#      FG3M_PROM REAL,
#      FG3A_PROM REAL,
#      FG3_PCT_PROM REAL,
#      FTM_PROM REAL,
#      FTA_PROM REAL,
#      FT_PCT_PROM REAL,
#      OREB_PROM REAL,
#      DREB_PROM REAL,
#      REB_PROM REAL,
#      AST_PROM REAL,
#      TOV_PROM REAL,
#      STL_PROM REAL,
#      BLK_PROM REAL,
#      BLKA_PROM REAL,
#      PF_PROM REAL,
#      PFD_PROM REAL,
#      PTS_PROM REAL,
#      PLUS_MINUS_PROM REAL,
#      PTSRTeam_PROM REAL,
#      PTSTeam_PROM REAL,
#      W_PCTTeam_PROM REAL,
#      PRIMARY KEY (SEASON_YEAR, PLAYER_ID, TEAM_ID, GAME_ID)
#      );""")

con.close()
