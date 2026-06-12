import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# 1. KONFIGURASI HALAMAN & THEME PREMIUM
# ==========================================
st.set_page_config(
    page_title="NexusNano Hub",
    page_icon="🧬",
    layout="wide"
)

# Custom CSS untuk tampilan Dashboard Laboratorium Modern
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stMetric {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        border: 1px solid #e2e8f0;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(90deg, #1e3a8a, #3b82f6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .sub-text {
        color: #64748b;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. CENTRAL DATA ENGINE & DATABASES
# ==========================================
@st.cache_data
def get_dls_data():
    data = [
        [1, "Polistirena (PS-1)", 67.0, 0.154, "DLS (Malvern)", "Polimerisasi emulsi", "Aqueous; 25°C", "DOI:10.3390/polym12020477"],
        [2, "Polistirena (PS-2)", 50.0, 0.055, "DLS (Malvern)", "Polimerisasi emulsi", "Aqueous; 25°C", "Wong et al. 2020"],
        [3, "Polistirena (PS-3)", 28.0, 0.085, "DLS (Malvern)", "Polimerisasi emulsi", "Aqueous; 25°C", "Wong et al. 2020"],
        [4, "Polistirena (PS-4)", 20.8, 0.093, "DLS (Malvern)", "Polimerisasi emulsi", "Aqueous; 25°C", "Wong et al. 2020"],
        [5, "nZVI (Coffee + Tween)", 14.6, 0.24, "DLS (Malvern)", "Sintesis Hijau", "Aqueous; 25°C", "Fernandes et al. 2025"],
        [6, "nZVI (Coffee Raw)", 565.6, 0.56, "DLS (Malvern)", "Sintesis Hijau", "Aqueous; 25°C", "Fernandes et al. 2025"],
        [7, "nZVI (Labdanum + Tween)", 13.4, 0.31, "DLS (Malvern)", "Sintesis Hijau", "Aqueous; 25°C", "Fernandes et al. 2025"],
        [8, "nZVI (Labdanum Raw)", 218.1, 0.43, "DLS (Malvern)", "Sintesis Hijau", "Aqueous; 25°C", "Fernandes et al. 2025"],
        [9, "AuNP (Turkevich)", 3.3, 0.574, "DLS (Malvern)", "Reduksi Sitrat", "Aqueous; 90°C", "Oliveira et al. 2023"],
        [10, "AuNP (Citrate 5nm)", 12.92, 0.20, "DLS", "Reduksi Sitrat", "Aqueous; 25°C", "Ibrahim et al. 2023"],
        [11, "AuNP (Citrate 10nm)", 16.4, 0.20, "DLS", "Reduksi Sitrat", "Aqueous; 25°C", "Ibrahim et al. 2023"],
        [12, "AuNP (Citrate 80nm)", 85.85, 0.15, "DLS", "Reduksi Sitrat", "Aqueous; 25°C", "Ibrahim et al. 2023"],
        [13, "NP Emas Stabil Polimer", 50.0, 0.20, "DLS", "Sintesis Kimia", "Aqueous; 25°C", "Hipotetis"],
        [14, "Silika (Stöber)", 30.0, 0.10, "DLS", "Sintesis Stöber", "Etanol; 25°C", "N/A"],
        [15, "Silika (Large)", 300.0, 0.15, "DLS", "Modifikasi Stöber", "Aqueous; 25°C", "N/A"],
        [16, "AgNP (Green Synth)", 40.0, 0.18, "DLS", "Bio-Sintesis", "Aqueous; 25°C", "N/A"],
        [17, "ZnO NP", 100.0, 0.35, "DLS", "Hidrotermal", "Etanol; 60°C", "N/A"],
        [18, "Liposome", 100.0, 0.10, "DLS", "Film Lipid", "PBS; 25°C", "N/A"],
        [19, "LNP (Lipid Nano)", 80.0, 0.12, "DLS", "Nano Emulsi", "PBS; 25°C", "N/A"],
        [20, "Nanodiamant AKP", 7.5, 0.01, "DLS", "Penggilingan", "Air; 25°C", "N/A"],
        [21, "Graphene Oxide", 250.0, 0.20, "DLS", "Reduksi GO", "Air; 25°C", "N/A"],
        [22, "TiO₂ (Anatase)", 25.0, 0.30, "DLS", "Sol-Gel", "Air; 25°C", "N/A"],
        [23, "Al₂O₃ (Gamma)", 50.0, 0.25, "DLS", "Sol-Gel", "Air; 25°C", "N/A"],
        [24, "Fe₃O₄ (Magnetit)", 100.0, 0.20, "DLS", "Ko-Presipitasi", "Air; 25°C", "N/A"],
        [25, "Fe₃O₄@CA", 125.0, 0.22, "DLS", "Komposit", "Air; 25°C", "N/A"],
        [26, "Polimer PIC", 150.0, 0.18, "DLS", "Emulsi Polimerisasi", "Air; 25°C", "N/A"],
        [27, "PLGA (Nanokapsul)", 200.0, 0.15, "DLS", "Nanopresipitasi", "Air; 25°C", "N/A"],
        [28, "Lipid-Polimer Vesikel", 120.0, 0.10, "DLS", "Formulasi Ganda", "PBS; 25°C", "N/A"],
        [29, "PLA (Emulsi)", 250.0, 0.20, "DLS", "Solvent Evaporation", "Air; 25°C", "N/A"],
        [30, "Kitosan (Solubilized)", 80.0, 0.25, "DLS", "Ionotropik Gelasi", "Air; 25°C", "N/A"],
        [31, "Nanosfer (Au-Silica)", 90.0, 0.22, "DLS", "Core-Shell", "Air; 25°C", "N/A"],
        [32, "Silika Mesopori", 200.0, 0.30, "DLS", "Sintesis MCM-41", "Air; 25°C", "N/A"],
        [33, "Quantum Dot CdSe", 10.0, 0.10, "DLS", "Hot-Injection", "Organik; 25°C", "N/A"],
        [34, "PEG-PLGA Micelle", 80.0, 0.15, "DLS", "Self-Assembly", "PBS; 37°C", "N/A"],
        [35, "Nanoclay (Sepiolite)", 200.0, 0.35, "DLS", "Ultrasonikasi", "Air; 25°C", "N/A"],
        [36, "Silk Fibroin NP", 100.0, 0.25, "DLS", "Desolvasi", "Air; 25°C", "N/A"],
        [37, "Perovskite NP", 150.0, 0.40, "DLS", "Larutan Kimia", "DMF; 25°C", "N/A"],
        [38, "Carbon Black", 50.0, 0.30, "DLS", "Peleburan", "Air; 25°C", "N/A"],
        [39, "Platinum NP", 10.0, 0.20, "DLS", "Reduksi Sitrat", "Air; 25°C", "N/A"],
        [40, "TiN (Nitride)", 100.0, 0.25, "DLS", "Laminasi", "IPA; 25°C", "N/A"],
        [41, "Fullerene C60", 100.0, 0.30, "DLS", "Dispersi Kimia", "Toluena; 25°C", "N/A"],
        [42, "CuO NP", 150.0, 0.30, "DLS", "Reaksi Basah", "Air; 25°C", "N/A"],
        [43, "ZnS (Thiol)", 50.0, 0.25, "DLS", "Ko-Presipitasi", "Air; 25°C", "N/A"],
        [44, "ITO (Indium Tin)", 200.0, 0.40, "DLS", "Sol-Gel", "Air; 25°C", "N/A"],
        [45, "Silika + Safranin", 75.0, 0.28, "DLS", "Adsorpsi", "Air; 25°C", "N/A"],
        [46, "Iridium NP", 5.0, 0.10, "DLS", "Kimia Gas", "Air; 25°C", "N/A"],
        [47, "Nickel NP", 20.0, 0.20, "DLS", "Reaksi Basah", "Air; 25°C", "N/A"],
        [48, "CaCO3 (Thermal)", 100.0, 0.30, "DLS", "Kalsinasi", "Air; 25°C", "N/A"],
        [49, "ZrO2 (Zirconia)", 150.0, 0.35, "DLS", "Sol-Gel", "Air; 25°C", "N/A"],
        [50, "CoFe2O4 (Cobalt)", 100.0, 0.30, "DLS", "Ko-Presipitasi", "Air; 25°C", "N/A"]
    ]
    columns = ["ID", "Material", "Size (nm)", "PDI", "Instrument", "Metode Sintesis", "Kondisi", "Referensi"]
    return pd.DataFrame(data, columns=columns)

ftir_db = [
    ("O-H Stretching", 3200, 3550, "Alcohol / Phenol"),
    ("N-H Stretching", 3250, 3550, "Amine"),
    ("≡C-H Stretching", 3200, 3310, "Alkyne"),
    ("C-H Stretching", 2850, 2990, "Alkane"),
    ("Aldehyde C-H", 2700, 2900, "Aldehyde"),
    ("S-H Stretching", 2550, 2600, "Thiol"),
    ("C≡N Stretching", 2200, 2280, "Nitrile"),
    ("C≡C Stretching", 2100, 2250, "Alkyne"),
    ("Anhydride C=O", 1740, 1850, "Anhydride"),
    ("Ester C=O", 1735, 1765, "Ester"),
    ("Carbonyl C=O", 1700, 1750, "Carbonyl"),
    ("Carboxylic Acid", 1700, 1725, "Carboxylic Acid"),
    ("Amide", 1630, 1700, "Amide"),
    ("C=C Stretching", 1620, 1680, "Alkene"),
    ("Aromatic Ring", 1495, 1615, "Aromatic"),
    ("Nitro Group", 1300, 1570, "Nitro"),
    ("C-O Stretching", 1000, 1300, "Alcohol/Ether"),
    ("C-F", 1000, 1400, "Fluoride"),
    ("C-Cl", 600, 800, "Chloride"),
    ("C-Br", 500, 700, "Bromide")
]

uvvis_data = [
    {"Material":"AuNP", "Category":"Metal Nanoparticle", "Lambda_max":520, "Peak_Type":"SPR", "Particle_Size_nm":10, "PDI":"-", "Synthesis":"Chemical Reduction", "Medium":"Water", "Year":2024, "Journal":"Photonics", "DOI":"10.3390/photonics11080691", "Reference":"Pham et al."},
    {"Material":"AgNP", "Category":"Metal Nanoparticle", "Lambda_max":420, "Peak_Type":"SPR", "Particle_Size_nm":20, "PDI":"-", "Synthesis":"Green Synthesis", "Medium":"Water", "Year":2024, "Journal":"Scientific Reports", "DOI":"10.1038/s41598-024-82341-7", "Reference":"Mahanta et al."},
    {"Material":"ZnO", "Category":"Metal Oxide", "Lambda_max":320, "Peak_Type":"Excitonic", "Particle_Size_nm":40, "PDI":"-", "Synthesis":"Microbial Synthesis", "Medium":"Water", "Year":2025, "Journal":"Scientific Reports", "DOI":"10.1038/s41598-025-03421-w", "Reference":"Elkady et al."},
    {"Material":"TiO₂", "Category":"Metal Oxide", "Lambda_max":350, "Peak_Type":"Band Gap Absorption", "Particle_Size_nm":None, "PDI":"-", "Synthesis":"Green Synthesis", "Medium":"Water", "Year":2025, "Journal":"Discover Applied Sciences", "DOI":"10.1007/s42452-025-07521-0", "Reference":"Kaliammal et al."},
    {"Material":"CdSe QDs", "Category":"Quantum Dot", "Lambda_max":593, "Peak_Type":"Excitonic", "Particle_Size_nm":4.3, "PDI":"-", "Synthesis":"Hot Injection", "Medium":"Hexane", "Year":2023, "Journal":"Materials", "DOI":"10.3390/ma16217007", "Reference":"Wang et al."}
]
df_uvvis = pd.DataFrame(uvvis_data)

# ==========================================
# 3. SIDEBAR MULTI-MODULE NAVIGATION & LANG
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/external-flatart-icons-flat-flatarticons/128/external-nanotechnology-biotechnology-flatart-icons-flat-flatarticons.png", width=70)
    
    # SYSTEM DUAL-LANGUAGE SWITCHER INTERACTIVE
    language = st.radio(
        "🌐 Language / Bahasa",
        ["English", "Indonesia"],
        horizontal=True
    )
    
    st.title("Lab Navigation Panel" if language == "English" else "Panel Navigasi Lab")
    st.markdown("Select analysis module below:" if language == "English" else "Pilih modul analisis database dibawah ini:")
    
    menu_options = [
        "DLS Inventory & Property Analytics", 
        "UV-Vis Nanoparticle Database", 
        "FTIR Functional Group Analyzer"
    ]
    menu = st.radio(
        "Analysis Module:" if language == "English" else "Modul Analisis:", 
        menu_options
    )
    st.sidebar.divider()
    st.sidebar.caption(
        "💡 **Tip:** Use this navigation to process specific instrument data directly." 
        if language == "English" else 
        "💡 **Tip:** Gunakan navigasi ini untuk mengolah data instrumen spesifik secara langsung."
    )

# ==========================================
# MODULE 1: DLS INVENTORY & ANALYTICS
# ==========================================
if menu == "DLS Inventory & Property Analytics":
    if language == "English":
        st.markdown('<div class="main-header">🧬 DLS Nanomaterial Inventory & Analytics</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-text">Advanced Database System for Colloidal Size and Polydispersity Exploration</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="main-header">🧬 DLS Nanomaterial Inventory & Analytics</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-text">Sistem Basis Data Canggih Eksplorasi Ukuran dan Polidispersitas Koloid</div>', unsafe_allow_html=True)
    
    df_nano = get_dls_data()

    # Dashboard Metrics translation logic
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Material" if language == "English" else "Total Material", len(df_nano))
    m2.metric("Avg. Size" if language == "English" else "Rata-rata Ukuran", f"{df_nano['Size (nm)'].mean():.1f} nm")
    m3.metric("Min. Size" if language == "English" else "Ukuran Min.", f"{df_nano['Size (nm)'].min():.1f} nm")
    m4.metric("Avg. PDI" if language == "English" else "Rata-rata PDI", f"{df_nano['PDI'].mean():.3f}")

    st.divider()

    # Filter Interaktif
    expander_title = "🔍 Filter & Search Engine Panel" if language == "English" else "🔍 Panel Filter & Mesin Pencari"
    with st.expander(expander_title, expanded=True):
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            search_lbl = "Search Material Name" if language == "English" else "Cari Nama Material"
            search = st.text_input(search_lbl, "")
        with f_col2:
            method_lbl = "Select Synthesis Method" if language == "English" else "Pilih Metode Sintesis"
            metode = st.multiselect(method_lbl, df_nano["Metode Sintesis"].unique())
        with f_col3:
            range_lbl = "Size Range (nm)" if language == "English" else "Rentang Ukuran (nm)"
            size_range = st.slider(range_lbl, 0.0, 600.0, (0.0, 600.0))

    # Filter Logic
    filtered_df = df_nano.copy()
    if search:
        filtered_df = filtered_df[filtered_df["Material"].str.contains(search, case=False)]
    if metode:
        filtered_df = filtered_df[filtered_df["Metode Sintesis"].isin(metode)]
    filtered_df = filtered_df[(filtered_df["Size (nm)"] >= size_range[0]) & (filtered_df["Size (nm)"] <= size_range[1])]

    # Visualisasi & Tabel Master
    tab_titles = ["📊 Distribution Plot", "📈 Property Correlation", "📋 Master Database"] if language == "English" else ["📊 Plot Distribusi", "📈 Korelasi Properti", "📋 Basis Data Master"]
    tab1, tab2, tab3 = st.tabs(tab_titles)

    with tab1:
        st.subheader("Nanoparticle Size Distribution" if language == "English" else "Distribusi Ukuran Nanopartikel")
        if not filtered_df.empty:
            title_graph = "Size Frequency Visualization" if language == "English" else "Visualisasi Frekuensi Ukuran"
            fig_hist = px.histogram(filtered_df, x="Size (nm)", color="Metode Sintesis", 
                                   marginal="rug", hover_data=filtered_df.columns,
                                   title=title_graph,
                                   color_discrete_sequence=px.colors.qualitative.Bold)
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("No data found for graph visualization." if language == "English" else "Data tidak ditemukan untuk visualisasi grafik.")

    with tab2:
        st.subheader("Correlation: Size vs Polydispersity (PDI)" if language == "English" else "Korelasi Ukuran vs Polidispersitas (PDI)")
        if not filtered_df.empty:
            title_scatter = "Dispersion Quality Mapping" if language == "English" else "Mapping Kualitas Dispersi"
            fig_scatter = px.scatter(filtered_df, x="Size (nm)", y="PDI", 
                                    size="Size (nm)", color="Metode Sintesis",
                                    hover_name="Material", log_x=True,
                                    title=title_scatter)
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.info("No data found for graph visualization." if language == "English" else "Data tidak ditemukan untuk visualisasi grafik.")

    with tab3:
        st.subheader("Nanomaterial Registry Data" if language == "English" else "Data Registri Nanomaterial")
        # Menyesuaikan nama kolom tabel agar dinamis mengikuti bahasa
        if language == "English":
            display_df = filtered_df.rename(columns={"Metode Sintesis": "Synthesis Method", "Kondisi": "Condition", "Referensi": "Reference"})
            ref_col_key = "Reference"
        else:
            display_df = filtered_df
            ref_col_key = "Referensi"
            
        st.dataframe(display_df, use_container_width=True, hide_index=True,
                     column_config={
                         "Size (nm)": st.column_config.NumberColumn(format="%.2f nm"),
                         "PDI": st.column_config.NumberColumn(format="%.3f"),
                         ref_col_key: st.column_config.LinkColumn()
                     })

    # Stability Calculator
    st.divider()
    st.subheader("🧪 Predictive Lab Tool: Stability Estimator")
    st.info(
        "Use this simulator to predict dispersion stability based on your DLS inputs."
        if language == "English" else
        "Gunakan simulator ini untuk memprediksi kestabilan dispersi berdasarkan input DLS Anda."
    )

    c1, c2 = st.columns([1, 2])
    with c1:
        u_size = st.number_input("Input Size (nm)", 0.0, 1000.0, 50.0)
        u_pdi = st.number_input("Input PDI", 0.0, 1.0, 0.2)
        
    with c2:
        if u_pdi < 0.1: 
            stability = "Highly Monodisperse (Highly Stable)" if language == "English" else "Sangat Monodispers (Sangat Stabil)"
            color = "green"
        elif u_pdi < 0.3: 
            stability = "Moderate (Stable)" if language == "English" else "Moderat (Stabil)"
            color = "blue"
        else: 
            stability = "Polydisperse (Prone to Aggregation)" if language == "English" else "Polidispers (Cenderung Agregasi)"
            color = "orange"
        
        st.markdown(f"### Status: <span style='color:{color}'>{stability}</span>", unsafe_allow_html=True)
        st.progress(u_pdi)
        
        if language == "English":
            st.write(f"Particles sized **{u_size} nm** with a PDI of **{u_pdi}** indicate characteristics of a **{stability.lower()}** colloidal system.")
        else:
            st.write(f"Partikel berukuran **{u_size} nm** dengan PDI **{u_pdi}** menunjukkan karakteristik sistem koloid yang **{stability.lower()}**.")

# ==========================================
# MODULE 2: UV-VIS NANOPARTICLE DATABASE
# ==========================================
elif menu == "UV-Vis Nanoparticle Database":
    st.markdown('<div class="main-header">🔬 UV-Vis Nanoparticle Database</div>', unsafe_allow_html=True)
    if language == "English":
        st.markdown('<div class="sub-text">Comprehensive Literature Database for UV-Visible Spectrophotometric Characterization</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="sub-text">Database Literatur Komprehensif untuk Karakterisasi Spektrofotometri UV-Visible</div>', unsafe_allow_html=True)

    # Filter Sidebar Tambahan khusus UV-Vis
    st.sidebar.markdown("---")
    st.sidebar.header("⚙ UV-Vis Filters" if language == "English" else "⚙ Filter UV-Vis")
    uv_material = st.sidebar.multiselect("Material", df_uvvis["Material"].unique(), default=df_uvvis["Material"].unique())
    uv_category = st.sidebar.multiselect("Category" if language == "English" else "Kategori", df_uvvis["Category"].unique(), default=df_uvvis["Category"].unique())
    year_lbl = "Publication Year" if language == "English" else "Tahun Publikasi"
    uv_year = st.sidebar.slider(year_lbl, int(df_uvvis["Year"].min()), int(df_uvvis["Year"].max()), (int(df_uvvis["Year"].min()), int(df_uvvis["Year"].max())))

    # Apply Filters
    df_uv_filtered = df_uvvis[
        (df_uvvis["Material"].isin(uv_material)) & 
        (df_uvvis["Category"].isin(uv_category)) & 
        (df_uvvis["Year"] >= uv_year[0]) & (df_uvvis["Year"] <= uv_year[1])
    ]

    # Statistics Row
    st.subheader("📊 Database Statistics" if language == "English" else "📊 Statistik Basis Data")
    uc1, uc2, uc3, uc4 = st.columns(4)
    uc1.metric("Literatures" if language == "English" else "Literatur", len(df_uv_filtered))
    uc2.metric("Materials" if language == "English" else "Material", df_uv_filtered["Material"].nunique())
    uc3.metric("Average λmax" if language == "English" else "Rata-rata λmax", f"{df_uv_filtered['Lambda_max'].mean():.1f} nm" if not df_uv_filtered.empty else "N/A")
    uc4.metric("Latest Publication" if language == "English" else "Publikasi Terbaru", df_uv_filtered["Year"].max() if not df_uv_filtered.empty else "N/A")

    st.divider()

    # UV-Vis Real-time Interpretation Tool
    st.subheader("🧠 UV-Vis Peak Real-time Interpreter" if language == "English" else "🧠 Interpreter Real-time Puncak UV-Vis")
    peak_input_uv = st.number_input("Input λmax (nm)", min_value=200, max_value=1000, value=420)
    
    if peak_input_uv < 380:
        if language == "English":
            st.success("**Possible Interpretation:**\n\n• Metal Oxide Nanoparticle (ZnO, TiO₂, MgO)\n\n*Associated with:* Band Gap Absorption / Excitonic Transition")
        else:
            st.success("**Interpretasi yang Memungkinkan:**\n\n• Nanopartikel Oksida Logam (ZnO, TiO₂, MgO)\n\n*Asosiasi Karakter:* Absorpsi Band Gap / Transisi Eksitonik")
    elif 380 <= peak_input_uv <= 550:
        if language == "English":
            st.success("**Possible Interpretation:**\n\n• Silver Nanoparticle (AgNP) or Gold Nanoparticle (Small size)\n\n*Associated with:* Localized Surface Plasmon Resonance (LSPR)")
        else:
            st.success("**Interpretasi yang Memungkinkan:**\n\n• Nanopartikel Perak (AgNP) atau Nanopartikel Emas Ukuran Kecil (AuNP)\n\n*Asosiasi Karakter:* Resonansi Plasmon Permukaan Terlokalisasi (LSPR)")
    else:
        if language == "English":
            st.success("**Possible Interpretation:**\n\n• Quantum Dots / Larger AuNP / Core-Shell Nanoparticles\n\n*Associated with:* Red-shifted SPR / Quantum Confinement Effects")
        else:
            st.success("**Interpretasi yang Memungkinkan:**\n\n• Quantum Dots / AuNP Ukuran Besar / Nanopartikel Core-Shell\n\n*Asosiasi Karakter:* Efek Pergeseran Merah (Red-shifted) SPR / Efek Batasan Kuantum")

    st.divider()

    # Multiplots Grid
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.subheader("📈 Particle Size vs λmax Mapping" if language == "English" else "📈 Pemetaan Ukuran Partikel vs λmax")
        if not df_uv_filtered.empty:
            fig_scat_uv = px.scatter(df_uv_filtered, x="Particle_Size_nm", y="Lambda_max", color="Category", size_max=15, hover_name="Material")
            fig_scat_uv.update_layout(height=350)
            st.plotly_chart(fig_scat_uv, use_container_width=True)
        else:
            st.info("No data available for plotting." if language == "English" else "Tidak ada data yang tersedia untuk grafik.")

    with g_col2:
        st.subheader("🥧 Material Composition Share" if language == "English" else "🥧 Proporsi Komposisi Material")
        if not df_uv_filtered.empty:
            fig_pie_uv = px.pie(df_uv_filtered, names="Material", color_discrete_sequence=px.colors.sequential.RdBu)
            fig_pie_uv.update_layout(height=350)
            st.plotly_chart(fig_pie_uv, use_container_width=True)
        else:
            st.info("No data available for plotting." if language == "English" else "Tidak ada data yang tersedia untuk grafik.")

    # Spectra Region Multi-band Map
    st.subheader("🌈 Interactive UV-Vis Spectral Region Grid" if language == "English" else "🌈 Kisi Wilayah Spektral UV-Vis Interaktif")
    fig_region = go.Figure()
    fig_region.add_vrect(x0=200, x1=400, fillcolor="rgba(142, 68, 173, 0.1)", line_width=0, annotation_text="UV Region", annotation_position="top left")
    fig_region.add_vrect(x0=400, x1=700, fillcolor="rgba(39, 174, 96, 0.1)", line_width=0, annotation_text="Visible Region", annotation_position="top left")
    
    if not df_uv_filtered.empty:
        fig_region.add_trace(go.Scatter(
            x=df_uv_filtered["Lambda_max"], y=[1]*len(df_uv_filtered),
            mode="markers+text", text=df_uv_filtered["Material"],
            textposition="top center", marker=dict(size=12, color="blue", symbol="circle")
        ))
    fig_region.update_layout(xaxis_title="Wavelength (nm)", yaxis_visible=False, height=250, margin=dict(t=10, b=10))
    st.plotly_chart(fig_region, use_container_width=True)

    # Master Datatables & Expandable Details
    st.subheader("📚 UV-Vis Records Reference Register" if language == "English" else "📚 Registri Referensi Data UV-Vis")
    st.dataframe(df_uv_filtered, use_container_width=True, hide_index=True)

    # Expander Literature Details
    st.subheader("📖 Literature Deep Analysis" if language == "English" else "📖 Analisis Mendalam Literatur")
    for _, row in df_uv_filtered.iterrows():
        with st.expander(f"📑 Details: {row['Material']} | {row['Reference']} ({row['Year']})"):
            dl1, dl2 = st.columns(2)
            with dl1:
                st.write(f"**Journal:** {row['Journal']}")
                st.write(f"**Peak Type:** {row['Peak_Type']}")
                st.write(f"**Synthesis:** {row['Synthesis']}")
            with dl2:
                st.write(f"**λmax:** {row['Lambda_max']} nm")
                st.write(f"**Particle Size:** {row['Particle_Size_nm']} nm")
                st.write(f"**Medium:** {row['Medium']}")
                st.markdown(f"🔗 [Direct DOI Reference Link](https://doi.org/{row['DOI']})")

    # Download Button
    csv_uv = df_uv_filtered.to_csv(index=False)
    btn_lbl = "⬇ Download Filtered UV-Vis CSV Database" if language == "English" else "⬇ Unduh Database CSV UV-Vis Terfilter"
    st.download_button(btn_lbl, csv_uv, "UVVIS_DATABASE.csv", "text/csv")

    # Library Section
    st.subheader("📚 UV-Vis Spectrometry Reference Theory Library" if language == "English" else "📚 Perpustakaan Teori Referensi Spektrometri UV-Vis")
    topic_lbl = "Select Spectrum Target Topic" if language == "English" else "Pilih Topik Target Spektrum"
    topic_uv = st.selectbox(topic_lbl, ["SPR", "Band Gap", "Quantum Dot"])
    if topic_uv == "SPR":
        if language == "English":
            st.info("**Localized Surface Plasmon Resonance (LSPR):** Occurs due to the collective oscillation of conduction electrons in resonance with incident light waves. Typical characteristics: AgNPs (400–450 nm) & AuNPs (520–560 nm).")
        else:
            st.info("**Localized Surface Plasmon Resonance (LSPR):** Terjadi akibat osilasi kolektif elektron konduksi yang beresonansi dengan gelombang cahaya insiden. Karakteristik khas: AgNP (400–450 nm) & AuNP (520–560 nm).")
    elif topic_uv == "Band Gap":
        if language == "English":
            st.info("**Band Gap Absorption:** Electron transition from the valence band to the conduction band in metal oxide semiconductor materials. Typical characteristics: ZnO (320–380 nm) & TiO₂ (300–380 nm).")
        else:
            st.info("**Band Gap Absorption:** Terjadi perpindahan elektron dari pita valensi ke pita konduksi pada material semikonduktor oksida logam. Karakteristik khas: ZnO (320–380 nm) & TiO₂ (300–380 nm).")
    elif topic_uv == "Quantum Dot":
        if language == "English":
            st.info("**Quantum Confinement Effect:** Optical shift due to nanometer-scale manipulation. The smaller the semiconductor particle size, the wider the band gap, causing the absorption spectrum to shift toward shorter wavelengths (*Blue Shift*).")
        else:
            st.info("**Quantum Confinement Effect:** Pergeseran optik akibat manipulasi ukuran nanometer. Semakin kecil ukuran partikel semikonduktor, rentang band gap semakin melebar sehingga spektrum menyerap ke arah panjang gelombang lebih pendek (*Blue Shift*).")

# ==========================================
# MODULE 3: FTIR FUNCTIONAL GROUP ANALYZER
# ==========================================
else:
    st.markdown('<div class="main-header">🔬 FTIR Functional Group Analyzer</div>', unsafe_allow_html=True)
    if language == "English":
        st.markdown('<div class="sub-text">Automated FTIR Peak Analysis, Identification of Chemical Fingerprints & Matrix Prediction</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="sub-text">Analisis Puncak FTIR Otomatis, Identifikasi Sidik Jari Kimia & Prediksi Matriks</div>', unsafe_allow_html=True)

    col_input, col_view = st.columns([1, 2])

    with col_input:
        st.subheader("FTIR Peak Input" if language == "English" else "Input Puncak FTIR")
        input_lbl = "Enter FTIR Peaks (cm⁻¹) separated by comma" if language == "English" else "Masukkan Puncak FTIR (cm⁻¹) dipisahkan tanda koma"
        peak_input = st.text_input(input_lbl, "3400,2920,1730,1630,1050")
        
    # Processing Peaks String Input safely
    try:
        peaks = [float(x.strip()) for x in peak_input.split(",") if x.strip() != ""]
    except ValueError:
        if language == "English":
            st.error("Invalid input format. Please only enter numbers separated by commas.")
        else:
            st.error("Format input salah. Mohon hanya masukkan angka dan dipisahkan tanda koma.")
        peaks = [3400, 2920, 1730, 1630, 1050]

    functional_groups = []
    for peak in peaks:
        for name, minv, maxv, group in ftir_db:
            if minv <= peak <= maxv:
                functional_groups.append([peak, name, group])

    df_ftir_result = pd.DataFrame(functional_groups, columns=["Peak (cm⁻¹)", "Vibration", "Functional Group"])

    with col_view:
        st.subheader("🧬 Spectrum Complexity Status" if language == "English" else "🧬 Status Kompleksitas Spektrum")
        if len(peaks) < 5:
            if language == "English":
                st.success(f"✔ {len(peaks)} Peaks Detected → Likely Simple Compound Structure")
            else:
                st.success(f"✔ {len(peaks)} Puncak Terdeteksi → Struktur Senyawa Cenderung Sederhana")
        else:
            if language == "English":
                st.warning(f"⚠ {len(peaks)} Peaks Detected → Complex Matrix Molecule Dynamic")
            else:
                st.warning(f"⚠ {len(peaks)} Puncak Terdeteksi → Dinamika Molekul Matriks Kompleks")

    st.divider()

    # Results Table Identification
    st.subheader("📊 Functional Group Identification Results" if language == "English" else "📊 Hasil Identifikasi Gugus Fungsional")
    if not df_ftir_result.empty:
        if language == "English":
            st.dataframe(df_ftir_result.rename(columns={"Vibration":"Vibration Type","Functional Group":"Chemical Group/Class"}), use_container_width=True, hide_index=True)
        else:
            st.dataframe(df_ftir_result, use_container_width=True, hide_index=True)
        groups = df_ftir_result["Functional Group"].tolist()
    else:
        st.info("No organic functional groups matched the input peaks in current database." if language == "English" else "Tidak ada gugus fungsional organik yang cocok dengan input puncak dalam database saat ini.")
        groups = []

    # Interpretasi Terpadu & Prediksi Material
    int_col, mat_col = st.columns(2)

    with int_col:
        st.subheader("🧠 Chemical Fingerprint Interpretation" if language == "English" else "🧠 Interpretasi Sidik Jari Kimia")
        interpretation = []
        if "Alcohol / Phenol" in groups: 
            interpretation.append("Hydroxyl structural bands detected (-OH stretching)." if language == "English" else "Pita struktural hidroksil terdeteksi (-OH stretching).")
        if any(g in groups for g in ["Carbonyl", "Ester C=O", "Carboxylic Acid"]): 
            interpretation.append("Carbonyl compounds detected (C=O validation)." if language == "English" else "Senyawa karbonil terdeteksi (validasi C=O).")
        if "Amide" in groups: 
            interpretation.append("Protein backbone structure / aliphatic amide detected." if language == "English" else "Struktur tulang punggung protein / amida alifatik terdeteksi.")
        if "Aromatic" in groups: 
            interpretation.append("Aromatic core ring system compound present." if language == "English" else "Terdapat senyawa sistem cincin inti aromatik.")
        
        if interpretation:
            for item in interpretation:
                st.write("✔", item)
        else:
            st.write("No major diagnostic chemical fingerprints interpreted." if language == "English" else "Tidak ada sidik jari kimia diagnostik utama yang dapat diinterpretasikan.")

    with mat_col:
        st.subheader("🚀 Smart Material Prediction Matrix" if language == "English" else "🚀 Matriks Prediksi Material Cerdas")
        peakset = set([round(x) for x in peaks])
        
        # Algoritma Pencocokan Material Berdasarkan Cluster Penanda Utama
        predicted = False
        if any(p in peakset for p in range(3350, 3450)) and any(p in peakset for p in range(2900, 2950)) and any(p in peakset for p in range(1000, 1100)):
            st.success("High Confidence Match: **Cellulose Matrix**" if language == "English" else "Kesesuaian Akurasi Tinggi: **Matriks Selulosa**")
            predicted = True
        if any(p in peakset for p in range(1720, 1740)) and any(p in peakset for p in range(2900, 2950)):
            st.success("High Confidence Match: **PLA Film (Polylactic Acid)**" if language == "English" else "Kesesuaian Akurasi Tinggi: **Film PLA (Asam Polilaktat)**")
            predicted = True
        if any(p in peakset for p in range(3350, 3450)) and any(p in peakset for p in range(1620, 1640)):
            st.success("High Confidence Match: **Protein-Based Bio-nanocomposite Film**" if language == "English" else "Kesesuaian Akurasi Tinggi: **Film Bio-nanokomposit Berbasis Protein**")
            predicted = True
        if any(p in peakset for p in range(3350, 3450)) and any(p in peakset for p in range(1640, 1660)) and any(p in peakset for p in range(1540, 1560)):
            st.success("High Confidence Match: **Chitosan Biocompatible Matrix**" if language == "English" else "Kesesuaian Akurasi Tinggi: **Matriks Biokompatibel Kitosan**")
            predicted = True
            
        if not predicted:
            st.info("Pattern matrix did not confidently match known specific materials (Cellulose, PLA, Chitosan, etc.)." if language == "English" else "Pola matriks tidak cocok secara signifikan dengan material spesifik yang diketahui (Selulosa, PLA, Kitosan, dll).")

    # Spectrum Digital Mapping Graph
    st.divider()
    st.subheader("📈 Interactive Functional Grid Mapping Layout" if language == "English" else "📈 Tata Letak Pemetaan Kisi Fungsional Interaktif")
    
    fig_ftir = go.Figure()
    fig_ftir.add_vrect(x0=2500, x1=4000, fillcolor="rgba(46, 204, 113, 0.1)", line_width=0, annotation_text="Single Bond Region (-OH, -CH, -NH)", annotation_position="top left")
    fig_ftir.add_vrect(x0=2000, x1=2500, fillcolor="rgba(52, 152, 219, 0.1)", line_width=0, annotation_text="Triple Bond Region (C≡C, C≡N)", annotation_position="top left")
    fig_ftir.add_vrect(x0=1500, x1=2000, fillcolor="rgba(155, 89, 182, 0.1)", line_width=0, annotation_text="Double Bond Region (C=O, C=C)", annotation_position="top left")
    fig_ftir.add_vrect(x0=500,  x1=1500, fillcolor="rgba(230, 126, 34, 0.1)", line_width=0, annotation_text="Fingerprint Region", annotation_position="top left")

    # Plot Current Input Peaks Line
    txt_lbl = "Your Detected Peaks" if language == "English" else "Puncak Terdeteksi Anda"
    fig_ftir.add_trace(go.Scatter(
        x=peaks, y=[1] * len(peaks), mode="markers+text",
        text=[f"{p} cm⁻¹" for p in peaks], textposition="top center",
        marker=dict(size=12, color="crimson", symbol="diamond"), name=txt_lbl
    ))

    fig_ftir.update_layout(
        xaxis=dict(title="Wavenumber (cm⁻¹)" if language == "English" else "Bilangan Gelombang (cm⁻¹)", range=[4000, 500]), # Spektrum FTIR diplot terbalik
        yaxis=dict(showticklabels=False, range=[0, 2]),
        height=300, margin=dict(t=30, b=30, l=20, r=20), showlegend=False
    )
    st.plotly_chart(fig_ftir, use_container_width=True)

    # Reference Database Expander & Theory Block
    st.divider()
    lib_col_ftir, db_col_ftir = st.columns(2)

    with lib_col_ftir:
        st.subheader("📚 FTIR Theory Quick Guide" if language == "English" else "📚 Panduan Cepat Teori FTIR")
        topic_lbl_ftir = "Select Target Library Topic" if language == "English" else "Pilih Topik Target Pustaka"
        topic_ftir = st.selectbox(topic_lbl_ftir, ["Carbonyl", "O-H", "N-H", "Amide", "Aromatic", "Fingerprint Region"])
        if topic_ftir == "Carbonyl":
            if language == "English":
                st.info("Intense sharp band between **1750–1700 cm⁻¹**. Characteristics of ester, ketone, aldehyde, or carboxylic acid groups in polymer materials such as **PLA**.")
            else:
                st.info("Puncak tajam intens antara **1750–1700 cm⁻¹**. Karakteristik gugus ester, keton, aldehid, maupun asam karboksilat pada material polimer seperti **PLA**.")
        elif topic_ftir == "O-H":
            if language == "English":
                st.info("Very strong broad band in the range of **3550–3200 cm⁻¹** due to inter-molecular hydrogen bonding. Highly intense in **cellulose, starch, and polysaccharide matrices**.")
            else:
                st.info("Pita lebar (broad band) sangat kuat di rentang **3550–3200 cm⁻¹** akibat ikatan hidrogen inter-molekul. Sangat intens pada **selulosa, pati, dan matriks polisakarida**.")
        elif topic_ftir == "N-H":
            if language == "English":
                st.info("Primary/secondary amine stretching in the **3550–3250 cm⁻¹** region. Essential for detecting nitrogen group functionalization in chemical modifications of **chitosan**.")
            else:
                st.info("Peregangan amin primer/sekunder di daerah **3550–3250 cm⁻¹**. Esensial mendeteksi fungsionalisasi gugus nitrogen pada modifikasi kimia **kitosan**.")
        elif topic_ftir == "Amide":
            if language == "English":
                st.info("Displays sharp peaks of Amide I (~1650 cm⁻¹) and Amide II (~1550 cm⁻¹). Widely used to map functional groups in nanostructured proteins.")
            else:
                st.info("Menunjukkan puncak tajam Amida I (~1650 cm⁻¹) dan Amida II (~1550 cm⁻¹). Digunakan secara luas untuk memetakan gugus fungsional protein nanostruktur.")
        elif topic_ftir == "Aromatic":
            if language == "English":
                st.info("Sharp C=C aromatic ring stretching in the **1615–1495 cm⁻¹** region, detecting phenolic compounds or nanoparticle capping ligands.")
            else:
                st.info("Peregangan cincin karbon C=C aromatik yang tajam di daerah **1615–1495 cm⁻¹**, mendeteksi senyawa fenolik atau ligan penudung nanopartikel.")
        elif topic_ftir == "Fingerprint Region":
            if language == "English":
                st.info("Characteristic area below **1500–500 cm⁻¹** reflecting specific molecular bending deformation vibrations unique to each chemical isomer structural type.")
            else:
                st.info("Daerah khas di bawah **1500–500 cm⁻¹** yang merefleksikan getaran deformasi tekukan (bending) molekul secara spesifik untuk tiap jenis isomer struktur kimia.")

    with db_col_ftir:
        st.subheader("📋 Core Standard Reference Database" if language == "English" else "📋 Basis Data Referensi Standar Utama")
        exp_title = "📖 View Complete Infrared Standard Correlation Table" if language == "English" else "📖 Lihat Tabel Korelasi Standar Inframerah Lengkap"
        with st.expander(exp_title):
            if language == "English":
                df_full_ftir = pd.DataFrame(ftir_db, columns=["Vibration Type", "Min Wavenumber", "Max Wavenumber", "Chemical Group/Class"])
            else:
                df_full_ftir = pd.DataFrame(ftir_db, columns=["Jenis Getaran", "Wavenumber Minimum", "Wavenumber Maksimum", "Gugus/Kelas Kimia"])
            st.dataframe(df_full_ftir, use_container_width=True, hide_index=True)

# ==========================================
# 4. GLOBAL FOOTER SYSTEM (CLOSING INTERACTIVITY)
# ==========================================
st.divider()

# Sistem Penutup Halaman Interaktif / Web Closing Section
close_col1, close_col2 = st.columns([3, 1])
with close_col1:
    if language == "English":
        st.markdown("### 🏁 Session Completed")
        st.markdown(
            "Thank you for using **NexusNano Hub**. All calculations, multi-instrument spectrum adjustments, "
            "and active filters have been cached into the temporary laboratory session engine. Ready for safe deployment."
        )
    else:
        st.markdown("### 🏁 Sesi Selesai")
        st.markdown(
            "Terima kasih telah menggunakan **NexusNano Hub**. Seluruh kalkulasi, pencocokan spektrum multi-instrumen, "
            "dan filter aktif telah disimpan ke dalam sistem penyimpanan laboratorium sementara. Siap digunakan dengan aman."
        )

with close_col2:
    # Tombol Penutup Interaktif Konfirmasi
    if language == "English":
        st.button("Save & Exit Session", use_container_width=True, type="primary")
    else:
        st.button("Simpan & Akhiri Sesi", use_container_width=True, type="primary")

st.markdown("<p style='text-align: center; color: #94a3b8; margin-top: 30px;'>© 2024 - 2026 Lab Food Nanotechnology - Nanomaterial Property Database & Spectroscopy Integrated Hub System</p>", unsafe_allow_html=True)

