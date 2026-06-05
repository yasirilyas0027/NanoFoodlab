import streamlit as st

st.title("Python Playground")

code = st.text_area("Write Python Code")

if st.button("Run Code"):

    try:
        exec(code)
    except Exception as e:
        st.error(e)

