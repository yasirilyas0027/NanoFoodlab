import streamlit as st
import os

st.write("CURRENT FILE:", __file__)
st.write("CURRENT DIRECTORY:", os.getcwd())

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap');

html,body,[class*="css"]{
font-family:'Inter',sans-serif;
}

h1,h2,h3{
font-family:'Montserrat',sans-serif;
}

.stApp{
background:#F5F7FA;
}

/* HERO */

.hero{

height:650px;

background-image:url("https://images.unsplash.com/photo-1532187643603-ba119ca4109e");

background-size:cover;
background-position:center;

position:relative;

overflow:hidden;

border-radius:0;
}

.hero-overlay{

height:650px;

background:rgba(0,0,0,0.60);

display:flex;

align-items:center;

padding-left:120px;
padding-right:120px;
}

.hero-content{

max-width:850px;
}

.hero-title{

font-size:78px;

font-weight:800;

color:white;

line-height:1.1;

margin-bottom:20px;
}

.hero-subtitle{

font-size:30px;

font-weight:600;

color:#38BDF8;

margin-bottom:25px;
}

.hero-description{

font-size:22px;

color:white;

line-height:1.8;

margin-bottom:40px;
}

.hero-button{

display:inline-block;

background:#0066CC;

color:white !important;

padding:18px 40px;

border-radius:50px;

font-size:18px;

font-weight:600;

text-decoration:none;

transition:0.3s;
}

.hero-button:hover{

background:#0052A3;
}

/* NAVIGATION STRIP */

.nav-wrapper{

margin-top:-40px;

position:relative;

z-index:100;
}

.nav-card{

background:white;

padding:25px;

text-align:center;

font-weight:600;

font-size:18px;

border-top:4px solid #0066CC;

box-shadow:0 8px 25px rgba(0,0,0,0.08);

transition:0.3s;

cursor:pointer;
}

.nav-card:hover{

transform:translateY(-5px);

box-shadow:0 15px 30px rgba(0,0,0,0.12);
}

</style>
""",
unsafe_allow_html=True)

st.markdown("""

<div class="hero">

<div class="hero-overlay">

<div class="hero-content">

<div class="hero-title">

NanoFood Intelligence Lab

</div>

<div class="hero-subtitle">

Integrated Research Platform
for Food Nanotechnology

</div>

<div class="hero-description">

Research • Characterization • Education • Laboratory Support

</div>

<a href="#tools" class="hero-button">

Explore Platform

</a>

</div>

</div>

</div>

""",
unsafe_allow_html=True)     
            

st.markdown("""
<style>
                       
/* SECTION TITLE */

.section-title{

font-size:48px;

font-weight:800;

color:#111827;

margin-top:100px;

margin-bottom:40px;
}

/* FEATURED TOOLS */

.service-card{

background:white;

padding:40px;

min-height:280px;

border:1px solid #E5E7EB;

transition:all .3s ease;

display:flex;

flex-direction:column;

justify-content:space-between;
}

.service-card:hover{

transform:translateY(-5px);

box-shadow:
0 15px 40px rgba(
0,
0,
0,
0.12
);
}

.service-card h3{

font-size:28px;

font-weight:700;

margin-bottom:20px;

color:#111827;
}

.service-card p{

font-size:17px;

line-height:1.8;

color:#4B5563;
}

.service-arrow{

font-size:28px;

font-weight:700;

margin-top:25px;

color:#0066CC;
}

.research-section{

background:white;

padding:70px;

border-radius:20px;

margin-top:90px;

margin-bottom:90px;

box-shadow:
0 10px 35px rgba(
0,
0,
0,
0.08
);
}

.research-title{

font-size:48px;

font-weight:800;

margin-bottom:30px;

color:#111827;
}

.research-text{

font-size:19px;

line-height:2;

color:#4B5563;
}

.research-list{

font-size:22px;

font-weight:600;

line-height:2.2;

color:#0F172A;
}

.research-image{

width:100%;

border-radius:18px;
}

.capability-card{

background:white;

padding:40px;

border:1px solid #E5E7EB;

min-height:280px;

transition:all .3s ease;

display:flex;

flex-direction:column;

justify-content:space-between;

border-radius:12px;
}

.capability-card:hover{

transform:translateY(-6px);

box-shadow:
0 15px 40px rgba(
0,
0,
0,
0.10
);
}

.capability-icon{

font-size:42px;

margin-bottom:20px;
}

.capability-card h3{

font-size:28px;

font-weight:700;

color:#111827;

margin-bottom:15px;
}

.capability-card p{

font-size:17px;

line-height:1.8;

color:#4B5563;
}

.why-section{

background:white;

padding:80px;

border-radius:20px;

box-shadow:
0 15px 40px rgba(
0,
0,
0,
0.08
);
}

.why-title{

font-size:52px;

font-weight:800;

color:#111827;

margin-bottom:25px;
}

.why-text{

font-size:20px;

line-height:2;

color:#4B5563;
}

.highlight{

font-weight:700;

color:#0066CC;
}

/* ===========================
STATISTICS
=========================== */

.stats-section{

margin-top:100px;
margin-bottom:100px;
}

.metric-box{

text-align:center;

padding:40px 20px;

background:white;

border-radius:12px;

border:1px solid #E5E7EB;

transition:all .3s ease;
}

.metric-box:hover{

transform:translateY(-5px);

box-shadow:
0 12px 30px rgba(
0,
0,
0,
0.08
);
}

.metric-number{

font-size:64px;

font-weight:800;

color:#0066CC;

margin-bottom:10px;
}

.metric-label{

font-size:20px;

font-weight:600;

color:#111827;
}

.metric-desc{

font-size:15px;

color:#6B7280;

margin-top:10px;
}

            /* ===========================
LATEST RESOURCES
=========================== */

.resource-card{

background:white;

border:1px solid #E5E7EB;

border-radius:12px;

overflow:hidden;

transition:all .3s ease;

height:100%;
}

.resource-card:hover{

transform:translateY(-6px);

box-shadow:
0 15px 40px rgba(
0,
0,
0,
0.10
);
}

.resource-image{

width:100%;

height:220px;

object-fit:cover;
}

.resource-content{

padding:30px;
}

.resource-category{

font-size:14px;

font-weight:700;

letter-spacing:1px;

color:#0066CC;

margin-bottom:15px;
}

.resource-title{

font-size:28px;

font-weight:700;

color:#111827;

margin-bottom:15px;
}

.resource-text{

font-size:16px;

line-height:1.8;

color:#4B5563;
}

.resource-link{

margin-top:20px;

font-weight:700;

color:#0066CC;
}

/* ===========================
CALL TO ACTION
=========================== */

.cta{

background:
linear-gradient(
135deg,
#001B44,
#002B6B
);

padding:90px;

border-radius:24px;

text-align:center;

margin-top:120px;

margin-bottom:100px;

box-shadow:
0 20px 50px rgba(
0,
0,
0,
0.15
);
}

.cta-title{

font-size:54px;

font-weight:800;

color:white;

margin-bottom:20px;
}

.cta-subtitle{

font-size:22px;

color:#D1D5DB;

margin-bottom:40px;
}

.cta-button{

display:inline-block;

background:white;

color:#001B44 !important;

padding:18px 40px;

border-radius:50px;

font-size:18px;

font-weight:700;

text-decoration:none;

transition:all .3s ease;
}

.cta-button:hover{

transform:translateY(-3px);

box-shadow:
0 10px 25px rgba(
255,
255,
255,
0.20
);
}

/* ===========================
FOOTER
=========================== */

.footer{

background:#0F172A;

padding:80px 60px 40px 60px;

color:white;

margin-top:60px;
}

.footer-title{

font-size:36px;

font-weight:800;

margin-bottom:20px;
}

.footer-subtitle{

font-size:18px;

color:#CBD5E1;

margin-bottom:40px;
}

.footer-heading{

font-size:20px;

font-weight:700;

margin-bottom:15px;

color:white;
}

.footer-item{

font-size:16px;

color:#CBD5E1;

margin-bottom:10px;
}

.footer-credit{

margin-top:50px;

padding-top:30px;

border-top:1px solid rgba(
255,
255,
255,
0.15
);

text-align:center;

color:#94A3B8;

font-size:15px;
}

.credit-name{

font-weight:600;

color:white;
}
                                                 
""",
unsafe_allow_html=True)

st.markdown(
'<div class="nav-wrapper">',
unsafe_allow_html=True
)

nav1,nav2,nav3,nav4,nav5,nav6 = st.columns(6)

with nav1:

    st.markdown("""
    <div class="nav-card">
    Calculator
    </div>
    """,
    unsafe_allow_html=True)

with nav2:

    st.markdown("""
    <div class="nav-card">
    FTIR
    </div>
    """,
    unsafe_allow_html=True)

with nav3:

    st.markdown("""
    <div class="nav-card">
    Database
    </div>
    """,
    unsafe_allow_html=True)

with nav4:

    st.markdown("""
    <div class="nav-card">
    Methods
    </div>
    """,
    unsafe_allow_html=True)

with nav5:

    st.markdown("""
    <div class="nav-card">
    Learning
    </div>
    """,
    unsafe_allow_html=True)

with nav6:

    st.markdown("""
    <div class="nav-card">
    Troubleshooting
    </div>
    """,
    unsafe_allow_html=True)

st.markdown(
'</div>',
unsafe_allow_html=True
)

st.markdown(
"""
<div class="section-title">

Featured Scientific Tools

</div>
""",
unsafe_allow_html=True
)

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.markdown("""

    <div class="service-card">

    <div>

    <h3>
    Laboratory Calculator
    </h3>

    <p>

    Scientific calculations for
    dilution, molarity,
    encapsulation efficiency,
    IC50, EC50,
    release efficiency
    and laboratory data analysis.

    </p>

    </div>

    <div class="service-arrow">

    →

    </div>

    </div>

    """,
    unsafe_allow_html=True)

    st.page_link(
    "pages/3_Laboratory_Calculator.py",
    label="Open Tool"
    )

with c2:

    st.markdown("""

    <div class="service-card">

    <div>

    <h3>
    FTIR Analyzer
    </h3>

    <p>

    Functional group
    identification,
    spectral interpretation,
    peak assignment,
    and analytical support
    for food nanomaterials.

    </p>

    </div>

    <div class="service-arrow">

    →

    </div>
                
    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
    "pages/6_FTIR_Analyzer.py",
    label="Open Tool"
    )

with c3:

    st.markdown("""

    <div class="service-card">

    <div>

    <h3>
    Material Database
    </h3>

    <p>

    Explore nanomaterials
    commonly applied
    in food systems,
    packaging,
    nanoencapsulation,
    and delivery technologies.

    </p>

    </div>

    <div class="service-arrow">

    →

    </div>

    </div>

    """,
    unsafe_allow_html=True)

    st.page_link(
    "pages/5_Food_Nanotech_Material_Database.py",
    label="Open Tool"
    )

with c4:

    st.markdown("""

    <div class="service-card">

    <div>

    <h3>
    Methods Library
    </h3>

    <p>

    Experimental methods,
    characterization workflows,
    laboratory protocols,
    and scientific procedures
    for nanotechnology research.

    </p>

    </div>

    <div class="service-arrow">

    →

    </div>

    </div>
    """,
    unsafe_allow_html=True)

    st.page_link(
    "pages/5_Food_Nanotech_Material_Database.py",
    label="Open Tool"
    )


st.markdown("""

<div class="quick-card">
<div class="section-title">

Research Domains

</div>

""",
unsafe_allow_html=True)

left,right = st.columns([1,1.3])

with left:

    st.markdown("""

    <div class="impact-card">
                
    <div class="research-section">

    <div class="research-title">

    Food Nanotechnology

    </div>

    <div class="research-text">

    Scientific development of nanoscale systems
    to improve food quality,
    safety,
    functionality,
    stability,
    and bioavailability.

    </div>

    <br>

    <div class="research-list">

    • Nanoencapsulation<br>

    • Nanoemulsion<br>

    • Nanoparticles<br>

    • Functional Foods<br>

    • Active Packaging<br>

    • Smart Packaging

    </div>
                
    </div>
    """,
    unsafe_allow_html=True)

with right:

    st.image(
        "https://images.unsplash.com/photo-1576086213369-97a306d36557",
        use_container_width=True
    )

st.markdown("""

<div class="section-title">

Platform Capabilities

</div>

""",
unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:

    st.markdown("""

    <div class="capability-card">

    <div>

    <div class="capability-icon">

    🧪

    </div>

    <h3>

    Laboratory Calculations

    </h3>

    <p>

    Scientific calculations
    including dilution,
    molarity,
    IC50,
    EC50,
    WVTR,
    encapsulation efficiency,
    and release efficiency.

    </p>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with c2:

    st.markdown("""

    <div class="capability-card">

    <div>

    <div class="capability-icon">

    🔬

    </div>

    <h3>

    Characterization Support

    </h3>

    <p>

    Interpretation support
    for FTIR,
    XRD,
    UV-Vis,
    particle size analysis,
    crystallinity,
    and nanomaterial evaluation.

    </p>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with c3:

    st.markdown("""

    <div class="capability-card">

    <div>

    <div class="capability-icon">

    🗂️

    </div>

    <h3>

    Research Database

    </h3>

    <p>

    Centralized access
    to food nanomaterials,
    active compounds,
    applications,
    and scientific references.

    </p>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

c4,c5,c6 = st.columns(3)

with c4:

    st.markdown("""

    <div class="capability-card">

    <div>

    <div class="capability-icon">

    📑

    </div>

    <h3>

    Method Development

    </h3>

    <p>

    Experimental workflows,
    protocol libraries,
    laboratory procedures,
    and research guidance.

    </p>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with c5:

    st.markdown("""

    <div class="capability-card">

    <div>

    <div class="capability-icon">

    🎓

    </div>

    <h3>

    Scientific Education

    </h3>

    <p>

    Learning resources
    covering food nanotechnology,
    nanoencapsulation,
    packaging,
    and characterization.

    </p>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with c6:

    st.markdown("""

    <div class="capability-card">

    <div>

    <div class="capability-icon">

    ⚙️

    </div>

    <h3>

    Troubleshooting

    </h3>

    <p>

    Laboratory problem solving,
    experimental optimization,
    and analytical support
    for research activities.

    </p>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

st.markdown("""

<div class="section-title">

Why NanoFoodLab

</div>

""",
unsafe_allow_html=True)

left,right = st.columns([1.2,1])

with left:

    st.markdown("""

    <div class="why-section">

    <div class="why-title">

    Why NanoFoodLab?

    </div>

    <div class="why-text">

    Researchers in food nanotechnology
    frequently rely on multiple software
    platforms, spreadsheets,
    scientific databases,
    manual calculations,
    and fragmented educational resources.

    <br><br>

    This fragmented workflow
    often increases analysis time,
    introduces calculation errors,
    and limits research efficiency.

    <br><br>

    <span class="highlight">

    NanoFoodLab integrates
    scientific calculations,
    characterization support,
    educational resources,
    material databases,
    and troubleshooting assistance
    into a single research platform.

    </span>

    <br><br>

    The platform is designed to support
    students,
    researchers,
    and laboratory personnel
    throughout the entire research workflow,
    from experimental design
    to scientific publication.

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with right:
    st.image(
        "images/research_workflow.png",
        use_container_width=True
    )

st.markdown("""

<div class="section-title">

Research Impact

</div>

""",
unsafe_allow_html=True)

m1,m2,m3,m4 = st.columns(4)

with m1:

    st.markdown("""

    <div class="metric-box">

    <div class="metric-number">

    15+

    </div>

    <div class="metric-label">

    Research Tools

    </div>

    <div class="metric-desc">

    Integrated scientific tools
    supporting laboratory research.

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with m2:

    st.markdown("""

    <div class="metric-box">

    <div class="metric-number">

    100+

    </div>

    <div class="metric-label">

    Methods

    </div>

    <div class="metric-desc">

    Experimental workflows
    and scientific protocols.

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with m3:

    st.markdown("""

    <div class="metric-box">

    <div class="metric-number">

    50+

    </div>

    <div class="metric-label">

    Materials

    </div>

    <div class="metric-desc">

    Food nanomaterials
    and active compounds.

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with m4:

    st.markdown("""

    <div class="metric-box">

    <div class="metric-number">

    1000+

    </div>

    <div class="metric-label">

    Users

    </div>

    <div class="metric-desc">

    Students,
    researchers,
    and educators.

    </div>

    </div>

    """,
    unsafe_allow_html=True)

st.markdown("""

<div class="section-title">

Latest Scientific Resources

</div>

""",
unsafe_allow_html=True)

r1,r2,r3 = st.columns(3)

with r1:

    st.markdown("""

    <div class="resource-card">

    <img
    class="resource-image"
    src="https://images.unsplash.com/photo-1532187643603-ba119ca4109e">

    <div class="resource-content">

    <div class="resource-category">

    EDUCATION

    </div>

    <div class="resource-title">

    Food Nanotechnology

    </div>

    <div class="resource-text">

    Introduction to food
    nanotechnology,
    applications,
    benefits,
    challenges,
    and future directions.

    </div>

    <div class="resource-link">

    Read More →

    </div>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with r2:

    st.markdown("""

    <div class="resource-card">

    <img
    class="resource-image"
    src="https://images.unsplash.com/photo-1581092921461-eab62e97a780">

    <div class="resource-content">

    <div class="resource-category">

    CHARACTERIZATION

    </div>

    <div class="resource-title">

    FTIR Interpretation

    </div>

    <div class="resource-text">

    Learn how to identify
    functional groups,
    interpret spectra,
    and analyze FTIR peaks.

    </div>

    <div class="resource-link">

    Read More →

    </div>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

with r3:

    st.markdown("""

    <div class="resource-card">

    <img
    class="resource-image"
    src="https://images.unsplash.com/photo-1576086213369-97a306d36557">

    <div class="resource-content">

    <div class="resource-category">

    RESEARCH GUIDE

    </div>

    <div class="resource-title">

    Nanoencapsulation Guide

    </div>

    <div class="resource-text">

    Comprehensive guide
    to encapsulation systems,
    delivery mechanisms,
    and food applications.

    </div>

    <div class="resource-link">

    Read More →

    </div>

    </div>

    </div>

    """,
    unsafe_allow_html=True)

st.markdown("""

<div class="cta">

<div class="cta-title">

Ready to Explore
Food Nanotechnology?

</div>

<div class="cta-subtitle">

One Platform.
Multiple Research Solutions.

</div>

<div style="margin-bottom:40px;">

🧪 15+ Research Tools &nbsp;&nbsp;&nbsp;
📚 100+ Methods &nbsp;&nbsp;&nbsp;
🗂️ 50+ Materials

</div>

<a href="#top" class="cta-button">

Launch Platform

</a>

</div>

""",
unsafe_allow_html=True)

st.markdown(
"""
<div class="footer">
""",
unsafe_allow_html=True
)

f1,f2,f3,f4 = st.columns(4)

with f1:

    st.markdown("""

    <div class="footer-title">

    NanoFood Intelligence Lab

    </div>

    <div class="footer-subtitle">

    Integrated Research Platform
    for Food Nanotechnology

    </div>

    """,
    unsafe_allow_html=True)

with f2:

    st.markdown("""

    <div class="footer-heading">

    Platform

    </div>

    <div class="footer-item">
    Laboratory Calculator
    </div>

    <div class="footer-item">
    Material Database
    </div>

    <div class="footer-item">
    Methods Library
    </div>

    <div class="footer-item">
    FTIR Analyzer
    </div>

    """,
    unsafe_allow_html=True)

with f3:

    st.markdown("""

    <div class="footer-heading">

    Research Areas

    </div>

    <div class="footer-item">
    Nanoencapsulation
    </div>

    <div class="footer-item">
    Active Packaging
    </div>

    <div class="footer-item">
    Smart Packaging
    </div>

    <div class="footer-item">
    Nanomaterials
    </div>

    """,
    unsafe_allow_html=True)

with f4:

    st.markdown("""

    <div class="footer-heading">

    Resources

    </div>

    <div class="footer-item">
    Learning Center
    </div>

    <div class="footer-item">
    Troubleshooting
    </div>

    <div class="footer-item">
    FTIR Resources
    </div>

    <div class="footer-item">
    Scientific Methods
    </div>

    """,
    unsafe_allow_html=True)

st.markdown("""

<div class="footer-credit">

Developed by

<br><br>

<span class="credit-name">

Putri Aprilia

</span>

&nbsp;•&nbsp;

<span class="credit-name">

Sifa Resti Nur Ranyanti

</span>

&nbsp;•&nbsp;

<span class="credit-name">

Yasir Ilyas Trikurnianto

</span>

<br><br>

Food Nanotechnology Program

<br>

Universitas Ahmad Dahlan

<br><br>

© 2026 NanoFood Intelligence Lab

All Rights Reserved.

</div>

""",
unsafe_allow_html=True)

st.markdown(
"</div>",
unsafe_allow_html=True
)