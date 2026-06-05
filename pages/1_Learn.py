import streamlit as st

st.title("Learning Module")
st.title("This is a title")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

topic = st.selectbox(
    "Choose topic",
    ["Algorithm", "Python Basics", "Conditional", "Loop", "Data Structure", "Function"]
)

if topic == "Algorithm":
    st.write("Algorithm is a step-by-step procedure to solve a problem.")

elif topic == "Python Basics":
    st.code("""
x = 5
y = 10
print(x+y)
""")

elif topic == "Conditional":
    st.code("""
if x > 5:
    print("Big")
else:
    print("Small")
""")

elif topic == "Loop":
    st.code("""
for i in range(5):
    print(i)
""")

elif topic == "Data Structure":
    st.code("""
numbers = [1,2,3,4]
print(numbers[0])
""")

elif topic == "Function":
    st.code("""
def greet(name):
    print("Hello", name)
""")
