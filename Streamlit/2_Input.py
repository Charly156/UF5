import streamlit as st
st.write('Esta aplicación calculará el módulo 2 de un número')

#   Introducir el número para calcular su número 2
x = st.number_input('Introduzca un número:')

#Indicarle a la aplicación que debe devolver el factorial del número
st.write(f'El modulo 2 de {x} es:', x%2)