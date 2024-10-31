import streamlit as st
from PIL import Image

image = Image.open('Remmy.png')
st.image(image, caption='.', width=300)

st.write("¿Qué quieres preparar el día de hoy?")

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image(image, caption='.', width=300)  # Cambia el valor de width según lo necesites
st.markdown("</div>", unsafe_allow_html=True)


# Aquí puedes manejar la lógica para buscar recetas basadas en la consulta
if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")
    # Aquí puedes agregar la lógica para filtrar o mostrar recetas basadas en la búsqueda

