import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Crear un DataFrame de ejemplo con datos aleatorios
np.random.seed(42) #Fijar la semilla para reproducibilidad
fecha_inicio = pd.to_datetime('2023-01-01')
fecha_fin = pd.to_datetime('2023-01-10')

data = {
    'Fecha': pd.date_range(start = fecha_inicio, end = fecha_fin),
    'Producto': np.random.choice(['Producto A', 'Producto B'], size = 10),
    'Cantidad': np.random.randint(5, 20, size = 10),
    'Ingresos': np.random.randint(50, 200, size = 10)
}

df_ventas = pd.DataFrame(data)

#Usar st.dataframe para mostrar el DataFrame en Streamlit
st.title('Análisis de Ventas')
st.dataframe(df_ventas)

#Agregar un gráfico de barras para mostrar las ventas por producto
fig, ax = plt.subplots()
ax.bar(df_ventas['Producto'], df_ventas['Cantidad'], color = 'blue')

#Añadir título al gráfico
plt.title('Ventas por producto')
plt.xlabel('Producto')
plt.ylabel('Cantidad vendida')

#Mostrar el gráfico
st.pyplot(fig)
