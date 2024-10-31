import streamlit as st
from PIL import Image

# Título centrado con estilo
st.markdown("<h1 style='text-align: center; color: #661200;'>TÚ chinito de confianza</h1>", unsafe_allow_html=True)

# Cargar y mostrar la imagen
image = Image.open('Remmy.png')
st.image(image, caption='Tu imagen aquí', use_column_width=True)

# Texto interactivo
st.write("¿Qué quieres preparar el día de hoy?")
