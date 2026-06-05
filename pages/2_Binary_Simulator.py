import streamlit as st

st.title("Binary Converter Simulator")

number = st.number_input("Enter decimal number", min_value=0)

if st.button("Convert"):

    n = int(number)
    steps = []

    while n > 0:
        remainder = n % 2
        steps.append(remainder)
        n = n // 2

    binary = "".join(map(str, steps[::-1]))

    st.subheader("Binary Result")
    st.success(binary)

    st.write("Conversion steps:")
    st.write(steps)
