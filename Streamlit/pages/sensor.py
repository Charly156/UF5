import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Cargar el archivo de Excel en un DataFrame

df = pd.read_excel("sensor_data_general.xlsx", index_col=0)

# Título de la aplicación
st.title("Despliegue de Información del sensor")

# Desplegar el DataFrame
st.subheader("Información del Sensor")
st.write(df)

# Crear un mapa con Folium
st.subheader("Mapa de Sensores")

# Obtener la ubicación promedio para centrar el mapa
center_lat = df["sensor_latitude"].mean()
center_lon = df["sensor_longitude"].mean()

# Slider para ajustar el nivel de zoom del mapa
zoom_level = st.slider("Ajusta el nivel de zoom:", 1, 17, 5)
# Coordenadas específicas

map_data = pd.DataFrame({
    "latitude": [center_lat],
    "longitude": [center_lon]
})

# Mostrar el mapa
st.map(map_data, zoom=zoom_level)