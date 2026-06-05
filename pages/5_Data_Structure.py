import streamlit as st

st.title("Data Structure Explorer")

data = st.text_input("Enter numbers separated by comma")

if data:

    numbers = list(map(int,data.split(",")))

    st.write("List:", numbers)

    st.write("Sorted:", sorted(numbers))

    st.write("Length:", len(numbers))

