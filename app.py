import streamlit as st

st.set_page_config(
    page_title="NanoFood Intelligence Lab",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {display:none;}
</style>
""", unsafe_allow_html=True)

# Background
st.markdown("""
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1581093458791-9d42e07b8b6a");
background-size: cover;
background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)

# Navbar
menu = st.columns(6)

with menu[0]:
    st.page_link("app.py", label="Home")

with menu[1]:
    st.page_link("pages/learn.py", label="Learn")

with menu[2]:
    st.page_link("pages/nano_simulator.py", label="Simulation")

with menu[3]:
    st.page_link("pages/visualization.py", label="Visualization")

with menu[4]:
    st.page_link("pages/coding_lab.py", label="Coding Lab")

with menu[5]:
    st.page_link("pages/game.py", label="Game")


# Hero Section
st.markdown("""
<h1 style='text-align:center;font-size:60px;color:white;'>
NanoFood Intelligence Lab
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;color:white;'>
Interactive Platform for Food Nanotechnology
</h3>
""", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/9/9b/Nanotechnology.png", use_container_width=True)

# Feature Section
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Learn Nanotech")
    st.write("Explore nano materials used in food science.")

with col2:
    st.subheader("Nano Simulation")
    st.write("Visualize nanoparticle behavior in food systems.")

with col3:
    st.subheader("Coding Lab")
    st.write("Practice programming logic interactively.")