import streamlit as st
from PIL import Image

#st.markdown("<h1 style='text-align: center; color: #661200;'>TÚ chinito de confianza</h1>", unsafe_allow_html=True)

image = Image.open('Remmy.png')

 st.write("¿Que quieres preparar el día de hoy?")

