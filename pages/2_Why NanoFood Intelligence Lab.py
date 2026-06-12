import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Why NanoFood Intelligence Lab",
    page_icon="🚀",
    layout="wide"
)

# =============================================================================
# HIGH-END PREMIUM CUSTOM CSS & ANIMATIONS
# =============================================================================
st.markdown("""
<style>
/* App Background & Global Reset */
.stAppDeployButton { display: none; } 
[data-testid="stAppViewContainer"] {
    background-color: #F8FAFC;
}

/* HERO SYSTEM */
.hero {
    height: auto;
    min-height: 55vh;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0369A1 100%);
    border-radius: 0 0 35px 35px;
    padding: 60px 20px;
    margin-bottom: 40px;
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08);
}

.hero-content {
    position: relative;
    z-index: 10;
    max-width: 1000px;
    margin: auto;
}

.hero-title {
    font-size: clamp(32px, 4.5vw, 56px);
    font-weight: 800;
    color: white;
    margin-bottom: 15px;
    letter-spacing: -1.5px;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: clamp(16px, 2vw, 22px);
    color: #38BDF8;
    margin-bottom: 25px;
    font-weight: 500;
    letter-spacing: 0.5px;
}

.hero-text {
    font-size: clamp(14px, 1.4vw, 17px);
    color: #94A3B8;
    line-height: 1.8;
    max-width: 850px;
    margin: auto;
}

/* ANIMATED PARTICLES FOR HERO BACKGROUND */
.particle {
    position: absolute;
    border-radius: 50%;
    background: rgba(56, 189, 248, 0.2);
    animation: float 12s infinite linear;
}
.p1 { width: 30px; height: 30px; top: 15%; left: 8%; animation-duration: 14s; }
.p2 { width: 15px; height: 15px; top: 75%; left: 15%; animation-duration: 9s; }
.p3 { width: 22px; height: 22px; top: 45%; left: 85%; animation-duration: 11s; }
.p4 { width: 40px; height: 40px; top: 20%; left: 75%; animation-duration: 16s; }
.p5 { width: 12px; height: 12px; top: 80%; left: 65%; animation-duration: 8s; }

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-25px) rotate(180deg); }
}

/* CORE DESIGN SYSTEM COMPONENTS */
.section-title {
    font-size: 28px;
    font-weight: 800;
    color: #0F172A;
    margin-top: 45px;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}

.section-subtitle {
    font-size: 15px;
    color: #64748B;
    margin-bottom: 30px;
}

.glass-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.02);
    margin-bottom: 25px;
    border: 1px solid #E2E8F0;
}

/* INTERACTIVE LAB CHALLENGE CARDS */
.lab-card {
    background: white;
    padding: 30px 25px;
    border-radius: 20px;
    height: 100%;
    min-height: 240px;
    position: relative;
    overflow: hidden;
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 10px 25px rgba(0,0,0,0.02);
    border: 1px solid #E2E8F0;
    border-top: 4px solid #0284C7;
}

.lab-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 35px rgba(2, 132, 199, 0.08);
    border-top-color: #0EA5E9;
}

.lab-icon { font-size: 36px; margin-bottom: 15px; }
.lab-title { font-size: 19px; font-weight: 700; color: #0F172A; margin-bottom: 10px; }
.lab-desc { font-size: 14px; color: #475569; line-height: 1.6; }

/* CRISIS AND EFFECT INTERFACES */
.crisis-box {
    background: #FEF2F2;
    padding: 30px;
    border-left: 6px solid #EF4444;
    border-radius: 16px;
    height: 100%;
}
.crisis-box h4 { color: #991B1B; font-weight: 700; font-size: 18px; margin-top:0; }
.crisis-box li { color: #7F1D1D; font-size: 14.5px; margin-bottom: 8px; }

.effect-box {
    background: #EFF6FF;
    padding: 30px;
    border-left: 6px solid #3B82F6;
    border-radius: 16px;
    height: 100%;
}
.effect-box h4 { color: #1E40AF; font-weight: 700; font-size: 18px; margin-top:0; }
.effect-box li { color: #1E3A8A; font-size: 14.5px; margin-bottom: 8px; }

/* PIPELINE VISUALIZATION */
.pipeline-container {
    background: white;
    padding: 35px;
    border-radius: 24px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.02);
    border: 1px solid #E2E8F0;
}
.pipe-step {
    background: #F8FAFC;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #E2E8F0;
    transition: all 0.3s ease;
}
.pipe-step:hover {
    background: #F0F9FF;
    border-color: #0EA5E9;
}
.pipe-badge {
    background: #E0F2FE;
    color: #0369A1;
    font-size: 12px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    display: inline-block;
    margin-bottom: 8px;
}
.pipe-title { font-weight: 700; color: #0F172A; font-size: 15px; margin-bottom: 4px; }
.pipe-desc { font-size: 12px; color: #64748B; }

/* COGNITIVE MATRIX (BEFORE VS AFTER) */
.comp-card-before {
    background: #FFF5F5;
    padding: 25px;
    border-radius: 16px;
    border-left: 5px solid #EF4444;
    height: 100%;
}
.comp-card-after {
    background: #F0FDF4;
    padding: 25px;
    border-radius: 16px;
    border-left: 5px solid #10B981;
    height: 100%;
}
.comp-header { font-size: 16px; font-weight: 700; margin-bottom: 12px; }
.comp-card-before .comp-header { color: #991B1B; }
.comp-card-after .comp-header { color: #065F46; }
.comp-item { font-size: 14px; margin-bottom: 8px; color: #334155; display: flex; align-items: center; gap: 8px; }

/* SCIENTIFIC FOUNDATION CHIPS */
.chip-container { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 15px; }
.sc-chip {
    background: #F1F5F9;
    color: #334155;
    padding: 8px 16px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #E2E8F0;
    transition: all 0.3s ease;
}
.sc-chip:hover {
    background: #0F172A;
    color: white;
    border-color: #0F172A;
}

/* GRAPHIC & QUOTE BANNER */
.premium-quote {
    background: linear-gradient(135deg, #0F172A 0%, #0284C7 100%);
    padding: 40px;
    border-radius: 24px;
    color: white;
    text-align: center;
    margin-top: 40px;
    margin-bottom: 25px;
    box-shadow: 0 15px 30px rgba(2, 132, 199, 0.15);
}
.quote-text { font-size: 22px; font-style: italic; font-weight: 600; line-height: 1.6; }
.quote-author { font-size: 14px; opacity: 0.8; margin-top: 12px; letter-spacing: 1px; text-transform: uppercase; }

/* KNOWLEDGE CORNER BOX */
.quiz-box {
    background: white;
    padding: 30px;
    border-radius: 20px;
    border-right: 1px solid #E2E8F0; border-top: 1px solid #E2E8F0; border-bottom: 1px solid #E2E8F0;
    border-left: 5px solid #0F172A;
    box-shadow: 0 5px 20px rgba(0,0,0,0.02);
}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# HERO SECTION WITH ANIMATED BACKDROP
# =============================================================================
st.markdown("""
<div class="hero">
    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="particle p5"></div>
    <div class="hero-content">
        <h1 class="hero-title">🚀 Why NanoFood Intelligence Lab Was Developed</h1>
        <h3 class="hero-subtitle">Bridging Food Nanotechnology Research, Laboratory Calculations, and Scientific Education</h3>
        <p class="hero-text">
            Sistem lab konvensional menghadapi tantangan fragmentasi data, risiko human-error tinggi, 
            dan kurva pembelajaran kalkulasi yang kompleks. Platform terintegrasi ini dirancang sebagai infrastruktur 
            komputasi ilmiah cerdas untuk memvalidasi dan mempercepat riset rekayasa pangan skala nano.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# SECTION 1: BACKGROUND & CRISIS ANALYSIS
# =============================================================================
st.markdown('<h2 class="section-title">Background and Urgency</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Analisis Kritis Tantangan Operasional dan Dampak Sistemik Terhadap Keberlanjutan Riset</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown("""
    <div class="crisis-box">
        <h4>⚠ Current Challenges (Tantangan Lapangan)</h4>
        <ul>
            <li><b>Kalkulasi Manual Tradisional:</b> Pemrosesan rumus pengenceran dan efisiensi enkapsulasi menggunakan kalkulator fisik berisiko keliru.</li>
            <li><b>Fragmentasi Perangkat Lunak:</b> Peneliti dipaksa beralih di antara berbagai aplikasi *spreadsheet* yang tidak sinkron.</li>
            <li><b>Data Terisolasi:</b> Dokumentasi hasil karakterisasi ukuran partikel tidak tersimpan secara terpusat.</li>
            <li><b>In-efisiensi Waktu:</b> Alur kerja analisis kurva standar menyerap porsi waktu riset yang sangat masif.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="effect-box">
        <h4>📉 Impact on Research (Dampak Sistemik)</h4>
        <ul>
            <li><b>Penurunan Efisiensi:</b> Kecepatan publikasi melambat akibat birokrasi pengolahan data mentah yang manual.</li>
            <li><b>Inkonsistensi Data:</b> Variabilitas hasil tinggi akibat perbedaan pembulatan desimal antar software pengolah.</li>
            <li><b>Kurva Belajar Curam:</b> Mahasiswa dan peneliti muda membutuhkan waktu lama untuk menguasai interpretasi instrumen kimia murni.</li>
            <li><b>Pemborosan Bahan Kimia:</b> Pengulangan eksperimen (trial-and-error) akibat kesalahan hitung stock solution awal.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 2: INTERACTIVE LABORATORY ARCHITECTURE CARDS
# =============================================================================
st.markdown('<h2 class="section-title">The 6 Core Laboratory Pillars</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Pilar Rekayasa Komputasi Lab yang Ditransformasikan Oleh NanoFood Intelligence Lab</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("""
    <div class="lab-card">
        <div class="lab-icon">🧪</div>
        <div class="lab-title">Dilution Calculations</div>
        <div class="lab-desc">Otomatisasi formulasi larutan stok, penyesuaian molaritas presisi, dan kalkulasi pengenceran bertingkat untuk akurasi media nanoemulsi.</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="lab-card">
        <div class="lab-icon">🔬</div>
        <div class="lab-title">Nanoparticle Characterization</div>
        <div class="lab-desc">Pemetaan data ukuran partikel (DLS), stabilitas muatan zeta potential, serta simplifikasi pembacaan spektra XRD & FTIR secara matematis.</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="lab-card">
        <div class="lab-icon">📦</div>
        <div class="lab-title">Packaging Analysis</div>
        <div class="lab-desc">Perhitungan matematis Water Vapor Transmission Rate (WVTR), swelling index, dan laju biodegradasi polimer komposit *active packaging*.</div>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Spacer

c4, c5, c6 = st.columns(3)
with c4:
    st.markdown("""
    <div class="lab-card">
        <div class="lab-icon">🌱</div>
        <div class="lab-title">IC50 Antioxidant Analysis</div>
        <div class="lab-desc">Penentuan kapasitas inhibisi radikal bebas (DPPH/ABTS) senyawa aktif melalui regresi linear otomatis demi akurasi efikasi antioksidan.</div>
    </div>
    """, unsafe_allow_html=True)
with c5:
    st.markdown("""
    <div class="lab-card">
        <div class="lab-icon">📊</div>
        <div class="lab-title">Standard Curve Analysis</div>
        <div class="lab-desc">Generasi koefisien determinasi ($R^2$) kurva kalibrasi instrumen spektrofotometri untuk kuantifikasi analit bioaktif tanpa deviasi bias.</div>
    </div>
    """, unsafe_allow_html=True)
with c6:
    st.markdown("""
    <div class="lab-card">
        <div class="lab-icon">🧬</div>
        <div class="lab-title">Encapsulation Efficiency</div>
        <div class="lab-desc">Evaluasi kuantitatif persentase inti zat aktif (core) yang berhasil terperangkap sempurna di dalam dinding nanokarier lipid atau kitosan.</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 3: WORKFLOW PIPELINE INTERACTIVE EXPLORER
# =============================================================================
st.markdown('<h2 class="section-title">Why Existing Methods Are Limited</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Studi Bottleneck Alur Kerja Tradisional — Klik Langkah Untuk Solusi Interaktif</p>', unsafe_allow_html=True)

# Pipeline Layout
p_col1, p_col2, p_col3, p_col4, p_col5 = st.columns(5)

with p_col1:
    st.markdown('<div class="pipe-step"><span class="pipe-badge">Langkah 1</span><div class="pipe-title">Manual Calculator</div><div class="pipe-desc">Akurasi rendah & rawan typo</div></div>', unsafe_allow_html=True)
with p_col2:
    st.markdown('<div class="pipe-step"><span class="pipe-badge">Langkah 2</span><div class="pipe-title">Spreadsheet Pro</div><div class="pipe-desc">Rumus rumit & tidak tervalidasi</div></div>', unsafe_allow_html=True)
with p_col3:
    st.markdown('<div class="pipe-step"><span class="pipe-badge">Langkah 3</span><div class="pipe-title">Data Transfer</div><div class="pipe-desc">Risiko data korup & hilang</div></div>', unsafe_allow_html=True)
with p_col4:
    st.markdown('<div class="pipe-step"><span class="pipe-badge">Langkah 4</span><div class="pipe-title">Interpretation</div><div class="pipe-desc">Analisis subyektif non-standar</div></div>', unsafe_allow_html=True)
with p_col5:
    st.markdown('<div class="pipe-step"><span class="pipe-badge">Hasil Akhir</span><div class="pipe-title">Potential Error</div><div class="pipe-desc">Kegagalan replikasi riset</div></div>', unsafe_allow_html=True)

st.write("")
# Interactive Deep Dive via Selection Box
selected_step = st.selectbox(
    "Analisis Penyebab Bottleneck Tradisional & Intervensi Sistem NanoFoodLab:",
    ["Manual Calculator & Spreadsheet Processing", "Data Transfer Disruption", "Subjective Result Interpretation"]
)

if "Manual Calculator" in selected_step:
    st.error("🚨 **Masalah Tradisional:** Memasukkan data absorbansi secara manual ke spreadsheet rentan terhadap pergeseran baris data. Kesalahan input satu sel merusak seluruh kurva regresi.")
    st.success("⚡ **Solusi NanoFoodLab:** Validasi formula otomatis secara *built-in*. Pengguna cukup memasukkan parameter dasar, sistem mengunci algoritma matematika sesuai standar IUPAC.")
elif "Data Transfer" in selected_step:
    st.error("🚨 **Masalah Tradisional:** Pemindahan file biner instrumen karakterisasi melintasi komputer laboratorium yang berbeda memicu risiko korupsi metadata ekosistem.")
    st.success("⚡ **Solusi NanoFoodLab:** Platform berbasis awan terpadu (*Single Integrated Platform*) menghilangkan kebutuhan transfer berkas antar-aplikasi.")
else:
    st.error("🚨 **Masalah Tradisional:** Membaca tren degradasi biodegradasi kemasan tanpa landasan statistik baku melahirkan kesimpulan ilmiah yang bias antar peneliti.")
    st.success("⚡ **Solusi NanoFoodLab:** Dilengkapi *built-in scientific explanations* yang merujuk langsung ke standar ISO dan jurnal global terakreditasi.")

# =============================================================================
# SECTION 4: COGNITIVE MATRIX (BEFORE VS AFTER PARADIGM SHIFT)
# =============================================================================
st.markdown('<h2 class="section-title">The Paradigm Shift: NanoFoodLab Solution</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Komparasi Struktural Sebelum vs Sesudah Implementasi Platform</p>', unsafe_allow_html=True)

b_left, b_right = st.columns(2, gap="large")

with b_left:
    st.markdown("""
    <div class="comp-card-before">
        <div class="comp-header">❌ Konvensional (Tanpa NanoFoodLab)</div>
        <div class="comp-item">🔴 Penghitungan piringan cawan dan nilai IC50 memakan waktu berjam-jam secara manual.</div>
        <div class="comp-item">🔴 Inkonsistensi kompilasi rumus antar komputer peneliti laboratorium.</div>
        <div class="comp-item">🔴 Kebingungan interpretasi mahasiswa terhadap output data instrumen mentah.</div>
        <div class="comp-item">🔴 Resiko kegagalan replikasi formula pangan fungsional akibat bias pembulatan angka.</div>
    </div>
    """, unsafe_allow_html=True)

with b_right:
    st.markdown("""
    <div class="comp-card-after">
        <div class="comp-header">✓ Modern (Dengan NanoFoodLab)</div>
        <div class="comp-item">🟢 Otomatisasi kalkulasi tuntas dalam hitungan detik dengan komputasi latar belakang.</div>
        <div class="comp-item">🟢 Integrasi satu pintu (Single Unified Platform) menjamin standardisasi data.</div>
        <div class="comp-item">🟢 Modul penjelasan teoretis memandu interpretasi ilmiah secara otomatis.</div>
        <div class="comp-item">🟢 Replikabilitas riset tinggi berkat validasi formula matematis absolut.</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 5: INTERACTIVE SIMULATION & SCIENTIFIC DATA FOUNDATION
# =============================================================================
st.markdown('<h2 class="section-title">Scientific Foundation & Impact Matrix</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Landasan Regulasi Internasional dan Visualisasi Distribusi Publikasi Riset Lab</p>', unsafe_allow_html=True)

sf_left, sf_right = st.columns([4, 3], gap="large")

with sf_left:
    st.markdown("""
    <div class="glass-card" style="height:100%;">
        <h4 style="color:#0F172A; margin-top:0;">Standardization Matrix</h4>
        <p style="font-size:14px; color:#475569;">NanoFood Intelligence Lab tidak dibangun di atas asumsi alur kerja acak. Arsitektur algoritma platform kami patuh sepenuhnya pada konvensi internasional dan jurnal rujukan berdampak tinggi (*High-Impact Journals*):</p>
        <div class="chip-container">
            <span class="sc-chip">ASTM Standards</span>
            <span class="sc-chip">ISO Standards</span>
            <span class="sc-chip">IUPAC Recommendations</span>
            <span class="sc-chip">AOAC Methods</span>
            <span class="sc-chip">Food Hydrocolloids</span>
            <span class="sc-chip">Carbohydrate Polymers</span>
            <span class="sc-chip">Journal of Food Engineering</span>
            <span class="sc-chip">Trends in Food Science & Tech</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with sf_right:
    # Embedded Dynamic Streamlit Chart tracking publication burden simulation
    chart_data = pd.DataFrame({
        "Lab Modules": ["Dilution", "Nano-Characterization", "Packaging", "IC50 Analysis", "Std Curve", "Encapsulation"],
        "Calculations Load (%)": [15, 25, 20, 12, 10, 18]
    })
    st.markdown("<p style='font-size:14px; font-weight:700; color:#0F172A; margin-bottom:5px;'>Lab Computational Burden Profile</p>", unsafe_allow_html=True)
    st.bar_chart(data=chart_data.set_index("Lab Modules"), use_container_width=True)

# =============================================================================
# SECTION 6: RESEARCH IMPACT METRICS
# =============================================================================
st.write("")
st.markdown("<p style='text-align:center; font-weight:700; color:#0F172A; margin-bottom:10px;'>Simulated Research Impact Vector</p>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("🎓 Impact on Education", "Sangat Meningkat", "94% Pemahaman")
m2.metric("🔬 Impact on Research", "Siklus Lebih Cepat", "-40% Time-Loss")
m3.metric("🧪 Lab Activities", "Bebas Error Manual", "100% Akurasi")
m4.metric("📊 Data Interpretation", "Terstandardisasi", "ISO Compliant")

# =============================================================================
# KNOWLEDGE CORNER: EDUCATIONAL INTERACTIVE QUIZ
# =============================================================================
st.markdown('<h2 class="section-title">Knowledge Corner</h2>', unsafe_allow_html=True)
st.markdown('<p class="section-subtitle">Evaluasi Mengapa Pendekatan Berbasis Platform Diperlukan Dalam Ekosistem Riset Modern</p>', unsafe_allow_html=True)

st.markdown("""
<div class="quiz-box">
    <h4 style="color:#0F172A; margin-top:0; margin-bottom:5px;">Quick Verification Quiz</h4>
    <p style="color:#64748B; font-size:14px; margin-bottom:20px;">Mengapa metode pemrosesan kurva standar menggunakan kalkulator konvensional dipandang memiliki keterbatasan besar?</p>
</div>
""", unsafe_allow_html=True)

quiz_answer = st.radio(
    "Pilih kesimpulan arsitektur yang paling tepat:",
    [
        "Kalkulator konvensional tidak memiliki sistem validasi silang (cross-validation) otomatis sehingga memicu perambatan galat (error propagation).",
        "Kalkulator fisik membutuhkan daya baterai yang terlalu boros untuk menghitung regresi linear.",
        "Metode konvensional sengaja dilarang oleh standar ISO internasional."
    ],
    index=None,
    key="why_quiz"
)

if quiz_answer is not None:
    if "validasi silang" in quiz_answer:
        st.balloons()
        st.success("🎉 **Jawaban Tepat!** Ketiadaan sistem penguncian rumus otomatis pada kalkulator konvensional memicu perambatan galat deskriptif yang berisiko menggagalkan replikasi produk.")
    else:
        st.error("❌ **Kurang Tepat.** Alasan utamanya bukan masalah teknis baterai atau larangan ISO secara mentah, melainkan tingginya akumulasi galat (human error propagation) pada entri manual.")

# =============================================================================
# PREMIUM CLOSING QUOTE & MISSION MANIFESTO
# =============================================================================
st.markdown("""
<div class="premium-quote">
    <div class="quote-text">
        "Transforming complex food nanotechnology calculations into accessible, 
        accurate, and scientifically validated tools."
    </div>
    <div class="quote-author">The NanoFood Intelligence Lab Core Manifesto</div>
</div>
""", unsafe_allow_html=True)

st.info("""
**Sinergi Ekosistem:** Platform ini dikembangkan secara inklusif untuk menyokong pilar edukasi teknologi pangan fungsional, 
aktivitas laboratorium madya, riset ilmiah mutakhir, dan akurasi interpretasi data melalui lingkungan komputasi terintegrasi, 
*user-friendly*, dan tervalidasi secara ilmiah.
""")

