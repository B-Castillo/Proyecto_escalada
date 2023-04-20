import numpy as np
import pandas as pd
import streamlit as st
import os

# librerías de visualización
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from keplergl import KeplerGl


def grad_max_country(df_, columna, original):
    scaler_country = df_.groupby(columna)["grades_max"].median().reset_index()
    scaler_country = scaler_country.sort_values(by = "grades_max", ascending=False)

    plt.figure(figsize = (15, 6))
    
    # creación barplot

    df = scaler_country.copy()

    if original == "País":
        sns.scatterplot(data=df, x=columna, y="grades_max")

    else:
        sns.regplot(x = df[columna], y = df["grades_max"],
            color = "gray", 
            marker = ".", 
            scatter_kws = {"alpha": 0.4}, 
            line_kws = {"color": "blue", "alpha": 0.7 })


    plt.title(f"Mediana de grados por {original}")
    plt.xlabel(original) # para poner etiqueta en el eje x
    plt.ylabel("Máximo Grado") # para poner etiqueta en el eje y

    plt.savefig("image/exlu.jpg", bbox_inches='tight')


def dep_val(df_):
    fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize = (30, 15))

    axes = axes.flat

    columnas_numeric = df_.select_dtypes(include = np.number).columns[1:6]

    for i, colum in enumerate(columnas_numeric[1:]):
        sns.regplot(
            x = df_[colum], 
            y = df_["grades_max"], 
            color = "gray", 
            marker = ".", 
            scatter_kws = {"alpha": 0.4}, 
            line_kws = {"color": "red", "alpha": 0.7 }, 
            ax = axes[i])
        
        axes[i].set_title(f"Maximo escalado vs {colum}", fontsize = 20, fontweight = "bold")
        axes[i].tick_params(labelsize = 20)
        axes[i].set_xlabel("")
        axes[i].set_ylabel("")
    # fig.delaxes(axes[0])
        
    plt.savefig("image/dep_val.jpg", bbox_inches='tight')

def grad_mean(new_mon):
    mountain_country = new_mon.groupby("pais")["grade_mean"].mean().reset_index()
    df = mountain_country.sort_values(by = "grade_mean", ascending=False).head(10)

    fig = plt.figure(figsize = (30, 12))
    

    plt.bar(df["pais"], df["grade_mean"])

    plt.title(f"Median de dificultad por Pais")
    plt.xlabel("Paises") # para poner etiqueta en el eje x
    plt.ylabel("Median Grado") # para poner etiqueta en el eje y

    plt.savefig("image/grad_mean.jpg", bbox_inches='tight')

def tarta_country(mon_limp):
    fig = plt.figure(figsize = (25, 12))

    explode = (0, 0.1 ,0.1, 0, 0, 0.1, 0, 0.1, 0.2, 0) # para sacar los quesitos hacia fuera

    plt.pie(mon_limp['pais'],
        labels = mon_limp["index"],
        explode = explode)  # para sacar los quesitos hacia fuera

    plt.title("Total montañas por pais") # para poner el título
    plt.legend(bbox_to_anchor=(1.2, 1)) # sacar leyenda y donde colocarla. El primer índice (derecha-izquierda), segundo índice(arriba, abajo) )

    # fig = plt.figure(figsize = (30, 15))

    # px.pie(mon_limp, values='pais', names='index', 
    #     title='Total montañas por pais', # poner el título de la figura
    #     color_discrete_sequence = px.colors.sequential.haline, # para elegir la escala de colores
    #     )

    plt.savefig("image/tarta.jpg", bbox_inches='tight')

def comp(df, pais1, pais2):

    df_1 = df[(df["country"] == pais1)]
    df_2 = df[(df["country"] == pais2)]

    #Creamos una lista con las estadisticas que se van a comparar
    categorias = ['age', 'years_cl', 'weight' ,'grades_mean']
    
    #Creamos una lista con los argumentos de la primera y con el primer argumento en ultimo lugar par que se cierre gráfica.
    categorias = [*categorias, categorias[0]]
    
    #Creamos una lista con las estadisticas de los peleadores extraidas anteriormente de la BBDD.
    escalador_1 = [df_1["age"].median(), df_1["years_cl"].median(), df_1["weight"].median(), df_1["grades_mean"].median()]
    escalador_2 = [df_2["age"].median(), df_2["years_cl"].median(), df_2["weight"].median(), df_2["grades_mean"].median()]

    #Creamos una lista con los argumentos de la primera y con el primer argumento en ultimo lugar par que se cierre gráfica.
    escalador_1 = [*escalador_1, escalador_1[0]]
    escalador_2 = [*escalador_2, escalador_2[0]]
    
    #Generamos los angulos en los que se ubicara cada porcentaje, queremos que esten separados de forma uniforme 
    # y para eso utilizamos "linspace".
    angulos = np.linspace(start=0, stop=2 * np.pi, num=len(escalador_1))
    
    #Decidimos el tamaño de la figura.
    plt.figure(figsize=(10, 10))
    
    #Creamos el primer trazado de lineas, correspondiente al primer peleador.
    plt.polar(angulos, escalador_1, 'o-',
              label = f"{pais1}")
    
    #Creamos el segundo trazado de lineas, correspondiente al segundo peleador peleador.
    plt.polar(angulos, escalador_2, 'o-',
              label = f"{pais2}")
    
    #Para asignar los nombres de las estadisticas a los angulos.
    lines, labels = plt.thetagrids(np.degrees(angulos), labels=categorias)
    
    #Generamos ul titulo para la figura.
    plt.title('Porcentaje de acierto', size=20, y=1.05)
    
    #Y por ultimo generamos una leyenda para la figura.
    plt.legend()
    
    plt.savefig("image/comp.jpg", bbox_inches='tight')


def super_map():
    # URL de la página web que deseas mostrar
    url = os.getenv("url")

    # Mostrar página web en Streamlit usando un iframe
    return st.components.v1.html(f'<iframe src="{url}" width="100%" height="600px"></iframe>', height=600)

