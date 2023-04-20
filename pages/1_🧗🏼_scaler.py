import streamlit as st
import pandas as pd
from PIL import Image


import sys
sys.path.append("../")

import src.graficas as gr

scaler = pd.read_csv("data/climber_df.csv", index_col=0)

st.markdown('<h1>Los escaladores</h1>', unsafe_allow_html=True)

image = Image.open("image/escalador.jpg")
st.image(image, width=1100)

def fun1():
    gr.dep_val(scaler)
    graf1 = st.image("image/dep_val.jpg")
    return graf1

def fun2():
    sip = {"Edad": "age" , "Experiencia": "years_cl", "País": "country" , "Peso":"weight" }
    
    gr.grad_max_country(scaler, sip[columna], columna)
    graf2 = st.image("image/exlu.jpg")
    return graf2

def fun3():
    gr.comp(scaler, p1, p2)
    graf3 = st.image("image/comp.jpg")
    return graf3


st.markdown('<h3>Que factores tienen relación con el nivel del escalador</h3>', unsafe_allow_html=True)

st.sidebar.markdown('<h4>Filto para la condicion optima</h4>', unsafe_allow_html=True)
columna = st.sidebar.selectbox("Clasificación", ["Edad", "País", "Peso", "Experiencia"])

st.sidebar.markdown('<h4>Seleción de perfil para escaladores</h4>', unsafe_allow_html=True)
peso = st.sidebar.number_input("Peso", 40,140)
xp = st.sidebar.number_input("Experiencia", 1,40)
edad = st.sidebar.number_input("Edad", 5, 100)

st.sidebar.markdown('<h4>Seleción de perfil para escaladores</h4>', unsafe_allow_html=True)

lista = scaler["country"].unique()

col1, col2 = st.sidebar.columns(2)

with col1:
    p1 = st.sidebar.selectbox("Pais 1", lista)

with col2:
    p2 = st.sidebar.selectbox("Pais 2", lista[::-1])

with st.spinner('Cargando datos... Espere un monento'):

    fig1 = fun1()
    st.text("Se pued ver que caracteristicas tiene influencia Grado maximo al que se puede llegar en las escalada")

with st.spinner('Cargando datos... Espere un monento'):

    st.markdown('<h4>Sabiendo cuales son las más relevantes \n ¿Qué grupo tiene mayor capacidad?\n</h4>', unsafe_allow_html=True)

    gig2 = fun2()

    st.markdown('Se puede observar que hay paises con una que tiene a escaladores con marcas más altas, pero, ¿Sera por los parametros que emos determinado anteriormente como los mas optimos?', unsafe_allow_html=True)

with st.spinner('Cargando datos... Espere un monento'):

    gig3 = fun3()

best_sacler = scaler[(scaler["age"] >= edad) & (scaler["weight"] >= peso) & (scaler["years_cl"] >= xp)]
best_sacler = best_sacler[['grades_count', 'grades_first','grades_last', 'grades_max', 'grades_mean']]
st.write(best_sacler)
