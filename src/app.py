import streamlit as st
import diccionarios
import pickle
import numpy as np
import base64
from pickle import load

# Function to encode image as base64 string (for security)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
        return base64.b64encode(data).decode('utf-8')

# Path to your local image file
image_filename = "src/aro3.jpg"  # Replace with your actual path

# Encode image as base64 string
encoded_image = get_base64_of_bin_file(image_filename)

# Set background image using base64 string
background_image = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
  background-image: url("data:image/jpg;base64,{encoded_image}");  # Use data URI with base64 string
  background-size: 100vw 100vh;
  background-position: center;
  background-repeat: no-repeat;
}}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

#cargo el modelo optimizado
with open('models/random_forest_randstate42_min_samp_leaf_60_n_est_400_max_depth_10_resto_default.pkl', 'rb') as archivo_modelo:
    model = pickle.load(archivo_modelo)

#cargo los diccionarios
players_dict = diccionarios.players_dict
team_abbre_dict = diccionarios.team_abbre_dict
team_name_dict = diccionarios.team_name_dict

players_dict = {k: v for k, v in sorted(players_dict.items(), key=lambda item: item[1])}


st.title('Predicción de puntos para un jugador')
player = st.selectbox('Jugador',list(players_dict.values()))

st.write("Promedios de las estadísticas del jugador en los últimos 5 partidos")
panel_izquierdo, panel_derecho = st.columns(2, gap='large')

# Agregar contenido al panel izquierdo

with panel_izquierdo:
    
    pts_prom = st.slider("Puntos", min_value=0.0, max_value=60.0, step=0.5)#
    min_prom = st.slider("Minutos", min_value=0.0, max_value=50.0, step=0.5) #


# Agregar contenido al panel derecho
with panel_derecho:
    
    fga_prom = st.slider("Tiros de campo intentados", min_value=0.0, max_value=40.0, step=0.5) #
    pfd_prom = st.slider("Faltas recibidas", min_value=0.0, max_value=20.0, step=0.5) #

if st.button("Predecir puntos"):
    # -- Obtengo la key del jugador

    player_key = next((clave for clave, valor in players_dict.items() if valor == player), None)

    #valores = np.array([player_key, fga_prom, pts_prom, min_prom, pfd_prom])

    prediction = str(round(model.predict([[player_key, fga_prom, pts_prom, min_prom, pfd_prom]])[0]))               
    
    st.write("Predicción:", prediction, "Puntos")