import streamlit as st

st.set_page_config(
    page_title="Why NanoFoodLab Was Developed",
    page_icon="🚀",
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

    padding:50px;
    border-radius:20px;
    text-align:center;
    margin-bottom:30px;
}

.hero h1{
    color:white;
    font-size:55px;
}

.hero p{
    color:white;
    font-size:20px;
}

.problem{
    background:#FEF2F2;
    padding:30px;
    border-left:8px solid #EF4444;
    border-radius:15px;
    box-shadow:0 6px 15px rgba(0,0,0,0.1);
}

.impact{
    background:#EFF6FF;
    padding:30px;
    border-left:8px solid #3B82F6;
    border-radius:15px;
    box-shadow:0 6px 15px rgba(0,0,0,0.1);
}

.card{
    background:white;
    padding:25px;
    border-radius:15px;
    border-left:6px solid #06B6D4;
    box-shadow:0 6px 15px rgba(0,0,0,0.1);
    min-height:220px;
}

.challenge{
    background:#FEF2F2;
    padding:30px;
    border-radius:15px;
    border-left:8px solid #EF4444;
}

.solution{
    background:#ECFDF5;
    padding:30px;
    border-radius:15px;
    border-left:8px solid #10B981;
}

.timeline{
    background:white;
    padding:30px;
    border-radius:20px;
    text-align:center;
    font-size:22px;
    box-shadow:0 8px 25px rgba(0,0,0,0.1);
}

.glass{
    background:rgba(255,255,255,0.95);
    padding:30px;
    border-radius:20px;
    box-shadow:0 8px 25px rgba(0,0,0,0.1);
}

.quote{
    background:linear-gradient(
        135deg,
        #06B6D4,
        #0891B2
    );

    padding:40px;

    border-radius:20px;

    color:white;

    font-size:28px;

    font-weight:bold;

    text-align:center;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>
🚀 Why NanoFood Intelligence Lab Was Developed
</h1>

<p>
Bridging Food Nanotechnology Research,
Laboratory Calculations,
and Scientific Education
in a Single Integrated Platform.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>
🚀 Why NanoFood Intelligence Lab Was Developed
</h1>

<p>
Bridging Food Nanotechnology Research,
Laboratory Calculations,
and Scientific Education
in a Single Integrated Platform.
</p>

</div>
""", unsafe_allow_html=True)

st.header("Background and Urgency")

col1,col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="problem">

    <h3>⚠ Current Challenges</h3>

    <ul>

    <li>Manual calculations</li>

    <li>Multiple software usage</li>

    <li>Data fragmentation</li>

    <li>Time-consuming workflows</li>

    <li>Human calculation errors</li>

    </ul>

    </div>
    """,
    unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="impact">

    <h3>📉 Impact on Research</h3>

    <ul>

    <li>Reduced efficiency</li>

    <li>Inconsistent results</li>

    <li>Difficult learning process</li>

    <li>Repeated calculations</li>

    <li>Increased error risk</li>

    </ul>

    </div>
    """,
    unsafe_allow_html=True)

st.header("Laboratory Challenges")

c1,c2,c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">

    <h3>🧪 Dilution Calculations</h3>

    Preparation of laboratory solutions,
    concentration adjustment,
    and stock solution formulation.

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">

    <h3>🔬 Nanoparticle Characterization</h3>

    Particle size,
    zeta potential,
    XRD and FTIR interpretation.

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">

    <h3>📦 Packaging Analysis</h3>

    WVTR,
    moisture content,
    swelling index,
    and biodegradation.

    </div>
    """, unsafe_allow_html=True)

c4,c5,c6 = st.columns(3)

with c4:
    st.markdown("""
    <div class="card">
    <h3>🌱 IC50 Analysis</h3>
    Antioxidant activity assessment.
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="card">
    <h3>📊 Standard Curve Analysis</h3>
    Calibration and quantification.
    </div>
    """, unsafe_allow_html=True)

with c6:
    st.markdown("""
    <div class="card">
    <h3>🧬 Encapsulation Efficiency</h3>
    Evaluation of active compound loading.
    </div>
    """, unsafe_allow_html=True)

st.header(
    "Why Existing Methods Are Limited"
)

st.markdown("""
<div class="timeline">

Manual Calculator

<br>⬇<br>

Spreadsheet Processing

<br>⬇<br>

Data Transfer

<br>⬇<br>

Result Interpretation

<br>⬇<br>

Potential Error

</div>
""",
unsafe_allow_html=True)

st.header(
    "NanoFoodLab Solution"
)

left,right = st.columns(2)

with left:

    st.markdown("""
    <div class="challenge">

    <h3>Challenges</h3>

    • Manual calculations<br>
    • Multiple software<br>
    • Human error<br>
    • Complex interpretation

    </div>
    """,
    unsafe_allow_html=True)

with right:

    st.markdown("""
    <div class="solution">

    <h3>Solutions</h3>

    • Automated calculators<br>
    • Single integrated platform<br>
    • Formula validation<br>
    • Built-in scientific explanations

    </div>
    """,
    unsafe_allow_html=True)

st.header(
    "Scientific Foundation"
)

st.markdown("""
<div class="glass">

<h3>
Scientific Foundation
</h3>

NanoFood Intelligence Lab was developed based on:

<ul>

<li>ASTM Standards</li>

<li>ISO Standards</li>

<li>IUPAC Recommendations</li>

<li>AOAC Methods</li>

<li>Food Hydrocolloids</li>

<li>Carbohydrate Polymers</li>

<li>Journal of Food Engineering</li>

<li>Trends in Food Science & Technology</li>

</ul>

</div>
""",
unsafe_allow_html=True)

st.header(
    "Research Impact"
)

r1,r2,r3,r4 = st.columns(4)

with r1:
    st.info("🎓 Impact on Education")

with r2:
    st.info("🔬 Impact on Research")

with r3:
    st.info("🧪 Impact on Laboratory Activities")

with r4:
    st.info("📊 Impact on Data Interpretation")

st.markdown("""
<div class="quote">

"Transforming complex food nanotechnology
calculations into accessible,
accurate,
and scientifically validated tools."

</div>
""",
unsafe_allow_html=True)

st.success("""
This platform was developed to support
food nanotechnology education,
laboratory activities,
scientific research,
and data interpretation through an integrated,
user-friendly,
and scientifically validated environment.
""")

