import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('tabular_data_docentes.xlsx', index_col=0)

from datetime import datetime, date, time

data['Day'] = data['timestamp'].dt.day_name()

#Crear check box
show_dt = st.sidebar.checkbox('Visualizar DataFrame', value = False)

if show_dt:
    #Usar st.dataframe para mostrar el DataFrame en Streamlit
    st.title('Análisis de datos tabulares')
    st.dataframe(data)

#Selección y control de fechas
st.sidebar.header('Control de Fechas')
start_date = st.sidebar.date_input('Seleccionar fecha de inicio', data['timestamp'].min())
end_date = st.sidebar.date_input('Seleccionar fecha de fin', data['timestamp'].max())

#Convertir objetos a datetime64[ns]
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

#Crear filtro
filtro_fecha = data[(data['timestamp'] >= start_date) & (data['timestamp'] <= end_date)]


#Crear check box
show_dt = st.sidebar.checkbox('Mostrar por día de la semana', value = False)

if show_dt:
    # Añadir un selectbox para elegir el tipo de gráfico
    st.sidebar.header('Control de días')
    dias = st.sidebar.selectbox('Selecciona el día de la semana',
                                      ['Monday','Tuesday','Wednesday','Thursday',
                                       'Friday','Saturday','Sunday'])
    filtro_fecha = filtro_fecha[filtro_fecha['Day'] == dias]

# Añadir un selectbox para elegir el tipo de gráfico
chart_type = st.sidebar.selectbox('Selecciona el tipo de gráfico que desee visualizar', 
                          ['Gráfico de líneas', 'Gráfico de áreas', 'Gráfico de barras',
                           'Gráfico de boxplot', 'Gráfico de densidad', 'Gráfico de hexbin',
                           'Gráfico de hist', 'Gráfico de line', 'Gráfico de pie',
                           'Gráfico de scatter'])

if chart_type == 'Gráfico de líneas':
    # Gráfico de líneas
    st.subheader("Gráfico de líneas")
    fig, ax = plt.subplots()
    data[['Day', 'total_visits']].groupby(data['Day']).sum().plot(ax=ax, kind='line',
                                                              title='Visitas por día')
    st.pyplot(fig)
elif chart_type == 'Gráfico de áreas':
    # Gráfico de áreas
    st.subheader('Gráfico de áreas')
    fig, ax = plt.subplots()
    filtro_fecha[['incoming_inner_count', 'incoming_outer_count']].head(96).plot.area(ax=ax,
                                                                            title='Entradas en un día', stacked=False)
    st.pyplot(fig)
elif chart_type == 'Gráfico de barras':
    #Gráfico de barras
    st.subheader('Gráfico de barras')
    fig, ax = plt.subplots()
    plot = filtro_fecha[['Day','total_visits']].groupby('Day').sum().plot.bar(ax = ax, title = 'Visitas por día')
    st.pyplot(fig)

    #Gráfico de barras horizontal
    st.subheader('Gráfico de barras horizontal')
    fig, ax = plt.subplots()
    plot = filtro_fecha[['Day','total_visits']].groupby('Day').sum().plot.barh(ax = ax, title = 'Visitas por día')
    st.pyplot(fig)
elif chart_type == 'Gráfico de boxplot':
    #Gráfico de boxplot
    st.subheader('Gráfico de boxplot')
    fig, ax = plt.subplots()
    plot = filtro_fecha[['Day','total_visits']].head(7*96).plot.box(ax = ax, column = 'total_visits',title = 'Visitas por día')
    st.pyplot(fig)
elif chart_type == 'Gráfico de densidad':
    #Gráfico de densidad
    st.subheader('Gráfico de densidad')
    fig, ax = plt.subplots()
    plot = filtro_fecha[['incoming_inner_count','outgoing_inner_count']].head(96).plot.density(ax = ax)
    st.pyplot(fig)
elif chart_type == 'Gráfico de hexbin':
    #Gráfico de hexbin
    st.subheader('Gráfico de hexbin')
    fig, ax = plt.subplots()
    plot = filtro_fecha.head(96).plot.hexbin(ax = ax, x= 'incoming_outer_count',
                                         y = 'outgoing_outer_count',
                                         gridsize = 10, bins = 'log')
    st.pyplot(fig)
elif chart_type == 'Gráfico de hist':
    #Gráfico de hist
    st.subheader('Gráfico de hist')
    fig, ax = plt.subplots()
    plot = filtro_fecha[['incoming_inner_count','outgoing_inner_count']].plot.hist(ax= ax, title = 'Gráfico de histograma')
    st.pyplot(fig)
elif chart_type == 'Gráfico de line':
    #Gráfico de line
    st.subheader('Gráfico de line')
    fig, ax = plt.subplots()
    plot = filtro_fecha[['incoming_inner_count','outgoing_inner_count']].plot.line(ax= ax, title = 'Gráfico de lineas')
    st.pyplot(fig)
elif chart_type == 'Gráfico de pie':
    #Gráfico de pie
    st.subheader('Gráfico de pie')
    fig, ax = plt.subplots()
    plot = data[['Day','total_visits']].groupby('Day').sum().plot.pie(ax= ax, y = 'total_visits', title = 'Visitas por día')
    st.pyplot(fig)
elif chart_type == 'Gráfico de scatter':
    #Gráfico de scatter
    st.subheader('Gráfico de scatter')
    fig, ax = plt.subplots()
    plot = filtro_fecha.plot.scatter(ax= ax, x = 'incoming_inner_count', y = 'outgoing_inner_count')
    st.pyplot(fig)

    st.subheader('Gráfico de scatter')
    fig, ax = plt.subplots()
    plot = filtro_fecha.plot.scatter(ax= ax, x = 'incoming_inner_count', y = 'outgoing_inner_count', c = 'total_visits')
    st.pyplot(fig)