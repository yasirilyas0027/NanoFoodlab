import streamlit as st

st.title("Python Coding Lab")

code = st.text_area("Write Python code")

if st.button("Run"):
    st.write("Your code:")
    st.code(code)
    