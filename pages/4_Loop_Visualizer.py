import streamlit as st

st.title("Loop Visualizer")

n = st.slider("Number of iterations",1,20)

st.write("Loop Output")

for i in range(n):
    st.write("Iteration", i)

