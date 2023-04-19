
import streamlit as st
import pandas as pd
from PIL import Image


st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        layout='wide'
    )

st.sidebar.success("Select a demo above.")



st.markdown('<h1>Deporte de precisión</h1>', unsafe_allow_html=True)

image = Image.open("image/roc.jpg")
st.image(image, width=900)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<h3>Montañas</h3>', unsafe_allow_html=True)

    st.markdown("""
    |**cluster** | Rutas en 9 clusters diferentes que pueden ser más o menos identificados como|
    |---|---|
    |0 | Rutas blandas|
    |1 | Rutas por alguna razón preferidas por mujeres|
    |2 | Rutas famosas|
    |3 | Rutas muy duras|
    |4 | Rutas muy repetidas|
    |5 | Chipped rutas, con tarifa blanda|
    |6 | Rutas tradicionales, no chippeadas|
    |7 | Rutas fáciles a vista, poco repetidas|
    |8 | Rutas muy famosas pero no tan repetidas y no tan tradicionales|""")

with col2:
    st.markdown('<h3>Ecalador</h3>', unsafe_allow_html=True)

    st.markdown("""
        date_first -> fecha de la primera ascensión

        date_last -> fecha de la última ascensión

        grades_first -> grado de la primera ascensión

        grades_last -> grado de la última ascensión

        years_cl -> años escalando

        grades_count -> número de vías realizadas por escalador

        year_first -> año de la primera ascensión

        year_last -> año de la última ascensión""")

st.markdown('<h3>Tabla de dificultades de los grados de escalada</h3>', unsafe_allow_html=True)


image = Image.open("image/dificultad.jpg")
st.image(image, width=600)


# 📋main.py
