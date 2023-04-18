
import streamlit as st
import pandas as pd
import sqlalchemy as alch

import sys
sys.path.append("../")
import src.graficas as gr

st.markdown('<h1>La montaña ideal</h1>', unsafe_allow_html=True)

st.image("../image/montaña.jpg")

dif = pd.read_csv("../data/grades_conversion_table.csv", index_col=0)
dif['grade_id'] = dif['grade_id'].astype('int64')
mountain = pd.read_csv("../data/routes2.csv", index_col=0)


# st.write(name_bd)
def limp(looc):
    looc.strip("()")
    looc.split(",")

    return looc



peleadores = []

col1, col2, col3 = st.columns(3)

with col1:
    peso = st.number_input("Peso.", 40,140)

with col2:
    altura = st.number_input("Altura.", 100, 220)

with col3:
    edad = st.number_input("Edad.", 16, 100)

with col1:
    pais = st.text_input("Pais.", "")

with col2:
    grade = st.selectbox("Dificultad ultima escalada.", ['5', '5a', '5a+', '5b', '5b+',
       '5c', '5c+', '6', '6a', '6a/+', '6a+', '6a+/6b', '6b', '6b/+',
       '6b+', '6b+/6c', '6c', '6c/+', '6c+', '6c+/7a', '7a', '7a/+',
       '7a+', '7a+/7b', '7b', '7b/+', '7b+', '7b+/7c', '7c', '7c/+',
       '7c+', '7c+/8a', '8a', '8a/+', '8a+', '8a+/8b', '8b', '8b/+',
       '8b+', '8b+/8c', '8c', '8c/+', '8c+', '8c+/9a', '9a', '9a/+',
       '9a+', '9a+/9b', '9b', '9b/+', '9b+', '9b+/9c', '9c', '9c/+',
       '9c+', '9c+/10a'])
st.write(grade)
grade2 = 0
st.write(mountain.shape)


if  grade or pais!= "":

    if st.button("Montañas"):


        for i, f in dif.iterrows():

            if grade == f["grade_fra"]:
                grade2 = f["grade_id"]
                break

        opcion = mountain[((mountain["grade_mean"] < grade2+4) & (mountain["grade_mean"] > grade2-4)) & (mountain["country"] == pais)]

        st.write(opcion.head(20))
        df = opcion[["lat", "lon"]]


        st.map(df)
    else:
        st.write("parametros insuficientes.")

else: 

    st.write("...")
    # with col2:
    #     q_2 = f"""
    #     select * from peleador
    #     where peleador REGEXP "{peleador_b}";
    #     """
    #     df_2 = pd.read_sql(q_2, base)

    #     options = df_2['peleador'].tolist()

    #     peleador_2 =  st.selectbox("Elige el peleador", options)

    #     st.write("Has elegido:", peleador_2)

    # grafic = st.radio("Seleciona la gráfica que quieres analizar 👉", ["radar", "barplot", "img_golpeo"])

    # if st.button("Visualizar"):

#         peleadores.append(peleador_1)
#         peleadores.append(peleador_2)

#         if grafic == "radar":
#             gr.comparate(peleadores, base)
#             st.image("images/radar.png")

#         elif grafic == "barplot":
#             gr.stats(peleadores, base)
#             st.image("images/comparacion_total.png")

#         elif grafic == "img_golpeo":
#             gr.m_golpeo(peleadores, base)
#             st.image("images/golpeo.png")
#         else:
#             st.write("No se ha podido generar la gráfica 😢😢")
            

# else:
#     st.write("Generando desplegable...")S

