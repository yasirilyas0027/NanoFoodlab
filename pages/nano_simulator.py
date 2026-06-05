import streamlit as st

st.title("Nanoparticle Size Simulator")

size = st.slider("Particle Size (nm)",1,100,10)

surface_area = size * 10

st.write("Estimated Surface Area:", surface_area)

st.write("Smaller nanoparticles have higher surface interaction with food components.")