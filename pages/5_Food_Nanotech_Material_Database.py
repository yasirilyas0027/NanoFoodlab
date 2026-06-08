import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Food Nanomaterial Database",
    page_icon="🔬",
    layout="wide"
)

# ======================
# CUSTOM CSS
# ======================

st.markdown("""
<style>

#database{

padding:100px 8%;

background:
linear-gradient(
180deg,
#f8fbff,
#eef7ff
);

font-family:'Poppins',sans-serif;

}

/* HERO */

.database-hero{

position:relative;

overflow:hidden;

padding:100px;

border-radius:35px;

background:
linear-gradient(
135deg,
#001f54,
#003566,
#00509d,
#0a9396
);

color:white;

box-shadow:
0 25px 60px rgba(0,0,0,.25);

}

.hero-content{

position:relative;
z-index:2;

}

.hero-tag{

display:inline-block;

padding:12px 24px;

border-radius:50px;

background:
rgba(255,255,255,.15);

backdrop-filter:blur(10px);

font-size:13px;

letter-spacing:1px;

}

.hero-content h1{

font-size:70px;

font-weight:800;

margin-top:25px;

margin-bottom:25px;

}

.hero-content p{

max-width:850px;

font-size:21px;

line-height:1.9;

}

.hero-stats{

display:flex;

gap:25px;

margin-top:50px;

flex-wrap:wrap;

}

.stat-box{

padding:30px;

min-width:220px;

border-radius:20px;

background:
rgba(255,255,255,.12);

backdrop-filter:blur(12px);

text-align:center;

transition:.4s;

}

.stat-box:hover{

transform:translateY(-10px);

}

.stat-box h2{

font-size:45px;

margin-bottom:10px;

}

/* PARTICLE */

.hero-particles{

position:absolute;

width:100%;
height:100%;

top:0;
left:0;

background-image:
radial-gradient(
white 1.5px,
transparent 1.5px
);

background-size:
50px 50px;

opacity:.15;

animation:
moveParticles 25s linear infinite;

}

@keyframes moveParticles{

0%{
transform:translateY(0);
}

100%{
transform:translateY(-200px);
}

}

/* SEARCH */

.database-tools{

margin-top:60px;

margin-bottom:60px;

}

#searchNano{

width:100%;

padding:22px;

font-size:18px;

border:none;

border-radius:20px;

box-shadow:
0 10px 25px rgba(0,0,0,.08);

}

/* FILTER */

.filter-area{

display:flex;

gap:15px;

justify-content:center;

margin-top:30px;

flex-wrap:wrap;

}

.filter-area button{

padding:15px 30px;

border:none;

border-radius:50px;

cursor:pointer;

font-weight:600;

background:white;

transition:.3s;

box-shadow:
0 4px 15px rgba(0,0,0,.08);

}

.filter-area button:hover,
.filter-area .active{

background:#00509d;

color:white;

}

/* GRID */

.nano-grid{

display:grid;

grid-template-columns:
repeat(auto-fit,minmax(450px,1fr));

gap:35px;

}

/* CARD */

.nano-card{

position:relative;

background:white;

border-radius:30px;

padding:30px;

box-shadow:
0 15px 40px rgba(0,0,0,.10);

transition:.4s;

overflow:hidden;

}

.nano-card:hover{

transform:
translateY(-12px);

box-shadow:
0 25px 60px rgba(0,0,0,.18);

}

.nano-card::before{

content:"";

position:absolute;

top:0;
left:0;

height:6px;
width:100%;

background:
linear-gradient(
90deg,
#00b4d8,
#0a9396
);

}

.nano-badge{

position:absolute;

top:20px;
right:20px;

padding:8px 18px;

border-radius:50px;

font-size:12px;

font-weight:600;

background:#0a9396;

color:white;

}

.nano-header{

display:flex;

gap:20px;

align-items:center;

margin-bottom:25px;

}

.nano-header img{

width:90px;
height:90px;

padding:15px;

background:#f2f8ff;

border-radius:20px;

}

.nano-header h2{

color:#003566;

font-size:30px;

}

.nano-body{

display:grid;

grid-template-columns:
repeat(2,1fr);

gap:18px;

}

.info-box{

background:#f8fbff;

padding:20px;

border-radius:18px;

}

.info-box h3{

margin-bottom:10px;

color:#00509d;

}

.safety{

background:
linear-gradient(
135deg,
#fff5f5,
#ffe4e4
);

border:
1px solid #ffc9c9;

}

.learn-btn{

margin-top:25px;

width:100%;

padding:16px;

border:none;

border-radius:15px;

background:
linear-gradient(
90deg,
#00509d,
#00b4d8
);

color:white;

font-weight:700;

cursor:pointer;

}

/* TABLE */

.comparison-table{

margin-top:100px;

background:white;

padding:40px;

border-radius:30px;

box-shadow:
0 12px 35px rgba(0,0,0,.08);

}

.comparison-table h2{

text-align:center;

margin-bottom:30px;

color:#003566;

}

table{

width:100%;

border-collapse:collapse;

}

th{

background:#003566;

color:white;

padding:18px;

}

td{

padding:18px;

text-align:center;

border-bottom:
1px solid #eee;

}

/* FACTS */

.nano-facts{

margin-top:80px;

}

.nano-facts h2{

text-align:center;

margin-bottom:40px;

color:#003566;

}

.fact-grid{

display:grid;

grid-template-columns:
repeat(auto-fit,minmax(300px,1fr));

gap:25px;

}

.fact-card{

padding:35px;

border-radius:25px;

background:
linear-gradient(
135deg,
#ffffff,
#eef8ff
);

box-shadow:
0 10px 30px rgba(0,0,0,.08);

font-size:18px;

line-height:1.8;

transition:.4s;

}

.fact-card:hover{

transform:
translateY(-10px);

}
            
</style>
""", unsafe_allow_html=True)

# ======================
# HERO
# ======================

st.markdown("""
<div class="hero">

<h4>🔬 FOOD NANOTECHNOLOGY KNOWLEDGE CENTER</h4>

<h1>Food Nanomaterial Database</h1>

<p>
Explore advanced nanomaterials used in modern food systems,
including food packaging, antimicrobial protection,
nutrient delivery, food preservation,
and smart sensing technologies.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="statbox">
    <h1>5</h1>
    Core Nanomaterials
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="statbox">
    <h1>25+</h1>
    Food Applications
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="statbox">
    <h1>100%</h1>
    Educational Resource
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ======================
# SEARCH
# ======================

search = st.text_input(
    "🔍 Search Nanomaterial"
)

category = st.selectbox(
    "Filter Category",
    [
        "All",
        "Antimicrobial",
        "Packaging",
        "Delivery System",
        "Biosensor"
    ]
)

# ======================
# DATABASE
# ======================

materials = [

{
    "Material":"ZnO NP",
    "Category":"Antimicrobial",
    "Function":"Antibacterial activity and UV blocking",
    "Advantages":[
        "Strong antimicrobial activity",
        "High stability",
        "Affordable production"
    ],
    "Applications":[
        "Food packaging",
        "Edible coating",
        "Food preservation"
    ],
    "Safety":
    "Requires concentration control and toxicity assessment."
},

{
    "Material":"TiO₂ NP",
    "Category":"Packaging",
    "Function":"UV shielding and photocatalytic activity",
    "Advantages":[
        "Excellent UV protection",
        "Photocatalytic cleaning",
        "Improves shelf life"
    ],
    "Applications":[
        "Active packaging",
        "Food coating",
        "Smart films"
    ],
    "Safety":
    "Migration studies required."
},

{
    "Material":"Chitosan NP",
    "Category":"Delivery System",
    "Function":"Controlled release carrier",
    "Advantages":[
        "Biodegradable",
        "Biocompatible",
        "Natural polymer"
    ],
    "Applications":[
        "Nutrient delivery",
        "Encapsulation",
        "Active packaging"
    ],
    "Safety":
    "Generally regarded as safe."
},

{
    "Material":"Silica NP",
    "Category":"Packaging",
    "Function":"Barrier enhancement",
    "Advantages":[
        "Improves strength",
        "Enhances barrier properties",
        "Low cost"
    ],
    "Applications":[
        "Packaging film",
        "Composite materials",
        "Food containers"
    ],
    "Safety":
    "Requires migration evaluation."
},

{
    "Material":"Silver NP",
    "Category":"Antimicrobial",
    "Function":"Broad-spectrum antimicrobial",
    "Advantages":[
        "Excellent antimicrobial activity",
        "Long-term protection",
        "High effectiveness"
    ],
    "Applications":[
        "Food packaging",
        "Surface coatings",
        "Active preservation"
    ],
    "Safety":
    "Potential toxicity concerns at high concentrations."
}

]

st.header("🧪 Nanomaterial Profiles")

for item in materials:

    if search.lower() not in item["Material"].lower():
        continue

    if category != "All" and category != item["Category"]:
        continue

    with st.expander(item["Material"]):

        st.markdown(f"""
        <div class="card">

        <h3>{item["Material"]}</h3>

        <b>Function</b><br>
        {item["Function"]}

        <br><br>

        <b>Advantages</b>

        </div>
        """, unsafe_allow_html=True)

        for adv in item["Advantages"]:
            st.write("✓", adv)

        st.write("")

        st.subheader("Applications")

        for app in item["Applications"]:
            st.write("•", app)

        st.warning(item["Safety"])

# ======================
# COMPARISON MATRIX
# ======================

st.header("📊 Nanomaterial Comparison Matrix")

comparison = pd.DataFrame({

"Material":[
    "ZnO NP",
    "TiO₂ NP",
    "Chitosan NP",
    "Silica NP",
    "Silver NP"
],

"Antimicrobial":[
    "★★★★★",
    "★★★★☆",
    "★★★★☆",
    "★★☆☆☆",
    "★★★★★"
],

"Barrier":[
    "★★★★☆",
    "★★★★★",
    "★★★★☆",
    "★★★★★",
    "★★★★☆"
],

"Safety":[
    "★★★☆☆",
    "★★★☆☆",
    "★★★★★",
    "★★★★☆",
    "★★☆☆☆"
],

"Cost":[
    "★★★★☆",
    "★★★★☆",
    "★★★☆☆",
    "★★★★★",
    "★★☆☆☆"
]

})

st.dataframe(
    comparison,
    use_container_width=True
)

# ======================
# SCIENTIFIC FACTS
# ======================

st.header("🧠 Scientific Facts")

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="fact">
    ZnO nanoparticles inhibit
    foodborne pathogens such as
    E. coli and Salmonella.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="fact">
    Silver nanoparticles exhibit
    broad-spectrum antimicrobial
    activity through Ag⁺ release.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="fact">
    Chitosan nanoparticles are
    biodegradable and derived
    from natural polymers.
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.caption(
    "Food Nanotechnology Database • Educational Demonstration Platform"
)