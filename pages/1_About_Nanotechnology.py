import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="About Food Nanotechnology",
    layout="wide"
)

# =============================================================================
# CLEANED & SCOPED CUSTOM CSS
# =============================================================================
st.markdown("""
<style>
/* Scoped Main Background modification */
.stAppDeployButton { display: none; } 

[data-testid="stAppViewContainer"] {
    background-color: #F8FAFC;
}

/* HERO SECTION */
.hero {
    height: auto;
    min-height: 60vh;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #001219 0%, #003566 40%, #0A9396 100%);
    border-radius: 0 0 30px 30px;
    padding: 60px 20px;
    margin-bottom: 40px;
}

.hero::before {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0; left: 0;
    background: radial-gradient(circle at center, rgba(255,255,255,0.08), transparent 70%);
}

.hero-content {
    position: relative;
    z-index: 10;
    max-width: 1000px;
    margin: auto;
}

.hero-title {
    font-size: clamp(36px, 5vw, 64px);
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
    letter-spacing: -1px;
}

.hero-subtitle {
    font-size: clamp(18px, 2.5vw, 24px);
    color: #D1FAE5;
    margin-bottom: 25px;
    font-weight: 400;
}

.hero-text {
    font-size: clamp(15px, 1.6vw, 18px);
    color: white;
    line-height: 1.8;
    max-width: 800px;
    margin: auto;
    opacity: 0.9;
}

/* ANIMATED PARTICLES */
.particle {
    position: absolute;
    border-radius: 50%;
    background: rgba(255,255,255,0.4);
    animation: float 15s infinite linear;
}
.p1 { width: 18px; height: 18px; top: 20%; left: 10%; }
.p2 { width: 10px; height: 10px; top: 70%; left: 20%; }
.p3 { width: 15px; height: 15px; top: 50%; left: 80%; }
.p4 { width: 25px; height: 25px; top: 25%; left: 70%; }
.p5 { width: 12px; height: 12px; top: 80%; left: 90%; }

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-30px); }
}

/* CONTAINERS & CARDS */
.glass-card {
    background: rgba(255,255,255,0.95);
    backdrop-filter: blur(15px);
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    margin-bottom: 20px;
    border: 1px solid rgba(0,0,0,0.05);
}

.section-title {
    font-size: 32px;
    font-weight: 700;
    color: #003566;
    margin-top: 40px;
    margin-bottom: 20px;
    letter-spacing: -0.5px;
}

.highlight {
    color: #0A9396;
    font-weight: bold;
}

/* MATERIAL NANO CARDS */
.nano-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    height: 300px;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 5px 20px rgba(0,0,0,0.04);
    margin-bottom: 25px;
    border: 1px solid #E2E8F0;
}

.nano-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.08);
}

.nano-icon { font-size: 40px; margin-bottom: 10px; }
.nano-title { font-size: 22px; font-weight: 700; color: #003566; }
.bulk { margin-top: 10px; color: #DC2626; font-weight: 600; font-size: 14px; }
.nano { margin-top: 5px; color: #059669; font-weight: 600; font-size: 14px; }

.nano-info {
    position: absolute;
    bottom: -100%; left: 0;
    width: 100%; height: 100%;
    padding: 25px;
    background: linear-gradient(135deg, #003566, #0A9396);
    color: white;
    transition: bottom 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

.nano-card:hover .nano-info { bottom: 0; }
.nano-info ul { padding-left: 20px; margin-top: 10px; }

/* INTERACTIVE EXPLORER */
.nano-scale { font-size: 60px; text-align: center; margin: 15px 0; }
.nano-result {
    padding: 15px; border-radius: 12px;
    font-size: 18px; font-weight: 600;
    text-align: center; margin-top: 20px; margin-bottom: 15px;
}
.nano-description {
    background: white; padding: 25px;
    border-radius: 12px; line-height: 1.8; font-size: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02);
    border: 1px solid #E2E8F0;
}

/* TIMELINE */
.timeline-section { padding: 10px 0 30px 0; }
.timeline-item {
    position: relative;
    border-left: 3px solid #0A9396;
    margin-left: 20px;
    padding-left: 30px;
    padding-bottom: 30px;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -11px; top: 5px;
    width: 18px; height: 18px;
    border-radius: 50%;
    background: #003566;
    border: 3px solid #D1FAE5;
    box-shadow: 0 0 8px rgba(10, 147, 150, 0.3);
}
.timeline-header { display: flex; align-items: center; gap: 15px; margin-bottom: 8px; flex-wrap: wrap; }
.timeline-v-year { font-size: 20px; font-weight: 800; color: #003566; background: #E0F2FE; padding: 2px 12px; border-radius: 8px; }
.timeline-v-event { font-size: 18px; font-weight: 700; color: #0A9396; }
.timeline-v-desc { font-size: 15px; color: #475569; line-height: 1.6; max-width: 900px; }

/* RESEARCH EXPLORER */
.research-card { background: white; padding: 35px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); border: 1px solid #E2E8F0; }
.research-title { font-size: 26px; font-weight: 700; color: #003566; margin-bottom: 10px; }
.research-badge { display: inline-block; padding: 4px 14px; background: #E0F2FE; color: #0369A1; border-radius: 20px; font-weight: 600; margin-bottom: 15px; font-size: 14px; }
.research-desc { font-size: 15px; line-height: 1.8; color: #475569; }
.application-card { background: white; padding: 20px; border-radius: 15px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.02); margin-bottom: 15px; border: 1px solid #E2E8F0; font-weight: 500; color: #334155; }
.application-icon { font-size: 32px; margin-bottom: 5px; }

/* PRODUCT SHOWCASE */
.product-card { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 8px 25px rgba(0,0,0,0.04); border: 1px solid #E2E8F0; }
.product-title { font-size: 24px; font-weight: 700; color: #003566; margin-bottom: 12px; }
.product-tag { display: inline-block; padding: 4px 12px; background: #DCFCE7; color: #166534; border-radius: 20px; margin-right: 6px; margin-bottom: 6px; font-size: 13px; font-weight: 500; }

/* SUPPLY CHAIN */
.supply-section-title { font-size: 32px; font-weight: 800; color: #003566; margin-top: 40px; margin-bottom: 10px; text-align: center; }
.supply-subtitle { font-size: 16px; color: #475569; text-align: center; margin-bottom: 35px; }
.supply-card { background: white; padding: 25px 20px; border-radius: 20px; text-align: center; height: 100%; min-height: 220px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.03); border: 1px solid #E2E8F0; transition: transform 0.3s ease, box-shadow 0.3s ease; }
.supply-card:hover { transform: translateY(-5px); box-shadow: 0 15px 30px rgba(10, 147, 150, 0.08); border-color: rgba(10, 147, 150, 0.2); }
.supply-icon { font-size: 40px; margin-bottom: 12px; }
.supply-title { font-size: 20px; font-weight: 700; color: #003566; margin-bottom: 10px; }
.supply-desc-list { list-style: none; padding: 0; margin: 0; }
.supply-desc-list li { font-size: 14px; color: #475569; line-height: 1.8; }
.supply-flow-badge { display: flex; justify-content: center; align-items: center; gap: 15px; background: rgba(0,53,102,0.03); padding: 12px 25px; border-radius: 30px; max-width: 500px; margin: 30px auto 10px auto; border: 1px dashed rgba(10, 147, 150, 0.2); }
.flow-step { font-size: 20px; }
.flow-arrow { color: #0A9396; font-weight: 700; }

/* BEFORE VS AFTER */
.comp-section-title { font-size: 32px; font-weight: 800; color: #003566; margin-top: 50px; margin-bottom: 10px; text-align: center; }
.comp-subtitle { font-size: 16px; color: #475569; text-align: center; margin-bottom: 35px; }
.before-card { background: #FFF5F5; padding: 30px; border-radius: 20px; height: 100%; min-height: 260px; border-left: 6px solid #EF4444; box-shadow: 0 8px 25px rgba(239, 68, 68, 0.02); }
.after-card { background: #F0FDF4; padding: 30px; border-radius: 20px; height: 100%; min-height: 260px; border-left: 6px solid #10B981; box-shadow: 0 8px 25px rgba(16, 185, 129, 0.02); }
.compare-title { font-size: 20px; font-weight: 700; margin-bottom: 18px; }
.before-card .compare-title { color: #991B1B; }
.after-card .compare-title { color: #065F46; }
.compare-list { list-style: none; padding: 0; margin: 0; }
.compare-item { font-size: 15px; margin-bottom: 12px; line-height: 1.6; color: #334155; display: flex; align-items: center; gap: 8px; }
.vs-arrow-container { display: flex; justify-content: center; align-items: center; height: 100%; min-height: 260px; }
.vs-arrow { font-size: 36px; color: #0A9396; font-weight: bold; }

/* STATISTICS & IMPACT */
.stats-container { margin-top: 20px; margin-bottom: 30px; }
.stat-box { background: linear-gradient(135deg, #003566 0%, #0A9396 100%); padding: 25px 20px; border-radius: 20px; text-align: center; color: white; box-shadow: 0 8px 25px rgba(10, 147, 150, 0.1); min-height: 140px; display: flex; flex-direction: column; justify-content: center; }
.stat-number { font-size: 40px; font-weight: 800; line-height: 1; margin-bottom: 6px; }
.stat-label { font-size: 14px; font-weight: 500; opacity: 0.9; }
.ranking-list { margin-top: 15px; }
.ranking-item { padding: 15px; background: rgba(248, 250, 252, 0.9); border-radius: 12px; margin-bottom: 12px; border-left: 4px solid #0A9396; border-right: 1px solid #E2E8F0; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; }
.ranking-item h5 { margin: 0 0 5px 0; font-size: 15px; color: #003566; font-weight: 700; }
.ranking-item p { margin: 0; font-size: 13px; color: #475569; }

/* ECOSYSTEM */
.eco-card { background: white; padding: 25px 15px; border-radius: 20px; text-align: center; min-height: 240px; height: 100%; box-shadow: 0 8px 25px rgba(0,0,0,0.02); border: 1px solid #E2E8F0; display: flex; flex-direction: column; justify-content: flex-start; align-items: center; }
.eco-icon { font-size: 40px; margin-bottom: 10px; }
.eco-title { font-size: 16px; font-weight: 700; color: #003566; margin-bottom: 12px; }
.eco-desc-tag { display: inline-block; font-size: 12px; color: #475569; background: #F1F5F9; padding: 3px 10px; border-radius: 6px; margin: 3px 0; width: 90%; font-weight: 500; }
.eco-pipeline-badge { display: flex; justify-content: center; align-items: center; gap: 20px; background: rgba(0,53,102,0.03); padding: 15px 35px; border-radius: 30px; max-width: 600px; margin: 40px auto 20px auto; border: 1px dashed rgba(10, 147, 150, 0.2); }
.eco-flow-step { font-size: 24px; }
.eco-flow-arrow { color: #0A9396; font-size: 20px; }

/* FUTURE SECTION */
.future-card { background: linear-gradient(135deg, #003566, #0A9396); padding: 35px; border-radius: 20px; color: white; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
.future-title { font-size: 26px; font-weight: 700; margin-bottom: 12px; }
.future-desc { font-size: 16px; line-height: 1.8; opacity: 0.95; }
.future-stat { background: white; padding: 20px; border-radius: 15px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.03); margin-bottom: 25px; border: 1px solid #E2E8F0; }
.future-number { font-size: 32px; font-weight: 800; color: #003566; margin-bottom: 5px; }
.future-label { font-size: 13px; color: #475569; font-weight: 500; }

/* IMPACT DASHBOARD */
.impact-card { background: linear-gradient(135deg, #003566, #0A9396); padding: 25px 15px; border-radius: 20px; text-align: center; color: white !important; min-height: 180px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); margin-bottom: 20px; }
.impact-icon { font-size: 36px; margin-bottom: 8px; }
.impact-number { font-size: 32px; font-weight: 800; line-height: 1.2; }
.impact-title { font-size: 14px; margin-top: 6px; font-weight: 500; opacity: 0.9; }
.impact-growth { font-size: 14px; color: #A7F3D0; font-weight: 700; margin-top: 6px; background: rgba(167, 243, 208, 0.15); padding: 2px 10px; border-radius: 15px; display: inline-block; }

/* QUIZ CENTER */
.quiz-header-box { background: #ffffff; padding: 25px; border-radius: 15px; border-left: 5px solid #003566; box-shadow: 0 5px 20px rgba(0,0,0,0.03); margin-bottom: 25px; border-right: 1px solid #E2E8F0; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; }
.quiz-question-title { font-size: 18px; font-weight: 600; color: #003566; margin-bottom: 5px; }

/* CLOSING QUOTE */
.quote-container { background: #F8FAFC; border-left: 4px solid #0A9396; padding: 25px; border-radius: 0 20px 20px 0; margin: 40px 0 30px 0; text-align: center; border-right: 1px solid #E2E8F0; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0; }
.quote-text { font-size: 20px; font-style: italic; color: #003566; line-height: 1.6; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HERO SECTION
# =============================================================================
st.markdown("""
<div class="hero">
    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="particle p5"></div>
    <div class="hero-content">
        <h1 class="hero-title">FOOD NANOTECHNOLOGY</h1>
        <h3 class="hero-subtitle">Transforming Food Systems at the Nanoscale</h3>
        <p class="hero-text">
            Exploring nanoscale innovations that enhance food quality, bioavailability, safety, 
            active packaging performance, and sustainable food systems for the next generation.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# SECTION 1: INTRODUCTION
# =============================================================================
st.markdown('<h1 class="section-title">What is Food Nanotechnology?</h1>', unsafe_allow_html=True)
left, right = st.columns([1, 1], gap="large")

with left:
    # PERBAIKAN: Menggunakan tautan gambar langsung (direct link) yang valid dari Wikimedia
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/b/b8/A_high-resolution_translation_of_nanotechnology_concept.jpg",
        use_container_width=True,
        caption="Nanotechnology Engineering & Research Laboratory"
    )

with right:
    st.markdown("""
    <div class="glass-card">
        <h2>Understanding Nanotechnology</h2>
        <p>
            Food nanotechnology refers to the application of nanoscale materials and engineered systems 
            ranging from <span class="highlight">1–100 nanometers</span> to improve food quality, 
            safety, functionality, and nutrient delivery.
        </p>
        <p>
            At this scale, particles exhibit unique physicochemical properties including larger surface area, 
            improved reactivity, enhanced solubility, and controlled release behavior.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 2: WHY NANOSCALE IS SPECIAL
# =============================================================================
st.markdown('<h1 class="section-title">Why Nanoscale Is Special?</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <h3>The Nanoscale Advantage</h3>
    <p>
        When particle size is reduced to 1–100 nm, materials develop unique properties 
        that can significantly improve food functionality, stability, bioavailability, 
        and antimicrobial performance.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="nano-card">
        <div class="nano-icon">🪨</div>
        <div class="nano-title">Silver</div>
        <div class="bulk">Bulk: Lower antibacterial activity</div>
        <div class="nano">Nano: Strong antibacterial activity</div>
        <div class="nano-info">
            <h3>Silver Nanoparticles</h3>
            <ul>
                <li>Enhanced surface area</li>
                <li>Strong antimicrobial effect</li>
                <li>Food packaging applications</li>
                <li>Shelf life extension</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="nano-card">
        <div class="nano-icon">🫚</div>
        <div class="nano-title">Curcumin</div>
        <div class="bulk">Bulk: Poor water solubility</div>
        <div class="nano">Nano: Improved bioavailability</div>
        <div class="nano-info">
            <h3>Nano Curcumin</h3>
            <ul>
                <li>Improved absorption</li>
                <li>Enhanced stability</li>
                <li>Controlled release profile</li>
                <li>Functional ingredient</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="nano-card">
        <div class="nano-icon">☀️</div>
        <div class="nano-title">Vitamin D</div>
        <div class="bulk">Bulk: Low stability</div>
        <div class="nano">Nano: Enhanced stability</div>
        <div class="nano-info">
            <h3>Nano Vitamin D</h3>
            <ul>
                <li>Protected from degradation</li>
                <li>Better intestinal absorption</li>
                <li>Targeted food fortification</li>
                <li>Longer shelf stability</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

col4, col5 = st.columns(2)
with col4:
    st.markdown("""
    <div class="nano-card">
        <div class="nano-icon">🥕</div>
        <div class="nano-title">β-Carotene</div>
        <div class="bulk">Bulk: Low absorption</div>
        <div class="nano">Nano: Higher absorption</div>
        <div class="nano-info">
            <h3>Nano β-Carotene</h3>
            <ul>
                <li>Improved cellular uptake</li>
                <li>Oxidation protection</li>
                <li>Color stabilization</li>
                <li>Nutrient enhancement</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="nano-card">
        <div class="nano-icon">🌿</div>
        <div class="nano-title">Essential Oil</div>
        <div class="bulk">Bulk: Highly volatile</div>
        <div class="nano">Nano: Controlled release</div>
        <div class="nano-info">
            <h3>Nano Essential Oil</h3>
            <ul>
                <li>Reduced core volatility</li>
                <li>Sustained controlled release</li>
                <li>Prolonged antimicrobial activity</li>
                <li>Active packaging integration</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

selected = st.selectbox(
    "Explore Detailed Material Analysis",
    ["Silver", "Curcumin", "Vitamin D", "β-Carotene", "Essential Oil"]
)

# 1. CURCUMIN
if selected == "Curcumin":
    show_structure = st.checkbox("👁️ Tampilkan Diagram Struktur Kimia Curcumin", value=True)
    if show_structure:
        sc1, sc2, sc3 = st.columns([1, 2, 1])
        with sc2:
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/9/98/Curcumin_structure.svg",
                use_container_width=True
            )
            if st.button("❌ Tutup Gambar Struktur", key="btn_curcumin"):
                st.rerun()
        st.info("""
        **Nanoencapsulation of Curcumin** meningkatkan dispersibilitas air, stabilitas saluran pencernaan, 
        dan tingkat bioavailabilitas sistemik, menjadikannya sangat ideal untuk komponen pangan fungsional.
        """)

# 2. SILVER (PERAK)
elif selected == "Silver":
    show_structure = st.checkbox("👁️ Tampilkan Ilustrasi Mekanisme Nanopartikel Perak", value=True)
    if show_structure:
        sc1, sc2, sc3 = st.columns([1, 2, 1])
        with sc2:
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/e/ee/Silver_crystal.svg",
                use_container_width=True
            )
            if st.button("❌ Tutup Gambar Struktur", key="btn_silver"):
                st.rerun()
        st.success("""
        **Silver Nanoparticles (AgNPs)** memberikan luas permukaan kontak yang masif untuk berinteraksi dengan dinding sel mikroba. 
        Sistem ini merusak membran sel bakteri dan sangat efektif diaplikasikan pada *active packaging* untuk memperpanjang masa simpan produk makanan.
        """)

# 3. VITAMIN D
elif selected == "Vitamin D":
    show_structure = st.checkbox("👁️ Tampilkan Diagram Struktur Kimia Vitamin D3", value=True)
    if show_structure:
        sc1, sc2, sc3 = st.columns([1, 2, 1])
        with sc2:
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/9/9f/Cholecalciferol2.svg",
                use_container_width=True
            )
            if st.button("❌ Tutup Gambar Struktur", key="btn_vitd"):
                st.rerun()
        st.info("""
        **Nanoencapsulation of Vitamin D** memproteksi senyawa hidrofobik ini dari degradasi akibat paparan asam lambung, panas, dan oksigen. 
        Sistem pembawa nano (seperti nanoemulsi) mengaburkan fase minyaknya sehingga Vitamin D dapat larut jernih dalam produk berbasis air seperti susu rendah lemak atau minuman fungsional.
        """)

# 4. β-CAROTENE
elif selected == "β-Carotene":
    show_structure = st.checkbox("👁️ Tampilkan Diagram Struktur Kimia β-Carotene", value=True)
    if show_structure:
        sc1, sc2, sc3 = st.columns([1, 1.5, 1])
        with sc2:
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/7/70/Beta-carotene-2D-skeletal.svg",
                use_container_width=True
            )
            if st.button("❌ Tutup Gambar Struktur", key="btn_beta"):
                st.rerun()
        st.warning("""
        **Beta-Carotene Nanoparticles** memperkecil ukuran droplet kristal menjadi skala nano untuk melewati lapisan batas tidak teraduk (*unstirred water layer*) di usus secara efisien. 
        Rekayasa ini meningkatkan penyerapan seluler (bioavailabilitas) sekaligus melindungi stabilitas warna alaminya dari proses oksidasi.
        """)

# 5. ESSENTIAL OIL (MINYAK ATSIRI)
elif selected == "Essential Oil":
    show_structure = st.checkbox("👁️ Tampilkan Ilustrasi Sistem Penghantaran Minyak Atsiri", value=True)
    if show_structure:
        sc1, sc2, sc3 = st.columns([1, 2, 1])
        with sc2:
            st.image(
                "https://upload.wikimedia.org/wikipedia/commons/a/a4/Micelle_scheme-en.svg",
                use_container_width=True
            )
            if st.button("❌ Tutup Gambar Struktur", key="btn_eo"):
                st.rerun()
        st.success("""
        **Nanoencapsulated Essential Oil** berhasil mengunci sifat inti minyak atsiri yang sangat volatil (mudah menguap) dan berbau menyengat. 
        Enkapsulasi dalam nanostruktur (seperti lipid padat atau liposom) menjamin *sustained controlled release* (pelepasan antimikroba secara berkala) di dalam kemasan pintar.
        """)
        
# =============================================================================
# SECTION 3: INTERACTIVE NANOSCALE EXPLORER
# =============================================================================
st.markdown('<h1 class="section-title">Interactive Nanoscale Explorer</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <h3>Explore Particle Size Behavior</h3>
    <p>Geser nilai slider di bawah untuk melihat bagaimana ukuran partikel memengaruhi karakteristik material serta pengaplikasiannya pada teknologi pangan fungsional.</p>
</div>
""", unsafe_allow_html=True)

size = st.slider("Particle Size (nm)", min_value=1, max_value=100, value=50)

st.markdown(f"""
<div class="nano-scale">⚛️</div>
<h2 style='text-align:center; color:#0A9396; margin-bottom: 15px;'>{size} nm</h2>
""", unsafe_allow_html=True)

st.progress(size / 100)

if size <= 20:
    st.markdown('<div class="nano-result" style="background:#DCFCE7; color:#166534;">Ultra-Small Nanoparticles</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nano-description">
        Partikel pada rentang ekstrem ini memiliki luas permukaan spesifik dan reaktivitas yang sangat tinggi.<br><br>
        <b>Aplikasi Utama:</b><br>
        • Advanced Nanoencapsulation & Targeted Drug Delivery<br>
        • Penyerapan presisi senyawa bioaktif murni<br>
        • Sistem penghantaran seluler intraselular
    </div>
    """, unsafe_allow_html=True)
elif size <= 50:
    st.markdown('<div class="nano-result" style="background:#DBEAFE; color:#1E40AF;">Typical Nanoencapsulation Range</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nano-description">
        Rentang standar emas yang paling sering digunakan industri pangan fungsional saat ini.<br><br>
        <b>Aplikasi Utama:</b><br>
        • Formulasi Nanoemulsi stabil<br>
        • Proteksi Curcumin & Vitamin larut lemak dari degradasi asam lambung<br>
        • Pengawetan antioksidan peka cahaya
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown('<div class="nano-result" style="background:#FEF3C7; color:#92400E;">Approaching Micro-scale</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nano-description">
        Keunggulan fenomena mekanika kuantum dan luas permukaan mulai menurun seiring mendekatnya ukuran ke skala makro.<br><br>
        <b>Catatan Sistem:</b> Penggunaan energi sistem mungkin menjadi kurang efisien dibandingkan performa *true nanosystems* (&lt; 50 nm) untuk pemuatan zat aktif hidrofobik.
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 4: EVOLUTION OF FOOD NANOTECHNOLOGY
# =============================================================================
st.markdown('<h1 class="section-title">Evolution of Food Nanotechnology</h1>', unsafe_allow_html=True)
st.markdown('<div class="timeline-section">', unsafe_allow_html=True)

timeline_data = [
    {"year": "1980", "event": "Nanoscience Development", "desc": "Fase fondasi dasar. Penemuan awal fenomena skala nano dan rekayasa material mulai diamati secara intensif di laboratorium fisika/kimia murni."},
    {"year": "2000", "event": "Nanofood Research Begins", "desc": "Penelitian aplikasi pangan pertama kali dieksplorasi secara global, fokus pada rekayasa makromolekul dan modifikasi tekstur dasar makanan."},
    {"year": "2010", "event": "Nanoencapsulation Boom", "desc": "Terjadi lonjakan masif pada riset sistem penghantaran zat bioaktif. Enkapsulasi vitamin dan probiotik sukses mendongkrak stabilitas nutrisi."},
    {"year": "2020", "event": "Smart & Active Packaging Era", "desc": "Komersialisasi kemasan pintar berbasis polimer antimikroba (nanosilver/ZnO) untuk mendeteksi pembusukan daging & buah secara berkala."},
    {"year": "2030", "event": "Intelligent Food Systems (Future Vision)", "desc": "Visi sistem pangan berbasis kecerdasan buatan (AI) terintegrasi dengan pelepasan nutrisi otomatis di tubuh serta personalized nutrition."}
]

for item in timeline_data:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-header">
            <span class="timeline-v-year">{item['year']}</span>
            <span class="timeline-v-event">{item['event']}</span>
        </div>
        <div class="timeline-v-desc">{item['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =============================================================================
# SECTION 5: RESEARCH FIELD EXPLORER
# =============================================================================
st.markdown('<h1 class="section-title">Research Field Explorer</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <h3>Explore Major Research Areas</h3>
    <p>Food nanotechnology integrates multiple research fields aimed at improving food quality, safety, sustainability, and nutritional performance.</p>
</div>
""", unsafe_allow_html=True)

field = st.selectbox(
    "Select Research Area",
    ["Nanoencapsulation", "Nanoemulsion", "Edible Coating", "Nanosensor", "Active Packaging"]
)

def render_research_area(badge, title, desc, app1, app2, app3, img_url):
    show_img = st.checkbox(f"📷 Tampilkan Visualisasi Terkait {title}", value=True)
    
    if show_img:
        r_left, r_right = st.columns([1, 1], gap="medium")
        with r_left:
            st.image(img_url, use_container_width=True)
            if st.button("❌ Sembunyikan Gambar Visualisasi"):
                st.rerun()
        with r_right:
            st.markdown(f"""
            <div class="research-card">
                <div class="research-badge">{badge}</div>
                <div class="research-title">{title}</div>
                <div class="research-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="research-card" style="margin-bottom: 20px;">
            <div class="research-badge">{badge}</div>
            <div class="research-title">{title}</div>
            <div class="research-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("") 
    a1, a2, a3 = st.columns(3)
    with a1: st.markdown(f'<div class="application-card"><div class="application-icon">{app1[0]}</div>{app1[1]}</div>', unsafe_allow_html=True)
    with a2: st.markdown(f'<div class="application-card"><div class="application-icon">{app2[0]}</div>{app2[1]}</div>', unsafe_allow_html=True)
    with a3: st.markdown(f'<div class="application-card"><div class="application-icon">{app3[0]}</div>{app3[1]}</div>', unsafe_allow_html=True)

if field == "Nanoencapsulation":
    render_research_area(
        "Bioactive Delivery Systems", "Nanoencapsulation",
        "Nanoencapsulation melindungi senyawa sensitif seperti vitamin, antioksidan, probiotik, dan fitokimia dari kerusakan lingkungan luar guna meningkatkan aspek bioavailabilitas tubuh.",
        ("💊", "Functional Foods"), ("🧬", "Nutraceuticals"), ("🍊", "Vitamin Delivery"),
        "https://images.unsplash.com/photo-1584017911766-d451b3d0e843?auto=format&fit=crop&q=80&w=800"
    )
elif field == "Nanoemulsion":
    render_research_area(
        "Lipid-Based Delivery System", "Nanoemulsion",
        "Sistem koloid droplet minyak-air berskala 20–200 nm untuk mempermudah pelarutan komponen hidrofobik/lipofilik seperti kurkuminoid dan minyak esensial ke produk minuman encer.",
        ("🥛", "Dairy Products"), ("🥤", "Functional Beverages"), ("🍋", "Essential Oils"),
        "https://images.unsplash.com/photo-1628771065518-0d82f1938462"
    )
elif field == "Edible Coating":
    render_research_area(
        "Sustainable Preservation Technology", "Edible Coating",
        "Lapisan pelindung biodegradable tipis berbasis hidrokoloid yang diperkuat serat nanofiller (seperti nanocellulose) untuk menahan laju migrasi gas oksigen dan air pada komoditas segar.",
        ("🍓", "Strawberry Protection"), ("🍎", "Apple Preservation"), ("🥭", "Mango Shelf-Life"),
        "https://images.unsplash.com/photo-1464965911861-746a04b4bca6"
    )
elif field == "Nanosensor":
    render_research_area(
        "Intelligent Monitoring System", "Nanosensor",
        "Perangkat analitik nano guna mengidentifikasi perubahan volatilitas gas amonia, kelembaban, atau perkembangan koloni bakteri patogen pada produk segar pangan secara real-time.",
        ("📡", "Spoilage Detection"), ("🌡️", "Temperature Monitoring"), ("🦠", "Pathogen Detection"),
        "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789"
    )
elif field == "Active Packaging":
    render_research_area(
        "Smart Food Packaging Technology", "Active Packaging",
        "Kemasan aktif yang melepaskan senyawa fungsional antimikroba secara terkendali ke ruang kosong kemasan guna menekan aktivitas pembusukan mikroba eksternal.",
        ("📦", "Shelf-Life Extension"), ("🦠", "Antimicrobial Packaging"), ("🌿", "Essential Oil Packaging"),
        "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da"
    )

# =============================================================================
# SECTION 6: INTERACTIVE PRODUCT SHOWCASE
# =============================================================================
st.write("")
st.markdown('<h1 class="section-title">Interactive Food Product Showcase</h1>', unsafe_allow_html=True)

tabs = st.tabs(["🥛 Milk", "🍓 Fruit", "🥩 Meat", "🥤 Beverage"])

with tabs[0]:
    t_left, t_right = st.columns(2, gap="medium")
    with t_left:
        st.image("https://images.unsplash.com/photo-1550583724-b2692b85b150", use_container_width=True)
    with t_right:
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Nano Fortified Milk</div>
            Sistem nanoemulsi mampu mendispersikan konsentrasi Vitamin D lipid secara merata dalam matriks air susu tanpa memicu separasi krim fase lemak.
            <br><br>
            <span class="product-tag">Vitamin D</span>
            <span class="product-tag">Calcium</span>
            <span class="product-tag">Nanoemulsion</span>
        </div>
        """, unsafe_allow_html=True)

with tabs[1]:
    t_left, t_right = st.columns(2, gap="medium")
    with t_left:
        st.image("https://images.unsplash.com/photo-1464965911861-746a04b4bca6", use_container_width=True)
    with t_right:
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Nano Edible Coating</div>
            Pelapis berbahan matriks kitosan/nanoselulosa terbukti mampu menghambat proses respirasi buah klimaterik dan menjaga kekerasan tekstur buah.
            <br><br>
            <span class="product-tag">Edible Coating</span>
            <span class="product-tag">Nanocellulose</span>
            <span class="product-tag">Shelf-Life Extension</span>
        </div>
        """, unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    c1.metric("Weight Loss Reduction", "↓ 35%")
    c2.metric("Shelf Life Expansion", "+7 Days")
    c3.metric("Microbial Growth", "Highly Reduced")
    st.success("Nano edible coatings secara signifikan mempertahankan kadar air, kesegaran warna, dan menghambat pertumbuhan jamur pembusuk strawberry.")

with tabs[2]:
    t_left, t_right = st.columns(2, gap="medium")
    with t_left:
        st.image("https://images.unsplash.com/photo-1607623814075-e51df1bdc82f", use_container_width=True)
    with t_right:
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Active Packaging for Meat</div>
            Sistem pengemasan film polimer hibrida nano-silver mematikan replikasi dinding sel bakeri gram negatif/positif pada permukaan daging segar.
            <br><br>
            <span class="product-tag">Silver Nanoparticles</span>
            <span class="product-tag">Antimicrobial</span>
            <span class="product-tag">Active Packaging</span>
        </div>
        """, unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    c1.metric("Shelf Life Expansion", "+40%")
    c2.metric("Microbial Bio-burden", "↓ Significant")
    c3.metric("Food Safety Rate", "Improved")
    st.info("Integrasi partikel nano-perak mengeliminasi kolonisasi kontaminan mikroba patogen berbahaya selama fase distribusi logistik rantai dingin.")

with tabs[3]:
    t_left, t_right = st.columns(2, gap="medium")
    with t_left:
        st.image("https://images.unsplash.com/photo-1547592180-85f173990554", use_container_width=True)
    with t_right:
        st.markdown("""
        <div class="product-card">
            <div class="product-title">Nanoemulsion Beverage</div>
            Formulasi droplet minyak seukuran sub-mikron menjamin kejernihan sifat optik minuman fungsional berbasis kurkuminoid tanpa pengendapan kotoran.
            <br><br>
            <span class="product-tag">Curcumin</span>
            <span class="product-tag">Nanoemulsion</span>
            <span class="product-tag">Antioxidant Delivery</span>
        </div>
        """, unsafe_allow_html=True)
    st.write("")
    c1, c2, c3 = st.columns(3)
    c1.metric("Bioavailability Rate", "↑ High")
    c2.metric("Water Solubility", "Optimized")
    c3.metric("Thermostability", "Enhanced")
    st.success("Formulasi nanoemulsi kurkumin mengoptimalkan tingkat absorpsi usus dan stabilitas antioksidan dalam fasa sediaan cair.")

# =============================================================================
# REVISED SECTION: NANOTECHNOLOGY ACROSS THE FOOD SUPPLY CHAIN
# =============================================================================
st.markdown('<h1 class="supply-section-title">Nanotechnology Across the Food Supply Chain</h1>', unsafe_allow_html=True)
st.markdown('<p class="supply-subtitle">From Farm to Fork: Exploring How Nanomaterials Reshape Every Milestone of the Food Lifecycle</p>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-card" style="margin-bottom: 30px;">
    <h4 style="color:#003566; margin-bottom:10px;">The Ecosystem Transformation</h4>
    <p style="color:#475569; font-size:16px; margin:0; line-height:1.7;">
        Intervensi rekayasa skala nano tidak bekerja secara parsial. Keberhasilan integrasi dimulai dari minimalisasi input agrokimia di lahan pertanian hingga optimalisasi absorbsi nutrisi tingkat seluler di dalam tubuh konsumen.
    </p>
</div>
""", unsafe_allow_html=True)

row1_col1, row1_col2, row1_col3 = st.columns(3, gap="medium")

with row1_col1:
    st.markdown("""
    <div class="supply-card">
        <div class="supply-icon">🌱</div>
        <div class="supply-title">1. Agriculture</div>
        <ul class="supply-desc-list">
            <li>• Targeted Nanofertilizers</li>
            <li>• Smart Nanopesticides</li>
            <li>• Real-time Crop Monitoring</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="supply-card">
        <div class="supply-icon">🏭</div>
        <div class="supply-title">2. Processing</div>
        <ul class="supply-desc-list">
            <li>• Kinetic-stable Nanoemulsions</li>
            <li>• Controlled Nanoencapsulation</li>
            <li>• Tailored Bioactive Ingredients</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown("""
    <div class="supply-card">
        <div class="supply-icon">📦</div>
        <div class="supply-title">3. Packaging</div>
        <ul class="supply-desc-list">
            <li>• Active Antimicrobial Films</li>
            <li>• Gas Barrier Enhancements</li>
            <li>• Smart Spoilage Indicators</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col_side1, row2_col1, row2_col2, col_side2 = st.columns([0.5, 2, 2, 0.5], gap="medium")

with row2_col1:
    st.markdown("""
    <div class="supply-card">
        <div class="supply-icon">🚚</div>
        <div class="supply-title">4. Distribution</div>
        <ul class="supply-desc-list">
            <li>• Nanowire Temperature Sensors</li>
            <li>• Dynamic Freshness Tracking</li>
            <li>• Cold-chain Logistics IoT</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
    <div class="supply-card">
        <div class="supply-icon">🍽️</div>
        <div class="supply-title">5. Consumer Health</div>
        <ul class="supply-desc-list">
            <li>• Precision Bioavailability</li>
            <li>• Accelerated Intestinal Uptake</li>
            <li>• Personalized Functional Foods</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="supply-flow-badge">
    <span class="flow-step">🌱</span>
    <span class="flow-arrow">→</span>
    <span class="flow-step">🏭</span>
    <span class="flow-arrow">→</span>
    <span class="flow-step">📦</span>
    <span class="flow-arrow">→</span>
    <span class="flow-step">🚚</span>
    <span class="flow-arrow">→</span>
    <span class="flow-step">🍽️</span>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# DATA DICTIONARY (BEFORE VS AFTER)
# =============================================================================
compound_data = {
    "Curcumin": {
        "before_title": "Conventional Curcumin",
        "before_points": ["Low water solubility", "Poor gastrointestinal stability", "Limited intestinal absorption", "Rapid metabolic degradation"],
        "after_title": "Nanoencapsulated Curcumin",
        "after_points": ["High water solubility (Up to 10,000x)", "Enhanced gastric acid stability", "Significantly improved bioavailability", "Controlled & sustained cellular release"]
    },
    "Vitamin D": {
        "before_title": "Standard Vitamin D3",
        "before_points": ["Highly sensitive to UV light & air", "Low stability in liquid food matrices", "Inconsistent absorption with low-fat meals", "Prone to oxidation during storage"],
        "after_title": "Nanostructured Lipid Vitamin D",
        "after_points": ["Robust thermal and UV protection", "Perfect dispersion in water-based drinks", "High absorption regardless of diet fat content", "Extended shelf-life with zero potency loss"]
    },
    "Essential Oil": {
        "before_title": "Raw Essential Oils",
        "before_points": ["Strong, overpowering volatile aroma", "Rapid evaporation when exposed to heat", "Immiscible in water (phases separate)", "High oxidation speed"],
        "after_title": "Nanoemulsified Essential Oils",
        "after_points": ["Masked taste & controlled odor profile", "Thermal stability during pasteurization", "Homogeneous clear water solubility", "Long-lasting antimicrobial active protection"]
    },
    "β-Carotene": {
        "before_title": "Crystalline β-Carotene",
        "before_points": ["Poor dissolution in bio-fluids", "Extremely low cellular uptake", "Changes color easily under light stress", "Prone to chemical degradation"],
        "after_title": "Nanomicellar β-Carotene",
        "after_points": ["Instant micellar solubilization", "Maximised intestinal permeability", "High color stability in transparent drinks", "Protected antioxidant properties"]
    }
}

# =============================================================================
# SECTION: BEFORE VS AFTER INTERFACES
# =============================================================================
st.markdown('<h1 class="comp-section-title">Before vs After Nanotechnology</h1>', unsafe_allow_html=True)
st.markdown('<p class="comp-subtitle">Melihat Perubahan Nyata Karakteristik Senyawa Bioaktif Melalui Rekayasa Skala Nano</p>', unsafe_allow_html=True)

st.markdown('<div class="glass-card" style="padding: 25px; margin-bottom: 35px;">', unsafe_allow_html=True)
selected_compound = st.selectbox(
    "Pilih Senyawa untuk Analisis Perbandingan:",
    list(compound_data.keys()),
    index=0
)
st.markdown("""
    <p style="color:#64748B; font-size:14px; margin: 10px 0 0 0;">
        *Gunakan menu dropdown di atas untuk beralih senyawa dan melihat bagaimana struktur nano memecahkan keterbatasan fisik senyawa organik konvensional.
    </p>
</div>
""", unsafe_allow_html=True)

data = compound_data[selected_compound]

left, middle, right = st.columns([4.5, 1, 4.5])

with left:
    before_html = f"""
    <div class="before-card">
        <div class="compare-title">{data['before_title']}</div>
        <ul class="compare-list">
    """
    for point in data['before_points']:
        before_html += f'<li class="compare-item">❌ {point}</li>'
    before_html += "</ul></div>"
    st.markdown(before_html, unsafe_allow_html=True)

with middle:
    st.markdown("""
    <div class="vs-arrow-container">
        <div class="vs-arrow">➜</div>
    </div>
    """, unsafe_allow_html=True)

with right:
    after_html = f"""
    <div class="after-card">
        <div class="compare-title">{data['after_title']}</div>
        <ul class="compare-list">
    """
    for point in data['after_points']:
        after_html += f'<li class="compare-item">✓ {point}</li>'
    after_html += "</ul></div>"
    st.markdown(after_html, unsafe_allow_html=True)

# =============================================================================
# SECTION 9: REAL RESEARCH STATISTICS
# =============================================================================
st.markdown('<h1 class="section-title">Research Statistics Dashboard</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <h3>Global Research Trends Analysis</h3>
    <p>
        Food nanotechnology terus mengalami ekspansi eksponensial di kancah global. Dataset di bawah ini merangkum total volume 
        publikasi ilmiah internasional (peer-reviewed papers) yang berfokus pada optimasi sistem pangan fungsional berskala nano.
    </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">540</div>
        <div class="stat-label">Nanoencapsulation</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">320</div>
        <div class="stat-label">Active Packaging</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">260</div>
        <div class="stat-label">Nanoemulsion</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-number">180</div>
        <div class="stat-label">Nanosensors</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

chart_col, insight_col = st.columns([5, 4], gap="large")

with chart_col:
    st.markdown("<h3 style='color:#003566; margin-bottom:15px;'>Research Publications by Area</h3>", unsafe_allow_html=True)
    
    stats_data = pd.DataFrame({
        "Research Field": ["Nanoencapsulation", "Active Packaging", "Nanoemulsion", "Nanosensors"],
        "Total Published Papers": [540, 320, 260, 180]
    })
    
    st.bar_chart(
        data=stats_data.set_index("Research Field"),
        width="stretch"
    )

with insight_col:
    st.markdown("<h3 style='color:#003566; margin-bottom:15px;'>Premium Research Insights</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card" style="padding: 25px; height: 100%;">
        <div class="ranking-list">
            <div class="ranking-item" style="border-left-color: #F59E0B;">
                <h5>1. Nanoencapsulation Systems</h5>
                <p>Menjadi bidang riset paling masif karena perannya yang sangat vital dalam memproteksi senyawa bioaktif sensitif dan meningkatkan efisiensi translasi klinis di dalam tubuh.</p>
            </div>
            <div class="ranking-item" style="border-left-color: #94A3B8;">
                <h5>2. Active & Smart Packaging</h5>
                <p>Mengalami pertumbuhan tahunan (CAGR) yang pesat, didorong oleh urgensi global terhadap isu sustainability, pengurangan food waste, dan degradasi plastik linear.</p>
            </div>
            <div class="ranking-item" style="border-left-color: #B45309;">
                <h5>3. Nanoemulsion Formulations</h5>
                <p>Adopsinya meningkat tajam pada sektor industri meningkatkan stabilitas senyawa larut lemak dalam sediaan sereal dan minuman fungsional.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 10: FOOD NANOTECHNOLOGY ECOSYSTEM
# =============================================================================
st.markdown('<h1 class="section-title">Food Nanotechnology Ecosystem</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="glass-card">
    <h3>From Natural Sources to Consumer Health</h3>
    <p>
        Ekosistem teknologi pangan fungsional menjembatani ekstraksi senyawa alami murni menuju rekayasa pembawa (carrier) 
        tingkat lanjut, guna menghasilkan produk akhir komersial yang berdampak langsung pada pemulihan kesehatan konsumen.
    </p>
</div>
""", unsafe_allow_html=True)

eco_cols = st.columns(5, gap="small")

with eco_cols[0]:
    st.markdown("""
    <div class="eco-card">
        <div class="eco-icon">🌿</div>
        <div class="eco-title">1. Natural Extract</div>
        <div class="eco-desc-tag">Curcumin</div>
        <div class="eco-desc-tag">Polyphenols</div>
        <div class="eco-desc-tag">Essential Oils</div>
    </div>
    """, unsafe_allow_html=True)

with eco_cols[1]:
    st.markdown("""
    <div class="eco-card">
        <div class="eco-icon">⚛️</div>
        <div class="eco-title">2. Nano Carrier</div>
        <div class="eco-desc-tag">Chitosan Matrix</div>
        <div class="eco-desc-tag">Liposomes</div>
        <div class="eco-desc-tag">Nanoemulsions</div>
    </div>
    """, unsafe_allow_html=True)

with eco_cols[2]:
    st.markdown("""
    <div class="eco-card">
        <div class="eco-icon">🧬</div>
        <div class="eco-title">3. Nanoformulation</div>
        <div class="eco-desc-tag">Encapsulation</div>
        <div class="eco-desc-tag">Stabilization</div>
        <div class="eco-desc-tag">Controlled Release</div>
    </div>
    """, unsafe_allow_html=True)

with eco_cols[3]:
    st.markdown("""
    <div class="eco-card">
        <div class="eco-icon">🥛</div>
        <div class="eco-title">4. Food Product</div>
        <div class="eco-desc-tag">Functional Foods</div>
        <div class="eco-desc-tag">Beverages</div>
        <div class="eco-desc-tag">Smart Packaging</div>
    </div>
    """, unsafe_allow_html=True)

with eco_cols[4]:
    st.markdown("""
    <div class="eco-card">
        <div class="eco-icon">❤️</div>
        <div class="eco-title">5. Consumer Health</div>
        <div class="eco-desc-tag">Precision Nutrition</div>
        <div class="eco-desc-tag">Bioavailability ↑</div>
        <div class="eco-desc-tag">Cellular Wellness</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="eco-pipeline-badge">
    <span class="eco-flow-step">🌿</span>
    <span class="eco-flow-arrow">→</span>
    <span class="eco-flow-step">⚛️</span>
    <span class="eco-flow-arrow">→</span>
    <span class="eco-flow-step">🧬</span>
    <span class="eco-flow-arrow">→</span>
    <span class="eco-flow-step">🥛</span>
    <span class="eco-flow-arrow">→</span>
    <span class="eco-flow-step">❤️</span>
</div>
""", unsafe_allow_html=True)

st.write("")
st.markdown("<h3 style='text-align:center; color:#003566; margin-bottom:15px;'>Deep-Dive Interactive Ecosystem Explorer</h3>", unsafe_allow_html=True)

active_step = st.radio(
    "Pilih langkah ekosistem untuk menganalisis mekanisme transformasinya:",
    ["1. Natural Extract", "2. Nano Carrier", "3. Nanoformulation", "4. Food Product", "5. Consumer Health"],
    horizontal=True
)

if "1. Natural Extract" in active_step:
    st.info("""
    **Mekanisme Tahap 1 (Natural Extract):** Bahan aktif diisolasi dari matriks alaminya (misal: kurkumin dari kunyit atau polifenol dari teh hijau). 
    Tantangan utama pada tahap ini adalah senyawa hasil ekstrak murni biasanya bersifat hidrofobik (tak larut air) dan sangat rentan rusak oleh paparan cahaya, oksigen, serta asam lambung.
    """)
elif "2. Nano Carrier" in active_step:
    st.info("""
    **Mekanisme Tahap 2 (Nano Carrier):** Peneliti memilih material biopolimer pembungkus berskala nano yang bersifat aman bagi tubuh (*Generally Recognized as Safe / GRAS*). 
    Kitosan, liposom, dan lipid emulsi dipilih untuk membentuk cangkang pelindung pelapis molekul aktif target.
    """)
elif "3. Nanoformulation" in active_step:
    st.info("""
    **Mekanisme Tahap 3 (Nanoformulation):** Proses fabrikasi mekanis atau kimia dilakukan (seperti *sonication* atau *homogenization*) untuk mengawinkan ekstrak alami ke dalam nano-carrier. 
    Langkah ini menghasilkan sistem dispersi koloid stabil yang memiliki properti pelepasan terkendali (*controlled-release profile*).
    """)
elif "4. Food Product" in active_step:
    st.info("""
    **Mekanisme Tahap 4 (Food Product):** Formula nanoformulasi cair atau bubuk diinkorporasikan ke dalam produk pangan komersial asli, seperti susu, jus buah fungsional, yogurt, atau dijadikan komponen lapisan *edible coating* kemasan aktif tanpa mengubah rasa asli produk pangan.
    """)
elif "5. Consumer Health" in active_step:
    st.info("""
    **Mekanisme Tahap 5 (Consumer Health):** Ketika dikonsumsi, enkapsulasi nano mencegah pencernaan dini di lambung dan melepas zat aktif langsung di usus halus. 
    Hal ini meningkatkan penyerapan dinding seluler (bioavailabilitas) secara drastis untuk mengoptimalkan kebugaran sistem imun tubuh secara presisi.
    """)

# ==========================================
# 11. FUTURE OF FOOD NANOTECHNOLOGY
# ==========================================
st.markdown('<h1 class="section-title">Future of Food Nanotechnology</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="future-card">
    <div class="future-title">The Next Generation of Food Systems</div>
    <div class="future-desc">
        Food nanotechnology is expected to revolutionize nutrition, food safety, 
        intelligent packaging, and personalized health solutions. Future innovations 
        will integrate artificial intelligence, biosensing technologies, and advanced 
        nanoformulations to create smarter, more resilient food ecosystems.
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="future-stat">
        <div class="future-number">AI</div>
        <div class="future-label">Intelligent Food Analytics</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="future-stat">
        <div class="future-number">IoT</div>
        <div class="future-label">Smart Monitoring Systems</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="future-stat">
        <div class="future-number">Nano</div>
        <div class="future-label">Precision Delivery Tech</div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("AI + Nanotechnology"):
    st.markdown("""
    Artificial Intelligence can optimize nanoformulation design, predict nanoparticle behavior, 
    and significantly accelerate food product development cycles.
    
    * **AI-driven nanoencapsulation:** Precise target optimization.
    * **Predictive food quality analysis:** Machine learning algorithms for safety shelf-life.
    * **Automated formulation:** Self-correcting nano-ingredient mixtures.
    * **Intelligent manufacturing systems:** Real-time nano-scale monitoring.
    """)

with st.expander("Smart Packaging"):
    st.markdown("""
    Future packaging systems will transition from passive barriers to active, communicative guards.
    
    * **Nanosensors:** Detecting volatile compounds emitted by spoiling food.
    * **Freshness & Temperature indicators:** Visual cues for consumers.
    * **Real-time spoilage detection:** Immediate notifications across the global supply chain.
    """)

with st.expander("Personalized Nutrition"):
    st.markdown("""
    Nano-delivery systems will enable precision nutrition strategies tailored perfectly to individual biomicrobiology and health profiles.
    
    * **Personalized vitamin delivery:** Releasing nutrients based on bio-deficiencies.
    * **Targeted nutrient release:** Controlled dissolution inside specific areas of the digestive tract.
    * **Customized functional foods:** Foods that adapt their nutritional profiles to the consumer.
    """)

with st.expander("Sustainable Nanotechnology"):
    st.markdown("""
    Green synthesis methods, biodegradable nanomaterials, and circular-economy packaging solutions 
    are expected to dominate the trajectory of future research.
    
    * **Plant-mediated synthesis:** Eliminating toxic chemicals in nanoparticle manufacturing.
    * **Biopolymer nanocomposites:** Eco-friendly materials that dissolve safely in nature.
    * **Circular food systems:** Utilizing food processing waste into valuable nanostructured resources.
    """)

# ==========================================
# EDUCATIONAL VIDEO CENTER
# ==========================================
st.markdown('<h2 class="section-title" style="margin-top:50px;">Educational Video Center</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <h3>Explore Food Nanotechnology Through Visual Learning</h3>
    <p>Interactive videos help explain complex nanoscale concepts through animations, laboratory demonstrations, and cutting-edge industrial applications.</p>
</div>
""", unsafe_allow_html=True)

v_tabs = st.tabs([
    "Nanoencapsulation",
    "Smart Packaging",
    "Future Technology"
])

with v_tabs[0]:
    st.video("https://www.youtube.com/watch?v=f7hMhL_N4k8")
    st.info("**Learn:** How nanoencapsulation improves stability, target protection, and the overall bioavailability of critical bioactive compounds.")

with v_tabs[1]:
    st.video("https://www.youtube.com/watch?v=k0kpOoe-42g")
    st.info("**Explore:** Active packaging and intelligent food monitoring systems using advanced nanomaterials.")

with v_tabs[2]:
    st.video("https://www.youtube.com/watch?v=KfB2sx9uCkI")
    st.info("**Discover:** Future global trends combining nanotechnology, Artificial Intelligence, and personalized nutrition.")

# ==========================================
# 13. RESEARCH IMPACT DASHBOARD
# ==========================================
st.markdown('<h1 class="section-title">Global Research Impact</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <h3>Food Nanotechnology Growth Worldwide</h3>
    <p>Global research activities, industrial innovations, and patent registrations continue to experience explosive exponential growth over the last decade.</p>
</div>
""", unsafe_allow_html=True)

ic1, ic2, ic3, ic4 = st.columns(4)

with ic1:
    st.markdown("""
    <div class="impact-card">
        <div class="impact-icon">📚</div>
        <div class="impact-number">15,000+</div>
        <div class="impact-title">Research Papers</div>
        <div class="impact-growth">↑ 18% / yr</div>
    </div>
    """, unsafe_allow_html=True)

with ic2:
    st.markdown("""
    <div class="impact-card">
        <div class="impact-icon">💡</div>
        <div class="impact-number">5,000+</div>
        <div class="impact-title">Registered Patents</div>
        <div class="impact-growth">↑ 12% / yr</div>
    </div>
    """, unsafe_allow_html=True)

with ic3:
    st.markdown("""
    <div class="impact-card">
        <div class="impact-icon">🚀</div>
        <div class="impact-number">850+</div>
        <div class="impact-title">Deep-Tech Startups</div>
        <div class="impact-growth">↑ 9% / yr</div>
    </div>
    """, unsafe_allow_html=True)

with ic4:
    st.markdown("""
    <div class="impact-card">
        <div class="impact-icon">🏭</div>
        <div class="impact-number">120+</div>
        <div class="impact-title">Commercialized Products</div>
        <div class="impact-growth">↑ 15% / yr</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.progress(0.82)
st.caption("*Current global market adoption and integration trend of food nanotechnology (Estimated at 82% framework maturity).*")

# ==========================================
# 14. INTERACTIVE QUIZ CENTER
# ==========================================
st.markdown('<h1 class="section-title" style="margin-top: 60px;">Interactive Quiz Center</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="quiz-header-box">
    <div class="quiz-question-title">NanoFood Learning Verification</div>
    <p style="margin: 0; color: #555;">Evaluate your composite understanding of fundamental food nanotechnology concepts. Select an answer for each question below.</p>
</div>
""", unsafe_allow_html=True)

score = 0
questions_answered = 0

# --- QUESTION 1 ---
st.markdown("### **Question 1**")
q1 = st.radio(
    "What is the standard accepted scale range for nanomaterials?",
    ["1 – 100 nm", "1 – 100 μm", "100 – 1,000 nm"],
    index=None,
    key="q1"
)

if q1 is not None:
    questions_answered += 1
    if q1 == "1 – 100 nm":
        st.success("**Correct!** Nanomaterials are strictly defined within the 1 to 100 nanometer spectrum.")
        score += 1
    else:
        st.error("**Incorrect.** 1–100 μm is micro-scale. The true nanoscale is 1–100 nm.")

st.markdown("---")

# --- QUESTION 2 ---
st.markdown("### **Question 2**")
q2 = st.radio(
    "Which primary nanotechnology process is engineered specifically to enhance nutrient bioavailability?",
    ["Nanoencapsulation", "Pasteurization", "Cryogenic Freezing"],
    index=None,
    key="q2"
)

if q2 is not None:
    questions_answered += 1
    if q2 == "Nanoencapsulation":
        st.success("**Correct!** Nanoencapsulation shields and efficiently delivers active bioactive components to targeted bodily systems.")
        score += 1
    else:
        st.error("**Incorrect.** Pasteurization and freezing are conventional thermal preservation processing methods.")

st.markdown("---")

# --- QUESTION 3 ---
st.markdown("### **Question 3**")
q3 = st.radio(
    "Which advanced packaging modification actively interacts with the internal atmosphere to extend food product shelf life?",
    ["Active & Smart Packaging", "Synthetic Food Coloring", "High-Impact Mechanical Grinding"],
    index=None,
    key="q3"
)

if q3 is not None:
    questions_answered += 1
    if q3 == "Active & Smart Packaging":
        st.success("**Correct!** Active packaging incorporates nanosensors and antimicrobial release mechanics to prevent degradation.")
        score += 1
    else:
        st.error("**Incorrect.** Food coloring is cosmetic, and mechanical grinding is a pre-treatment size reduction process.")

# ==========================================
# AUTOMATED REAL-TIME EVALUATION SYSTEM
# ==========================================
if questions_answered > 0:
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Your Performance Summary")
    
    progress_percentage = score / 3
    st.progress(progress_percentage)
    
    if score == 3:
        st.balloons()
        st.success(f"**Perfect Score! ({score}/3)** — Outstanding! You have flawlessly mastered the baseline architecture of Food Nanotechnology.")
    elif score == 2:
        st.info(f"**Good Job! ({score}/3)** — You have a strong grasp of the material, but missed a minor detail.")
    else:
        st.warning(f"**Keep Learning! ({score}/3)** — Some core concepts require review.")
else:
    st.info("*Answer the questions above to automatically unlock your Knowledge Certification score.*")
    
# Closing Quote
st.markdown("""
<div class="quote-container">
    <div class="quote-text">
        "The future of food is not only healthier, safer, and smarter—<br>
        it is engineered at the nanoscale."
    </div>
</div>
""", unsafe_allow_html=True)