import streamlit as st

# =============================================================================
# SET PAGE CONFIG (Wajib berada di baris pertama sebelum render UI)
# =============================================================================
st.set_page_config(
    page_title="NanoFood Intelligence Lab",
    page_icon="🔬",
    layout="wide"
)

# =============================================================================
# CLEANED & SCOPED CUSTOM CSS (Gong & Premium UI Framework)
# =============================================================================
st.markdown("""
<style>
/* Sembunyikan Tombol Deploy Default Streamlit */
.stAppDeployButton { display: none; } 

/* Pengaturan Background Global */
[data-testid="stAppViewContainer"] {
    background-color: #F8FAFC;
}

/* HERO SECTION FUTURISTIK */
.hero {
    height: auto;
    min-height: 55vh;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 40%, #0891B2 100%);
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
    background: radial-gradient(circle at center, rgba(6, 182, 212, 0.15), transparent 70%);
}

.hero-content {
    position: relative;
    z-index: 10;
    max-width: 1000px;
    margin: auto;
}

.hero-title {
    font-size: clamp(36px, 5vw, 60px);
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
    letter-spacing: -1px;
}

.hero-subtitle {
    font-size: clamp(18px, 2.5vw, 24px);
    color: #38BDF8;
    margin-bottom: 25px;
    font-weight: 500;
}

.hero-text {
    font-size: clamp(15px, 1.6vw, 18px);
    color: #E2E8F0;
    line-height: 1.8;
    max-width: 850px;
    margin: auto;
    opacity: 0.95;
}

/* ANIMATED BACKGROUND PARTICLES */
.particle {
    position: absolute;
    border-radius: 50%;
    background: rgba(56, 189, 248, 0.2);
    animation: float 12s infinite linear;
}
.p1 { width: 20px; height: 20px; top: 15%; left: 8%; animation-delay: 0s; }
.p2 { width: 12px; height: 12px; top: 65%; left: 15%; animation-delay: 2s; }
.p3 { width: 16px; height: 16px; top: 45%; left: 85%; animation-delay: 1s; }
.p4 { width: 28px; height: 28px; top: 20%; left: 75%; animation-delay: 3s; }

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-25px) rotate(180deg); }
}

/* TITLES & SUBHEADERS */
.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #1E293B;
    margin-top: 45px;
    margin-bottom: 25px;
    letter-spacing: -0.5px;
    border-left: 6px solid #0891B2;
    padding-left: 15px;
}

/* GLASSMORPHISM CARDS */
.glass-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.02);
    border: 1px solid rgba(226, 232, 240, 0.8);
    height: 100%;
}

.feature-title-box {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 15px;
}
.feature-title-box h3 {
    margin: 0 !important;
    color: #1E293B;
    font-size: 22px;
    font-weight: 700;
}

/* WORKFLOW CONTAINER */
.workflow-container {
    background: #0F172A;
    padding: 35px 20px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
}
.workflow-flex {
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    gap: 15px;
}
.workflow-step {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 15px 22px;
    border-radius: 12px;
    color: #F1F5F9;
    font-weight: 600;
    font-size: 14px;
    text-align: center;
    min-width: 140px;
    transition: all 0.3s ease;
}
.workflow-step:hover {
    background: #0891B2;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(6, 182, 212, 0.25);
}
.workflow-arrow {
    color: #38BDF8;
    font-weight: 900;
    font-size: 20px;
}

/* INTERACTIVE INTERFACE INTERIOR CARDS (HOVER OVERLAYS) */
.tool-card {
    background: white;
    padding: 30px 25px;
    border-radius: 20px;
    height: 340px;
    position: relative;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    box-shadow: 0 5px 20px rgba(0,0,0,0.03);
    border: 1px solid #E2E8F0;
}
.tool-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(15, 23, 42, 0.08);
}
.tool-icon { font-size: 45px; margin-bottom: 12px; }
.tool-name { font-size: 22px; font-weight: 700; color: #1E293B; margin-bottom: 8px; }
.tool-brief { color: #64748B; font-size: 14px; line-height: 1.6; }

.tool-overlay {
    position: absolute;
    bottom: -100%; left: 0;
    width: 100%; height: 100%;
    padding: 30px 25px;
    background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
    color: white;
    transition: bottom 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.tool-card:hover .tool-overlay { bottom: 0; }
.tool-overlay h4 { color: #38BDF8 !important; font-size: 18px; font-weight: 700; margin-bottom: 10px; }
.tool-overlay ul { padding-left: 20px; font-size: 13.5px; color: #E2E8F0; line-height: 1.8; }

/* QUICK ACCESSIBLE LINKS BUTTON BAR */
.quick-access-box {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.01);
    text-align: center;
    height: 100%;
}
.quick-access-icon { font-size: 32px; margin-bottom: 5px; }
.quick-access-title { font-size: 16px; font-weight: 700; color: #1E293B; margin-bottom: 15px; }

/* REASONING CARDS */
.why-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border-bottom: 4px solid #0891B2;
    box-shadow: 0 6px 18px rgba(0,0,0,0.02);
    height: 100%;
    transition: transform 0.2s;
}
.why-card:hover { transform: translateY(-3px); }
.why-icon { font-size: 36px; margin-bottom: 8px; }
.why-title { font-size: 18px; font-weight: 700; color: #1E293B; margin-bottom: 6px; }
.why-desc { font-size: 14px; color: #64748B; line-height: 1.6; }

/* ECOSYSTEM SYSTEM CLOSING FOOTER */
.footer-container {
    background: #0F172A;
    color: #94A3B8;
    padding: 50px 20px;
    border-radius: 20px 20px 0 0;
    margin-top: 60px;
    text-align: center;
    border-top: 2px solid #1E293B;
}
.footer-logo { font-size: 26px; font-weight: 800; color: white; margin-bottom: 8px; }
.footer-tagline { font-size: 14px; color: #38BDF8; margin-bottom: 25px; font-weight: 500; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HERO SECTION (Gong Pembuka Animasi)
# =============================================================================
st.markdown("""
<div class="hero">
    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="hero-content">
        <h1 class="hero-title">🔬 NANOFOOD INTELLIGENCE LAB</h1>
        <h3 class="hero-subtitle">Interactive Platform for Advanced Food Nanotechnology</h3>
        <p class="hero-text">
            Mengintegrasikan kalkulator laboratorium presisi tinggi, modul karakterisasi material mutakhir, 
            analisis pengemasan fungsional, dan kecerdasan artifisial penanganan masalah laborat dalam satu platform ekosistem digital terpadu.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.info("💡 **Pengumuman Sistem:** Selamat datang! Platform ini dirancang khusus untuk mengakomodasi akselerasi Riset Eksperimental, Edukasi Berbasis Data, dan Aplikasi Laboratorium di bidang Teknologi Pangan.")

# =============================================================================
# PLATFORM CORE METRICS
# =============================================================================
st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric("Advanced Calculators", "20+", help="Kalkulasi Molaritas, Dilusi, IC50/EC50, Efisiensi Enkapsulasi, dll.")
with m2: st.metric("Learning Modules", "30+", help="Edukasi Teori Komposit, Karakteristik Interaksi Nano, & Jurnal Rujukan.")
with m3: st.metric("Characterization Tools", "10+", help="Analisis Puncak Spektra FTIR, XRD Crystalline, Polimer Barrier.")
with m4: st.metric("Research Ecosystems", "8 Areas", help="Cakupan Bidang Riset dari Pertanian Presisi Hingga Kesehatan Seluler.")

# =============================================================================
# SECTION 1: PLATFORM FEATURES OVERVIEW
# =============================================================================
st.markdown('<h2 class="section-title">Platform Features Overview</h2>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("""
    <div class="glass-card">
        <div class="feature-title-box">
            <span>🧪</span>
            <h3>Laboratory Calculator</h3>
        </div>
        <p style="color: #475569; font-size: 15px; line-height: 1.7; margin: 0;">
            Menyediakan otomatisasi perhitungan algoritma laboratorium yang kompleks seperti kalkulasi pengenceran bertingkat, 
            molaritas reagen aktif, rendemen sintesis, efisiensi enkapsulasi zat hidrofobik, serta analisis titik inhibisi IC50/EC50.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="glass-card">
        <div class="feature-title-box">
            <span>🔬</span>
            <h3>Characterization Tools</h3>
        </div>
        <p style="color: #475569; font-size: 15px; line-height: 1.7; margin: 0;">
            Memfasilitasi interpretasi data instrumen secara cerdas tanpa perlu berpindah-pindah software eksternal. Membantu identifikasi gugus fungsi kimia mikroba dan pengukuran parameter kristalinitas sampel rekayasa secara instan.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="glass-card">
        <div class="feature-title-box">
            <span>✅</span>
            <h3>Packaging Analysis</h3>
        </div>
        <p style="color: #475569; font-size: 15px; line-height: 1.7; margin: 0;">
            Modul pengujian matrik biopolimer untuk menganalisis performa <i>Active Packaging</i>, mencakup kalkulasi Water Vapor Transmission Rate (WVTR), Moisture Content, Water Solubility, Swelling Index, hingga biodegradasi alami polimer.
        </p>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 2: NANOTECHNOLOGY RESEARCH WORKFLOW
# =============================================================================
st.markdown('<h2 class="section-title">Food Nanotechnology Research Workflow</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="workflow-container">
    <div class="workflow-flex">
        <div class="workflow-step">📚 Literature Review</div>
        <div class="workflow-arrow">→</div>
        <div class="workflow-step">🧪 Material Selection</div>
        <div class="workflow-arrow">→</div>
        <div class="workflow-step">⚗️ Synthesis Phase</div>
        <div class="workflow-arrow">→</div>
        <div class="workflow-step">📈 Characterization</div>
        <div class="workflow-arrow">→</div>
        <div class="workflow-step">🧬 Bioactivity Analysis</div>
        <div class="workflow-arrow">→</div>
        <div class="workflow-step">📦 Packaging Evaluation</div>
        <div class="workflow-arrow">→</div>
        <div class="workflow-step">📝 Scientific Paper</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# SECTION 3: FEATURED LABORATORY INTERACTIVE TOOLS (HOVER METRIC OVERLAY)
# =============================================================================
st.markdown('<h2 class="section-title">Featured Laboratory Interactive Tools</h2>', unsafe_allow_html=True)
st.caption("*Arahkan kursor (hover) pada kartu laboratorium di bawah untuk melihat rincian kapabilitas analisis alat instrumen.*")
st.write("")

f1, f2, f3 = st.columns(3, gap="medium")

with f1:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-icon">🔬</div>
        <div class="tool-name">FTIR Analyzer</div>
        <div class="tool-brief">Identifikasi struktur kimia sampel, perubahan gugus fungsi organik, serta deteksi ikatan hidrogen baru pasca modifikasi nanoencapsulation.</div>
        <div class="tool-overlay">
            <h4>🎯 Capabililties & Peaks</h4>
            <ul>
                <li>• O-H Stretching (Alcohol/Phenols)</li>
                <li>• N-H Stretching (Chitosan Matrix)</li>
                <li>• C=O Carbonyl (Aldehydes/Esters)</li>
                <li>• C-O Stretching Functional Groups</li>
                <li>• Aromatic Rings & Fingerprint Regions</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/FTIR Analyzer.py", label="Buka Modul FTIR Analyzer", icon="🔥")

with f2:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-icon">🧮</div>
        <div class="tool-name">XRD Crystallinity Tech</div>
        <div class="tool-brief">Analisis fasa susunan atom matriks material kristalin, semi-kristalin, maupun amorf menggunakan data intensitas sudut difraksi sinar-X.</div>
        <div class="tool-overlay">
            <h4>📐 Mathematical Engines</h4>
            <ul>
                <li>• Scherrer Equation (Crystallite Size)</li>
                <li>• Crystallinity Index Calculation</li>
                <li>• Lattice Parameter d-spacing Evaluation</li>
                <li>• Bragg's Law Automated Multi-Peaks</li>
                <li>• Phase Interpretation & Dispersity Index</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/Laboratory Calculator.py", label="Buka XRD Tools Matrix", icon="⚡")

with f3:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-icon">🧪</div>
        <div class="tool-name">IC50 Bio-Calculator</div>
        <div class="tool-brief">Evaluasi efektivitas penangkapan radikal bebas (antioaksidan) senyawa aktif atau penekanan laju pertumbuhan mikroba patogen.</div>
        <div class="tool-overlay">
            <h4>📈 Analytical Models</h4>
            <ul>
                <li>• Linear Regression Line Modeling</li>
                <li>• Precision IC50/EC50 Value Estimation</li>
                <li>• Dose-Response Scatter Curve Rendering</li>
                <li>• In-situ Automated Data Cleansing</li>
                <li>• Biological Activity Curve Interpretation</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/Laboratory Calculator.py", label="Buka IC50 Tools Engine", icon="🚀")

# =============================================================================
# SECTION 4: WHY CHOOSE NANOFOOD INTELLIGENCE LAB
# =============================================================================
st.markdown('<h2 class="section-title">Why Choose NanoFood Intelligence Lab?</h2>', unsafe_allow_html=True)
w1, w2, w3, w4 = st.columns(4)

with w1:
    st.markdown("""
    <div class="why-card">
        <div class="why-icon">🔬</div>
        <div class="why-title">Research-Oriented</div>
        <div class="why-desc">Arsitektur data disesuaikan khusus dengan kebutuhan riset nanoteknologi pangan modern dan kimia polimer.</div>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown("""
    <div class="why-card">
        <div class="why-icon">💡</div>
        <div class="why-title">User Friendly UI</div>
        <div class="why-desc">Tampilan antarmuka yang bersih, intuitif, dan responsif untuk mahasiswa, dosen, serta laboran profesional.</div>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown("""
    <div class="why-card">
        <div class="why-icon">⚗️</div>
        <div class="why-title">Laboratory Ready</div>
        <div class="why-desc">Formula komputasi matematis tervalidasi yang siap digunakan untuk mempercepat pengerjaan skripsi/tesis.</div>
    </div>
    """, unsafe_allow_html=True)

with w4:
    st.markdown("""
    <div class="why-card">
        <div class="why-icon">📚</div>
        <div class="why-title">Educational Node</div>
        <div class="why-desc">Menggabungkan jembatan teori fundamental nano dengan implementasi analisis data laboratorium nyata.</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 5: QUICK ACCESS TO ALL PAGES (CLEAN & ERROR FREE LINK BAR)
# =============================================================================
st.markdown('<h2 class="section-title">Ecosystem Hub Quick Access</h2>', unsafe_allow_html=True)

qa1, qa2, qa3, qa4, qa5, qa6 = st.columns(6)

with qa1:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🔬</div><div class="quick-access-title">FTIR Inst</div></div>', unsafe_allow_html=True)
    st.page_link("pages/FTIR Analyzer.py", label="Open FTIR")

with qa2:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🧮</div><div class="quick-access-title">Lab Calc</div></div>', unsafe_allow_html=True)
    st.page_link("pages/Laboratory Calculator.py", label="Open Calc")

with qa3:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">📡</div><div class="quick-access-title">Database</div></div>', unsafe_allow_html=True)
    st.page_link("pages/NexusNano Hub.py", label="Open Nexus")

with qa4:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🛠️</div><div class="quick-access-title">Trouble</div></div>', unsafe_allow_html=True)
    st.page_link("pages/Laboratory Troubleshooting.py", label="Open Solve")

with qa5:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">📖</div><div class="quick-access-title">About Info</div></div>', unsafe_allow_html=True)
    st.page_link("pages/About Nanotechnology.py", label="Open About")

with qa6:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🎨</div><div class="quick-access-title">Visual</div></div>', unsafe_allow_html=True)
    st.page_link("pages/visualization.py", label="Open Model")

# =============================================================================
# PLATFORM SYSTEM CLOSING FOOTER
# =============================================================================
st.markdown("""
<div class="footer-container">
    <div class="footer-logo">🔬 NanoFood Intelligence Lab</div>
    <div class="footer-tagline">Food Nanotechnology • Material Characterization • Packaging Science • Intelligent Bioactivity</div>
    <p style="font-size: 13px; max-width:600px; margin:auto; opacity: 0.7; line-height: 1.6;">
        Sistem terintegrasi untuk optimasi pengolahan data nanostruktur pangan fungsional global. Dikembangkan untuk mendukung efisiensi pengerjaan alur riset laboratorium secara akurat dan presisi.
    </p>
    <br>
    <p style="font-size: 12px; margin-top:20px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
        © 2026 NanoFood Intelligence Lab | Version 1.0.0 Stable Deployment Framework
    </p>
</div>
""", unsafe_allow_html=True)

