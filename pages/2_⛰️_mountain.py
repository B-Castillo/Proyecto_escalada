import streamlit as st
import pandas as pd
from PIL import Image

import sys
sys.path.append("../")

import src.graficas as gr

mountain = pd.read_csv("data/routes2.csv", index_col=0)
mon_limp = mountain["pais"].value_counts()[:31].reset_index()
lista = mon_limp["index"].to_list()
new_mon = mountain[mountain["pais"].isin(lista)]
mon_limp_10 = mon_limp[:10]


def fun1():
    gr.grad_mean(new_mon)
    graf1 = st.image("image/grad_mean.jpg")
    return graf1

def fun2():
    sip = {"Blandas":0, "Preferidas por mujeres":1, "Famosas":2, "Muy duras":3, "Muy repetidas":4,
    "Asperas":5, "Tradicionales":6, "Fáciles a vista":7, "no tan tradicionales":8}
    mejor_por  = new_mon[(new_mon["cluster"] == sip[clus])]
    df = mejor_por[["lat", "lon"]]
    
    st.map(df)

def fun3():
    gr.tarta_country(mon_limp_10)
    graf3 = st.image("image/tarta.jpg")
    return graf3





st.markdown('<h1>Montañas, escalada al aire libre</h1>', unsafe_allow_html=True)

clus = st.sidebar.selectbox("Rutas",["Blandas", "Preferidas por mujeres", "Famosas", "Muy duras", "Muy repetidas",
    "Asperas", "Tradicionales", "Fáciles a vista", "no tan tradicionales"])

image = Image.open("image/best_mountain.jpg")
st.image(image, width=900)


with st.spinner('Cargando datos... Espere un monento'):
    fun1()

    fun2()

    fun3()





