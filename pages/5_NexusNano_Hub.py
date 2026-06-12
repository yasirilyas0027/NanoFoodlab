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
# 3. SIDEBAR MULTI-MODULE NAVIGATION
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/external-flatart-icons-flat-flatarticons/128/external-nanotechnology-biotechnology-flatart-icons-flat-flatarticons.png", width=70)
    st.title("Lab Navigation Panel")
    st.markdown("Pilih modul analisis database dibawah ini:")
    menu = st.radio(
        "Modul Analisis:", 
        ["DLS Inventory & Property Analytics", "UV-Vis Nanoparticle Database", "FTIR Functional Group Analyzer"]
    )
    st.sidebar.divider()
    st.sidebar.caption("💡 **Tip:** Gunakan navigasi ini untuk mengolah data instrumen spesifik secara langsung.")

# ==========================================
# MODULE 1: DLS INVENTORY & ANALYTICS
# ==========================================
if menu == "DLS Inventory & Property Analytics":
    st.markdown('<div class="main-header">🧬 DLS Nanomaterial Inventory & Analytics</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Sistem Basis Data Canggih Eksplorasi Ukuran dan Polidispersitas Koloid</div>', unsafe_allow_html=True)
    
    df_nano = get_dls_data()

    # Dashboard Metrics
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Material", len(df_nano))
    m2.metric("Avg. Size", f"{df_nano['Size (nm)'].mean():.1f} nm")
    m3.metric("Min. Size", f"{df_nano['Size (nm)'].min():.1f} nm")
    m4.metric("Avg. PDI", f"{df_nano['PDI'].mean():.3f}")

    st.divider()

    # Filter Interaktif
    with st.expander("🔍 Filter & Search Engine Panel", expanded=True):
        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            search = st.text_input("Cari Nama Material", "")
        with f_col2:
            metode = st.multiselect("Pilih Metode Sintesis", df_nano["Metode Sintesis"].unique())
        with f_col3:
            size_range = st.slider("Rentang Ukuran (nm)", 0.0, 600.0, (0.0, 600.0))

    # Filter Logic
    filtered_df = df_nano.copy()
    if search:
        filtered_df = filtered_df[filtered_df["Material"].str.contains(search, case=False)]
    if metode:
        filtered_df = filtered_df[filtered_df["Metode Sintesis"].isin(metode)]
    filtered_df = filtered_df[(filtered_df["Size (nm)"] >= size_range[0]) & (filtered_df["Size (nm)"] <= size_range[1])]

    # Visualisasi & Tabel Master
    tab1, tab2, tab3 = st.tabs(["📊 Distribution Plot", "📈 Property Correlation", "📋 Master Database"])

    with tab1:
        st.subheader("Distribusi Ukuran Nanopartikel")
        if not filtered_df.empty:
            fig_hist = px.histogram(filtered_df, x="Size (nm)", color="Metode Sintesis", 
                                   marginal="rug", hover_data=filtered_df.columns,
                                   title="Visualisasi Frekuensi Ukuran",
                                   color_discrete_sequence=px.colors.qualitative.Bold)
            st.plotly_chart(fig_hist, use_container_width=True)
        else:
            st.info("Data tidak ditemukan untuk visualisasi grafik.")

    with tab2:
        st.subheader("Korelasi Ukuran vs Polidispersitas (PDI)")
        if not filtered_df.empty:
            fig_scatter = px.scatter(filtered_df, x="Size (nm)", y="PDI", 
                                    size="Size (nm)", color="Metode Sintesis",
                                    hover_name="Material", log_x=True,
                                    title="Mapping Kualitas Dispersi")
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.info("Data tidak ditemukan untuk visualisasi grafik.")

    with tab3:
        st.subheader("Data Registri Nanomaterial")
        st.dataframe(filtered_df, use_container_width=True, hide_index=True,
                     column_config={
                         "Size (nm)": st.column_config.NumberColumn(format="%.2f nm"),
                         "PDI": st.column_config.NumberColumn(format="%.3f"),
                         "Referensi": st.column_config.LinkColumn()
                     })

    # Stability Calculator
    st.divider()
    st.subheader("🧪 Predictive Lab Tool: Stability Estimator")
    st.info("Gunakan simulator ini untuk memprediksi kestabilan dispersi berdasarkan input DLS Anda.")

    c1, c2 = st.columns([1, 2])
    with c1:
        u_size = st.number_input("Input Size (nm)", 0.0, 1000.0, 50.0)
        u_pdi = st.number_input("Input PDI", 0.0, 1.0, 0.2)
        
    with c2:
        if u_pdi < 0.1: stability = "Sangat Monodispers (Sangat Stabil)"; color = "green"
        elif u_pdi < 0.3: stability = "Moderat (Stabil)"; color = "blue"
        else: stability = "Polidispers (Cenderung Agregasi)"; color = "orange"
        
        st.markdown(f"### Status: <span style='color:{color}'>{stability}</span>", unsafe_allow_html=True)
        st.progress(u_pdi)
        st.write(f"Partikel berukuran **{u_size} nm** dengan PDI **{u_pdi}** menunjukkan karakteristik sistem koloid yang **{stability.lower()}**.")

# ==========================================
# MODULE 2: UV-VIS NANOPARTICLE DATABASE
# ==========================================
elif menu == "UV-Vis Nanoparticle Database":
    st.markdown('<div class="main-header">🔬 UV-Vis Nanoparticle Database</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Comprehensive Literature Database for UV-Visible Spectrophotometric Characterization</div>', unsafe_allow_html=True)

    # Filter Sidebar Tambahan khusus UV-Vis
    st.sidebar.markdown("---")
    st.sidebar.header("⚙ UV-Vis Filters")
    uv_material = st.sidebar.multiselect("Material", df_uvvis["Material"].unique(), default=df_uvvis["Material"].unique())
    uv_category = st.sidebar.multiselect("Category", df_uvvis["Category"].unique(), default=df_uvvis["Category"].unique())
    uv_year = st.sidebar.slider("Publication Year", int(df_uvvis["Year"].min()), int(df_uvvis["Year"].max()), (int(df_uvvis["Year"].min()), int(df_uvvis["Year"].max())))

    # Apply Filters
    df_uv_filtered = df_uvvis[
        (df_uvvis["Material"].isin(uv_material)) & 
        (df_uvvis["Category"].isin(uv_category)) & 
        (df_uvvis["Year"] >= uv_year[0]) & (df_uvvis["Year"] <= uv_year[1])
    ]

    # Statistics Row
    st.subheader("📊 Database Statistics")
    uc1, uc2, uc3, uc4 = st.columns(4)
    uc1.metric("Literatures", len(df_uv_filtered))
    uc2.metric("Materials", df_uv_filtered["Material"].nunique())
    uc3.metric("Average λmax", f"{df_uv_filtered['Lambda_max'].mean():.1f} nm" if not df_uv_filtered.empty else "N/A")
    uc4.metric("Latest Publication", df_uv_filtered["Year"].max() if not df_uv_filtered.empty else "N/A")

    st.divider()

    # UV-Vis Real-time Interpretation Tool
    st.subheader("🧠 UV-Vis Peak Real-time Interpreter")
    peak_input_uv = st.number_input("Input λmax (nm)", min_value=200, max_value=1000, value=420)
    
    if peak_input_uv < 380:
        st.success("**Possible Interpretation:**\n\n• Metal Oxide Nanoparticle (ZnO, TiO₂, MgO)\n\n*Associated with:* Band Gap Absorption / Excitonic Transition")
    elif 380 <= peak_input_uv <= 550:
        st.success("**Possible Interpretation:**\n\n• Silver Nanoparticle (AgNP) atau Gold Nanoparticle (Small size)\n\n*Associated with:* Localized Surface Plasmon Resonance (LSPR)")
    else:
        st.success("**Possible Interpretation:**\n\n• Quantum Dots / Larger AuNP / Core-Shell Nanoparticles\n\n*Associated with:* Red-shifted SPR / Quantum Confinement Effects")

    st.divider()

    # Multiplots Grid
    g_col1, g_col2 = st.columns(2)
    with g_col1:
        st.subheader("📈 Particle Size vs λmax Mapping")
        if not df_uv_filtered.empty:
            fig_scat_uv = px.scatter(df_uv_filtered, x="Particle_Size_nm", y="Lambda_max", color="Category", size_max=15, hover_name="Material")
            fig_scat_uv.update_layout(height=350)
            st.plotly_chart(fig_scat_uv, use_container_width=True)
        else:
            st.info("No data available for plotting.")

    with g_col2:
        st.subheader("🥧 Material Composition Share")
        if not df_uv_filtered.empty:
            fig_pie_uv = px.pie(df_uv_filtered, names="Material", color_discrete_sequence=px.colors.sequential.RdBu)
            fig_pie_uv.update_layout(height=350)
            st.plotly_chart(fig_pie_uv, use_container_width=True)
        else:
            st.info("No data available for plotting.")

    # Spectra Region Multi-band Map
    st.subheader("🌈 Interactive UV-Vis Spectral Region Grid")
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
    st.subheader("📚 UV-Vis Records Reference Register")
    st.dataframe(df_uv_filtered, use_container_width=True, hide_index=True)

    # Expander Literature Details
    st.subheader("📖 Literature Deep Analysis")
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
    st.download_button("⬇ Download Filtered UV-Vis CSV Database", csv_uv, "UVVIS_DATABASE.csv", "text/csv")

    # Library Section
    st.subheader("📚 UV-Vis Spectrometry Reference Theory Library")
    topic_uv = st.selectbox("Select Spectrum Target Topic", ["SPR", "Band Gap", "Quantum Dot"])
    if topic_uv == "SPR":
        st.info("**Localized Surface Plasmon Resonance (LSPR):** Terjadi akibat osilasi kolektif elektron konduksi yang beresonansi dengan gelombang cahaya insiden. Karakteristik khas: AgNP (400–450 nm) & AuNP (520–560 nm).")
    elif topic_uv == "Band Gap":
        st.info("**Band Gap Absorption:** Terjadi perpindahan elektron dari pita valensi ke pita konduksi pada material semikonduktor oksida logam. Karakteristik khas: ZnO (320–380 nm) & TiO₂ (300–380 nm).")
    elif topic_uv == "Quantum Dot":
        st.info("**Quantum Confinement Effect:** Pergeseran optik akibat manipulasi ukuran nanometer. Semakin kecil ukuran partikel semikonduktor, rentang band gap semakin melebar sehingga spektrum menyerap ke arah panjang gelombang lebih pendek (*Blue Shift*).")

# ==========================================
# MODULE 3: FTIR FUNCTIONAL GROUP ANALYZER
# ==========================================
else:
    st.markdown('<div class="main-header">🔬 FTIR Functional Group Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-text">Automated FTIR Peak Analysis, Identification of Chemical Fingerprints & Matrix Prediction</div>', unsafe_allow_html=True)

    col_input, col_view = st.columns([1, 2])

    with col_input:
        st.subheader("FTIR Peak Input")
        peak_input = st.text_input("Enter FTIR Peaks (cm⁻¹) separated by comma", "3400,2920,1730,1630,1050")
        
    # Processing Peaks String Input safely
    try:
        peaks = [float(x.strip()) for x in peak_input.split(",") if x.strip() != ""]
    except ValueError:
        st.error("Format input salah. Mohon hanya masukkan angka dan dipisahkan tanda koma.")
        peaks = [3400, 2920, 1730, 1630, 1050]

    functional_groups = []
    for peak in peaks:
        for name, minv, maxv, group in ftir_db:
            if minv <= peak <= maxv:
                functional_groups.append([peak, name, group])

    df_ftir_result = pd.DataFrame(functional_groups, columns=["Peak (cm⁻¹)", "Vibration", "Functional Group"])

    with col_view:
        st.subheader("🧬 Spectrum Complexity Status")
        if len(peaks) < 5:
            st.success(f"✔ {len(peaks)} Peaks Detected → Likely Simple Compound Structure")
        else:
            st.warning(f"⚠ {len(peaks)} Peaks Detected → Complex Matrix Molecule Dynamic")

    st.divider()

    # Results Table Identification
    st.subheader("📊 Functional Group Identification Results")
    if not df_ftir_result.empty:
        st.dataframe(df_ftir_result, use_container_width=True, hide_index=True)
        groups = df_ftir_result["Functional Group"].tolist()
    else:
        st.info("No organic functional groups matched the input peaks in current database.")
        groups = []

    # Interpretasi Terpadu & Prediksi Material
    int_col, mat_col = st.columns(2)

    with int_col:
        st.subheader("🧠 Chemical Fingerprint Interpretation")
        interpretation = []
        if "Alcohol / Phenol" in groups: interpretation.append("Hydroxyl structural bands detected (-OH stretching).")
        if any(g in groups for g in ["Carbonyl", "Ester C=O", "Carboxylic Acid"]): interpretation.append("Carbonyl compounds detected (C=O validation).")
        if "Amide" in groups: interpretation.append("Protein backbone structure / aliphatic amide detected.")
        if "Aromatic" in groups: interpretation.append("Aromatic core ring system compound present.")
        
        if interpretation:
            for item in interpretation:
                st.write("✔", item)
        else:
            st.write("No major diagnostic chemical fingerprints interpreted.")

    with mat_col:
        st.subheader("🚀 Smart Material Prediction Matrix")
        peakset = set([round(x) for x in peaks])
        
        # Algoritma Pencocokan Material Berdasarkan Cluster Penanda Utama
        predicted = False
        if any(p in peakset for p in range(3350, 3450)) and any(p in peakset for p in range(2900, 2950)) and any(p in peakset for p in range(1000, 1100)):
            st.success("High Confidence Match: **Cellulose Matrix**")
            predicted = True
        if any(p in peakset for p in range(1720, 1740)) and any(p in peakset for p in range(2900, 2950)):
            st.success("High Confidence Match: **PLA Film (Polylactic Acid)**")
            predicted = True
        if any(p in peakset for p in range(3350, 3450)) and any(p in peakset for p in range(1620, 1640)):
            st.success("High Confidence Match: **Protein-Based Bio-nanocomposite Film**")
            predicted = True
        if any(p in peakset for p in range(3350, 3450)) and any(p in peakset for p in range(1640, 1660)) and any(p in peakset for p in range(1540, 1560)):
            st.success("High Confidence Match: **Chitosan Biocompatible Matrix**")
            predicted = True
            
        if not predicted:
            st.info("Pattern matrix did not confidently match known specific materials (Cellulose, PLA, Chitosan, etc.).")

    # Spectrum Digital Mapping Graph
    st.divider()
    st.subheader("📈 Interactive Functional Grid Mapping Layout")
    
    fig_ftir = go.Figure()
    fig_ftir.add_vrect(x0=2500, x1=4000, fillcolor="rgba(46, 204, 113, 0.1)", line_width=0, annotation_text="Single Bond Region (-OH, -CH, -NH)", annotation_position="top left")
    fig_ftir.add_vrect(x0=2000, x1=2500, fillcolor="rgba(52, 152, 219, 0.1)", line_width=0, annotation_text="Triple Bond Region (C≡C, C≡N)", annotation_position="top left")
    fig_ftir.add_vrect(x0=1500, x1=2000, fillcolor="rgba(155, 89, 182, 0.1)", line_width=0, annotation_text="Double Bond Region (C=O, C=C)", annotation_position="top left")
    fig_ftir.add_vrect(x0=500,  x1=1500, fillcolor="rgba(230, 126, 34, 0.1)", line_width=0, annotation_text="Fingerprint Region", annotation_position="top left")

    # Plot Current Input Peaks Line
    fig_ftir.add_trace(go.Scatter(
        x=peaks, y=[1] * len(peaks), mode="markers+text",
        text=[f"{p} cm⁻¹" for p in peaks], textposition="top center",
        marker=dict(size=12, color="crimson", symbol="diamond"), name="Your Detected Peaks"
    ))

    fig_ftir.update_layout(
        xaxis=dict(title="Wavenumber (cm⁻¹)", range=[4000, 500]), # Spektrum FTIR diplot terbalik (standar kimia)
        yaxis=dict(showticklabels=False, range=[0, 2]),
        height=300, margin=dict(t=30, b=30, l=20, r=20), showlegend=False
    )
    st.plotly_chart(fig_ftir, use_container_width=True)

    # Reference Database Expander & Theory Block
    st.divider()
    lib_col_ftir, db_col_ftir = st.columns(2)

    with lib_col_ftir:
        st.subheader("📚 FTIR Theory Quick Guide")
        topic_ftir = st.selectbox("Select Target Library Topic", ["Carbonyl", "O-H", "N-H", "Amide", "Aromatic", "Fingerprint Region"])
        if topic_ftir == "Carbonyl":
            st.info("Sharp band intense antara **1750–1700 cm⁻¹**. Karakteristik gugus ester, keton, aldehid, maupun asam karboksilat pada material polimer seperti **PLA**.")
        elif topic_ftir == "O-H":
            st.info("Pita lebar (broad band) sangat kuat di rentang **3550–3200 cm⁻¹** akibat ikatan hidrogen inter-molekul. Sangat intens pada **selulosa, pati, dan matriks polisakarida**.")
        elif topic_ftir == "N-H":
            st.info("Stretching amin primer/sekunder di daerah **3550–3250 cm⁻¹**. Esensial mendeteksi fungsionalisasi gugus nitrogen pada modifikasi kimia **kitosan**.")
        elif topic_ftir == "Amide":
            st.info("Menunjukkan puncak tajam Amida I (~1650 cm⁻¹) dan Amida II (~1550 cm⁻¹). Digunakan secara luas untuk memetakan gugus fungsional protein nanostruktur.")
        elif topic_ftir == "Aromatic":
            st.info("Peregangan cincin karbon C=C aromatik yang tajam di daerah **1615–1495 cm⁻¹**, mendeteksi senyawa fenolik atau ligan penudung nanopartikel.")
        elif topic_ftir == "Fingerprint Region":
            st.info("Daerah khas di bawah **1500–500 cm⁻¹** yang merefleksikan getaran deformasi tekukan (bending) molekul secara spesifik untuk tiap jenis isomer struktur kimia.")

    with db_col_ftir:
        st.subheader("📋 Core Standard Reference Database")
        with st.expander("📖 View Complete Infrared Standard Correlation Table"):
            df_full_ftir = pd.DataFrame(ftir_db, columns=["Vibration Type", "Min Wavenumber", "Max Wavenumber", "Chemical Group/Class"])
            st.dataframe(df_full_ftir, use_container_width=True, hide_index=True)

# ==========================================
# 4. GLOBAL FOOTER SYSTEM
# ==========================================
st.divider()
st.markdown("<p style='text-align: center; color: #94a3b8;'>© 2024 - 2026 Lab Food Nanotechnology - Nanomaterial Property Database & Spectroscopy Integrated Hub System</p>", unsafe_allow_html=True)

