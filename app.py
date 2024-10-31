import streamlit as st
from PIL import Image

# Título centrado con estilo
#st.markdown("<h1 style='text-align: center; color: #661200;'>TÚ chinito de confianza</h1>", unsafe_allow_html=True)

# Cargar y mostrar la imagen
image = Image.open('Remmy.png')
st.image(image, caption='Tu imagen aquí', use_column_width=True)

# Texto interactivo
st.write("¿Qué quieres preparar el día de hoy?")

# Buscador
search_query = st.text_input("Buscar recetas:", "")

# Aquí puedes manejar la lógica para buscar recetas basadas en la consulta
if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")
    # Aquí puedes agregar la lógica para filtrar o mostrar recetas basadas en la búsqueda
else:
    st.write("Introduce un ingrediente o tipo de comida para buscar recetas.")
