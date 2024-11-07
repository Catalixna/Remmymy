import streamlit as st
from PIL import Image
from gtts import gTTS
import os


image = Image.open('Remmy.png')
col1, col2, col3 = st.columns([1, 2, 1]) 
with col2:
    st.image(image, caption='Tu receta a un clic', width=300)

st.write("¿Qué quieres preparar el día de hoy?")


search_query = st.text_input("Buscar recetas:", "")
if search_query:
    st.write(f"Buscando recetas para: **{search_query}**")
    #texto a audio
    tts = gTTS(text=search_query, lang='es')
    audio_file = "search_query.mp3"
    tts.save(audio_file)  # Guarda el audio en un archivo

    st.audio(audio_file, format='audio/mp3') #reproducir audio
    
    if os.path.exists(audio_file):
        os.remove(audio_file)

