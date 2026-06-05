import streamlit as st

st.title("Coding Challenge")

st.write("Make a loop that prints numbers 1 to 5")

answer = st.text_area("Your Code")

if st.button("Check"):

    if "for" in answer and "range" in answer:
        st.success("Correct!")
    else:
        st.error("Try again")

