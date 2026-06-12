import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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
    color: #FFFFFF !important;
    margin-bottom: 15px;
    letter-spacing: -1.5px;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: clamp(16px, 2vw, 22px);
    color: #38BDF8 !important;
    margin-bottom: 25px;
    font-weight: 500;
    letter-spacing: 0.5px;
}

.hero-text {
    font-size: clamp(14px, 1.4vw, 17px);
    color: #E2E8F0 !important;
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
# MULTI-LANGUAGE SYSTEM DICTIONARY (100% EXCLUSIVE PER LANGUAGE)
# =============================================================================
language = st.radio(
    "🌐 Language",
    ["English", "Indonesia"],
    horizontal=True
)

text_dict = {
    "English": {
        "hero_title": "🚀 Why NanoFood Intelligence Lab Was Developed",
        "hero_subtitle": "Bridging Food Nanotechnology Research, Laboratory Calculations, and Scientific Education",
        "hero_text": "Conventional lab systems face challenges of data fragmentation, high risk of human error, and complex calculation learning curves. This integrated platform is engineered as an intelligent scientific computing infrastructure to validate and accelerate nano-scale food engineering research.",
        "sec1_title": "Background and Urgency",
        "sec1_subtitle": "Critical Analysis of Operational Challenges and Systemic Impacts on Research Sustainability",
        "crisis_title": "⚠ Current Challenges",
        "crisis_item1": "<b>Traditional Manual Calculations:</b> Processing dilution formulas and encapsulation efficiency using physical calculators is highly error-prone.",
        "crisis_item2": "<b>Software Fragmentation:</b> Researchers are forced to constantly switch between various unsynchronized spreadsheet applications.",
        "crisis_item3": "<b>Isolated Data:</b> Characterization results such as particle size distribution documentation are not stored centrally.",
        "crisis_item4": "<b>Time Inefficiency:</b> Standard curve analysis workflows consume a massive chunk of valuable active research time.",
        "effect_title": "📉 Impact on Research",
        "effect_item1": "<b>Decreased Efficiency:</b> Publication speed slows down due to the bureaucratic hurdle of manual raw data processing.",
        "effect_item2": "<b>Data Inconsistency:</b> High variability in results due to minor decimal rounding discrepancies across different software packages.",
        "effect_item3": "<b>Steep Learning Curve:</b> Students and junior researchers require extensive time to master pure chemical instrument interpretations.",
        "effect_item4": "<b>Chemical Wastage:</b> Prolific trial-and-error experiment repetitions triggered by initial stock solution miscalculations.",
        "sec2_title": "The 6 Core Laboratory Pillars",
        "sec2_subtitle": "Lab Computational Engineering Pillars Transformed By NanoFood Intelligence Lab",
        "p1_title": "Dilution Calculations",
        "p1_desc": "Automation of stock solution formulations, precise molarity adjustments, and serial dilution calculations for nanoemulsion media accuracy.",
        "p2_title": "Nanoparticle Characterization",
        "p2_desc": "Mapping particle size data (DLS), zeta potential charge stability, and mathematically simplifying XRD & FTIR spectra interpretations.",
        "p3_title": "Packaging Analysis",
        "p3_desc": "Mathematical computation of Water Vapor Transmission Rate (WVTR), swelling index, and biodegradation rates of active composite polymer packaging.",
        "p4_title": "IC50 Antioxidant Analysis",
        "p4_desc": "Determining free radical inhibition capacity (DPPH/ABTS) of active compounds via automated linear regression for accurate antioxidant efficacy.",
        "p5_title": "Standard Curve Analysis",
        "p5_desc": "Generating coefficient of determination ($R^2$) for spectrophotometry calibration curves to quantify bioactive analytes without bias deviation.",
        "p6_title": "Encapsulation Efficiency",
        "p6_desc": "Quantitative evaluation of core bioactive substance percentages successfully trapped inside lipid or chitosan nanocarrier walls.",
        "sec3_title": "Why Existing Methods Are Limited",
        "sec3_subtitle": "Traditional Workflow Bottleneck Study — Click Steps Below For Interactive Solutions",
        "step1": "Step 1", "step1_title": "Manual Calculator", "step1_desc": "Low accuracy & typo prone",
        "step2": "Step 2", "step2_title": "Spreadsheet Pro", "step2_desc": "Complex & unvalidated formulas",
        "step3": "Step 3", "step3_title": "Data Transfer", "step3_desc": "Risk of corrupt & lost files",
        "step4": "Step 4", "step4_title": "Interpretation", "step4_desc": "Non-standard subjective analysis",
        "step5": "Final Output", "step5_title": "Potential Error", "step5_desc": "Research replication failure",
        "selector_label": "Analysis of Traditional Bottleneck Causes & NanoFoodLab Interventions:",
        "opt1": "Manual Calculator & Spreadsheet Processing",
        "opt2": "Data Transfer Disruption",
        "opt3": "Subjective Result Interpretation",
        "err1": "🚨 **Traditional Problem:** Manually entering absorbance data into spreadsheets is highly vulnerable to row shifting. A single cell input error ruins the entire regression curve.",
        "succ1": "⚡ **NanoFoodLab Solution:** Built-in automated formula validation. Users simply enter basic parameters, and the system locks mathematical algorithms to IUPAC standards.",
        "err2": "🚨 **Traditional Problem:** Transferring raw binary files from characterization instruments across different lab computers poses severe risks of metadata corruption.",
        "succ2": "⚡ **NanoFoodLab Solution:** A unified cloud-based system (Single Integrated Platform) completely eliminates the need for file transfers across separate apps.",
        "err3": "🚨 **Traditional Problem:** Reading packaging biodegradation decay trends without established statistical bases births biased scientific conclusions between researchers.",
        "succ3": "⚡ **NanoFoodLab Solution:** Equipped with built-in scientific explanations that reference directly back to ISO standards and accredited global journals.",
        "sec4_title": "The Paradigm Shift: NanoFoodLab Solution",
        "sec4_subtitle": "Structural Comparison of Before vs After Platform Implementation",
        "before_h": "❌ Conventional (Without NanoFoodLab)",
        "before_1": "🔴 Plate count calculations and IC50 value determination consume hours of manual labor.",
        "before_2": "🔴 Inconsistent formula compilations across separate lab researcher computers.",
        "before_3": "🔴 Student confusion during raw instrument output data analysis and interpretation.",
        "before_4": "🔴 High risk of functional food formula replication failure due to decimal rounding bias.",
        "after_h": "✓ Modern (With NanoFoodLab)",
        "after_1": "🟢 Calculation automation successfully completed within seconds via background computing.",
        "after_2": "🟢 Single Unified Platform integration guarantees total data standardization.",
        "after_3": "🟢 Theoretical explanation modules systematically guide scientific data interpretation.",
        "after_4": "🟢 High research replicability achieved thanks to absolute mathematical formula validation.",
        "sec5_title": "Scientific Foundation & Impact Matrix",
        "sec5_subtitle": "International Regulatory Frameworks and Lab Research Publication Distribution Visualization",
        "matrix_title": "Standardization Matrix",
        "matrix_desc": "NanoFood Intelligence Lab is not built on arbitrary workflow assumptions. Our platform's algorithmic architecture complies fully with international conventions and high-impact peer-reviewed journals:",
        "chart_title": "Lab Computational Burden Profile",
        "chart_col": "Calculations Load (%)",
        "vector_title": "Simulated Research Impact Vector",
        "m1_t": "🎓 Impact on Education", "m1_v": "Greatly Increased", "m1_d": "94% Comprehension",
        "m2_t": "🔬 Impact on Research", "m2_v": "Faster Cycles", "m2_d": "-40% Time-Loss",
        "m3_t": "🧪 Lab Activities", "m3_v": "Manual Error Free", "m3_d": "100% Accuracy",
        "m4_t": "📊 Data Interpretation", "m4_v": "Standardized", "m4_d": "ISO Compliant",
        "sec6_title": "Knowledge Corner",
        "sec6_subtitle": "Evaluating Why Platform-Based Approaches Are Essential in Modern Research Ecosystems",
        "quiz_h": "Quick Verification Quiz",
        "quiz_q": "Why is the method of standard curve processing using conventional calculators considered to have a huge limitation?",
        "radio_label": "Select the most appropriate architectural conclusion:",
        "ans1": "Conventional calculators lack an automated cross-validation system, thereby triggering error propagation.",
        "ans2": "Physical calculators consume too much battery power to compute complex linear regressions.",
        "ans3": "The conventional method is deliberately prohibited by international ISO standards.",
        "quiz_succ": "🎉 **Correct Answer!** The absence of automatic formula locking on conventional calculators triggers descriptive error propagation that risks failing product replication.",
        "quiz_err": "❌ **Incorrect.** The primary reason is not a technical battery issue or raw ISO bans, but rather the high accumulation of human error propagation from manual entries.",
        "ecosystem_info": "**Ecosystem Synergy:** This platform is inclusively developed to support the pillars of functional food technology education, intermediate laboratory activities, cutting-edge scientific research, and data interpretation accuracy through an integrated, user-friendly, and scientifically validated computing environment."
    },
    "Indonesia": {
        "hero_title": "🚀 Mengapa NanoFood Intelligence Lab Dikembangkan",
        "hero_subtitle": "Menjembatani Riset Nanoteknologi Pangan, Kalkulasi Laboratorium, dan Edukasi Ilmiah",
        "hero_text": "Sistem laboratorium konvensional menghadapi tantangan fragmentasi data, risiko kesalahan manusia yang tinggi, dan kurva pembelajaran kalkulasi yang kompleks. Platform terintegrasi ini dirancang sebagai infrastruktur komputasi ilmiah cerdas untuk memvalidasi dan mempercepat riset rekayasa pangan skala nano.",
        "sec1_title": "Latar Belakang dan Urgensi",
        "sec1_subtitle": "Analisis Kritis Tantangan Operasional dan Dampak Sistemik Terhadap Keberlanjutan Riset",
        "crisis_title": "⚠ Tantangan Saat Ini",
        "crisis_item1": "<b>Kalkulasi Manual Tradisional:</b> Pemrosesan rumus pengenceran dan efisiensi enkapsulasi menggunakan kalkulator fisik sangat rentan terhadap kesalahan.",
        "crisis_item2": "<b>Fragmentasi Perangkat Lunak:</b> Peneliti terpaksa terus-menerus beralih di antara berbagai aplikasi spreadsheet yang tidak sinkron.",
        "crisis_item3": "<b>Data Terisolasi:</b> Dokumentasi hasil karakterisasi seperti distribusi ukuran partikel tidak tersimpan secara terpusat.",
        "crisis_item4": "<b>Inefisiensi Waktu:</b> Alur kerja analisis kurva standar menyerap porsi waktu riset aktif yang sangat besar.",
        "effect_title": "📉 Dampak pada Penelitian",
        "effect_item1": "<b>Penurunan Efisiensi:</b> Kecepatan publikasi melambat akibat hambatan birokrasi pengolahan data mentah secara manual.",
        "effect_item2": "<b>Inkonsistensi Data:</b> Variabilitas hasil yang tinggi akibat perbedaan kecil pembulatan desimal di berbagai paket perangkat lunak.",
        "effect_item3": "<b>Kurva Belajar Curam:</b> Mahasiswa dan peneliti muda membutuhkan waktu ekstensif untuk menguasai interpretasi instrumen kimia murni.",
        "effect_item4": "<b>Pemborosan Bahan Kimia:</b> Pengulangan eksperimen trial-and-error yang sering terjadi akibat kesalahan perhitungan larutan stok awal.",
        "sec2_title": "6 Pilar Utama Laboratorium",
        "sec2_subtitle": "Pilar Rekayasa Komputasi Lab yang Ditransformasikan Oleh NanoFood Intelligence Lab",
        "p1_title": "Kalkulasi Pengenceran",
        "p1_desc": "Otomatisasi formulasi larutan stok, penyesuaian molaritas yang presisi, dan kalkulasi pengenceran bertingkat untuk akurasi media nanoemulsi.",
        "p2_title": "Karakterisasi Nanopartikel",
        "p2_desc": "Pemetaan data ukuran partikel (DLS), stabilitas muatan potensial zeta, dan penyederhanaan interpretasi spektra XRD & FTIR secara matematis.",
        "p3_title": "Analisis Kemasan",
        "p3_desc": "Komputasi matematis Laju Transmisi Uap Air (WVTR), indeks pembengkakan, dan laju biodegradasi kemasan polimer komposit aktif.",
        "p4_title": "Analisis Antioksidan IC50",
        "p4_desc": "Penentuan kapasitas inhibisi radikal bebas (DPPH/ABTS) dari senyawa aktif melalui regresi linear otomatis untuk efikasi antioksidan yang akurat.",
        "p5_title": "Analisis Kurva Standar",
        "p5_desc": "Menghasilkan koefisien determinasi ($R^2$) untuk kurva kalibrasi spektrofotometri guna mengkuantifikasi analit bioaktif tanpa deviasi bias.",
        "p6_title": "Efisiensi Enkapsulasi",
        "p6_desc": "Evaluasi kuantitatif persentase zat bioaktif inti yang berhasil terperangkap di dalam dinding nanokarier lipid atau kitosan.",
        "sec3_title": "Mengapa Metode Konvensional Terbatas",
        "sec3_subtitle": "Studi Hambatan Alur Kerja Tradisional — Klik Langkah di Bawah untuk Solusi Interaktif",
        "step1": "Langkah 1", "step1_title": "Kalkulator Manual", "step1_desc": "Akurasi rendah & rentan salah ketik",
        "step2": "Langkah 2", "step2_title": "Spreadsheet Pro", "step2_desc": "Rumus rumit & tidak tervalidasi",
        "step3": "Langkah 3", "step3_title": "Transfer Data", "step3_desc": "Risiko file korup & hilang",
        "step4": "Langkah 4", "step4_title": "Interpretasi", "step4_desc": "Analisis subjektif non-standar",
        "step5": "Hasil Akhir", "step5_title": "Potensi Error", "step5_desc": "Kegagalan replikasi penelitian",
        "selector_label": "Analisis Penyebab Hambatan Tradisional & Intervensi NanoFoodLab:",
        "opt1": "Kalkulator Manual & Pemrosesan Spreadsheet",
        "opt2": "Gangguan Transfer Data",
        "opt3": "Interpretasi Hasil yang Subjektif",
        "err1": "🚨 **Masalah Tradisional:** Memasukkan data absorbansi secara manual ke dalam spreadsheet sangat rentan terhadap pergeseran baris. Satu kesalahan input sel merusak seluruh kurva regresi.",
        "succ1": "⚡ **Solusi NanoFoodLab:** Validasi formula otomatis bawaan. Pengguna cukup memasukkan parameter dasar, dan sistem mengunci algoritma matematika sesuai standar IUPAC.",
        "err2": "🚨 **Masalah Tradisional:** Mentransfer file biner mentah dari instrumen karakterisasi di berbagai komputer lab menimbulkan risiko serius korupsi metadata.",
        "succ2": "⚡ **Solusi NanoFoodLab:** Sistem berbasis cloud yang terpadu (Single Integrated Platform) sepenuhnya menghilangkan kebutuhan transfer file di antara aplikasi terpisah.",
        "err3": "🚨 **Masalah Tradisional:** Membaca tren peluruhan biodegradasi kemasan tanpa basis statistik yang mapan melahirkan kesimpulan ilmiah yang bias antar peneliti.",
        "succ3": "⚡ **Solusi NanoFoodLab:** Dilengkapi dengan modul penjelasan ilmiah bawaan yang merujuk langsung kembali ke standar ISO dan jurnal global terakreditasi.",
        "sec4_title": "Pergeseran Paradigma: Solusi NanoFoodLab",
        "sec4_subtitle": "Komparasi Struktural Sebelum vs Sesudah Implementasi Platform",
        "before_h": "❌ Konvensional (Tanpa NanoFoodLab)",
        "before_1": "🔴 Perhitungan angka lempeng total dan penentuan nilai IC50 menghabiskan waktu berjam-jam kerja manual.",
        "before_2": "🔴 Kompilasi rumus yang tidak konsisten di antara komputer peneliti laboratorium yang terpisah.",
        "before_3": "🔴 Kebingungan mahasiswa selama analisis data dan interpretasi output instrumen mentah.",
        "before_4": "🔴 Risiko tinggi kegagalan replikasi formula pangan fungsional karena bias pembulatan desimal.",
        "after_h": "✓ Modern (Dengan NanoFoodLab)",
        "after_1": "🟢 Otomatisasi kalkulasi berhasil diselesaikan dalam hitungan detik melalui komputasi latar belakang.",
        "after_2": "🟢 Integrasi Single Unified Platform menjamin standardisasi data total.",
        "after_3": "🟢 Modul penjelasan teoritis secara sistematis memandu interpretasi data ilmiah.",
        "after_4": "🟢 Replikabilitas penelitian tinggi dicapai berkat validasi formula matematis yang absolut.",
        "sec5_title": "Landasan Ilmiah & Matriks Dampak",
        "sec5_subtitle": "Kerangka Regulasi Internasional dan Visualisasi Distribusi Publikasi Riset Lab",
        "matrix_title": "Matriks Standardisasi",
        "matrix_desc": "NanoFood Intelligence Lab tidak dibangun di atas asumsi alur kerja yang sembarangan. Arsitektur algoritmik platform kami sepenuhnya mematuhi konvensi internasional dan jurnal ilmiah bereputasi tinggi:",
        "chart_title": "Profil Beban Komputasi Lab",
        "chart_col": "Beban Kalkulasi (%)",
        "vector_title": "Vektor Dampak Simulasi Penelitian",
        "m1_t": "🎓 Dampak pada Edukasi", "m1_v": "Sangat Meningkat", "m1_d": "94% Pemahaman",
        "m2_t": "🔬 Dampak pada Riset", "m2_v": "Siklus Lebih Cepat", "m2_d": "-40% Kehilangan Waktu",
        "m3_t": "🧪 Aktivitas Lab", "m3_v": "Bebas Kesalahan Manual", "m3_d": "100% Akurasi",
        "m4_t": "📊 Interpretasi Data", "m4_v": "Terstandardisasi", "m4_d": "Patuh ISO",
        "sec6_title": "Pojok Pengetahuan",
        "sec6_subtitle": "Mengevaluasi Mengapa Pendekatan Berbasis Platform Sangat Penting dalam Ekosistem Riset Modern",
        "quiz_h": "Kuis Verifikasi Cepat",
        "quiz_q": "Mengapa metode pemrosesan kurva standar menggunakan kalkulator konvensional dianggap memiliki keterbatasan besar?",
        "radio_label": "Pilih kesimpulan arsitektur yang paling tepat:",
        "ans1": "Kalkulator konvensional tidak memiliki sistem validasi silang otomatis, sehingga memicu perambatan galat.",
        "ans2": "Kalkulator fisik mengonsumsi terlalu banyak daya baterai untuk menghitung regresi linear yang kompleks.",
        "ans3": "Metode konvensional sengaja dilarang oleh standar ISO internasional.",
        "quiz_succ": "🎉 **Jawaban Benar!** Absennya penguncian formula otomatis pada kalkulator konvensional memicu perambatan galat deskriptif yang berisiko menggagalkan replikasi produk.",
        "quiz_err": "❌ **Salah.** Alasan utamanya bukanlah masalah teknis baterai atau larangan ISO yang mentah, melainkan tingginya akumulasi perambatan kesalahan manusia dari entri manual.",
        "ecosystem_info": "**Sinergi Ekosistem:** Platform ini dikembangkan secara inklusif untuk mendukung pilar pendidikan teknologi pangan fungsional, aktivitas laboratorium tingkat menengah, penelitian ilmiah mutakhir, dan akurasi interpretasi data melalui lingkungan komputasi yang terintegrasi, ramah pengguna, dan tervalidasi secara ilmiah."
    }
}

text = text_dict[language]

# =============================================================================
# HERO SECTION WITH ANIMATED BACKDROP
# =============================================================================
st.markdown(f"""
<div class="hero">
    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="particle p5"></div>
    <div class="hero-content">
        <h1 class="hero-title">{text['hero_title']}</h1>
        <h3 class="hero-subtitle">{text['hero_subtitle']}</h3>
        <p class="hero-text">
            {text['hero_text']}
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# SECTION 1: BACKGROUND & CRISIS ANALYSIS
# =============================================================================
st.markdown(f'<h2 class="section-title">{text["sec1_title"]}</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="section-subtitle">{text["sec1_subtitle"]}</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown(f"""
    <div class="crisis-box">
        <h4>{text['crisis_title']}</h4>
        <ul>
            <li>{text['crisis_item1']}</li>
            <li>{text['crisis_item2']}</li>
            <li>{text['crisis_item3']}</li>
            <li>{text['crisis_item4']}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="effect-box">
        <h4>{text['effect_title']}</h4>
        <ul>
            <li>{text['effect_item1']}</li>
            <li>{text['effect_item2']}</li>
            <li>{text['effect_item3']}</li>
            <li>{text['effect_item4']}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 2: INTERACTIVE LABORATORY ARCHITECTURE CARDS
# =============================================================================
st.markdown(f'<h2 class="section-title">{text["sec2_title"]}</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="section-subtitle">{text["sec2_subtitle"]}</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""
    <div class="lab-card">
        <div class="lab-icon">🧪</div>
        <div class="lab-title">{text['p1_title']}</div>
        <div class="lab-desc">{text['p1_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown(f"""
    <div class="lab-card">
        <div class="lab-icon">🔬</div>
        <div class="lab-title">{text['p2_title']}</div>
        <div class="lab-desc">{text['p2_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown(f"""
    <div class="lab-card">
        <div class="lab-icon">📦</div>
        <div class="lab-title">{text['p3_title']}</div>
        <div class="lab-desc">{text['p3_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("") 

c4, c5, c6 = st.columns(3)
with c4:
    st.markdown(f"""
    <div class="lab-card">
        <div class="lab-icon">🌱</div>
        <div class="lab-title">{text['p4_title']}</div>
        <div class="lab-desc">{text['p4_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
with c5:
    st.markdown(f"""
    <div class="lab-card">
        <div class="lab-icon">📊</div>
        <div class="lab-title">{text['p5_title']}</div>
        <div class="lab-desc">{text['p5_desc']}</div>
    </div>
    """, unsafe_allow_html=True)
with c6:
    st.markdown(f"""
    <div class="lab-card">
        <div class="lab-icon">🧬</div>
        <div class="lab-title">{text['p6_title']}</div>
        <div class="lab-desc">{text['p6_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 3: WORKFLOW PIPELINE INTERACTIVE EXPLORER
# =============================================================================
st.markdown(f'<h2 class="section-title">{text["sec3_title"]}</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="section-subtitle">{text["sec3_subtitle"]}</p>', unsafe_allow_html=True)

p_col1, p_col2, p_col3, p_col4, p_col5 = st.columns(5)

with p_col1:
    st.markdown(f'<div class="pipe-step"><span class="pipe-badge">{text["step1"]}</span><div class="pipe-title">{text["step1_title"]}</div><div class="pipe-desc">{text["step1_desc"]}</div></div>', unsafe_allow_html=True)
with p_col2:
    st.markdown(f'<div class="pipe-step"><span class="pipe-badge">{text["step2"]}</span><div class="pipe-title">{text["step2_title"]}</div><div class="pipe-desc">{text["step2_desc"]}</div></div>', unsafe_allow_html=True)
with p_col3:
    st.markdown(f'<div class="pipe-step"><span class="pipe-badge">{text["step3"]}</span><div class="pipe-title">{text["step3_title"]}</div><div class="pipe-desc">{text["step3_desc"]}</div></div>', unsafe_allow_html=True)
with p_col4:
    st.markdown(f'<div class="pipe-step"><span class="pipe-badge">{text["step4"]}</span><div class="pipe-title">{text["step4_title"]}</div><div class="pipe-desc">{text["step4_desc"]}</div></div>', unsafe_allow_html=True)
with p_col5:
    st.markdown(f'<div class="pipe-step"><span class="pipe-badge">{text["step5"]}</span><div class="pipe-title">{text["step5_title"]}</div><div class="pipe-desc">{text["step5_desc"]}</div></div>', unsafe_allow_html=True)

st.write("")

selected_step = st.selectbox(
    text["selector_label"],
    [text["opt1"], text["opt2"], text["opt3"]]
)

if text["opt1"] in selected_step:
    st.error(text["err1"])
    st.success(text["succ1"])
elif text["opt2"] in selected_step:
    st.error(text["err2"])
    st.success(text["succ2"])
else:
    st.error(text["err3"])
    st.success(text["succ3"])

# =============================================================================
# SECTION 4: COGNITIVE MATRIX (BEFORE VS AFTER PARADIGM SHIFT)
# =============================================================================
st.markdown(f'<h2 class="section-title">{text["sec4_title"]}</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="section-subtitle">{text["sec4_subtitle"]}</p>', unsafe_allow_html=True)

b_left, b_right = st.columns(2, gap="large")

with b_left:
    st.markdown(f"""
    <div class="comp-card-before">
        <div class="comp-header">{text['before_h']}</div>
        <div class="comp-item">{text['before_1']}</div>
        <div class="comp-item">{text['before_2']}</div>
        <div class="comp-item">{text['before_3']}</div>
        <div class="comp-item">{text['before_4']}</div>
    </div>
    """, unsafe_allow_html=True)

with b_right:
    st.markdown(f"""
    <div class="comp-card-after">
        <div class="comp-header">{text['after_h']}</div>
        <div class="comp-item">{text['after_1']}</div>
        <div class="comp-item">{text['after_2']}</div>
        <div class="comp-item">{text['after_3']}</div>
        <div class="comp-item">{text['after_4']}</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 5: INTERACTIVE SIMULATION & SCIENTIFIC DATA FOUNDATION
# =============================================================================
st.markdown(f'<h2 class="section-title">{text["sec5_title"]}</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="section-subtitle">{text["sec5_subtitle"]}</p>', unsafe_allow_html=True)

sf_left, sf_right = st.columns([4, 3], gap="large")

with sf_left:
    st.markdown(f"""
    <div class="glass-card" style="height:100%;">
        <h4 style="color:#0F172A; margin-top:0;">{text['matrix_title']}</h4>
        <p style="font-size:14px; color:#475569;">{text['matrix_desc']}</p>
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
    chart_data = pd.DataFrame({
        "Lab Modules": ["Dilution", "Nano-Characterization", "Packaging", "IC50 Analysis", "Std Curve", "Encapsulation"],
        text["chart_title"]: [15, 25, 20, 12, 10, 18]
    })
    st.markdown(f"<p style='font-size:14px; font-weight:700; color:#0F172A; margin-bottom:5px;'>{text['chart_title']}</p>", unsafe_allow_html=True)
    st.bar_chart(data=chart_data.set_index("Lab Modules"), use_container_width=True)

# =============================================================================
# SECTION 6: RESEARCH IMPACT METRICS
# =============================================================================
st.write("")
st.markdown(f"<p style='text-align:center; font-weight:700; color:#0F172A; margin-bottom:10px;'>{text['vector_title']}</p>", unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric(text["m1_t"], text["m1_v"], text["m1_d"])
m2.metric(text["m2_t"], text["m2_v"], text["m2_d"])
m3.metric(text["m3_t"], text["m3_v"], text["m3_d"])
m4.metric(text["m4_t"], text["m4_v"], text["m4_d"])

# =============================================================================
# KNOWLEDGE CORNER: EDUCATIONAL INTERACTIVE QUIZ
# =============================================================================
st.markdown(f'<h2 class="section-title">{text["sec6_title"]}</h2>', unsafe_allow_html=True)
st.markdown(f'<p class="section-subtitle">{text["sec6_subtitle"]}</p>', unsafe_allow_html=True)

st.markdown(f"""
<div class="quiz-box">
    <h4 style="color:#0F172A; margin-top:0; margin-bottom:5px;">{text['quiz_h']}</h4>
    <p style="color:#64748B; font-size:14px; margin-bottom:20px;">{text['quiz_q']}</p>
</div>
""", unsafe_allow_html=True)

quiz_answer = st.radio(
    text["radio_label"],
    [text["ans1"], text["ans2"], text["ans3"]],
    index=None,
    key="why_quiz"
)

if quiz_answer is not None:
    if text["ans1"] in quiz_answer:
        st.balloons()
        st.success(text["quiz_succ"])
    else:
        st.error(text["quiz_err"])

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

st.info(text["ecosystem_info"])

# =============================================================================
# KEYBOARD NAVIGATION SYSTEM (ARROW UP / ARROW DOWN KEY LISTENER)
# =============================================================================
components.html(
    """
    <script>
    const doc = window.parent.document;
    doc.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown') {
            window.parent.scrollBy({ top: 250, behavior: 'smooth' });
        }
        if (e.key === 'ArrowUp') {
            window.parent.scrollBy({ top: -250, behavior: 'smooth' });
        }
    });
    </script>
    """,
    height=0,
    width=0
)

