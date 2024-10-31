import streamlit as st
from PIL import Image

#st.markdown("<h1 style='text-align: center; color: #661200;'>TÚ chinito de confianza</h1>", unsafe_allow_html=True)

image = Image.open('Remmy.png')

st.image(image, caption='Capibara')

texto=st.text_input('Escribe que piensas de las capibaras: ','...')
st.write('¡Dato curioso! Los capibaras son tan sociables que a menudo se les ve conviviendo pacíficamente con otros animales, ¡incluso con cocodrilos! Su naturaleza relajada hace que muchas especies los toleren cerca, sin considerarlos una amenaza.',texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("!!Apoya a los capibaras¡¡")
  st.write("Los capibaras son esenciales para el equilibrio de los ecosistemas en los que viven. Ayudan a mantener bajo control el crecimiento de las plantas acuáticas, lo que beneficia a muchas otras especies. Además, son una fuente de alimento para depredadores naturales, lo que los convierte en una pieza clave en la cadena alimenticia. Cuidar a los capibaras no solo protege a una especie fascinante, sino que también preserva la salud de los humedales y la biodiversidad que depende de ellos. ¿Quieres más info? suscribete.")
  resp = st.checkbox('Suscribirse')
  if resp:
    st.write('Exelente!, te llegara info al correo...')

with col2:
  st.subheader("¿Que comen los capibaras?")
  modo = st.radio("Que modalidad es la principal en tu interfaz",('Peces','Frutas','Hierbas'))
  if modo == 'Peces':
    st.write('Parecia pero no, son herviboros!')
  if modo == 'Frutas':
    st.write('Nadaaaa')
  if modo == 'Hierbas':
    st.write('Exacto!, comen Hierba, plantas acuáticas y corteza de árboles.')

st.subheader("Te gusta esta info...")
if st.button ('Dale like!!'):
  st.write('Gracias por presionar')
else:
  st.write('Presiona el boton ')


with st.sidebar:
  st.subheader("Configura la modalidad")
  mod_radio = st.radio("Escoge la modalidad a usar",("Visual", "Auditiva", "Háptica"))
