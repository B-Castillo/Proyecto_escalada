
import streamlit as st
import pandas as pd
from PIL import Image


import sys
sys.path.append("../")
import src.graficas as gr

st.markdown('<h1>La montaña ideal</h1>', unsafe_allow_html=True)

image = Image.open("image/montaña.jpg")
st.image(image, width=900)

dif = pd.read_csv("data/grades_conversion_table.csv", index_col=0)
dif['grade_id'] = dif['grade_id'].astype('int64')
mountain = pd.read_csv("data/routes2.csv", index_col=0)


lista = mountain["pais"].unique()

col1, col2 = st.columns(2)

with col1:
    pais = st.selectbox("Pais", lista)

with col2:
    grade = st.selectbox("Dificultad ultima escalada.", ['5', '5a', '5a+', '5b', '5b+',
       '5c', '5c+', '6', '6a', '6a/+', '6a+', '6a+/6b', '6b', '6b/+',
       '6b+', '6b+/6c', '6c', '6c/+', '6c+', '6c+/7a', '7a', '7a/+',
       '7a+', '7a+/7b', '7b', '7b/+', '7b+', '7b+/7c', '7c', '7c/+',
       '7c+', '7c+/8a', '8a', '8a/+', '8a+', '8a+/8b', '8b', '8b/+',
       '8b+', '8b+/8c', '8c', '8c/+', '8c+', '8c+/9a', '9a', '9a/+',
       '9a+', '9a+/9b', '9b', '9b/+', '9b+', '9b+/9c', '9c', '9c/+',
       '9c+', '9c+/10a'])

grade2 = 0

if  grade or pais!= "":

    if st.button("Montañas"):


        for i, f in dif.iterrows():

            if grade == f["grade_fra"]:
                grade2 = f["grade_id"]
                break

        opcion = mountain[((mountain["grade_mean"] < grade2+4) & (mountain["grade_mean"] > grade2-4)) & (mountain["pais"] == pais)]

        
        df = opcion[["lat", "lon"]]

        with st.spinner('Cargando datos... Espere un monento'):
            st.map(df)
            st.write(opcion.head(10))


