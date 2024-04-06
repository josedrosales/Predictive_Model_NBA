import streamlit as st
import diccionarios
from pickle import load

#cargo el modelo optimizado
model = load(open("../models/random_forest_rs_42_nest_250_msamps_4_msampl_7_mxft_sqrt_mxdpth_15.sav", "rb"))

#cargo los diccionarios
players_dict = diccionarios.players_dict
team_abbre_dict = diccionarios.team_abbre_dict
team_name_dict = diccionarios.team_name_dict

st.title('Prediccion de puntos para un jugador')


player = st.selectbox('Jugador',list(players_dict.values()))