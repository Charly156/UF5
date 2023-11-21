import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#Generar datos aleatorios para el histograma
data = np.random.randn(1000)

#Configuración de la aplicación Streamlit
st.title('Histograma en Streamlit')
st.write('Ejemplo simple de un histograma usando Streamlit.')

#Desplegar histograma
fig, ax = plt.subplots()
ax.hist(data, bins = 30, edgecolor = 'black')
ax.set_title('Histograma de Datos Aleatorios')
ax.set_xlabel('Valores')
ax.set_ylabel('Frecuencia')

#Mostrar el histograma en Streamlit
st.pyplot(fig)