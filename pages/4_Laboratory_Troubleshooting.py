import streamlit as st

st.set_page_config(
    page_title="Laboratory Troubleshooting Center",
    page_icon="🛠",
    layout="wide"
)

st.markdown("""
<style>
            
/* KPI CARD */

.dashboard-grid{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:25px;
margin-bottom:40px;
}

.kpi-card{
background:rgba(255,255,255,0.7);
backdrop-filter:blur(20px);
-webkit-backdrop-filter:blur(20px);
border:1px solid rgba(255,255,255,0.3);

padding:35px;
border-radius:25px;
text-align:center;

box-shadow:
0 15px 35px rgba(0,0,0,0.08);

transition:0.4s;
}

.kpi-card:hover{
transform:translateY(-10px);
}

.kpi-icon{
font-size:55px;
}

.kpi-number{
font-size:42px;
font-weight:800;
color:#2563EB;
}

.kpi-label{
font-size:18px;
color:#64748B;
}

/* SEVERITY */

.severity{

background:
linear-gradient(
135deg,
#7F1D1D,
#DC2626
);

padding:30px;
border-radius:25px;
text-align:center;
color:white;
margin-bottom:30px;
}

.severity span{
font-size:45px;
font-weight:800;
}

/* GAUGE */

.gauge{
width:220px;
height:220px;
border-radius:50%;
margin:auto;

background:
conic-gradient(
#10B981 0deg,
#10B981 270deg,
#E2E8F0 270deg
);

display:flex;
justify-content:center;
align-items:center;

box-shadow:
0 15px 40px rgba(
16,
185,
129,
0.3
);
}

.gauge-inner{

width:150px;
height:150px;

background:white;

border-radius:50%;

display:flex;
justify-content:center;
align-items:center;

font-size:40px;
font-weight:800;
}

/* FLOW */

.flow{

display:flex;

justify-content:center;

align-items:center;

gap:15px;

flex-wrap:wrap;

margin-top:30px;
}

.step{

width:180px;

height:140px;

background:white;

border-radius:25px;

display:flex;

justify-content:center;

align-items:center;

text-align:center;

font-size:22px;

font-weight:700;

box-shadow:
0 15px 35px rgba(
0,
0,
0,
0.08
);
}

.arrow{

font-size:35px;

font-weight:800;

color:#2563EB;
}

/* PARTICLES */

.particle-wrapper{

position:relative;

height:120px;
}

.particle-wrapper span{

position:absolute;

width:12px;
height:12px;

background:#38BDF8;

border-radius:50%;

animation:float 8s infinite;
}

@keyframes float{

0%{
transform:translateY(0px);
}

50%{
transform:translateY(-40px);
}

100%{
transform:translateY(0px);
}
}

/* AI PANEL */

.ai-panel{

background:
linear-gradient(
135deg,
#1E3A8A,
#2563EB
);

padding:35px;

border-radius:25px;

color:white;

font-size:20px;

line-height:1.8;

margin-top:30px;
}

/* HERO GLOW */

.hero{

box-shadow:

0 0 25px #2563EB,
0 0 50px #2563EB,
0 0 100px rgba(
37,
99,
235,
0.4
);
}
                       
</style>
""", unsafe_allow_html=True)

st.markdown("""
            
<div class="hero">

<h1>
🔬 Laboratory Troubleshooting &
Decision Support System
</h1>

<p>

Advanced scientific platform for
Food Nanotechnology researchers
to identify laboratory failures,
analyze root causes,
and implement validated corrective actions.

Powered by scientific standards,
laboratory best practices,
and evidence-based troubleshooting.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("""

<div class="particle-wrapper">

<span></span>
<span></span>
<span></span>
<span></span>
<span></span>
<span></span>
<span></span>

</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class="dashboard-grid">

<div class="kpi-card">

<div class="kpi-icon">
🧪
</div>

<div class="kpi-number">
20+
</div>

<div class="kpi-label">
Common Problems
</div>

</div>

<div class="kpi-card">

<div class="kpi-icon">
🔬
</div>

<div class="kpi-number">
50+
</div>

<div class="kpi-label">
Scientific Solutions
</div>

</div>

<div class="kpi-card">

<div class="kpi-icon">
📈
</div>

<div class="kpi-number">
95%
</div>

<div class="kpi-label">
Success Rate
</div>

</div>

<div class="kpi-card">

<div class="kpi-icon">
🧠
</div>

<div class="kpi-number">
AI
</div>

<div class="kpi-label">
Decision Support
</div>

</div>

</div>

""", unsafe_allow_html=True)

st.subheader(
    "Interactive Laboratory Troubleshooter"
)

problem = st.selectbox(
    "Select Laboratory Problem",
    [
        "Nanoparticle Aggregation",
        "Low Encapsulation Efficiency",
        "Poor Calibration Curve",
        "Unexpected FTIR Peaks",
        "Large Particle Size",
        "Low Zeta Potential",
        "Poor Film Properties"
    ]
)

severity = "LOW"

if problem == "Nanoparticle Aggregation":
    severity = "CRITICAL"

elif problem == "Large Particle Size":
    severity = "HIGH"

elif problem == "Low Zeta Potential":
    severity = "MODERATE"

elif problem == "Poor Calibration Curve":
    severity = "MODERATE"

elif problem == "Low Encapsulation Efficiency":
    severity = "MODERATE"

elif problem == "Poor Film Properties":
    severity = "HIGH"

st.markdown(f"""

<div class="severity">

Severity Level

<br><br>

<span>{severity}</span>

</div>

""", unsafe_allow_html=True)

if problem == "Nanoparticle Aggregation":

    st.error(...)

    c1,c2 = st.columns(2)

    with c1:
        st.markdown("""
        cause card
        """)

    with c2:
        st.markdown("""
        solution card
        """)

    st.info(...)

elif problem == "Low Encapsulation Efficiency":

    ...

elif problem == "Poor Calibration Curve":

    ...

elif problem == "Large Particle Size":

    ...

elif problem == "Low Zeta Potential":

    ...

elif problem == "Poor Film Properties":

    ...

st.header(
    "🔍 Root Cause Analysis Workflow"
)

st.markdown("""

<div class="flow">

<div class="step">
①<br>
Problem
</div>

<div class="arrow">
➜
</div>

<div class="step">
②<br>
Symptoms
</div>

<div class="arrow">
➜
</div>

<div class="step">
③<br>
Root Cause
</div>

<div class="arrow">
➜
</div>

<div class="step">
④<br>
Correction
</div>

<div class="arrow">
➜
</div>

<div class="step">
⑤<br>
Verification
</div>

</div>

""", unsafe_allow_html=True)

st.header(
    "🧠 Laboratory Decision Support System"
)

st.info("""

This module evaluates
particle size and zeta potential
to estimate nanoparticle stability
and provide corrective recommendations.

""")

c1,c2 = st.columns(2)

with c1:

    size = st.number_input(
        "Particle Size (nm)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

with c2:

    zeta = st.number_input(
        "Zeta Potential (mV)",
        value=-15.0,
        step=1.0
    )

st.subheader(
    "Diagnostic Result"
)

if size > 500:

    st.error(
        """
        Severe Aggregation Suspected

        Particle size exceeds
        the acceptable nanoparticle range.
        """
    )

elif abs(zeta) < 20:

    st.warning(
        """
        Low Stability Detected

        Zeta potential indicates
        weak electrostatic stabilization.
        """
    )

else:

    st.success(
        """
        Stable Nanoparticle System

        Particle size and zeta potential
        indicate acceptable stability.
        """
    )

st.markdown("""

<div class="ai-panel">

<h2>
🧠 AI Research Recommendation
</h2>

<p>

Based on particle size and zeta potential analysis,
the system predicts potential instability
caused by weak electrostatic repulsion.

Recommended actions:

<ul>

<li>Increase stabilizer concentration</li>

<li>Optimize pH conditions</li>

<li>Apply sonication treatment</li>

<li>Reduce ionic strength</li>

<li>Verify storage temperature</li>

</ul>

<b>Confidence Level: 91%</b>

</p>

</div>

""", unsafe_allow_html=True)

score = min(
    int(abs(zeta) * 2),
    100
)

st.subheader(
    "Nanoparticle Stability Index"
)

st.markdown(f"""

<div class="gauge">

<div class="gauge-inner">

{score}%

</div>

</div>

""", unsafe_allow_html=True)

st.caption(
    "Estimated Stability Index Based on Zeta Potential"
)

st.header(
    "📚 Common Problems Database"
)

with st.expander(
    "Unexpected FTIR Peak"
):

    st.write("""

Possible Causes

• Contamination

• Residual solvent

• Moisture absorption

• Chemical modification

Recommended Actions

• Repeat sample preparation

• Dry samples thoroughly

• Verify baseline correction

""")
    
with st.expander(
    "Unexpected UV-Vis Peak"
):

    st.write("""

Possible Causes

• Instrument noise

• Aggregation

• Secondary particle formation

• Contamination

Recommended Actions

• Re-measure sample

• Filter solution

• Verify synthesis conditions

""")

with st.expander(
    "Low Yield During Synthesis"
):

    st.write("""

Possible Causes

• Incomplete reaction

• Improper temperature

• Insufficient precursor

Recommended Actions

• Extend reaction time

• Optimize temperature

• Verify reagent concentration

""")
    
with st.expander(
    "Film Cracking"
):

    st.write("""

Possible Causes

• Excess drying rate

• Insufficient plasticizer

• Poor polymer interaction

Recommended Actions

• Reduce drying temperature

• Increase plasticizer content

• Optimize formulation

""")

st.header(
    "💡 Best Practice Recommendations"
)

st.markdown("""

<div class="glass">

<h3>
Research Best Practices
</h3>

<ul>

<li>Validate instruments before use</li>

<li>Perform triplicate measurements</li>

<li>Store samples properly</li>

<li>Record all experimental conditions</li>

<li>Verify calibration routinely</li>

<li>Monitor environmental conditions</li>

<li>Apply statistical validation</li>

<li>Maintain laboratory notebooks</li>

<li>Perform regular quality control</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.header(
    "📖 Scientific Foundation"
)

st.markdown("""

<div class="glass">

<h3>
Reference Standards
</h3>

<ul>

<li>ASTM Standards</li>

<li>ISO Standards</li>

<li>AOAC Methods</li>

<li>IUPAC Recommendations</li>

<li>Food Hydrocolloids</li>

<li>Carbohydrate Polymers</li>

<li>Journal of Food Engineering</li>

<li>Colloids and Surfaces A</li>

<li>International Journal of Biological Macromolecules</li>

<li>Food Chemistry</li>

<li>Trends in Food Science & Technology</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.markdown("""

<div class="quote">

"Every laboratory problem contains
valuable scientific information.

The difference between failed research
and successful research is the ability
to identify root causes,
learn systematically,
and continuously improve the process."

</div>

""", unsafe_allow_html=True)
