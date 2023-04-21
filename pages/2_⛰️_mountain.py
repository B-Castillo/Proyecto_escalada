import streamlit as st
import pandas as pd
from PIL import Image

import sys
sys.path.append("../")

import src.graficas as gr

st.set_page_config(layout='wide')

# ---------------------------------------------------------Datos--------------------------------------------------------------

mountain = pd.read_csv("data/routes2.csv", index_col=0)
mon_limp = mountain["pais"].value_counts()[:31].reset_index()
lista1 = mon_limp["index"].to_list()
new_mon = mountain[mountain["pais"].isin(lista1)]
mon_limp_10 = mon_limp[:10]
lista2 = new_mon["pais"].unique()


# --------------------------------------------------------Funciones-----------------------------------------------------------

def fun1(new_mon):
    gr.grad_mean(new_mon)
    graf1 = st.image("image/grad_mean.jpg", width=1100)
    return graf1

def fun3(mon_limp_10):
    gr.tarta_country(mon_limp_10)
    graf3 = st.image("image/tarta.jpg", width=900)
    return graf3


# --------------------------------------------------------Contenido-----------------------------------------------------------


st.markdown('<h1>Montañas, escalada al aire libre</h1>', unsafe_allow_html=True)

image = Image.open("image/best_mountain.jpg")
st.image(image, width=1100)

st.markdown("""Después de determinar las características necesarias para ser un buen escalador, procederemos a ver si los países o sus costumbres 
tienen algo que ver con la habilidad de sus escaladores.""")

st.markdown("---")



with st.spinner('Cargando datos... Espere un monento'):

    st.markdown('<h4>Los paises con mayor cantidad de montañas conocidas para escalar.</h4>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,6])
    with col2:
        fun3(mon_limp_10)
    
    st.markdown("""Se observa una gran diferencia en cuanto a las montañas que suelen recibir escaladores, considerando los 10 países con más montañas. 
    Hay una clara superioridad numérica, pero esto puede deberse a la extensión de dichos países. Si bien es cierto que algunos países como Brasil, 
    Canadá o México superan ampliamente a España, Alemania o Reino Unido en extensión, estos últimos países también tienen una importante presencia de 
    montañas y, por lo tanto, reciben a un número significativo de escaladores.""")

st.markdown("---")

with st.spinner('Cargando datos... Espere un monento'):
    st.markdown('<h4>Ranking de dificultadad media</h4>', unsafe_allow_html=True)
    fun1(new_mon)

    st.markdown("""El ranking de dificultad media sigue siendo liderado por los países europeos, aunque también se cuelan algunos países americanos como 
    Canadá y Estados Unidos. Estas tendencias coinciden con las conclusiones obtenidas al analizar los datos de los escaladores. Para concluir, el 
    siguiente paso será analizar el tipo de ascensores que se encuentran en cada país.""")

st.markdown("---")

with st.spinner('Cargando datos... Espere un monento'):
    st.markdown('<h4>Tipos de rutas.</h4>', unsafe_allow_html=True)
    gr.super_map()
    # fun2_1(new_mon, pais)

    st.markdown("""Hemos visto que las rutas preferidas y las más abundantes son las famosas, lo que indica que se trata de una actividad lúdica. 
    Sin embargo, hay países en los que las rutas muy difíciles son más numerosas que en otros, y esto puede ser indicativo de que en esos países 
    hay escaladores más experimentados y competentes.""")

    st.markdown("---")

    st.markdown('<h4>Medallero olímpico de escalada</h4>', unsafe_allow_html=True)

    st.image("image/escalada_tokio.jpg", width= 1100)

    st.markdown("""En esta imagen se puede observar cómo los países con los escaladores más competentes y las montañas con ascensiones más duras 
    suelen tener atletas en el podio olímpico de escalada. A veces no nos damos cuenta de la influencia que puede tener nuestro entorno en nosotros, 
    y es posible que este deporte, la escalada, esté arraigado en algunas culturas. Después de este análisis, podemos concluir que, además de las 
    características necesarias para escalar, también influye el origen del escalador.""")