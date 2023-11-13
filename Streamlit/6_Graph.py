import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#Interfaz del usuario
num_lanzamientos = st.number_input(label = 'Número de lanzamientos',
                                   min_value = 1, max_value = 200, value = 100)                                
graph_title = st.text_input('Graph Title')

#Simulación del lanzamiento de dos datos
dados_1 = np.random.randint(1, 7, size = num_lanzamientos)
dados_2 = np.random.randint(1, 7, size = num_lanzamientos)
sumas = dados_1 + dados_2

#Crear histograma de las sumas de los lanzamientos
fig, ax = plt.subplots()
ax.hist(sumas, bins = np.arange(1.5, 13.5), edgecolor = 'black')
ax.set_xticks(range(2,13))
ax.set_title(graph_title)
ax.set_xlabel('Valores')
ax.set_ylabel('Frecuencia')

#Mostrar el histograma en Streamlit
st.pyplot(fig)