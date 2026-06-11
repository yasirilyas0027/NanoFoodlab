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
font-size:64px;
font-weight:800;
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

Integrating laboratory calculations,
material characterization,
food packaging analysis,
bioactivity evaluation,
scientific databases,
and educational resources
into one platform.

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
    """,
    unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">

    <h3>🔬 Characterization Tools</h3>

    Researchers frequently use
    multiple software tools
    for analysis,
    characterization,
    and data interpretation.

    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="card">

    <h2>✅ Solution</h2>

    <p>
    WVTR,
    Moisture Content,
    Water Solubility,
    Swelling Index,
    and Biodegradation Analysis.
    </p>

    </div>
    """,
    unsafe_allow_html=True)

st.subheader(
    "Food Nanotechnology Research Areas"
)

r1,r2,r3,r4 = st.columns(4)

with r1:

    st.markdown("""
    <div class="dashboard">

    <h1>📈</h1>

    <h3>FTIR Analyzer</h3>

    Analyze functional groups
    based on infrared absorption bands.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/FTIR Analyzer.py",
        label="Open Tool"
    )

with r2:
    st.info("""
    Nanoparticles

    <h1>🧮</h1>

    <h3>Laboratory Calculator</h3>

    Scientific calculations
    for food nanotechnology laboratories.

    </div>
    """,
    unsafe_allow_html=True)

with r3:
    st.info("""
    Active Packaging

    • Antimicrobial Film
    • Smart Packaging
    • Nanocomposite
    """)

with r4:

    st.markdown("""
    <div class="dashboard">

    <h1>🛠</h1>

    <h3>Troubleshooting</h3>

    AI-assisted laboratory
    problem solving.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Laboratory Troubleshooting.py",
        label="Open"
    )

st.markdown(
'<div class="section-title">Food Nanotechnology Research Workflow</div>',
unsafe_allow_html=True
)

st.markdown("""
<div class="workflow">

📚 Literature Review

⬇

🧪 Material Selection

⬇

⚗ Synthesis

⬇

📈 Characterization

⬇

🧬 Bioactivity Analysis

⬇

📦 Packaging Evaluation

⬇

📝 Publication

</div>
""",
unsafe_allow_html=True)

st.markdown(
'<div class="section-title">Featured Laboratory Tools</div>',
unsafe_allow_html=True
)

f1,f2,f3 = st.columns(3)

with f1:

    st.markdown("""
    <div class="feature-card">

    <h1>🔬</h1>

    <h2>FTIR Analyzer</h2>

    Identify functional groups
    from FTIR absorption peaks.

    <br>

    <b>Capabilities:</b>

    <ul>
    <li>O-H Stretching</li>
    <li>N-H Stretching</li>
    <li>C=O Carbonyl</li>
    <li>C-O Functional Groups</li>
    <li>Aromatic Rings</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/FTIR Analyzer.py",
        label="Open FTIR Analyzer"
    )

with f2:

    st.markdown("""
    <div class="feature-card">

    <h1>📈</h1>

    <h2>XRD Calculator</h2>

    Analyze crystalline
    nanomaterials using XRD data.

    <br>

    <b>Capabilities:</b>

    <ul>
    <li>Scherrer Size</li>
    <li>Crystallinity Index</li>
    <li>d-spacing</li>
    <li>Bragg Analysis</li>
    <li>Peak Interpretation</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Laboratory Calculator.py",
        label="Open XRD Tools"
    )

with f3:

    st.markdown("""
    <div class="feature-card">

    <h1>🧪</h1>

    <h2>IC50 Calculator</h2>

    Bioactivity evaluation
    for antioxidant and inhibition assays.

    <br>

    <b>Capabilities:</b>

    <ul>
    <li>Linear Regression</li>
    <li>IC50 Estimation</li>
    <li>Dose Response Analysis</li>
    <li>Data Visualization</li>
    <li>Curve Interpretation</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Laboratory Calculator.py",
        label="Open IC50 Tools"
    )

st.markdown(
'<div class="section-title">Platform Statistics</div>',
unsafe_allow_html=True
)

s1,s2,s3,s4 = st.columns(4)

with s1:
    st.metric(
        "Integrated Modules",
        "8+"
    )

with s2:
    st.metric(
        "Laboratory Calculators",
        "10+"
    )

with s3:
    st.metric(
        "Scientific References",
        "100+"
    )

with s4:
    st.metric(
        "Research Workflow",
        "Complete"
    )

st.markdown(
'<div class="section-title">Why Choose NanoFood Intelligence Lab?</div>',
unsafe_allow_html=True
)

w1,w2,w3,w4 = st.columns(4)

with w1:

    st.markdown("""
    <div class="choose-card">

    <h1>🔬</h1>

    <h3>Research-Oriented</h3>

    Designed specifically
    for nanotechnology
    and food science research.

    </div>
    """,
    unsafe_allow_html=True)

with w2:

    st.markdown("""
    <div class="choose-card">

    <h1>💡</h1>

    <h3>User Friendly</h3>

    Simple interface
    for students,
    researchers,
    and laboratory staff.

    </div>
    """,
    unsafe_allow_html=True)

with w3:

    st.markdown("""
    <div class="choose-card">

    <h1>⚗</h1>

    <h3>Laboratory Ready</h3>

    Supports routine
    laboratory calculations
    and characterization.

    </div>
    """,
    unsafe_allow_html=True)

with w4:

    st.markdown("""
    <div class="choose-card">

    <h1>📚</h1>

    <h3>Educational</h3>

    Combines theory,
    calculation,
    and interpretation.

    </div>
    """,
    unsafe_allow_html=True)

st.markdown(
'<div class="section-title">Quick Access</div>',
unsafe_allow_html=True
)

q1,q2,q3 = st.columns(3)

with q1:

    st.markdown("""
    <div class="quick-card">
    <h1>🔬</h1>
    <h3>FTIR Analyzer</h3>
    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/FTIR Analyzer.py",
        label="Open"
    )

with q2:

    st.markdown("""
    <div class="quick-card">
    <h1>🧪</h1>
    <h3>Laboratory Calculator</h3>
    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Laboratory Calculator.py",
        label="Open"
    )

with q3:

    st.markdown("""
    <div class="quick-card">
    <h1>📚</h1>
    <h3>Material Database</h3>
    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Food Nanotech Material Database.py",
        label="Open"
    )

q4,q5,q6 = st.columns(3)

with q4:

    st.markdown("""
    <div class="quick-card">
    <h1>🛠</h1>
    <h3>Troubleshooting</h3>
    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/shooting.py",
        label="Open"
    )

with q5:

    st.markdown("""
    <div class="quick-card">
    <h1>📖</h1>
    <h3>About Nanotechnology</h3>
    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/About Nanotechnology.py",
        label="Open"
    )

with q6:

    st.markdown("""
    <div class="quick-card">
    <h1>🎨</h1>
    <h3>Visualization</h3>
    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/visualization.py",
        label="Open"
    )

st.markdown("""
<div style="text-align:center">

<h1>
🔬 NanoFood Intelligence Lab
</h1>

<p>
Version 1.0.0
</p>

<br>

<b>Developed For</b>

<br><br>

Research

<br>

Education

<br>

Laboratory Applications

<br><br>

━━━━━━━━━━━━━━━━━━━━━━

<br><br>

Food Nanotechnology • Characterization • Bioactivity Analysis • Packaging Science

<br><br>

© 2026 NanoFood Intelligence Lab

</div>
""", unsafe_allow_html=True)



































