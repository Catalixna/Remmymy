import streamlit as st
from PIL import Image

image = Image.open('Remmy.png')
st.image(image, caption='.', use_column_width=True)

st.write("¿Qué quieres preparar el día de hoy?")

# Buscador
search_query = st.text_input("Buscar recetas:", "")

# Aquí puedes manejar la lógica para buscar recetas basadas en la consulta
if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")
    # Aquí puedes agregar la lógica para filtrar o mostrar recetas basadas en la búsqueda

