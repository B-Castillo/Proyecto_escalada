
import streamlit as st
from PIL import Image


st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        layout='wide'
    )

st.sidebar.write("Empezamos  🔍")



st.markdown('<h1>Deporte de precisión</h1>', unsafe_allow_html=True)

image = Image.open("image/montaña.jpg")
st.image(image, width=1100)
st.markdown("En este análisis se busca encontrar los rasgos que conforman a un buen escalador y conocer más acerca de este hermoso deporte.")

st.markdown("---")

st.markdown('<h1>Datos</h1>', unsafe_allow_html=True)
col1, col2, col3 = st.columns([15,1,8])

with col1:
    st.markdown('<h3>Montañas</h3>', unsafe_allow_html=True)

    st.markdown("""
    |**cluster** | Rutas en 9 clusters diferentes que pueden ser más o menos identificados como|
    |---|---|
    |0 | Rutas blandas|
    |1 | Rutas preferidas por mujeres|
    |2 | Rutas famosas|
    |3 | Rutas muy duras|
    |4 | Rutas muy repetidas|
    |5 | Chipped rutas, con tarifa blanda|
    |6 | Rutas tradicionales, no chippeadas|
    |7 | Rutas fáciles a vista, poco repetidas|
    |8 | Rutas muy famosas pero no tan repetidas y no tan tradicionales|""")

with col3:
    st.markdown('<h3>Escalador</h3>', unsafe_allow_html=True)

    st.markdown("""
        sex -> 0 Hombre, 1 Mujer
    
        date_first -> fecha de la primera ascensión

        date_last -> fecha de la última ascensión

        grades_first -> grado de la primera ascensión

        grades_last -> grado de la última ascensión

        years_cl -> años escalando

        grades_count -> número de vías realizadas por escalador

        year_first -> año de la primera ascensión

        year_last -> año de la última ascensión""")
    
st.markdown("---")

st.markdown('<h2>Tabla de dificultades de los grados de escalada</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,3])
with col2:
    image = Image.open("image/dificultad.jpg")
    st.image(image, width=600)


# 📋main.py
