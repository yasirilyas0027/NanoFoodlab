import streamlit as st

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap');

html,
body,
[class*="css"]{
font-family:'Inter',sans-serif;
}

h1,h2,h3,h4{
font-family:'Montserrat',sans-serif;
}

.stApp{
background:#F4F8FC;
}

section{
margin-top:70px;
margin-bottom:70px;
}

.hero{
background:
linear-gradient(
135deg,
#071426,
#0F172A,
#102A43
);

padding:80px;
border-radius:30px;

position:relative;

overflow:hidden;

box-shadow:
0 20px 60px rgba(
0,
0,
0,
0.15
);
}

.hero-title{
font-size:72px;
font-weight:800;
color:white;
margin-bottom:20px;
}

.hero-subtitle{
font-size:26px;
font-weight:600;
color:#38BDF8;
margin-bottom:30px;
}

.hero-description{
font-size:20px;
line-height:1.8;
color:#E2E8F0;
max-width:950px;
}

.section-title{
font-size:42px;
font-weight:800;
color:#0F172A;
margin-top:70px;
margin-bottom:35px;
}

.card{
background:white;
border-radius:24px;
padding:35px;

box-shadow:
0 10px 30px rgba(
0,
0,
0,
0.08
);

transition:0.3s;

height:100%;
}

.card:hover{
transform:translateY(-8px);
}

.metric-card{
background:white;

border-radius:24px;

padding:35px;

text-align:center;

box-shadow:
0 8px 25px rgba(
0,
0,
0,
0.08
);
}

.tool-card{
background:white;

border-radius:24px;

padding:35px;

min-height:320px;

box-shadow:
0 10px 30px rgba(
0,
0,
0,
0.08
);

transition:0.3s;
}

.feature-tool{
background:white;
padding:35px;
border-radius:24px;
box-shadow:
0 10px 30px rgba(
0,
0,
0,
0.08
);

min-height:420px;

transition:0.3s;
}

.feature-tool:hover{
transform:translateY(-8px);
}

.feature-tool h2{
font-size:28px;
font-weight:700;
margin-bottom:15px;
color:#0F172A;
}

.feature-tool ul{
padding-left:20px;
line-height:2;
}

.domain-card{
background:white;

padding:35px;

border-radius:24px;

box-shadow:
0 10px 30px rgba(
0,
0,
0,
0.08
);

min-height:280px;

transition:0.3s;
}

.domain-card:hover{
transform:translateY(-8px);
}

.domain-card h3{
font-size:26px;
margin-bottom:15px;
color:#0F172A;
}

.quick-card{
background:
linear-gradient(
135deg,
#0F172A,
#1E293B
);

padding:40px;

border-radius:24px;

text-align:center;

color:white;

min-height:220px;

transition:0.3s;

box-shadow:
0 15px 35px rgba(
0,
0,
0,
0.15
);
}

.quick-card:hover{
transform:scale(1.03);
}

.quick-card h2{
font-size:28px;
margin-bottom:15px;
}

.impact-card{
background:white;

padding:35px;

border-radius:24px;

text-align:center;

box-shadow:
0 10px 30px rgba(
0,
0,
0,
0.08
);

min-height:220px;
}

.impact-card h2{
font-size:40px;
font-weight:800;
color:#06B6D4;
}

.impact-card h4{
margin-top:15px;
}

</style>
""",
unsafe_allow_html=True)

st.markdown("""

<div class="hero">

<div class="hero-title">
NanoFood Intelligence Lab
</div>

<div class="hero-subtitle">
Integrated Research Platform for Food Nanotechnology
</div>

</div>

""",
unsafe_allow_html=True)

st.markdown(
'<div class="section-title">Research Ecosystem</div>',
unsafe_allow_html=True
)

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""
    <div class="card">

    <h3>Laboratory Calculator</h3>

    Scientific calculations for
    dilution,
    molarity,
    yield
    encapsulation efficiency,
    IC50,
    EC50,
    release efficiency,
    WVTR and more.

    </div>
    """,unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class="card">

    <h3>Characterization Tools</h3>

    FTIR,
    XRD,
    particle size analysis,
    crystallinity,
    spectroscopy interpretation
    and analytical support.

    </div>
    """,unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class="card">

    <h3>Methods Library</h3>

    Experimental procedures,
    analytical methods,
    characterization workflows,
    laboratory protocols.

    </div>
    """,unsafe_allow_html=True)

with c4:
    
    st.markdown("""
    <div class="card">

    <h3>Nanomaterial Database</h3>

    ZnO,
    TiO₂,
    Chitosan,
    Silica,
    Silver,
    Gold nanoparticles
    and their applications.

    </div>
    """,unsafe_allow_html=True)


st.markdown(
'<div class="section-title">Scientific Research Workflow</div>',
unsafe_allow_html=True
)

st.markdown("""

<div class="card">

Literature Review

↓

Research Design

↓

Material Synthesis

↓

Characterization

↓

Bioactivity Analysis

↓

Packaging Evaluation

↓

Data Interpretation

↓

Publication

</div>

""",
unsafe_allow_html=True)

st.markdown(
"""
<div class="section-title">
Featured Scientific Tools
</div>
""",
unsafe_allow_html=True
)

f1,f2,f3 = st.columns(3)

with f1:

    st.markdown("""
    <div class="feature-tool">

    <h2>FTIR Analyzer</h2>

    Identify functional groups
    from FTIR absorption peaks.

    <br>

    <b>Capabilities</b>

    <ul>

    <li>Peak Identification</li>

    <li>Functional Group Analysis</li>

    <li>O–H Stretching</li>

    <li>C=O Carbonyl Detection</li>

    <li>Aromatic Ring Analysis</li>

    <li>Interpretation Assistance</li>

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
    <div class="feature-tool">

    <h2>Laboratory Calculator</h2>

    Comprehensive scientific
    calculations for food
    nanotechnology laboratories.

    <br>

    <b>Capabilities</b>

    <ul>

    <li>Dilution Calculator</li>

    <li>Molarity Calculator</li>

    <li>IC50 Calculator</li>

    <li>EC50 Calculator</li>

    <li>WVTR Calculator</li>

    <li>Release Efficiency</li>

    </ul>

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Laboratory Calculator.py",
        label="Open Laboratory Calculator"
    )

with f3:

    st.markdown("""
    <div class="feature-tool">

    <h2>Material Database</h2>

    Explore nanomaterials
    widely applied in food systems.

    <br>

    <b>Included Materials</b>

    <ul>

    <li>Zinc Oxide Nanoparticles</li>

    <li>Titanium Dioxide</li>

    <li>Chitosan Nanoparticles</li>

    <li>Silica Nanoparticles</li>

    <li>Silver Nanoparticles</li>

    <li>Gold Nanoparticles</li>

    </ul>

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Food Nanotech Material Database.py",
        label="Open Material Database"
    )

st.markdown(
"""
<div class="section-title">
Research Domains
</div>
""",
unsafe_allow_html=True
)

d1,d2,d3 = st.columns(3)

with d1:

    st.markdown("""
    <div class="domain-card">

    <h3>Nanoencapsulation</h3>

    Controlled delivery systems
    designed to improve
    stability, bioavailability,
    and protection of active compounds.

    </div>
    """,
    unsafe_allow_html=True)

with d2:

    st.markdown("""
    <div class="domain-card">

    <h3>Active Packaging</h3>

    Antimicrobial packaging,
    oxygen scavengers,
    moisture regulators,
    and shelf-life extension systems.

    </div>
    """,
    unsafe_allow_html=True)

with d3:

    st.markdown("""
    <div class="domain-card">

    <h3>Food Safety</h3>

    Nanosensors,
    pathogen detection,
    contamination monitoring,
    and quality assurance.

    </div>
    """,
    unsafe_allow_html=True)

d4,d5,d6 = st.columns(3)

with d4:

    st.markdown("""
    <div class="domain-card">

    <h3>Nanomaterials</h3>

    Design, synthesis,
    characterization,
    and application of food-grade nanomaterials.

    </div>
    """,
    unsafe_allow_html=True)

with d5:

    st.markdown("""
    <div class="domain-card">

    <h3>Functional Foods</h3>

    Bioactive compounds,
    nutraceutical systems,
    and enhanced nutritional delivery.

    </div>
    """,
    unsafe_allow_html=True)

with d6:

    st.markdown("""
    <div class="domain-card">

    <h3>Smart Packaging</h3>

    Intelligent packaging systems
    capable of monitoring
    freshness and storage conditions.

    </div>
    """,
    unsafe_allow_html=True)

st.markdown(
"""
<div class="section-title">
Quick Navigation Hub
</div>
""",
unsafe_allow_html=True
)

q1,q2,q3 = st.columns(3)

with q1:

    st.markdown("""
    <div class="quick-card">

    <h2>FTIR Analyzer</h2>

    Spectral interpretation
    and functional group analysis.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/FTIR Analyzer.py",
        label="Launch Tool"
    )

with q2:

    st.markdown("""
    <div class="quick-card">

    <h2>Laboratory Calculator</h2>

    Scientific calculations
    for research applications.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Laboratory Calculator.py",
        label="Launch Tool"
    )

with q3:

    st.markdown("""
    <div class="quick-card">

    <h2>Material Database</h2>

    Food nanomaterial knowledge center.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Food Nanotech Material Database.py",
        label="Open Database"
    )

q4,q5,q6 = st.columns(3)

with q4:

    st.markdown("""
    <div class="quick-card">

    <h2>Methods Library</h2>

    Experimental methods,
    protocols,
    and workflows.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Methods Library.py",
        label="Open Library"
    )

with q5:

    st.markdown("""
    <div class="quick-card">

    <h2>About Nanotechnology</h2>

    Educational resources
    and scientific concepts.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/About Nanotechnology.py",
        label="Open Learning Center"
    )

with q6:

    st.markdown("""
    <div class="quick-card">

    <h2>Troubleshooting</h2>

    Laboratory problem-solving
    and analytical support.

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
        "pages/Laboratory Troubleshooting.py",
        label="Open Assistant"
    )

st.markdown(
"""
<div class="section-title">
Platform Impact
</div>
""",
unsafe_allow_html=True
)

i1,i2,i3,i4 = st.columns(4)

with i1:

    st.markdown("""
    <div class="impact-card">

    <h2>10+</h2>

    <h4>Integrated Research Tools</h4>

    Supporting calculations,
    interpretation,
    and laboratory workflows.

    </div>
    """,
    unsafe_allow_html=True)

with i2:

    st.markdown("""
    <div class="impact-card">

    <h2>30+</h2>

    <h4>Educational Resources</h4>

    Learning materials
    and scientific references.

    </div>
    """,
    unsafe_allow_html=True)

with i3:

    st.markdown("""
    <div class="impact-card">

    <h2>100+</h2>

    <h4>Scientific Database Entries</h4>

    Nanomaterials,
    applications,
    and characterization knowledge.

    </div>
    """,
    unsafe_allow_html=True)

with i4:

    st.markdown("""
    <div class="impact-card">

    <h2>Research</h2>

    <h4>Laboratory Applications</h4>

    Supporting education,
    research,
    and scientific innovation.

    </div>
    """,
    unsafe_allow_html=True)



st.markdown("""

<div class="footer">

<h2>
NanoFood Intelligence Lab
</h2>

<p>

Research • Education • Laboratory Applications

</p>

<hr>

Food Nanotechnology

Nanomaterials

Characterization

Bioactivity

Food Packaging

</div>
""",unsafe_allow_html=True)