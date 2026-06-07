import streamlit as st

st.set_page_config(
    page_title="About Food Nanotechnology",
    page_icon="🔬",
    layout="wide"
)
st.markdown("""
<style>

.glass{
background:rgba(255,255,255,0.95);
padding:30px;
border-radius:20px;
box-shadow:0 8px 25px rgba(0,0,0,0.12);
}

.timeline{
background:white;
padding:30px;
border-radius:20px;
text-align:center;
font-size:20px;
box-shadow:0 8px 20px rgba(0,0,0,0.1);
}

.challenge{
background:#FEF2F2;
padding:25px;
border-left:8px solid #EF4444;
border-radius:15px;
}

.solution{
background:#ECFDF5;
padding:25px;
border-left:8px solid #10B981;
border-radius:15px;
}

.benefit{
background:white;
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0 6px 15px rgba(0,0,0,0.1);
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
text-align:center;
font-size:28px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>🔬 FOOD NANOTECHNOLOGY</h1>

<h3>
Transforming Food Systems at the Nanoscale
</h3>

<p>
Exploring nanoscale innovations that improve
food quality, safety, bioavailability,
packaging performance, and sustainability.
</p>

</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)

with c1:
    st.metric(
        "Research Areas",
        "50+"
    )

with c2:
    st.metric(
        "Nanoscale Range",
        "1–100 nm"
    )

with c3:
    st.metric(
        "Laboratory Tools",
        "20+"
    )

st.header("What is Food Nanotechnology?")

left,right = st.columns([1,1])

with left:

    st.image(
        "https://assets-a1.kompasiana.com/items/album/2022/03/11/nanotech-flickr-622b3fe37a36cd0d07190213.jpg",
        use_container_width=True
    )

with right:

    st.markdown("""
    <div class="glass">

    <h3>
    What is Food Nanotechnology?
    </h3>

    <p>

    Food nanotechnology is the application
    of nanoscale materials and systems
    (1–100 nm) to improve food quality,
    safety, stability, functionality,
    packaging performance,
    and bioactive delivery.

    </p>

    <p>

    At the nanoscale,
    materials exhibit unique physical,
    chemical,
    and biological properties
    that differ from their bulk forms.

    </p>

    </div>
    """,
    unsafe_allow_html=True)

st.header("Size Comparison")

st.image(
        "https://hackernoon.imgix.net/images/pIGapHGH9NNT6tb7uPaRnsVFH123-541y319w.jpeg?auto=format%2Ccompress&w=828",
        use_container_width=True
    )

st.header(
    "Why Food Nanotechnology Matters"
)

col1,col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="challenge">

    <h3>
    Challenges in Conventional Food Systems
    </h3>

    • Poor bioavailability<br>
    • Low antioxidant stability<br>
    • Food spoilage<br>
    • Microbial contamination<br>
    • Short shelf life<br>
    • Packaging waste

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="solution">

    <h3>
    Nanotechnology Solutions
    </h3>

    • Nanoencapsulation<br>
    • Nanoemulsions<br>
    • Active Packaging<br>
    • Antimicrobial Nanoparticles<br>
    • Controlled Release Systems<br>
    • Smart Food Monitoring

    </div>
    """, unsafe_allow_html=True)

a1,a2,a3 = st.columns(3)

with a1:
    st.markdown("""
    <div class="glass">
    <h3>🧬 Nanoencapsulation</h3>
    Protects sensitive compounds and enables controlled release.
    </div>
    """, unsafe_allow_html=True)

with a2:
    st.markdown("""
    <div class="glass">
    <h3>💧 Nanoemulsion</h3>
    Improves solubility and bioavailability.
    </div>
    """, unsafe_allow_html=True)

with a3:
    st.markdown("""
    <div class="glass">
    <h3>📦 Active Packaging</h3>
    Extends shelf life and improves safety.
    </div>
    """, unsafe_allow_html=True)

b1,b2 = st.columns(2)

with b1:
    st.markdown("""
    <div class="glass">
    <h3>📡 Nanosensors</h3>
    Real-time food quality monitoring.
    </div>
    """, unsafe_allow_html=True)

with b2:
    st.markdown("""
    <div class="glass">
    <h3>🍎 Functional Foods</h3>
    Enhanced nutrient delivery and absorption.
    </div>
    """, unsafe_allow_html=True)

st.header("Benefits of Food Nanotechnology")

st.image(
    "https://www.mdpi.com/engproc/engproc-61-00004/article_deploy/html/images/engproc-61-00004-g001.png",
    use_container_width=True
)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="benefit">

    <h2>✅</h2>

    Improved Food Safety

    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="benefit">

    <h2>📦</h2>

    Extended Shelf Life

    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="benefit">

    <h2>🧬</h2>

    Enhanced Bioavailability

    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="benefit">

    <h2>♻️</h2>

    Reduced Packaging Waste

    </div>
    """, unsafe_allow_html=True)

st.header("Research Statistics")

s1,s2,s3,s4 = st.columns(4)

with s1:
    st.metric(
        "Nanometer Scale",
        "1–100"
    )

with s2:
    st.metric(
        "Applications",
        "20+"
    )

with s3:
    st.metric(
        "Research Fields",
        "15+"
    )

with s4:
    st.metric(
        "Industry Adoption",
        "Growing"
    )

st.markdown("""
<div class="quote">

"Small structures can create
big impacts in food systems."

</div>
""", unsafe_allow_html=True)

