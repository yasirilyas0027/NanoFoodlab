import streamlit as st

st.markdown(
    """
    <style>

    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/visualization-nano-particle-molecule-showcasing-nanotechnology-biotechnology-concepts_1335075-29149.jpg?w=1480");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="NanoFood Intelligence Lab",
    page_icon="🔬",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background:#F8FAFC;
}

.hero{
    background:linear-gradient(
        135deg,
        #0F172A,
        #1E293B
    );

    padding:40px;
    border-radius:20px;
    text-align:center;
    margin-bottom:25px;
}

.hero h1{
    color:white;
    font-size:48px;
}

.hero h3{
    color:#06B6D4;
}

.hero p{
    color:white;
    font-size:18px;
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    border-left:6px solid #06B6D4;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    min-height:220px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>🔬 NanoFood Intelligence Lab</h1>

<h3>
Interactive Platform for Food Nanotechnology
</h3>

<p>
A comprehensive digital platform integrating
laboratory calculations,
nanomaterial characterization,
food packaging evaluation,
bioactivity analysis,
and educational resources.
</p>

</div>
""", unsafe_allow_html=True)

st.success(
"Designed for Food Nanotechnology Education, Research and Laboratory Applications"
)

m1,m2,m3,m4 = st.columns(4)

with m1:
    st.metric("Calculators", "20+")

with m2:
    st.metric("Learning Modules", "30+")

with m3:
    st.metric("Characterization Tools", "10+")

with m4:
    st.metric("Research Areas", "8")


st.subheader("Platform Features")

c1,c2,c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class="card">

    <h3>🧪 Laboratory Calculator</h3>

    <p>
    Advanced calculations for:
    dilution,
    molarity,
    yield,
    encapsulation efficiency,
    IC50,
    EC50,
    and more.
    </p>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">

    <h3>🔬 Characterization Tools</h3>

    <p>
    XRD,
    FTIR,
    Particle Size Analysis,
    Zeta Potential,
    Scherrer Equation,
    and material interpretation.
    </p>

    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="card">

    <h3>📦 Food Packaging Analysis</h3>

    <p>
    WVTR,
    Moisture Content,
    Water Solubility,
    Swelling Index,
    and Biodegradation Analysis.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.subheader(
    "Food Nanotechnology Research Areas"
)

r1,r2,r3,r4 = st.columns(4)

with r1:
    st.info("""
    Nanoencapsulation

    • Controlled Release
    • Bioactive Compounds
    • Functional Ingredients
    """)

with r2:
    st.info("""
    Nanoparticles

    • ZnO
    • TiO₂
    • Silver NP
    • Chitosan NP
    """)

with r3:
    st.info("""
    Active Packaging

    • Antimicrobial Film
    • Smart Packaging
    • Nanocomposite
    """)

with r4:
    st.info("""
    Food Analysis

    • UV-Vis
    • FTIR
    • XRD
    • Antioxidant Activity
    """)

st.markdown("---")

st.markdown("""
<div style="text-align:center">

<h3>NanoFood Intelligence Lab</h3>

<p>
Version 1.0.0
</p>

<p>
Developed by <b>Putri Aprilia</b>, <b>Sifa Resti Nur Cahyanti</b>, and <b>Yasir Ilyas</b>
</p>

<p>
Department of Food Nanotechnology<br>
Politeknik AKA Bogor
</p>

<p>
2026
</p>

</div>
""", unsafe_allow_html=True)

