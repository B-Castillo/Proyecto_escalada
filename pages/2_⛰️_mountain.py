import streamlit as st
import pandas as pd
from PIL import Image
from streamlit_folium import folium_static
import folium
import os



import sys
sys.path.append("../")

import src.graficas as gr

mountain = pd.read_csv("data/routes2.csv", index_col=0)
mon_limp = mountain["pais"].value_counts()[:31].reset_index()
lista = mon_limp["index"].to_list()
new_mon = mountain[mountain["pais"].isin(lista)]
mon_limp_10 = mon_limp[:10]


def fun1(new_mon):
    gr.grad_mean(new_mon)
    graf1 = st.image("image/grad_mean.jpg", width=1100)
    return graf1

def fun2(new_mon):
    sip = {"Blandas":0, "Preferidas por mujeres":1, "Famosas":2, "Muy duras":3, "Muy repetidas":4,
    "Asperas":5, "Tradicionales":6, "Fáciles a vista":7, "no tan tradicionales":8}
    mejor_por  = new_mon[(new_mon["cluster"] == sip[clus])]
    df = mejor_por[["lat", "lon"]]
    
    st.map(df)

def fun2_1(df, pais):
    pai  = df[(df["pais"] == pais)]

    pai = pai.reset_index(drop=True)

    m = folium.Map(location=[pai["lat"][0], pai["lon"][0]], zoom_start=3)

    # Agregar capa topográfica
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri World Topo Map',
        overlay=False,
        control=True).add_to(m)

    # Agregar marcadores para cada ubicación en el DataFrame
    for i, row in pai.iterrows():
        if i == 0:
            pass
        else:
            folium.Marker(location=[row['lat'], row['lon']]).add_to(m)

    # Mostrar mapa en Streamlit
    folium_static(m, width=1100, height=600)

def fun3(mon_limp_10):
    gr.tarta_country(mon_limp_10)
    graf3 = st.image("image/tarta.jpg", width=1100)
    return graf3





st.markdown('<h1>Montañas, escalada al aire libre</h1>', unsafe_allow_html=True)

lista = new_mon["pais"].unique()

clus = st.sidebar.selectbox("Rutas",["Blandas", "Preferidas por mujeres", "Famosas", "Muy duras", "Muy repetidas",
    "Asperas", "Tradicionales", "Fáciles a vista", "no tan tradicionales"])

pais = st.sidebar.selectbox("Pais", lista)

image = Image.open("image/best_mountain.jpg")
st.image(image, width=1100)


with st.spinner('Cargando datos... Espere un monento'):

    st.markdown('<h4>Los paises con mayor cantidad de montañas conocidas para escalar.</h4>', unsafe_allow_html=True)
    fun3(mon_limp_10)
    st.markdown("---")

with st.spinner('Cargando datos... Espere un monento'):
    st.markdown('<h4>Ranking de dificultadad media</h4>', unsafe_allow_html=True)
    fun1(new_mon)
    st.markdown("---")
    url = os.getenv("url")
    gr.super_map()

# w1 = Keplergl(height=400)
# country_gdf = geopandas.read_file(url)
# w1.add_data(data=country_gdf, name="state")

with st.spinner('Cargando datos... Espere un monento'):
    st.markdown('<h4>Tipos de rutas.</h4>', unsafe_allow_html=True)
    fun2_1(new_mon, pais)
    st.markdown("---")





