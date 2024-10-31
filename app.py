import streamlit as st
from PIL import Image

# Cargar la imagen
image = Image.open('Remmy.png')

# Usar columnas para centrar la imagen
col1, col2, col3 = st.columns([1, 2, 1])  # Ajusta las proporciones según necesites
with col2:
    st.image(image, caption='Tu receta a un clic', width=300)  # Usa 'image' en lugar de 'img'

# Texto interactivo
st.write("¿Qué quieres preparar el día de hoy?")

# Buscador
search_query = st.text_input("Buscar recetas:", "")

if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")
