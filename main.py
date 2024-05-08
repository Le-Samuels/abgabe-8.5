import streamlit as st
from read_data import get_person_data
from read_data import get_person_name
from read_data import find_person_data_by_name
from PIL import Image


st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Dieses Mal speichern wir die Auswahl als Session State


st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = get_person_name(get_person_data()), key="sbVersuchsperson")

st.write("Der Name ist: ", st.session_state.current_user) 

#Bilder von den Personen

# Finden der Person - den String haben wir im Session state
current_person = find_person_data_by_name()
# Auslesen des Pfades aus dem zurückgegebenen Dictionary
current_picture_path = current_person["picture_path"]
# Laden eines Bilds
image = Image.open(st.session_state.picture_path)
# Anzeigen eines Bilds mit Caption
st.image(image, caption=st.session_state.current_user)