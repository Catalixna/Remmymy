try:
    import streamlit as st
    from PIL import Image
    from gtts import gTTS
    import os
except ModuleNotFoundError as e:
    st.error(f"Error de importación: {e}. Asegúrate de que todos los módulos necesarios están instalados.")
    st.stop()  # Detiene la ejecución si faltan módulos

# Cargar la imagen
image_path = 'Remmy.png'  # Asegúrate de que la imagen esté en el directorio correcto
if os.path.exists(image_path):
    image = Image.open(image_path)
else:
    st.error("No se encuentra la imagen 'Remmy.png'.")
    image = None

# Usar columnas para centrar la imagen
col1, col2, col3 = st.columns([1, 2, 1])  # Ajusta las proporciones según necesites
if image:
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

