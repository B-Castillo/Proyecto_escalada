import streamlit as st
import pandas as pd
from PIL import Image

st.markdown('<h1>Montañas, escalada al aire libre</h1>', unsafe_allow_html=True)

image = Image.open("image/best_mountain.jpg")
st.image(image, width=900)
