import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Nano Visualization")

data = pd.DataFrame({
"Particle Size":[10,20,30,40],
"Surface Area":[100,200,350,500]
})

fig = px.line(data,x="Particle Size",y="Surface Area")

st.plotly_chart(fig)
