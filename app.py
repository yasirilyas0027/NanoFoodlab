import streamlit as st
import os

# =============================================================================
# SET PAGE CONFIG (Wajib berada di baris pertama sebelum render UI)
# =============================================================================
st.set_page_config(
    page_title="NanoFood Intelligence Lab",
    page_icon="🔬",
    layout="wide"
)

# =============================================================================
# INTEGRASI KEYBOARD INTERACTION ENGINE (Arrow Up & Arrow Down Navigation)
# =============================================================================
st.components.v1.html("""
<script>
    // Akses window utama dari dalam iframe Streamlit
    const targetWindow = window.parent || window;
    
    targetWindow.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            targetWindow.scrollBy({ top: 180, behavior: 'smooth' });
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            targetWindow.scrollBy({ top: -180, behavior: 'smooth' });
        }
    });
</script>
""", height=0, width=0)

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

/* Memastikan teks tetap putih murni & cerah di tema terang/light mode */
.hero-title {
    font-size: clamp(36px, 5vw, 60px) !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    margin-bottom: 10px !important;
    letter-spacing: -1px !important;
    text-shadow: 0 4px 12px rgba(0,0,0,0.3);
}

.hero-subtitle {
    font-size: clamp(18px, 2.5vw, 24px) !important;
    color: #38BDF8 !important;
    margin-bottom: 25px !important;
    font-weight: 500 !important;
    text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.hero-text {
    font-size: clamp(15px, 1.6vw, 18px) !important;
    color: #E2E8F0 !important;
    line-height: 1.8 !important;
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
    overflow-x: auto;
}
.workflow-flex {
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: nowrap;
    gap: 10px;
    min-width: 900px; 
}
.workflow-step {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 12px 18px;
    border-radius: 12px;
    color: #F1F5F9;
    font-weight: 600;
    font-size: 13px;
    text-align: center;
    white-space: nowrap;
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
    font-size: 18px;
}

/* INTERACTIVE CARDS (HOVER OVERLAYS) */
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
    margin-bottom: 12px;
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
    margin-bottom: 10px;
}
.quick-access-icon { font-size: 32px; margin-bottom: 5px; }
.quick-access-title { font-size: 16px; font-weight: 700; color: #1E293B; margin-bottom: 5px; }

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
.footer-credits { font-size: 13.5px; color: #F1F5F9; font-weight: 600; margin-top: 15px; letter-spacing: 0.3px;}
.footer-credits span { color: #38BDF8; }
.footer-dept { font-size: 13px; color: #94A3B8; margin-top: 6px; font-weight: 500; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# MULTI-LANGUAGE DICTIONARY CONFIGURATION (100% ENG & 100% INDO)
# =============================================================================
# Menempatkan widget selektor bahasa di area kontrol atas halaman
language = st.radio(
    "🌐 Language / Bahasa",
    ["English", "Indonesia"],
    horizontal=True
)

# Definisi seluruh strings data tekstual aplikasi
lang_dict = {
    "English": {
        "hero_title": "🔬 NANOFOOD INTELLIGENCE LAB",
        "hero_sub": "Interactive Platform for Advanced Food Nanotechnology",
        "hero_desc": "Integrating high-precision laboratory calculators, cutting-edge material characterization modules, functional packaging analysis, and artificial intelligence for lab troubleshooting into a single unified digital ecosystem.",
        "announcement": "💡 **System Announcement:** Welcome! This platform is specifically designed to accommodate the acceleration of Experimental Research, Data-Driven Education, and Laboratory Applications in Food Technology. Use the $\\uparrow$ / $\\downarrow$ keys on your keyboard for precise page scrolling.",
        "metric_1_lbl": "Advanced Calculators",
        "metric_1_hlp": "Calculation of Molarities, Dilutions, IC50/EC50, Encapsulation Efficiency, etc.",
        "metric_2_lbl": "Learning Modules",
        "metric_2_hlp": "Composite Theory Education, Nano Interaction Characteristics, & Reference Journals.",
        "metric_3_lbl": "Characterization Tools",
        "metric_3_hlp": "Analysis of FTIR Spectra Peaks, XRD Crystallinity, Barrier Polymers.",
        "metric_4_lbl": "Research Ecosystems",
        "metric_4_hlp": "Research scope ranging from Precision Agriculture to Cellular Health.",
        "sec_1_title": "Platform Features Overview",
        "c1_title": "Laboratory Calculator",
        "c1_desc": "Provides automation for complex laboratory calculation algorithms such as serial dilutions, active reagent molarity, synthesis yield, hydrophobic substance encapsulation efficiency, and IC50/EC50 inhibition point analysis.",
        "c2_title": "Characterization Tools",
        "c2_desc": "Facilitates intelligent interpretation of instrument data without switching to external software. Assists in identifying microbial chemical functional groups and instantly measuring experimental sample crystallinity parameters.",
        "c3_title": "Packaging Analysis",
        "c3_desc": "Biopolymer matrix testing module to analyze Active Packaging performance, including calculations for Water Vapor Transmission Rate (WVTR), Moisture Content, Water Solubility, Swelling Index, and natural polymer biodegradation.",
        "sec_2_title": "Food Nanotechnology Research Workflow",
        "sec_3_title": "Featured Laboratory Interactive Tools",
        "sec_3_caption": "*Hover over the laboratory cards below to see full instrument capability details.*",
        "f1_title": "FTIR Analyzer",
        "f1_brief": "Identify the chemical structure of samples, organic functional group alterations, and detect newly formed hydrogen bonds post nanoencapsulation modifications.",
        "f1_overlay_h": "🎯 Capabilities & Peaks",
        "f2_title": "XRD Crystallinity Tech",
        "f2_brief": "Phase analysis of atomic arrangements in crystalline, semi-crystalline, or amorphous materials using X-ray diffraction angle intensity data.",
        "f2_overlay_h": "📐 Mathematical Engines",
        "f3_title": "IC50 Bio-Calculator",
        "f3_brief": "Evaluation of free radical scavenging efficiency (antioxidant) of active compounds or inhibition rate of pathogenic microbial growth.",
        "f3_overlay_h": "📈 Analytical Models",
        "btn_ftir": "Open FTIR Analyzer Module",
        "btn_xrd": "Open XRD Tools Matrix",
        "btn_ic50": "Open IC50 Tools Engine",
        "sec_4_title": "Why Choose NanoFood Intelligence Lab?",
        "w1_title": "Research-Oriented",
        "w1_desc": "Data architecture custom-tailored to modern food nanotechnology and polymer chemistry research needs.",
        "w2_title": "User Friendly UI",
        "w2_desc": "Clean, intuitive, and responsive interface design for students, lecturers, and professional lab analysts.",
        "w3_title": "Laboratory Ready",
        "w3_desc": "Validated mathematical computation formulas ready to accelerate thesis and research completions.",
        "w4_title": "Educational Node",
        "w4_desc": "Bridging fundamental nanotechnology theories with real-world laboratory data analysis implementation.",
        "sec_5_title": "Ecosystem Hub Quick Access",
        "footer_text": "Integrated system for global functional food nanostructure data optimization. Developed to support laboratory research workflow efficiency accurately and precisely.",
        "footer_credits": "Developed by:",
        "footer_dept": "Department / Study Program:",
        "pop_title": "Hub Laboratory Modern",
        "pop_info": "Module is currently in the data synchronization integration phase.",
        "pop_contact": "Please contact the development analysis team for raw computational parameters.",
        "pop_wait": "Waiting for Node Data Synchronization..."
    },
    "Indonesia": {
        "hero_title": "🔬 NANOFOOD INTELLIGENCE LAB",
        "hero_sub": "Platform Interaktif untuk Nanoteknologi Pangan Mutakhir",
        "hero_desc": "Mengintegrasikan kalkulator laboratorium presisi tinggi, modul karakterisasi material mutakhir, analisis pengemasan fungsional, dan kecerdasan artifisial penanganan masalah laborat dalam satu platform ekosistem digital terpadu.",
        "announcement": "💡 **Pengumuman Sistem:** Selamat datang! Platform ini dirancang khusus untuk mengakomodasi akselerasi Riset Eksperimental, Edukasi Berbasis Data, dan Aplikasi Laboratorium di bidang Teknologi Pangan. Gunakan tombol $\\uparrow$ / $\\downarrow$ pada keyboard untuk scrolling halaman secara presisi.",
        "metric_1_lbl": "Kalkulator Canggih",
        "metric_1_hlp": "Kalkulasi Molaritas, Dilusi, IC50/EC50, Efisiensi Enkapsulasi, dll.",
        "metric_2_lbl": "Modul Pembelajaran",
        "metric_2_hlp": "Edukasi Teori Komposit, Karakteristik Interaksi Nano, & Jurnal Rujukan.",
        "metric_3_lbl": "Alat Karakterisasi",
        "metric_3_hlp": "Analisis Puncak Spektra FTIR, XRD Crystalline, Polimer Barrier.",
        "metric_4_lbl": "Ekosistem Riset",
        "metric_4_hlp": "Cakupan Bidang Riset dari Pertanian Presisi Hingga Kesehatan Seluler.",
        "sec_1_title": "Tinjauan Fitur Platform",
        "c1_title": "Kalkulator Laboratorium",
        "c1_desc": "Menyediakan otomatisasi perhitungan algoritma laboratorium yang kompleks seperti kalkulasi pengenceran bertingkat, molaritas reagen aktif, rendemen sintesis, efisiensi enkapsulasi zat hidrofobik, serta analisis titik inhibisi IC50/EC50.",
        "c2_title": "Alat Karakterisasi",
        "c2_desc": "Memfasilitasi interpretasi data instrumen secara cerdas tanpa perlu berpindah-pindah software eksternal. Membantu identifikasi gugus fungsi kimia mikroba dan pengukuran parameter kristalinitas sampel rekayasa secara instan.",
        "c3_title": "Analisis Pengemasan",
        "c3_desc": "Modul pengujian matrik biopolimer untuk menganalisis performa Active Packaging, mencakup kalkulasi Water Vapor Transmission Rate (WVTR), Moisture Content, Water Solubility, Swelling Index, hingga biodegradasi alami polimer.",
        "sec_2_title": "Alur Riset Nanoteknologi Pangan",
        "sec_3_title": "Alat Interaktif Laboratorium Unggulan",
        "sec_3_caption": "*Arahkan kursor (hover) pada kartu laboratorium di bawah untuk melihat rincian kapabilitas analisis alat instrumen.*",
        "f1_title": "FTIR Analyzer",
        "f1_brief": "Identifikasi struktur kimia sampel, perubahan gugus fungsi organik, serta deteksi ikatan hidrogen baru pasca modifikasi nanoencapsulation.",
        "f1_overlay_h": "🎯 Kapabilitas & Puncak",
        "f2_title": "XRD Crystallinity Tech",
        "f2_brief": "Analisis fasa susunan atom matriks material kristalin, semi-kristalin, maupun amorf menggunakan data intensitas sudut difraksi sinar-X.",
        "f2_overlay_h": "📐 Mesin Matematika",
        "f3_title": "IC50 Bio-Calculator",
        "f3_brief": "Evaluasi efektivitas penangkapan radikal bebas (antioaksidan) senyawa aktif atau penekanan laju pertumbuhan mikroba patogen.",
        "f3_overlay_h": "📈 Model Analitis",
        "btn_ftir": "Buka Modul FTIR Analyzer",
        "btn_xrd": "Buka XRD Tools Matrix",
        "btn_ic50": "Buka IC50 Tools Engine",
        "sec_4_title": "Mengapa Memilih NanoFood Intelligence Lab?",
        "w1_title": "Berorientasi Riset",
        "w1_desc": "Arsitektur data disesuaikan khusus dengan kebutuhan riset nanoteknologi pangan modern dan kimia polimer.",
        "w2_title": "Antarmuka Ramah Pengguna",
        "w2_desc": "Tampilan antarmuka yang bersih, intuitif, dan responsif untuk mahasiswa, dosen, serta laboran profesional.",
        "w3_title": "Siap untuk Laboratorium",
        "w3_desc": "Formula komputasi matematis tervalidasi yang siap digunakan untuk mempercepat pengerjaan skripsi/tesis.",
        "w4_title": "Simpul Edukasi",
        "w4_desc": "Menggabungkan jembatan teori fundamental nano dengan implementasi analisis data laboratorium nyata.",
        "sec_5_title": "Akses Cepat Hub Ekosistem",
        "footer_text": "Sistem terintegrasi untuk optimasi pengolahan data nanostruktur pangan fungsional global. Dikembangkan untuk mendukung efisiensi pengerjaan alur riset laboratorium secara akurat dan presisi.",
        "footer_credits": "Dikembangkan oleh:",
        "footer_dept": "Program Studi:",
        "pop_title": "Hub Laboratorium Modern",
        "pop_info": "Modul sedang dalam fase integrasi sinkronisasi data.",
        "pop_contact": "Silakan hubungi tim analis pengembang untuk parameter komputasi mentah.",
        "pop_wait": "Menunggu Sinkronisasi Data Node..."
    }
}

# Menyimpan kamus aktif berdasarkan pilihan pengguna
txt = lang_dict[language]

# =============================================================================
# HELPER FUNCTION FOR SAFE PAGE LINKING & DYNAMIC ROUTING
# =============================================================================
def safe_page_link(page_path, label, icon="🔗", key_suffix="default", fallback_path=None, fallback_label=None):
    """
    Merender st.page_link secara aman tanpa merusak aplikasi.
    Jika target tidak ada, otomatis mengalihkan navigasi ke modul induk yang sesuai.
    """
    try:
        if os.path.exists(page_path) or os.path.exists(f"pages/{page_path}"):
            st.page_link(page_path, label=label, icon=icon, key=f"lnk_{page_path}_{key_suffix}")
        else:
            swapped_path = page_path.replace(" ", "_")
            if os.path.exists(swapped_path) or os.path.exists(f"pages/{swapped_path}"):
                st.page_link(swapped_path, label=label, icon=icon, key=f"lnk_swap_{page_path}_{key_suffix}")
            elif fallback_path and (os.path.exists(fallback_path) or os.path.exists(f"pages/{fallback_path}")):
                st.page_link(fallback_path, label=f"{label} ({'Open via' if language == 'English' else 'Buka via'} {fallback_label})", icon="🚀", key=f"lnk_fall_{page_path}_{key_suffix}")
            else:
                with st.popover(f"ℹ️ Info {label}", key=f"pop_{page_path}_{key_suffix}", use_container_width=True):
                    st.markdown(f"### 🔬 {txt['pop_title']}")
                    st.info(f"Modul **{label}** {txt['pop_info']}")
                    st.write(txt['pop_contact'])
    except Exception:
        with st.popover(f"📡 Status Server {label}", key=f"pop_err_{page_path}_{key_suffix}", use_container_width=True):
            st.warning(txt['pop_wait'])

# =============================================================================
# HERO SECTION (Gong Pembuka Animasi)
# =============================================================================
st.markdown(f"""
<div class="hero">
    <div class="particle p1"></div>
    <div class="particle p2"></div>
    <div class="particle p3"></div>
    <div class="particle p4"></div>
    <div class="hero-content">
        <h1 class="hero-title">{txt['hero_title']}</h1>
        <h3 class="hero-subtitle">{txt['hero_sub']}</h3>
        <p class="hero-text">{txt['hero_desc']}</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.info(txt['announcement'])

# =============================================================================
# PLATFORM CORE METRICS
# =============================================================================
st.write("")
m1, m2, m3, m4 = st.columns(4)
with m1: st.metric(txt['metric_1_lbl'], "20+", help=txt['metric_1_hlp'])
with m2: st.metric(txt['metric_2_lbl'], "30+", help=txt['metric_2_hlp'])
with m3: st.metric(txt['metric_3_lbl'], "10+", help=txt['metric_3_hlp'])
with m4: st.metric(txt['metric_4_lbl'], "8 Areas", help=txt['metric_4_hlp'])

# =============================================================================
# SECTION 1: PLATFORM FEATURES OVERVIEW
# =============================================================================
st.markdown(f'<h2 class="section-title">{txt["sec_1_title"]}</h2>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="glass-card">
        <div class="feature-title-box">
            <span>🧪</span>
            <h3>{txt['c1_title']}</h3>
        </div>
        <p style="color: #475569; font-size: 15px; line-height: 1.7; margin: 0;">
            {txt['c1_desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="glass-card">
        <div class="feature-title-box">
            <span>🔬</span>
            <h3>{txt['c2_title']}</h3>
        </div>
        <p style="color: #475569; font-size: 15px; line-height: 1.7; margin: 0;">
            {txt['c2_desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="glass-card">
        <div class="feature-title-box">
            <span>✅</span>
            <h3>{txt['c3_title']}</h3>
        </div>
        <p style="color: #475569; font-size: 15px; line-height: 1.7; margin: 0;">
            {txt['c3_desc']}
        </p>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 2: NANOTECHNOLOGY RESEARCH WORKFLOW
# =============================================================================
st.markdown(f'<h2 class="section-title">{txt["sec_2_title"]}</h2>', unsafe_allow_html=True)

# Alur Kerja Internasional tetap menggunakan terminologi universal publikasi ilmiah
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
# SECTION 3: FEATURED LABORATORY INTERACTIVE TOOLS
# =============================================================================
st.markdown(f'<h2 class="section-title">{txt["sec_3_title"]}</h2>', unsafe_allow_html=True)
st.caption(txt["sec_3_caption"])
st.write("")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown(f"""
    <div class="tool-card">
        <div class="tool-icon">🔬</div>
        <div class="tool-name">{txt['f1_title']}</div>
        <div class="tool-brief">{txt['f1_brief']}</div>
        <div class="tool-overlay">
            <h4>{txt['f1_overlay_h']}</h4>
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
    safe_page_link("pages/FTIR Analyzer.py", label=txt['btn_ftir'], icon="🔥", key_suffix="ftir_card", 
                   fallback_path="pages/NexusNano Hub.py", fallback_label="NexusNano Hub")

with f2:
    st.markdown(f"""
    <div class="tool-card">
        <div class="tool-icon">🧮</div>
        <div class="tool-name">{txt['f2_title']}</div>
        <div class="tool-brief">{txt['f2_brief']}</div>
        <div class="tool-overlay">
            <h4>{txt['f2_overlay_h']}</h4>
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
    safe_page_link("pages/Laboratory Calculator.py", label=txt['btn_xrd'], icon="⚡", key_suffix="xrd_card")

with f3:
    st.markdown(f"""
    <div class="tool-card">
        <div class="tool-icon">🧪</div>
        <div class="tool-name">{txt['f3_title']}</div>
        <div class="tool-brief">{txt['f3_brief']}</div>
        <div class="tool-overlay">
            <h4>{txt['f3_overlay_h']}</h4>
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
    safe_page_link("pages/IC50 Bio-Calculator.py", label=txt['btn_ic50'], icon="🚀", key_suffix="ic50_card",
                   fallback_path="pages/Laboratory Calculator.py", fallback_label="Laboratory Calculator")

# =============================================================================
# SECTION 4: WHY CHOOSE NANOFOOD INTELLIGENCE LAB
# =============================================================================
st.markdown(f'<h2 class="section-title">{txt["sec_4_title"]}</h2>', unsafe_allow_html=True)
w1, w2, w3, w4 = st.columns(4)

with w1:
    st.markdown(f"""
    <div class="why-card">
        <div class="why-icon">🔬</div>
        <div class="why-title">{txt['w1_title']}</div>
        <div class="why-desc">{txt['w1_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

with w2:
    st.markdown(f"""
    <div class="why-card">
        <div class="why-icon">💡</div>
        <div class="why-title">{txt['w2_title']}</div>
        <div class="why-desc">{txt['w2_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

with w3:
    st.markdown(f"""
    <div class="why-card">
        <div class="why-icon">⚗️</div>
        <div class="why-title">{txt['w3_title']}</div>
        <div class="why-desc">{txt['w3_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

with w4:
    st.markdown(f"""
    <div class="why-card">
        <div class="why-icon">📚</div>
        <div class="why-title">{txt['w4_title']}</div>
        <div class="why-desc">{txt['w4_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# SECTION 5: QUICK ACCESS TO ALL PAGES
# =============================================================================
st.markdown(f'<h2 class="section-title">{txt["sec_5_title"]}</h2>', unsafe_allow_html=True)

qa1, qa2, qa3, qa4, qa5, qa6 = st.columns(6)

with qa1:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🔬</div><div class="quick-access-title">FTIR Inst</div></div>', unsafe_allow_html=True)
    safe_page_link("pages/FTIR Analyzer.py", label="Open FTIR", icon="🔬", key_suffix="qa_ftir",
                   fallback_path="pages/NexusNano Hub.py", fallback_label="NexusNano Hub")

with qa2:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🧮</div><div class="quick-access-title">Lab Calc</div></div>', unsafe_allow_html=True)
    safe_page_link("pages/Laboratory Calculator.py", label="Open Calc", icon="🧮", key_suffix="qa_calc")

with qa3:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">📡</div><div class="quick-access-title">Database</div></div>', unsafe_allow_html=True)
    safe_page_link("pages/NexusNano Hub.py", label="Open Nexus", icon="📡", key_suffix="qa_nexus")

with qa4:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🤖</div><div class="quick-access-title">AuraNano</div></div>', unsafe_allow_html=True)
    safe_page_link("pages/AuraNano AI.py", label="Open AI", icon="🤖", key_suffix="qa_aura")

with qa5:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">📖</div><div class="quick-access-title">About Info</div></div>', unsafe_allow_html=True)
    safe_page_link("pages/About Info.py", label="Open About", icon="📖", key_suffix="qa_about",
                   fallback_path="pages/About Nanotechnology.py", fallback_label="About Nanotechnology")

with qa6:
    st.markdown('<div class="quick-access-box"><div class="quick-access-icon">🎨</div><div class="quick-access-title">Visual</div></div>', unsafe_allow_html=True)
    safe_page_link("pages/visualization.py", label="Open Model", icon="🎨", key_suffix="qa_visual")

# =============================================================================
# PLATFORM SYSTEM CLOSING FOOTER (CREDIT DEVELOPER UPDATE + DYNAMIC LANGUAGE)
# =============================================================================
st.markdown(f"""
<div class="footer-container">
    <div class="footer-logo">🔬 NanoFood Intelligence Lab</div>
    <div class="footer-tagline">Food Nanotechnology • Material Characterization • Packaging Science • Intelligent Bioactivity</div>
    <p style="font-size: 13px; max-width:600px; margin:auto; opacity: 0.7; line-height: 1.6;">
        {txt['footer_text']}
    </p>
    <div class="footer-credits">
        {txt['footer_credits']} <span>Putri Aprilia</span> • <span>Sifa Resti Nur Ranyanti</span> • <span>Yasir Ilyas Trikurnianto</span>
    </div>
    <div class="footer-dept">
        {txt['footer_dept']} <span>Nanoteknologi Pangan</span>
    </div>
    <br>
    <p style="font-size: 12px; margin-top:20px; border-top:1px solid rgba(255,255,255,0.05); padding-top:20px;">
        © 2026 NanoFood Intelligence Lab | Version 1.0.0 Stable Deployment Framework
    </p>
</div>
""", unsafe_allow_html=True)

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

