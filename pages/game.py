import streamlit as st

st.title("NanoFood Defender Game")

st.write("Choose the correct nanoparticle for food spoilage problem")

answer = st.radio(
"Problem: bacterial contamination",
[
"Silver nanoparticle",
"Titanium dioxide",
"Nano starch"
])

if st.button("Submit"):

    if answer == "Silver nanoparticle":
        st.success("Correct! Silver nanoparticles have antimicrobial properties.")
    else:
        st.error("Incorrect. Try again.")
        