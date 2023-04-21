import streamlit as st
import pandas as pd
from PIL import Image


import sys
sys.path.append("../")

import src.graficas as gr

st.set_page_config(layout='wide')

# ---------------------------------------------------------Datos--------------------------------------------------------------

scaler = pd.read_csv("data/climber_df.csv", index_col=0)


# --------------------------------------------------------Selectores-----------------------------------------------------------

st.sidebar.markdown('<h4>Filto para la condicion optima</h4>', unsafe_allow_html=True)
columna = st.sidebar.selectbox("Clasificación", ["Edad", "País", "Peso", "Experiencia"])

st.sidebar.markdown('<h4>Paises a comparar</h4>', unsafe_allow_html=True)
lista = scaler["country"].unique()
p1 = st.sidebar.selectbox("Pais 1", lista)
p2 = st.sidebar.selectbox("Pais 2", lista[::-1])

st.sidebar.markdown('<h4>Seleción de perfil para escaladores</h4>', unsafe_allow_html=True)
peso = st.sidebar.number_input("Peso", 40,140)
xp = st.sidebar.number_input("Experiencia", 1,40)
edad = st.sidebar.number_input("Edad", 5, 100)

# --------------------------------------------------------Funciones-----------------------------------------------------------

def fun1():
    gr.dep_val(scaler)
    graf1 = st.image("image/dep_val.jpg", width=1100)
    return graf1

def fun2():
    sip = {"Edad": "age" , "Experiencia": "years_cl", "País": "country" , "Peso":"weight" }
    
    gr.grad_max_country(scaler, sip[columna], columna)
    if columna == "País":
        graf2 = st.image("image/exlu.jpg", width=1100)
    else:
        graf2 = st.image("image/exlu.jpg", width=900)
    return graf2

def fun3():
    gr.comp(scaler, p1, p2)
    graf3 = st.image("image/comp.jpg", width=800)

    return graf3


# --------------------------------------------------------Contenido-----------------------------------------------------------

st.markdown('<h1>Escaladores</h1>', unsafe_allow_html=True)

image = Image.open("image/escalador.jpg")
st.image(image, width=1100)
st.markdown("En esta página se intentará sacar una conclusión sobre los factores que determinan la habilidad de un escalador.")

st.markdown("---")

st.markdown('<h2>Que factores tienen relación con el nivel del escalador</h2>', unsafe_allow_html=True)
with st.spinner('Cargando datos... Espere un monento'):

    fig1 = fun1()
    st.markdown("""Se puede ver qué características tienen influencia en el grado máximo al que se puede llegar en la escalada. 
    En este caso, la única que parece no tener relevancia es la altura, o al menos no tanta como las otras.""")

st.markdown("---")

st.markdown('<h2>Parametros de escalada</h2>', unsafe_allow_html=True)

with st.spinner('Cargando datos... Espere un monento'):

    st.markdown('Sabiendo cuales son las más relevantes \n ¿Qué grupo tiene mayor capacidad?\n', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,6])
    with col2:
        gig2 = fun2()

    st.markdown('Se puede observar que hay paises con una que tiene a escaladores con marcas más altas, pero, ¿Sera por los parametros que emos determinado anteriormente como los mas optimos?', unsafe_allow_html=True)

st.markdown("---")
st.markdown('<h2>Comparación de es escaladores por país</h2>', unsafe_allow_html=True)

with st.spinner('Cargando datos... Espere un monento'):

    col1, col2, col3 = st.columns([1,2,6])
    with col2:
        gig3 = fun3()
    
    st.markdown("""Es notoria la diferencia en las características de cada país, y con esto podemos concluir que el peso, la edad, la experiencia y 
    la dificultad media que se escala son influencias muy grandes en la escalada. La siguiente pregunta que surge después de ver la diferencia entre 
    los países es: ¿cuál es el factor diferencial para que en un país los ciudadanos se apeguen más a la escalada?""")

st.markdown("---")
st.markdown('<h2>Estadísticas escaladores</h2>', unsafe_allow_html=True)

with st.spinner('Cargando datos... Espere un monento'):
    st.markdown("""Aquí dejo un filtro por si se quiere ver las estadísticas de un determinado grupo de personas. Los filtros se encontrarán en la parte 
        derecha bajo el enunciado "Selección de perfil de escaladores".""")
    best_sacler = scaler[(scaler["age"] >= edad-2) & (scaler["age"] <= edad+2) & (scaler["weight"] >= peso-2) & (scaler["weight"] <= peso+2) & (scaler["years_cl"] >= xp) & (scaler["years_cl"] <= xp+2)]
    if best_sacler.shape[0] > 0:
        st.write(best_sacler)
    else:
        st.error("No se encuentran coincidencias.")


