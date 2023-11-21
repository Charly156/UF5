import streamlit as st

#Entrada de texto
user_text = st.text_input('Ingresa tu nombre:', 'Usuario 1')

#Entrada numérica
user_number = st.number_input('Ingresa tu edad:',min_value = 0, max_value = 110, value = 25, step = 1)

#Mostrar la información ingresada
st.write(f'Hola, {user_text}! Tienes {user_number} años. Bienvenido a esta interfaz')