import streamlit as st
import pandas as pd
import numpy as np

# Set Konfigurasi Halaman Premium
st.set_page_config(
    page_title="AuraNano.AI | Premium Laboratory Decision Support System",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================================================
# ENTERPRISE GLASSMORPHISM & SCI-TECH CUSTOM CSS
# =============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* Reset Global Font */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* App Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #0B0F19 0%, #111827 100%);
    color: #E2E8F0;
}

/* Hide Streamlit Elements */
.stAppDeployButton { display: none; }
footer {visibility: hidden;}

/* HERO PREMIUM GLOW PANEL */
.premium-hero {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.8) 0%, rgba(30, 58, 138, 0.4) 100%);
    border: 1px solid rgba(59, 130, 246, 0.2);
    backdrop-filter: blur(12px);
    border-radius: 24px;
    padding: 60px 40px;
    text-align: center;
    margin-bottom: 35px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3), inset 0 1px 1px rgba(255,255,255,0.1);
}

.premium-hero::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(56, 189, 248, 0.08) 0%, transparent 60%);
    pointer-events: none;
}

.premium-hero h1 {
    font-size: clamp(30px, 4.5vw, 52px) !important;
    font-weight: 800 !important;
    background: linear-gradient(135deg, #FFFFFF 30%, #38BDF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 15px;
    letter-spacing: -1px;
}

.premium-hero p {
    font-size: clamp(15px, 1.5vw, 18px);
    color: #94A3B8;
    max-width: 850px;
    margin: 0 auto;
    line-height: 1.8;
}

/* BADGE METRICS */
.metric-container {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 25px;
    flex-wrap: wrap;
}
.sci-badge {
    background: rgba(30, 41, 59, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 8px 16px;
    border-radius: 100px;
    font-size: 13px;
    font-weight: 600;
    color: #38BDF8;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* PREMIUM CARD COMPONENT */
.premium-card {
    background: rgba(17, 24, 39, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-top: 3px solid #2563EB;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.premium-card:hover {
    transform: translateY(-4px);
    border-top-color: #38BDF8;
    box-shadow: 0 15px 35px rgba(56, 189, 248, 0.1);
}

.card-title-root { color: #F87171; font-size: 20px; font-weight: 700; display: flex; align-items: center; gap: 10px; margin-bottom: 20px; }
.card-title-sol { color: #34D399; font-size: 20px; font-weight: 700; display: flex; align-items: center; gap: 10px; margin-bottom: 20px; }

/* CYBER GAUGE */
.cyber-gauge {
    width: 210px;
    height: 210px;
    border-radius: 50%;
    margin: 25px auto;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    box-shadow: 0 0 30px rgba(0,0,0,0.5);
}
.cyber-gauge-inner {
    width: 160px;
    height: 160px;
    background: #0B0F19;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 1px solid rgba(255,255,255,0.05);
}

/* STREAMLIT BUTTON STYLING FOR INTERACTIVE FLOW */
div[data-testid="stColumn"] div.stButton > button {
    background: rgba(30, 41, 59, 0.5) !important;
    color: #94A3B8 !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    padding: 15px 10px !important;
    border-radius: 16px !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    line-height: 1.4 !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    min-height: 80px !important;
    width: 100% !important;
}

/* ACTIVE STATE ON STREAMLIT BUTTONS */
div[data-testid="stColumn"] div.stButton > button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.25) 0%, rgba(56, 189, 248, 0.15) 100%) !important;
    color: #FFFFFF !important;
    border: 1px solid #38BDF8 !important;
    box-shadow: 0 0 18px rgba(56, 189, 248, 0.3) !important;
    font-weight: 700 !important;
}

div[data-testid="stColumn"] div.stButton > button:hover {
    border-color: #38BDF8 !important;
    color: #FFFFFF !important;
    transform: translateY(-2px) !important;
}

/* INTUITIVE AI RECOMMENDATION BLOCK */
.ai-glass-panel {
    background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(17, 24, 39, 0.9) 100%);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-left: 6px solid #38BDF8;
    padding: 35px;
    border-radius: 20px;
    margin-top: 30px;
}

/* SEVERITY STATUS BAR */
.status-pill {
    padding: 6px 16px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
    display: inline-block;
}
.pill-critical { background: rgba(220, 38, 38, 0.15); color: #F87171; border: 1px solid rgba(220, 38, 38, 0.3); }
.pill-high { background: rgba(234, 88, 12, 0.15); color: #FB923C; border: 1px solid rgba(234, 88, 12, 0.3); }
.pill-moderate { background: rgba(217, 119, 6, 0.15); color: #FBBF24; border: 1px solid rgba(217, 119, 6, 0.3); }
.pill-low { background: rgba(5, 150, 105, 0.15); color: #34D399; border: 1px solid rgba(5, 150, 105, 0.3); }

/* CUSTOM EXPANDER STYLE */
.stExpander {
    background: rgba(30, 41, 59, 0.3) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 12px !important;
    margin-bottom: 10px !important;
}

</style>
""", unsafe_allow_html=True)

# =============================================================================
# LANGUAGE SELECTION COMPONENT
# =============================================================================
language = st.radio(
    "🌐 Language",
    ["English", "Indonesia"],
    horizontal=True
)

# =============================================================================
# MULTILINGUAL DICTIONARY DEFINITION
# =============================================================================
lang_dict = {
    "English": {
        "hero_desc": "Next-Generation Scientific Decision Support System for Research Reliability & Formula Optimization in Food Nanotechnology. Isolates instrument deviations, analyzes colloidal structural failures, and generates validated corrective actions precisely.",
        "badge_matrix": "📊 20+ Case Matrix",
        "badge_compliant": "🛡️ ISO & IUPAC Compliant",
        "tab_1_title": "🛠️ Smart Laboratory Troubleshooter",
        "tab_2_title": "🧠 Advanced DLS AI Expert Panel",
        "tab_3_title": "📚 Scientific Knowledge Base",
        "t1_section_title": "### 🔎 Experimental Failure Investigation Workflow",
        "t1_col_left_title": "##### ⚙️ Input Symptoms & Parameters",
        "t1_select_label": "Identify Primary Anomaly:",
        "t1_severity_label": "Severity Status:",
        "t1_chk_calibrated": "Sample tested using calibrated instruments?",
        "t1_chk_triplo": "Replication method complies with triplo rules (n=3)?",
        "t1_col_right_title": "##### 📌 Root Cause Analysis Phase Position (Click Phase for Manual Navigation)",
        "card_cause_title": "⚠️ Potential Root Causes",
        "card_sol_title": "✅ Prescriptive Actions",
        "t2_section_title": "### 🧠 Dynamic DLS Decision Support Panel",
        "t2_section_desc": "The system evaluates the electrokinetic interactions of nano-suspensions based on the fundamental principles of colloid stability theory.",
        "t2_col1_title": "##### 📏 Colloidal Size",
        "t2_col1_caption": "Measured using Dynamic Light Scattering (DLS).",
        "t2_col2_title": "##### ⚡ Electrokinetic Potential",
        "t2_col2_caption": "Represents the net surface charge of the particle shear layer.",
        "t2_col3_title": "##### 📊 Physical Stability Index",
        "status_massive_agg": "Massive Aggregation Phase Detected",
        "status_low_kinetic": "Low Kinetic Stability (Van der Waals Attractive Forces Dominate)",
        "status_stable": "Physically Stable Colloidal System",
        "cond_critical": "Critical Condition",
        "cond_warning": "Attention",
        "cond_optimal": "Optimal",
        "ai_panel_title": "🧠 AI Scientific Justification & Prescriptive Recommendations",
        "ai_panel_p1": "Based on cross-analysis of particle size parameters $d_h = {input_size}\ nm$ and zeta voltage value $\zeta = {input_zeta}\ mV$, the system detects that the electrostatic repulsive energy is unable to overcome the macroscopic attractive forces between particles. Referring to the <b>Smoluchowski</b> equation approach, it is recommended to take the following structured mitigation steps:",
        "ai_li_1": "<li><b style='color:#FFF;'>Steric Hindrance Induction:</b> Add hydrophilic non-ionic polymers such as PEG matrix thicknesses or branched-chain carbohydrate modifications to form geometric space barriers.</li>",
        "ai_li_2": "<li><b style='color:#FFF;'>Electrical Double Layer (EDL) Modification:</b> Reduce solvent ionic strength via washing the dispersed phase to widen the <i>Debye screening length</i> ($\kappa^{{-1}}$).</li>",
        "ai_li_3": "<li><b style='color:#FFF;'>Acoustic Wave Disruption:</b> Apply post-synthesis probe-type ultrasonication technology at high amplitude, with an external ice bath to avoid polymer thermal degradation effects.</li>",
        "t3_title": "### 📚 Experimental Troubleshooting Validation Database",
        "t3_desc": "Collection of spectroscopy and mechanical failure references of composite matrices based on standard protocols.",
        "t3_c1_title": "🔬 Case: Unexpected FTIR Peak (Infrared Spectrum Anomaly)",
        "t3_c1_body": """
        * **Primary Root Cause:** Fingerprint contamination or residual water vapor on the Diamond ATR crystal; incomplete evaporation of the organic purification solvent phase; absorption of free atmospheric water molecules by hygroscopic hydrocolloid samples.
        * **Protocol Solution:** Run background baseline spectrum extraction processes periodically every 3 runs; clean the ATR loader pad with analytical pure grade n-hexane or acetone; store samples in a vacuum desiccator chamber before scanning.
        """,
        "t3_c2_title": "📊 Case: Unexpected UV-Vis Peak (Spectrum Absorbance Deviation)",
        "t3_c2_body": """
        * **Primary Root Cause:** Thermal degradation effects of spectrophotometer instrument lamp emission components; occurrence of light scattering phenomena due to local micro-aggregate particle formation; cross-contamination of cuvette residues.
        * **Protocol Solution:** Clean quartz micro-cuvette cells using dilute nitric acid solution followed by pure ethanol rinsing; filter suspension samples using a 0.22-micron membrane syringe filter before scanning.
        """,
        "t3_c3_title": "📉 Case: Low Yield During Synthesis (Reaction Yield Drop)",
        "t3_c3_body": """
        * **Primary Root Cause:** Particle nucleation formation kinetics blocked due to external temperature fluctuations; degradation of sensitive active phase precursor molecules during lab inventory storage.
        * **Protocol Solution:** Increase reaction residence time in a controlled manner; apply thermoregulated jacketed reactor circulators with a maximum deviation accuracy of ±0.5°C; perform periodic precursor purity testing via HPLC.
        """,
        "t3_c4_title": "🫓 Case: Film Cracking (Biopolymer Matrix Brittleness/Cracking)",
        "t3_c4_body": """
        * **Primary Root Cause:** Internal stress due to excessively high water evaporation rates during thermal drying; insufficient plasticizer agent fraction ratio to lower the glass transition temperature ($T_g$).
        * **Protocol Solution:** Lower the oven drying temperature gradient gradually; add precise doses of glycerol or sorbitol to enhance macromolecular film chain mobility.
        """,
        "sb_title": "### 📋 Regulatory & Standards Compliance",
        "sb_body": """
        All troubleshooting recommendations are aligned with international standards:
        - 🌐 **ISO/TS 12901** (Nanotechnologies)
        - 🧪 **ASTM E2490-09** (DLS Particle Size)
        - 📘 **IUPAC Nomenclature**
        - 🌾 **AOAC Official Methods**
        """,
        "sb_ref_title": "### 📖 Primary Reference Journals",
        "sb_tip": "💡 **Tips:** Always ensure the lab room temperature is stable at around 25°C when measuring particle size using DLS.",
        "closing_quote": '"Every data failure in the laboratory is a hidden scientific indicator. The true excellence of research stems from the capability to isolate root causes in a coherent, logical, and standardized empirical evidence-based manner."'
    },
    "Indonesia": {
        "hero_desc": "Next-Generation Scientific Decision Support System untuk Keandalan Riset & Optimasi Formula Food Nanotechnology. Mengisolasi deviasi instrumen, menganalisis kegagalan struktural koloid, dan menyusun aksi korektif tervalidasi secara presisi.",
        "badge_matrix": "📊 20+ Matrix Kasus",
        "badge_compliant": "🛡️ ISO & IUPAC Compliant",
        "tab_1_title": "🛠️ Smart Laboratory Troubleshooter",
        "tab_2_title": "🧠 Advanced DLS AI Expert Panel",
        "tab_3_title": "📚 Scientific Knowledge Base",
        "t1_section_title": "### 🔎 Alur Investigasi Kegagalan Eksperimen",
        "t1_col_left_title": "##### ⚙️ Input Gejala & Parameter",
        "t1_select_label": "Identifikasi Anomali Utama:",
        "t1_severity_label": "Status Tingkat Keparahan:",
        "t1_chk_calibrated": "Sampel diuji menggunakan instrumen terkalibrasi?",
        "t1_chk_triplo": "Metode replikasi telah memenuhi kaidah triplo (n=3)?",
        "t1_col_right_title": "##### 📌 Posisi Fase Analisis Akar Masalah (Klik Fase untuk Navigasi Manual)",
        "card_cause_title": "⚠️ Akar Masalah Potensial",
        "card_sol_title": "✅ Tindakan Preskriptif",
        "t2_section_title": "### 🧠 Dynamic DLS Decision Support Panel",
        "t2_section_desc": "Sistem mengevaluasi interaksi elektrokinetik suspensi nano berdasarkan prinsip dasar teori stabilitas koloid.",
        "t2_col1_title": "##### 📏 Ukuran Koloid",
        "t2_col1_caption": "Diukur menggunakan Dynamic Light Scattering (DLS).",
        "t2_col2_title": "##### ⚡ Potensial Elektrokinetik",
        "t2_col2_caption": "Merepresentasikan net muatan permukaan lapisan geser partikel.",
        "t2_col3_title": "##### 📊 Indeks Stabilitas Fisik",
        "status_massive_agg": "Fase Agregasi Masif Terdeteksi",
        "status_low_kinetic": "Stabilitas Kinetik Rendah (Gaya Tarik Van der Waals Mendominasi)",
        "status_stable": "Sistem Koloid Stabil Secara Fisik",
        "cond_critical": "Kondisi Kritis",
        "cond_warning": "Perhatian",
        "cond_optimal": "Optimal",
        "ai_panel_title": "🧠 Justifikasi Ilmiah & Rekomendasi Preskriptif AI",
        "ai_panel_p1": "Berdasarkan analisis silang parameter ukuran partikel $d_h = {input_size}\ nm$ dan nilai tegangan zeta $\zeta = {input_zeta}\ mV$, sistem mendeteksi bahwa energi repulsi elektrostatik tidak mampu mengatasi gaya tarik makroskopis antar partikel. Mengacu pada pendekatan persamaan <b>Smoluchowski</b>, disarankan mengambil tindakan mitigasi terstruktur berikut:",
        "ai_li_1": "<li><b style='color:#FFF;'>Induksi Steric Hindrance:</b> Tambahkan polimer non-ionik hidrofilik seperti ketebalan matriks PEG atau modifikasi karbohidrat rantai bercabang untuk membentuk rintangan ruang geometris.</li>",
        "ai_li_2": "<li><b style='color:#FFF;'>Modifikasi Lapisan Listrik Ganda (EDL):</b> Reduksi kekuatan ionik pelarut melalui pencucian fasa terdispersi guna memperlebar <i>Debye screening length</i> ($\kappa^{{-1}}$).</li>",
        "ai_li_3": "<li><b style='color:#FFF;'>Disrupsi Gelombang Akustik:</b> Aplikasikan teknologi ultrasonikasi tipe probe pasca-sintesis pada amplitudo tinggi, dengan penangas es eksternal untuk menghindari efek degradasi termal polimer.</li>",
        "t3_title": "### 📚 Database Validasi Penanganan Kasus Eksperimen",
        "t3_desc": "Kumpulan referensi kegagalan spektroskopi dan mekanis matriks komposit berdasarkan protokol standar.",
        "t3_c1_title": "🔬 Kasus: Unexpected FTIR Peak (Anomali Spektrum Inframerah)",
        "t3_c1_body": """
        * **Akar Masalah Utama:** Kontaminasi sisa sidik jari atau residu uap air pada kristal Diamond ATR; evaporasi fasa pelarut organik purifikasi tidak tuntas; absorbsi molekul air bebas atmosfer oleh sampel hidrokoloid higroskopis.
        * **Solusi Protokol:** Jalankan proses ekstraksi spektrum *background baseline* secara periodik setiap 3 kali running; bersihkan landasan loader ATR dengan n-heksana atau aseton tingkat analisis murni; simpan sampel di ruang vakum desikator sebelum pemindaian dilakukan.
        """,
        "t3_c2_title": "📊 Kasus: Unexpected UV-Vis Peak (Penyimpangan Absorbansi Spektrum)",
        "t3_c2_body": """
        * **Akar Masalah Utama:** Efek degradasi termal komponen emisi lampu instrumen spektrofotometer; timbulnya fenomena hamburan cahaya akibat pembentukan mikro-agregat partikel terlarut lokal; kontaminasi silang residu kuvet.
        * **Solusi Protokol:** Lakukan pembersihan sel mikro-kuvet kuarsa menggunakan larutan asam nitrat encer diikuti pembilasan etanol murni; lakukan penyaringan sampel suspensi menggunakan syringe filter membran berpori 0.22 mikron sebelum pemindaian.
        """,
        "t3_c3_title": "📉 Kasus: Low Yield During Synthesis (Penurunan Rendemen Hasil Reaksi)",
        "t3_c3_body": """
        * **Akar Masalah Utama:** Jalur kinetika pembentukan nukleasi partikel terhambat akibat fluktuasi suhu eksternal; degradasi fasa aktif molekul prekursor sensitif selama penyimpanan inventaris lab.
        * **Solusi Protokol:** Tingkatkan waktu tinggal reaksi (*residence time*) secara terkontrol; aplikasikan sirkulator jaket reaktor termoregulasi dengan akurasi deviasi maksimal ±0.5°C; lakukan uji kemurnian prekursor berkala via HPLC.
        """,
        "t3_c4_title": "🫓 Kasus: Film Cracking (Kerapuhan/Retak Matriks Biopolimer)",
        "t3_c4_body": """
        * **Akar Masalah Utama:** Tegangan internal akibat laju penguapan air terlalu tinggi selama pengeringan termal; fraksi rasio agen plasticizer tidak mencukupi untuk menurunkan temperatur transisi gelas ($T_g$).
        * **Solusi Protokol:** Turunkan gradien suhu pengeringan oven secara bertahap; tambahkan dosis gliserol atau sorbitol secara presisi untuk meningkatkan mobilitas rantai makromolekul film.
        """,
        "sb_title": "### 📋 Kepatuhan Regulasi & Standar",
        "sb_body": """
        Seluruh rekomendasi pemecahan masalah diselaraskan dengan standar internasional:
        - 🌐 **ISO/TS 12901** (Nanotechnologies)
        - 🧪 **ASTM E2490-09** (DLS Particle Size)
        - 📘 **IUPAC Nomenclature**
        - 🌾 **AOAC Official Methods**
        """,
        "sb_ref_title": "### 📖 Jurnal Rujukan Utama",
        "sb_tip": "💡 **Tips:** Selalu pastikan temperatur ruangan lab stabil di kisaran 25°C saat mengukur ukuran partikel menggunakan DLS.",
        "closing_quote": '"Setiap kegagalan data di laboratorium adalah sebuah indikator ilmiah tersembunyi. Keunggulan sejati riset bersumber dari kapabilitas mengisolasi akar masalah secara runtut, logis, dan berbasis bukti empiris terstandardisasi."'
    }
}

# Shortcut variabel bahasa aktif
L = lang_dict[language]

# =============================================================================
# HERO SECTION
# =============================================================================
st.markdown(f"""
<div class="premium-hero">
    <h1>🔬 AuraNano.AI</h1>
    <p>{L['hero_desc']}</p>
    <div class="metric-container">
        <div class="sci-badge">{L['badge_matrix']}</div>
        <div class="sci-badge">{L['badge_compliant']}</div>
        <div class="sci-badge">🧠 Dynamic DLVO Logic</div>
        <div class="sci-badge">⚡ Real-time Verification</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# DATA ARCHITECTURE MATRIX (Dual-Language Keys Setup)
# =============================================================================
if language == "English":
    trouble_matrix = {
        "Nanoparticle Aggregation": {
            "severity": "CRITICAL", "class": "pill-critical", "phase": 3,
            "causes": ["Operational pH is within the system's Isoelectric Point (IEP) zone.", "Ionic strength of the media is too high, inducing EDL compression.", "Stabilizer/surfactant concentration is below the critical micelle concentration (CMC)."],
            "solutions": ["Adjust system pH away from the IEP point to induce electrostatic repulsive forces.", "Perform extensive dialysis processing to reduce accumulation of free salts.", "Optimize the stoichiometric ratio of protective surfactant to core material."]
        },
        "Low Encapsulation Efficiency": {
            "severity": "MODERATE", "class": "pill-moderate", "phase": 4,
            "causes": ["Diffusion rate of bioactive compounds out of the wall matrix is too fast during cross-linking.", "The ratio of trapping polymer to active core compound is disproportionate.", "High solubility of active components in the continuous/outer phase."],
            "solutions": ["Lower the encapsulation process temperature to suppress thermal molecular migration rates.", "Increase matrix density by raising structural polymer concentrations.", "Modify continuous phase pH to alter active substance ionization status into an insoluble form."]
        },
        "Large Particle Size": {
            "severity": "HIGH", "class": "pill-high", "phase": 2,
            "causes": ["Mechanical homogenization energy input or ultra-sonication duration is insufficient.", "Continuous phase viscosity is too dense, restricting droplet breakage.", "Dispersed phase feeding rate into the continuous phase is too aggressive."],
            "solutions": ["Increase sonication amplitude or add high-pressure cycles on the homogenizer.", "Dilute continuous phase viscosity or optimize temperature to lower friction coefficient.", "Use an automatic syringe pump device to regulate feeding rate constantly."]
        },
        "Low Zeta Potential": {
            "severity": "MODERATE", "class": "pill-moderate", "phase": 3,
            "causes": ["Electrical double layer compression due to counter-ions adsorption.", "Environmental pH neutralizes active functional group charges on the nanostructure surface.", "Occurrence of steric masking phenomena by high molecular weight non-ionic polymers."],
            "solutions": ["Perform particle washing with gradient centrifugation using ultra-pure distilled water.", "Calibrate operational pH precisely to maximize surface charge dissociation.", "Use a binary system stabilizer combination (ionic and non-ionic) with high precision."]
        },
        "Poor Film Properties (Cracking)": {
            "severity": "HIGH", "class": "pill-high", "phase": 4,
            "causes": ["Water evaporation kinetics are too fast during the oven drying process.", "Plasticizer concentration (e.g., glycerol) is too low, causing brittleness.", "Phase incompatibility between mixing polymers (phase separation)."],
            "solutions": ["Apply a step-down drying temperature curve with relative air humidity control.", "Increase the volume fraction ratio of plasticizer components precisely.", "Integrate a compatibility agent (macromolecular surfactant) to bridge phase boundaries."]
        }
    }
else:
    trouble_matrix = {
        "Nanoparticle Aggregation": {
            "severity": "CRITICAL", "class": "pill-critical", "phase": 3,
            "causes": ["Nilai pH operasional berada di area Isoelectric Point (IEP) sistem.", "Kekuatan ionik (ionic strength) media terlalu tinggi memicu kompresi EDL.", "Konsentrasi stabilizer/surfaktan berada di bawah critical micelle concentration (CMC)."],
            "solutions": ["Adjust pH sistem menjauhi titik IEP guna menginduksi gaya tolak elektrostatik.", "Lakukan proses dialisis ekstvenif untuk mereduksi akumulasi garam bebas.", "Optimasi rasio stoikiometri surfaktan pelindung terhadap core material."]
        },
        "Low Encapsulation Efficiency": {
            "severity": "MODERATE", "class": "pill-moderate", "phase": 4,
            "causes": ["Laju difusi zat bioaktif keluar dari matriks dinding terlalu cepat saat cross-linking.", "Rasio polimer penjerat terhadap zat aktif tidak proporsional.", "Kelarutan komponen aktif tinggi di dalam fasa kontinu/luar."],
            "solutions": ["Turunkan suhu proses penjeratan untuk menekan laju migrasi termal molekul.", "Tingkatkan densitas matriks dengan menaikkan konsentrasi polimer struktural.", "Modifikasi pH fasa kontinu untuk mengubah status ionisasi zat aktif menjadi bentuk tidak larut."]
        },
        "Large Particle Size": {
            "severity": "HIGH", "class": "pill-high", "phase": 2,
            "causes": ["Input energi mekanis homogenisasi atau durasi ultra-sonikasi tidak memadai.", "Viskositas fasa kontinu terlalu pekat, menahan pemecahan tetesan (droplets).", "Laju penambahan fasa terdispersi ke dalam fasa kontinu terlalu agresif."],
            "solutions": ["Tingkatkan amplitudo sonikasi atau tambahkan siklus tekanan tinggi pada homogenizer.", "Encerkan viskositas fasa kontinu atau optimasi suhu untuk menurunkan koefisien gesek.", "Gunakan alat syringe pump otomatis untuk regulasi feeding rate secara konstan."]
        },
        "Low Zeta Potential": {
            "severity": "MODERATE", "class": "pill-moderate", "phase": 3,
            "causes": ["Kompresi lapisan ganda elektrik akibat adsorpsi ion lawan (counter-ions).", "pH lingkungan menetralkan muatan gugus fungsi aktif pada permukaan nanostruktur.", "Terjadinya fenomena steric masking oleh polimer non-ionik berbobot molekul tinggi."],
            "solutions": ["Lakukan pencucian partikel dengan sentrifugasi gradien menggunakan akuades ultra-murni.", "Kalibrasi pH operasional secara presisi untuk memaksimalkan disosiasi muatan permukaan.", "Gunakan kombinasi stabilizer sistem biner (ionik dan non-ionik) dengan presisi."]
        },
        "Poor Film Properties (Cracking)": {
            "severity": "HIGH", "class": "pill-high", "phase": 4,
            "causes": ["Kinetika evaporasi air terlalu cepat selama proses pengeringan di dalam oven.", "Konsentrasi plasticizer (misal: gliserol) terlalu rendah menyebabkan kerapuhan.", "Inkompatibilitas fase antar polimer pencampur (phase separation)."],
            "solutions": ["Terapkan kurva penurunan suhu pengeringan bertahap dengan kontrol kelembaban udara.", "Tingkatkan rasio fraksi volume komponen plasticizer secara presisi.", "Integrasikan agen kompatibilisasi (surfactant macromolecule) untuk menjembatani batas fase."]
        }
    }

# =============================================================================
# WORKSPACE TABS INTERACTION
# =============================================================================
tab1, tab2, tab3 = st.tabs([
    L["tab_1_title"], 
    L["tab_2_title"], 
    L["tab_3_title"]
])

# -----------------------------------------------------------------------------
# TAB 1: SMART TROUBLESHOOTER
# -----------------------------------------------------------------------------
with tab1:
    st.markdown(L["t1_section_title"])
    
    col_left, col_right = st.columns([1, 2], gap="large")
    
    with col_left:
        st.markdown(L["t1_col_left_title"])
        
        # Callback untuk mendeteksi perubahan selectbox
        selected_issue = st.selectbox(
            L["t1_select_label"],
            list(trouble_matrix.keys()),
            key="ts_issue"
        )
        
        item = trouble_matrix[selected_issue]
        
        # State Management untuk sinkronisasi Dropdown -> Alur Fase Aktif
        if "active_phase" not in st.session_state or st.session_state.get('prev_issue') != selected_issue:
            st.session_state.active_phase = item['phase']
            st.session_state.prev_issue = selected_issue
        
        st.markdown(f"""
        <div style="margin-top:20px;">
            <p style="margin-bottom:5px; font-size:14px; color:#94A3B8;">{L['t1_severity_label']}</p>
            <span class="status-pill {item['class']}">{item['severity']} IMPACT</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        st.checkbox(L["t1_chk_calibrated"], value=True)
        st.checkbox(L["t1_chk_triplo"], value=True)

    with col_right:
        st.markdown(L["t1_col_right_title"])
        
        # Membuat 5 kolom horizontal untuk merepresentasikan tombol alur interaktif
        fase_cols = st.columns(5)
        
        if language == "English":
            fases_list = [
                {"num": "Phase 01", "name": "Identification"},
                {"num": "Phase 02", "name": "Deviation Detection"},
                {"num": "Phase 03", "name": "Root Isolation"},
                {"num": "Phase 04", "name": "Formula Correction"},
                {"num": "Phase 05", "name": "Stability Validation"}
            ]
        else:
            fases_list = [
                {"num": "Fase 01", "name": "Identifikasi"},
                {"num": "Fase 02", "name": "Deteksi Deviasi"},
                {"num": "Fase 03", "name": "Isolasi Akar"},
                {"num": "Fase 04", "name": "Koreksi Formulasi"},
                {"num": "Fase 05", "name": "Validasi Stabilitas"}
            ]
        
        # Looping pembuatan tombol interaktif
        for i, fase in enumerate(fases_list, start=1):
            with fase_cols[i-1]:
                # Kondisi jika tombol ini adalah fase yang sedang aktif
                is_current_active = (st.session_state.active_phase == i)
                
                # Menggunakan parameter 'type' primary untuk menyalakan style kustom CSS active
                button_label = f"{fase['num']}\n{fase['name']}"
                if st.button(
                    button_label, 
                    key=f"flow_step_{i}", 
                    type="primary" if is_current_active else "secondary",
                    use_container_width=True
                ):
                    st.session_state.active_phase = i
                    st.rerun()

        # Jarak vertikal sebelum panel output card
        st.write("")
        
        # Content Output Cards (Dinamis menampilkan data berdasarkan masalah saat ini)
        c1, c2 = st.columns(2)
        with c1:
            causes_html = "".join([f"<li style='margin-bottom:10px; font-size:14px;'>{c}</li>" for c in item["causes"]])
            st.markdown(f"""
            <div class="premium-card" style="border-top-color: #EF4444; min-height: 220px;">
                <div class="card-title-root">{L['card_cause_title']}</div>
                <ul style="padding-left:15px; color:#E2E8F0;">{causes_html}</ul>
            </div>
            """, unsafe_allow_html=True)
            
        with c2:
            solutions_html = "".join([f"<li style='margin-bottom:10px; font-size:14px;'>{s}</li>" for s in item["solutions"]])
            st.markdown(f"""
            <div class="premium-card" style="border-top-color: #10B981; min-height: 220px;">
                <div class="card-title-sol">{L['card_sol_title']}</div>
                <ul style="padding-left:15px; color:#E2E8F0;">{solutions_html}</ul>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 2: ADVANCED DLS ANALYZER
# -----------------------------------------------------------------------------
with tab2:
    st.markdown(L["t2_section_title"])
    st.write(L["t2_section_desc"])
    
    dls_col1, dls_col2, dls_col3 = st.columns([1.5, 1.5, 2], gap="large")
    
    with dls_col1:
        st.markdown(L["t2_col1_title"])
        input_size = st.number_input("Particle Size / Hydrodynamic Diameter (nm)", min_value=1.0, max_value=2000.0, value=120.0, step=5.0)
        st.caption(L["t2_col1_caption"])

    with dls_col2:
        st.markdown(L["t2_col2_title"])
        input_zeta = st.number_input("Zeta Potential Value (mV)", min_value=-100.0, max_value=100.0, value=-18.0, step=1.0)
        st.caption(L["t2_col2_caption"])

    # Intelligent Logic Calculation for Stability Index & Confidence Level
    abs_zeta = abs(input_zeta)
    
    # Simple Fuzzy Rules Logic
    if input_size > 600.0:
        status_text = L["status_massive_agg"]
        status_type = "error"
        base_index = max(int(abs_zeta * 0.8), 8)
        stability_index = min(base_index, 35)
        confidence_score = 94 - int(input_size * 0.02)
    elif abs_zeta < 25.0:
        status_text = L["status_low_kinetic"]
        status_type = "warning"
        stability_index = min(max(int(abs_zeta * 1.8), 12), 58)
        confidence_score = 88 + int(abs_zeta * 0.3)
    else:
        status_text = L["status_stable"]
        status_type = "success"
        stability_index = min(int(abs_zeta * 2.6), 100)
        confidence_score = 92 + min(int(input_size * 0.01), 6)

    # Prevent out of bounds
    confidence_score = max(min(confidence_score, 98), 70)

    with dls_col3:
        st.markdown(L["t2_col3_title"])
        gauge_deg = int((stability_index / 100) * 360)
        gauge_color = "#10B981" if stability_index >= 65 else ("#F59E0B" if stability_index >= 40 else "#EF4444")
        
        st.markdown(f"""
        <div class="cyber-gauge" style="background: conic-gradient({gauge_color} 0deg, {gauge_color} {gauge_deg}deg, #1E293B {gauge_deg}deg);">
            <div class="cyber-gauge-inner">
                <span style="font-size: 36px; font-weight: 800; color: white;">{stability_index}%</span>
                <span style="font-size: 11px; color: #94A3B8; font-weight: 600; margin-top:5px; text-transform:uppercase;">Stability Index</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    
    # Render Diagnostic Result Dynamic Box
    if status_type == "error": st.error(f"**{L['cond_critical']}:** {status_text}")
    elif status_type == "warning": st.warning(f"**{L['cond_warning']}:** {status_text}")
    else: st.success(f"**{L['cond_optimal']}:** {status_text}")

    # Advanced Science Panel Justification (Dynamic Translation Rendering)
    ai_p1_rendered = L["ai_panel_p1"].format(input_size=input_size, input_zeta=input_zeta)
    
    st.markdown(f"""
    <div class="ai-glass-panel">
        <h4 style="color:#38BDF8; margin-top:0; font-weight:700; display:flex; align-items:center; gap:8px;">
            {L['ai_panel_title']}
        </h4>
        <p style="color:#CBD5E1; font-size:14.5px; line-height:1.7;">
            {ai_p1_rendered}
        </p>
        <ul style="color:#94A3B8; font-size:14px; padding-left:20px; line-height:1.8;">
            {L['ai_li_1']}
            {L['ai_li_2']}
            {L['ai_li_3']}
        </ul>
        <div style="margin-top:20px; display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.03); padding:10px 20px; border-radius:10px;">
            <span style="font-size:13px; color:#94A3B8;">Confidence Engine Matrix Score:</span>
            <span style="font-size:15px; font-weight:700; color:#38BDF8;">{confidence_score}% via Deterministic Fuzzy Rules</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TAB 3: KNOWLEDGE BASE & REFERENSI JURNAL
# -----------------------------------------------------------------------------
with tab3:
    st.markdown(L["t3_title"])
    st.write(L["t3_desc"])
    
    db_col1, db_col2 = st.columns(2, gap="medium")
    
    with db_col1:
        with st.expander(L["t3_c1_title"]):
            st.markdown(L["t3_c1_body"])
        with st.expander(L["t3_c2_title"]):
            st.markdown(L["t3_c2_body"])

    with db_col2:
        with st.expander(L["t3_c3_title"]):
            st.markdown(L["t3_c3_body"])
        with st.expander(L["t3_c4_title"]):
            st.markdown(L["t3_c4_body"])

# =============================================================================
# SIDEBAR FOOTER & SCIENTIFIC COMPLIANCE
# =============================================================================
with st.sidebar:
    st.markdown(L["sb_title"])
    st.markdown(L["sb_body"])
    st.write("---")
    st.markdown(L["sb_ref_title"])
    st.caption("- Food Hydrocolloids")
    st.caption("- Carbohydrate Polymers")
    st.caption("- Journal of Food Engineering")
    st.caption("- Colloids and Surfaces A")
    st.write("---")
    st.info(L["sb_tip"])

# Closing Premium Quote
st.markdown(f"""
<div style="background: rgba(30, 41, 59, 0.4); border-left: 4px solid #2563EB; padding: 20px; border-radius: 8px; text-align: center; font-style: italic; font-size: 15px; color: #94A3B8; line-height: 1.6; margin-top: 40px;">
    {L['closing_quote']}
</div>
""", unsafe_allow_html=True)

