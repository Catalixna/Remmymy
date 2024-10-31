import streamlit as st
from PIL import Image

# Título centrado con estilo
#st.markdown("<h1 style='text-align: center; color: #661200;'>TÚ chinito de confianza</h1>", unsafe_allow_html=True)

# Cargar la imagen
image = Image.open('Remmy.png')

# Centrar la imagen
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(image, caption='Tu imagen aquí', width=300)  # Cambia el valor de width según lo necesites
st.markdown("</div>", unsafe_allow_html=True)

# Texto interactivo
st.write("¿Qué quieres preparar el día de hoy?")

# Buscador
search_query = st.text_input("Buscar recetas:", "")

if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")

