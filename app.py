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

# Función para reproducir y manejar el archivo de audio
def play_audio(query):
    audio_file = "search_query.mp3"
    tts = gTTS(text=query, lang='es')
    tts.save(audio_file)
    st.audio(audio_file, format='audio/mp3')
    os.remove(audio_file)  # Eliminar después de reproducir

if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")
    play_audio(search_query)

