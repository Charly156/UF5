import streamlit as st

x = st.slider('Selecciona un valor')
st.write(x, 'elevado al cuadrado es ', x*x)