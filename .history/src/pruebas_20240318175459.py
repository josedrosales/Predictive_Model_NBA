import sqlite3
import pandas as pd

players = pd.read_csv(r'C:\Users\sebas\Documents\Proyecto_DS\ProyectoDS\data\raw\data_complete_raw.csv')
players_records = players.to_records(index=False)


# A database named "NBA.db" is generated in the current directory

con = sqlite3.connect("NBA.db")

cur = con.cursor()

cur.executemany("""
    INSERT INTO ESTADISTICAS (SEASON_YEAR, PLAYER_ID, PLAYER_NAME, NICKNAME, TEAM_ID,
                              TEAM_ABBREVIATION, TEAM_NAME, GAME_ID, GAME_DATE, MATCHUP,
                              WL, MIN, FGM, FGA, FG_PCT, FG3M, FG3A, FG3_PCT, FTM,
                              FTA, FT_PCT, OREB, DREB, REB, AST, TOV, STL, BLK,
                              BLKA, PF, PFD, PTS, PLUS_MINUS, AVAILABLE_FLAG, PTSRTeam,
                              PTSTeam, W_PCTTeam, HOME_AWAY, MIN_PROM, FGM_PROM, FGA_PROM,
                              FG_PCT_PROM, FG3M_PROM, FG3A_PROM, FG3_PCT_PROM, FTM_PROM,
                              FTA_PROM, FT_PCT_PROM, OREB_PROM, DREB_PROM, REB_PROM,
                              AST_PROM, TOV_PROM, STL_PROM, BLK_PROM, BLKA_PROM, PF_PROM,
                              PFD_PROM, PTS_PROM, PLUS_MINUS_PROM, PTSRTeam_PROM,
                              PTSTeam_PROM, W_PCTTeam_PROM)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
           ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
""", players_records)

cur.execute("SELECT * FROM ESTADISTICAS;")

print(cur.fetchall())

con.commit()

con.close()