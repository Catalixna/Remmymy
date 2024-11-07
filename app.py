import streamlit as st
from PIL import Image
from gtts import gTTS
import os

# Cargar la imagen
image = Image.open('Remmy.png')

# Usar columnas para centrar la imagen
col1, col2, col3 = st.columns([1, 2, 1])  # Ajusta las proporciones según necesites
with col2:
    st.image(image, caption='Tu receta a un clic', width=300)

# Texto interactivo
st.write("¿Qué quieres preparar el día de hoy?")

# Buscador
search_query = st.text_input("Buscar recetas:", "")

if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")
    
    # Convertir el texto a audio
    tts = gTTS(text=search_query, lang='es')
    audio_file = "search_query.mp3"
    tts.save(audio_file)  # Guarda el audio en un archivo
    
    # Reproduce el audio
    st.audio(audio_file, format='audio/mp3')

    # Limpia el archivo de audio después de usarlo
    if os.path.exists(audio_file):
        os.remove(audio_file)

