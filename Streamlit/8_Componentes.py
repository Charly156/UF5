import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Título principal
st.title('Ejemplo Práctico de Streamlit')

#Encabezado con Markdown
st.markdown('Exploración de datos y Visualización')

#Slider para seleccionar el número de puntos
num_data_points = st.slider('Selecciona el número de puntos de datos:', 10, 100, 50)

#Generar datos aleatorios
data = np.random.randn(num_data_points, 2)
df = pd.DataFrame(data, columns = ['X', 'Y'])

#Mpstrar tabla de datos
st.write('### Tabla de datos')
st.dataframe(df)

#Histograma interactivo
st.write('### Histograma de la columna X')
hist_values = np.histogram(df['X'], bins = 20)[0]
st.bar_chart(hist_values)

#Gráfico de dispersión
st.write('### Gráfico de Dispersión')
st.scatter_chart(df)

#Sección de mapa con Markdown
st.markdown('### Mapa Interactivo')

#Slider para ajustar el nivel de zoom del mapa
zoom_level = st.slider('Ajusta el nivel de zoom:', 1, 17, 5)

#Coordenadas aleatorias para simular ubicaciones en un mapa
#Coordenadas específicas

latitude = 19.0174471
longitude = -98.2413036
map_data = pd.DataFrame({
    'latitude': [latitude],
    'longitude': [longitude]
})

#Mostrar el mapa
st.map(map_data, zoom = zoom_level)

#Nota final con markdown
st.markdown('¡Gracias por explorar este navegador!')