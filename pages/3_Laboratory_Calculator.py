import streamlit as st
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

st.set_page_config(
    page_title="Laboratory Calculator",
    layout="wide"
)

st.title("NanoFood Laboratory Calculator Suite")

st.markdown("""
Integrated laboratory calculation system for
Food Nanotechnology.
""")

language = st.radio(
    "🌐 Language",
    ["English", "Indonesia"],
    horizontal=True
)

if "category" not in st.session_state:
    st.session_state.category = None

if "calculator" not in st.session_state:
    st.session_state.calculator = None

st.header("Select Category" if language == "English" else "Pilih Kategori")
col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

with col1:
    if st.button("Basic Chemistry" if language == "English" else "Kimia Dasar"):
        st.session_state.category = "basic"

with col2:
    if st.button("Nano Synthesis" if language == "English" else "Sintesis Nano"):
        st.session_state.category = "synthesis"

with col3:
    if st.button("Characterization" if language == "English" else "Karakterisasi"):
        st.session_state.category = "characterization"

with col4:
    if st.button("Food Packaging" if language == "English" else "Kemasan Pangan"):
        st.session_state.category = "packaging"

with col5:
    if st.button("Microbiology" if language == "English" else "Mikrobiologi"):
        st.session_state.category = "microbiology"

with col6:
    if st.button("Bioactivity" if language == "English" else "Bioaktivitas"):
        st.session_state.category = "bioactivity"

with col7:
    if st.button("Analytical Chemistry" if language == "English" else "Kimia Analitik"):
        st.session_state.category = "analytical"

if st.session_state.category == "basic":
    st.subheader("Basic Chemistry Calculators" if language == "English" else "Kalkulator Kimia Dasar")
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        if st.button("Dilution Calculator" if language == "English" else "Kalkulator Pengenceran"):
            st.session_state.calculator="dilution"
    with c2:
        if st.button("PPM Calculator" if language == "English" else "Kalkulator PPM"):
            st.session_state.calculator="ppm"
    with c3:
        if st.button("Molarity Calculator" if language == "English" else "Kalkulator Molaritas"):
            st.session_state.calculator="molarity"
    with c4:
        if st.button("Density Calculator" if language == "English" else "Kalkulator Densitas"):
            st.session_state.calculator="density"

if st.session_state.calculator == "dilution":
    st.header("Dilution Calculator" if language == "English" else "Kalkulator Pengenceran")
    if language == "English":
        st.markdown("""
        ### Dilution Principle
        Dilution is the process of reducing the concentration of a solution by adding solvent while keeping the amount of solute (number of moles) constant.
        ### Formula
        C₁V₁ = C₂V₂
        ### Where
        - C₁ = Initial concentration
        - V₁ = Initial volume
        - C₂ = Final concentration
        - V₂ = Final volume
        ### Applications
        - Nanoparticle suspension preparation
        - Standard solution preparation
        - UV–Vis sample preparation
        - Food additive formulation
        ### Scientific Note
        The dilution equation assumes that no chemical reaction occurs during dilution and that the amount of solute remains constant.
        """)
    else:
        st.markdown("""
        ### Prinsip Pengenceran
        Pengenceran adalah proses menurunkan konsentrasi suatu larutan dengan menambahkan pelarut, sementara jumlah zat terlarut (jumlah mol) tetap konstan.
        ### Rumus
        C₁V₁ = C₂V₂
        ### Keterangan
        - C₁ = Konsentrasi awal
        - V₁ = Volume awal
        - C₂ = Konsentrasi akhir
        - V₂ = Volume akhir
        ### Aplikasi
        - Preparasi suspensi nanopartikel
        - Pembuatan larutan standar
        - Preparasi sampel untuk UV-Vis
        - Formulasi bahan tambahan pangan
        ### Catatan Ilmiah
        Persamaan pengenceran mengasumsikan bahwa tidak ada reaksi kimia yang terjadi selama pengenceran dan jumlah zat terlarut tetap konstan.
        """)

    st.latex(r"C_1V_1=C_2V_2")
    c1 = st.number_input("Initial Concentration (C₁)" if language == "English" else "Konsentrasi Awal (C₁)", min_value=0.0)
    v1 = st.number_input("Initial Volume (V₁, mL)" if language == "English" else "Volume Awal (V₁, mL)", min_value=0.0)
    c2 = st.number_input("Final Concentration (C₂)" if language == "English" else "Konsentrasi Akhir (C₂)", min_value=0.0)

    if st.button("Calculate Dilution" if language == "English" else "Hitung Pengenceran", key="dilution_btn"):
        if c2 <= 0:
            st.error("Final concentration must be greater than zero." if language == "English" else "Konsentrasi akhir harus lebih besar dari nol.")
        else:
            v2 = (c1 * v1) / c2
            st.success(f"Final Volume (V₂) = {v2:.2f} mL" if language == "English" else f"Volume Akhir (V₂) = {v2:.2f} mL")

if st.session_state.calculator == "ppm":
    st.header("PPM Calculator" if language == "English" else "Kalkulator PPM")
    if language == "English":
        st.markdown("""
        ### Parts Per Million (PPM)
        PPM is a concentration unit that expresses the amount of a substance per one million parts of a solution.
        ### Formula
        For dilute aqueous solutions:
        PPM ≈ Mass (mg) / Volume (L)
        ### Applications
        - Heavy metal analysis
        - Food contaminant analysis
        - Nanoparticle concentration determination
        - Water quality testing
        ### Interpretation
        1 ppm ≈ 1 mg/L (for dilute aqueous solutions where the density is approximately 1 kg/L)
        ### Scientific Note
        The equivalence between ppm and mg/L is generally valid only for dilute aqueous solutions.
        """)
    else:
        st.markdown("""
        ### Parts Per Million (PPM)
        PPM adalah unit konsentrasi yang menyatakan jumlah zat per satu juta bagian larutan.
        ### Rumus
        Untuk larutan berair yang encer:
        PPM ≈ Massa (mg) / Volume (L)
        ### Aplikasi
        - Analisis logam berat
        - Analisis kontaminan pangan
        - Penentuan konsentrasi nanopartikel
        - Pengujian kualitas air
        ### Interpretasi
        1 ppm ≈ 1 mg/L (untuk larutan encer di mana densitasnya mendekati 1 kg/L)
        ### Catatan Ilmiah
        Kesetaraan antara ppm dan mg/L umumnya hanya berlaku untuk larutan berair yang encer.
        """)

    mass = st.number_input("Mass (mg)" if language == "English" else "Massa (mg)", min_value=0.0)
    volume = st.number_input("Volume (L)" if language == "English" else "Volume (L)", min_value=0.0)

    if st.button("Calculate PPM" if language == "English" else "Hitung PPM", key="ppm_btn"):
        if volume <= 0:
            st.error("Volume must be greater than zero." if language == "English" else "Volume harus lebih besar dari nol.")
        else:
            ppm = mass / volume
            st.success(f"Concentration = {ppm:.2f} ppm" if language == "English" else f"Konsentrasi = {ppm:.2f} ppm")

if st.session_state.calculator == "molarity":
    st.header("Molarity Calculator" if language == "English" else "Kalkulator Molaritas")
    if language == "English":
        st.markdown("""
        ### Molarity
        Molarity represents the number of moles of solute per liter of solution.
        ### Formula
        M = n / V
        ### Where
        n = mass / molar mass
        ### Unit
        mol/L (M)
        ### Applications
        - Chemical synthesis
        - Nanomaterial preparation
        - Reaction stoichiometry calculations
        - Laboratory solution formulation
        ### Scientific Note
        Molarity depends on the total volume of the solution and may vary with temperature due to volume changes.
        """)
    else:
        st.markdown("""
        ### Molaritas
        Molaritas menyatakan jumlah mol zat terlarut per liter larutan.
        ### Rumus
        M = n / V
        ### Keterangan
        n = massa / massa molar (berat molekul)
        ### Satuan
        mol/L (M)
        ### Aplikasi
        - Sintesis kimia
        - Preparasi nanomaterial
        - Perhitungan stoikiometri reaksi
        - Formulasi larutan laboratorium
        ### Catatan Ilmiah
        Molaritas bergantung pada volume total larutan dan dapat bervariasi mengikuti suhu karena adanya perubahan volume.
        """)

    mass = st.number_input("Mass (g)" if language == "English" else "Massa (g)", min_value=0.0, key="mol_mass")
    molar_mass = st.number_input("Molar Mass (g/mol)" if language == "English" else "Massa Molar (g/mol)", min_value=0.0, key="mol_mw")
    volume = st.number_input("Volume (L)" if language == "English" else "Volume (L)", min_value=0.0, key="mol_vol")

    if st.button("Calculate Molarity" if language == "English" else "Hitung Molaritas", key="molarity_btn"):
        if molar_mass <= 0:
            st.error("Molar mass must be greater than zero." if language == "English" else "Massa molar harus lebih besar dari nol.")
        elif volume <= 0:
            st.error("Volume must be greater than zero." if language == "English" else "Volume harus lebih besar dari nol.")
        else:
            molarity = (mass / molar_mass) / volume
            st.success(f"Molarity = {molarity:.4f} M" if language == "English" else f"Molaritas = {molarity:.4f} M")

if st.session_state.calculator == "density":
    st.header("Density Calculator" if language == "English" else "Kalkulator Densitas")
    if language == "English":
        st.markdown("""
        ### Density
        Density is the mass of a substance per unit volume.
        ### Formula
        ρ = m / V
        ### Units
        - g/mL
        - kg/L
        - g/cm³
        ### Applications
        - Polymer films
        - Nanoemulsions
        - Nanocomposites
        - Food packaging materials
        ### Scientific Note
        Density is a fundamental physical property commonly used for material characterization and quality control.
        """)
    else:
        st.markdown("""
        ### Densitas (Massa Jenis)
        Densitas adalah massa suatu zat per satuan volume.
        ### Rumus
        ρ = m / V
        ### Satuan
        - g/mL
        - kg/L
        - g/cm³
        ### Aplikasi
        - Film polimer
        - Nanoemulsi
        - Nanokomposit
        - Material kemasan pangan
        ### Catatan Ilmiah
        Densitas adalah sifat fisik fundamental yang umum digunakan untuk karakterisasi material dan kendali mutu (quality control).
        """)

    mass = st.number_input("Mass (g)" if language == "English" else "Massa (g)", min_value=0.0, key="dens_mass")
    volume = st.number_input("Volume (mL)" if language == "English" else "Volume (mL)", min_value=0.0, key="dens_vol")

    if st.button("Calculate Density" if language == "English" else "Hitung Densitas", key="density_btn"):
        if volume <= 0:
            st.error("Volume must be greater than zero." if language == "English" else "Volume harus lebih besar dari nol.")
        else:
            density = mass / volume
            st.success(f"Density = {density:.4f} g/mL" if language == "English" else f"Densitas = {density:.4f} g/mL")
            if density < 1:
                st.info("Less dense than water." if language == "English" else "Lebih ringan/kurang padat daripada air.")
            elif density > 1:
                st.info("More dense than water." if language == "English" else "Lebih padat daripada air.")
            else:
                st.info("Density is approximately equal to water." if language == "English" else "Densitas kiranya setara dengan air.")

if st.session_state.category=="synthesis":
    st.subheader("Nanomaterial Synthesis" if language == "English" else "Sintesis Nanomaterial")
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        if st.button("Yield Calculator" if language == "English" else "Kalkulator Rendemen"):
            st.session_state.calculator="yield"
    with c2:
        if st.button("Recovery Calculator" if language == "English" else "Kalkulator Recovery"):
            st.session_state.calculator="recovery"
    with c3:
        if st.button("Encapsulation Efficiency" if language == "English" else "Efisiensi Enkapsulasi"):
            st.session_state.calculator="ee"
    with c4:
        if st.button("Loading Capacity" if language == "English" else "Kapasitas Pemuatan"):
            st.session_state.calculator="lc"
            
if st.session_state.calculator=="yield":
    st.header("Yield Calculator" if language == "English" else "Kalkulator Rendemen")
    if language == "English":
        st.markdown("""
        ### Percent Yield
        Percent yield indicates the efficiency of a synthesis or production process by comparing the actual amount of product obtained with the theoretical amount expected.
        ### Formula
        Percent Yield (%) = (Actual Yield / Theoretical Yield) × 100
        ### Applications
        - Nanoparticle synthesis
        - Polymer synthesis
        - Extraction processes
        - Material production
        ### Interpretation
        Higher percent yield generally indicates a more efficient process.
        ### Scientific Note
        Percent yield may be influenced by side reactions, material losses during processing, purification steps, and experimental conditions.
        """)
    else:
        st.markdown("""
        ### Persentase Rendemen (Percent Yield)
        Persentase rendemen menunjukkan efisiensi suatu proses sintesis atau produksi dengan membandingkan jumlah produk aktual yang diperoleh terhadap jumlah produk teoritis yang diharapkan.
        ### Rumus
        Persentase Rendemen (%) = (Produk Aktual / Produk Teoritis) × 100
        ### Aplikasi
        - Sintesis nanopartikel
        - Sintesis polimer
        - Proses ekstraksi
        - Produksi material
        ### Interpretasi
        Nilai rendemen yang lebih tinggi umumnya menunjukkan proses yang lebih efisien.
        ### Catatan Ilmiah
        Persentase rendemen dapat dipengaruhi oleh reaksi samping, kehilangan material selama proses, tahapan pemurnian, dan kondisi eksperimen.
        """)
        
    actual_yield = st.number_input("Actual Yield" if language == "English" else "Produk Aktual", min_value=0.0, key="actual_yield")
    theoretical_yield = st.number_input("Theoretical Yield" if language == "English" else "Produk Teoritis", min_value=0.0, key="theoretical_yield")

    if st.button("Calculate Yield" if language == "English" else "Hitung Rendemen", key="yield_btn"):
        if theoretical_yield <= 0:
            st.error("Theoretical Yield must be greater than zero." if language == "English" else "Produk teoritis harus lebih besar dari nol.")
        else:
            yield_percent = (actual_yield / theoretical_yield) * 100
            st.success(f"Percent Yield = {yield_percent:.2f}%" if language == "English" else f"Persentase Rendemen = {yield_percent:.2f}%")
            if yield_percent > 100:
                st.warning("Yield exceeds 100%. Verify experimental data and purity of the product." if language == "English" else "Rendemen melebihi 100%. Verifikasi kembali data eksperimen dan kemurnian produk.")
            elif yield_percent >= 80:
                st.info("High synthesis efficiency." if language == "English" else "Efisiensi sintesis tinggi.")
            elif yield_percent >= 50:
                st.info("Moderate synthesis efficiency." if language == "English" else "Efisiensi sintesis sedang.")
            else:
                st.info("Low synthesis efficiency." if language == "English" else "Efisiensi sintesis rendah.")
            
if st.session_state.calculator=="recovery":
    st.header("Recovery Calculator" if language == "English" else "Kalkulator Recovery")
    if language == "English":
        st.markdown("""
        ### Recovery Percentage
        Recovery percentage indicates the proportion of material recovered relative to the original amount.
        ### Formula
        Recovery (%) = (Recovered Amount / Initial Amount) × 100
        ### Applications
        - Extraction processes
        - Adsorption studies
        - Nanomaterial purification
        - Bioactive compound recovery
        ### Interpretation
        Higher recovery values indicate more effective material retrieval.
        ### Scientific Note
        Recovery may be expressed using mass, concentration, or total amount depending on the analytical method employed.
        """)
    else:
        st.markdown("""
        ### Persentase Recovery (Perolehan Kembali)
        Persentase recovery menunjukkan proporsi material yang berhasil diperoleh kembali dibandingkan dengan jumlah awal material tersebut.
        ### Rumus
        Recovery (%) = (Jumlah yang Direcovery / Jumlah Awal) × 100
        ### Aplikasi
        - Proses ekstraksi
        - Studi adsorpsi
        - Pemurnian nanomaterial
        - Recovery senyawa bioaktif
        ### Interpretasi
        Nilai recovery yang lebih tinggi menunjukkan proses pemulihan material yang lebih efektif.
        ### Catatan Ilmiah
        Recovery dapat dinyatakan berdasarkan massa, konsentrasi, maupun jumlah total zat tergantung pada metode analisis yang digunakan.
        """)

    initial_amount = st.number_input("Initial Amount" if language == "English" else "Jumlah Awal", min_value=0.0, key="initial_amount")
    recovered_amount = st.number_input("Recovered Amount" if language == "English" else "Jumlah yang Direcovery", min_value=0.0, key="recovered_amount")

    if st.button("Calculate Recovery" if language == "English" else "Hitung Recovery", key="recovery_btn"):
        if initial_amount <= 0:
            st.error("Initial Amount must be greater than zero." if language == "English" else "Jumlah awal harus lebih besar dari nol.")
        else:
            recovery = (recovered_amount / initial_amount) * 100
            st.success(f"Recovery = {recovery:.2f}%")
            if recovery > 100:
                st.warning("Recovery exceeds 100%. Check analytical measurements." if language == "English" else "Recovery melebihi 100%. Periksa kembali pengukuran analitik Anda.")
            elif recovery >= 80:
                st.info("High recovery efficiency." if language == "English" else "Efisiensi recovery tinggi.")
            elif recovery >= 50:
                st.info("Moderate recovery efficiency." if language == "English" else "Efisiensi recovery sedang.")
            else:
                st.info("Low recovery efficiency." if language == "English" else "Efisiensi recovery rendah.")

if st.session_state.calculator=="ee":
    st.header("Encapsulation Efficiency" if language == "English" else "Efisiensi Enkapsulasi")
    if language == "English":
        st.markdown("""
        ### Encapsulation Efficiency
        Encapsulation efficiency measures the percentage of active compounds successfully entrapped within a carrier system.
        ### Formula
        EE (%) = [(Total Compound − Free Compound) / Total Compound] × 100
        ### Applications
        - Nanoemulsions
        - Liposomes
        - Nanoencapsulation systems
        - Active food packaging
        - Drug delivery systems
        ### Interpretation
        Higher EE values indicate more effective encapsulation.
        ### Scientific Note
        Encapsulation efficiency is affected by formulation composition, carrier properties, preparation method, and interactions between the active compound and the encapsulating material.
        """)
    else:
        st.markdown("""
        ### Efisiensi Enkapsulasi (Encapsulation Efficiency)
        Efisiensi enkapsulasi menunjukkan persentase senyawa aktif yang berhasil terperangkap di dalam sistem pembawa (carrier system).
        ### Rumus
        EE (%) = [(Senyawa Total − Senyawa Bebas) / Senyawa Total] × 100
        ### Aplikasi
        - Nanoemulsi
        - Liposom
        - Sistem nanoenkapsulasi
        - Kemasan pangan aktif
        - Sistem penghantaran obat
        ### Interpretasi
        Nilai EE yang lebih tinggi menunjukkan proses enkapsulasi yang lebih efektif.
        ### Catatan Ilmiah
        Efisiensi enkapsulasi dipengaruhi oleh komposisi formulasi, sifat material pembawa, metode preparasi, serta interaksi antara senyawa aktif dan bahan enkapsulan.
        """)

    total_compound = st.number_input("Total Compound" if language == "English" else "Senyawa Total", min_value=0.0, key="total_compound")
    free_compound = st.number_input("Free Compound" if language == "English" else "Senyawa Bebas (Tidak Terikat)", min_value=0.0, key="free_compound")

    if st.button("Calculate EE" if language == "English" else "Hitung EE", key="ee_btn"):
        if total_compound <= 0:
            st.error("Total Compound must be greater than zero." if language == "English" else "Senyawa total harus lebih besar dari nol.")
        elif free_compound > total_compound:
            st.error("Free Compound cannot exceed Total Compound." if language == "English" else "Senyawa bebas tidak boleh melebihi senyawa total.")
        else:
            ee = ((total_compound - free_compound) / total_compound) * 100
            st.success(f"Encapsulation Efficiency = {ee:.2f}%" if language == "English" else f"Efisiensi Enkapsulasi = {ee:.2f}%")
            if ee >= 80:
                st.info("High encapsulation efficiency." if language == "English" else "Efisiensi enkapsulasi tinggi.")
            elif ee >= 50:
                st.info("Moderate encapsulation efficiency." if language == "English" else "Efisiensi enkapsulasi sedang.")
            else:
                st.info("Low encapsulation efficiency." if language == "English" else "Efisiensi enkapsulasi rendah.")

if st.session_state.calculator=="lc":
    st.header("Loading Capacity Calculator" if language == "English" else "Kalkulator Loading Capacity")
    if language == "English":
        st.markdown("""
        ### Loading Capacity (LC)
        Loading Capacity describes the amount of active compound successfully loaded into a carrier material relative to the mass of the carrier.
        ### Formula
        LC (%) = (Encapsulated Compound / Carrier Mass) × 100
        ### Where
        - Encapsulated Compound = Mass of active compound retained in the carrier
        - Carrier Mass = Total mass of carrier material
        ### Applications
        - Nanoencapsulation systems
        - Liposomes
        - Chitosan nanoparticles
        - Nanoemulsions
        - Active food packaging
        ### Interpretation
        Higher LC values indicate that more active compound is incorporated per unit mass of carrier.
        ### Scientific Note
        Loading Capacity is commonly reported together with Encapsulation Efficiency (EE). While EE evaluates the effectiveness of entrapment, LC evaluates how much active compound is loaded into the carrier system.
        """)
    else:
        st.markdown("""
        ### Loading Capacity (LC / Kapasitas Pemuatan)
        Loading Capacity menunjukkan jumlah senyawa aktif yang berhasil dimuat ke dalam material pembawa dibandingkan dengan massa material pembawa tersebut.
        ### Rumus
        LC (%) = (Massa Senyawa Terenkapsulasi / Massa Carrier) × 100
        ### Keterangan
        - Massa Senyawa Terenkapsulasi = jumlah senyawa aktif yang tertahan dalam carrier
        - Massa Carrier = massa total material pembawa
        ### Aplikasi
        - Sistem nanoenkapsulasi
        - Liposom
        - Nanopartikel kitosan
        - Nanoemulsi
        - Kemasan pangan aktif
        ### Interpretasi
        Nilai LC yang lebih tinggi menunjukkan bahwa lebih banyak senyawa aktif berhasil dimuat ke dalam carrier.
        ### Catatan Ilmiah
        Loading Capacity biasanya dilaporkan bersama Encapsulation Efficiency (EE). EE menunjukkan efisiensi proses enkapsulasi, sedangkan LC menunjukkan seberapa banyak muatan senyawa aktif yang sanggup ditampung oleh sistem pembawa.
        """)

    encapsulated_compound = st.number_input("Encapsulated Compound Mass (mg)" if language == "English" else "Massa Senyawa Terenkapsulasi (mg)", min_value=0.0, key="lc_compound")
    carrier_mass = st.number_input("Carrier Mass (mg)" if language == "English" else "Massa Pembawa / Carrier (mg)", min_value=0.0, key="lc_carrier")

    if st.button("Calculate Loading Capacity" if language == "English" else "Hitung Loading Capacity", key="lc_btn"):
        if carrier_mass <= 0:
            st.error("Carrier mass must be greater than zero." if language == "English" else "Massa carrier harus lebih besar dari nol.")
        else:
            lc = (encapsulated_compound / carrier_mass) * 100
            st.success(f"Loading Capacity = {lc:.2f}%" if language == "English" else f"Kapasitas Pemuatan = {lc:.2f}%")
            if lc >= 50:
                st.success("Very High Loading Capacity" if language == "English" else "Kapasitas Pemuatan Sangat Tinggi")
            elif lc >= 25:
                st.info("Moderate Loading Capacity" if language == "English" else "Kapasitas Pemuatan Sedang")
            elif lc >= 10:
                st.warning("Low Loading Capacity" if language == "English" else "Kapasitas Pemuatan Rendah")
            else:
                st.error("Very Low Loading Capacity" if language == "English" else "Kapasitas Pemuatan Sangat Rendah")
            st.caption("Loading Capacity indicates the amount of active compound incorporated per unit mass of carrier material." if language == "English" else "Loading Capacity mengindikasikan jumlah senyawa aktif yang tergabung per unit massa material pembawa.")

if st.session_state.category=="characterization":
    st.subheader("Characterization Calculators" if language == "English" else "Kalkulator Karakterisasi")
    c1,c2,c3,c4,c5 = st.columns(5)
    with c1:
        if st.button("Scherrer Calculator"):
            st.session_state.calculator="scherrer"
    with c2:
        if st.button("Corrected Scherrer"):
            st.session_state.calculator="corrected_scherrer"
    with c3:
        if st.button("d-Spacing"):
            st.session_state.calculator="dspacing"
    with c4:
        if st.button("PDI Interpreter"):
            st.session_state.calculator="pdi"
    with c5:
        if st.button("Zeta Potential"):
            st.session_state.calculator="zeta"

if st.session_state.calculator=="scherrer":
    st.header("Scherrer Equation Calculator" if language == "English" else "Kalkulator Persamaan Scherrer")
    if language == "English":
        st.markdown("""
        ### Scherrer Equation
        The Scherrer equation is used to estimate crystallite size from X-ray diffraction (XRD) peak broadening.
        ### Formula
        D = Kλ / βcosθ
        ### Where
        - D = Crystallite size (nm)
        - K = Shape factor
        - λ = X-ray wavelength (nm)
        - β = Full Width at Half Maximum (FWHM) in radians
        - θ = Bragg angle in radians
        ### Applications
        - ZnO, TiO₂, Silver, Silica nanoparticles
        - Nanocomposite materials
        ### Instrumental Broadening Correction
        Experimental peak broadening contains contributions from both the sample and the instrument. Corrected peak broadening is calculated as:
        β = √(βobs² − βinst²)
        ### Scientific Note
        Instrumental broadening correction is recommended for accurate crystallite size estimation in XRD analysis.
        """)
    else:
        st.markdown("""
        ### Persamaan Scherrer
        Persamaan Scherrer digunakan untuk mengestimasi ukuran kristal (crystallite size) dari pelebaran puncak difraksi sinar-X (XRD).
        ### Rumus
        D = Kλ / βcosθ
        ### Keterangan
        - D = Ukuran kristal (nm)
        - K = Faktor bentuk (shape factor)
        - λ = Panjang gelombang sinar-X (nm)
        - β = Full Width at Half Maximum (FWHM) dalam satuan radian
        - θ = Sudut Bragg dalam satuan radian
        ### Aplikasi
        - Nanopartikel ZnO, TiO₂, Perak (Ag), Silika
        - Material nanokomposit
        ### Koreksi Pelebaran Instrumental
        Pelebaran puncak eksperimental mengandung kontribusi dari sampel dan instrumen. Pelebaran puncak terkoreksi dihitung sebagai:
        β = √(βobs² − βinst²)
        ### Catatan Ilmiah
        Koreksi pelebaran instrumental sangat disarankan untuk estimasi ukuran kristal yang akurat pada analisis XRD.
        """)

    k = st.number_input("Shape Factor (K)", min_value=0.1, value=0.9, key="scherrer_k")
    lam = st.number_input("X-ray Wavelength λ (nm)", min_value=0.0001, value=0.15406, key="scherrer_lambda")
    beta = st.number_input("FWHM β (degrees)" if language == "English" else "FWHM β (derajat)", min_value=0.0, key="scherrer_beta")
    theta = st.number_input("Bragg Angle θ (degrees)" if language == "English" else "Sudut Bragg θ (derajat)", min_value=0.0, key="scherrer_theta")

    if st.button("Calculate Crystallite Size" if language == "English" else "Hitung Ukuran Kristal", key="scherrer_btn"):
        if beta <= 0:
            st.error("FWHM β must be greater than zero." if language == "English" else "FWHM β harus lebih besar dari nol.")
        else:
            beta_rad = math.radians(beta)
            theta_rad = math.radians(theta)
            d = (k * lam) / (beta_rad * math.cos(theta_rad))
            st.success(f"Crystallite Size = {d:.2f} nm" if language == "English" else f"Ukuran Kristal = {d:.2f} nm")
            if d < 100:
                st.info("Crystallite size falls within the nanocrystalline range." if language == "English" else "Ukuran kristal masuk dalam rentang nanokristalin.")
            else:
                st.info("Crystallite size is above the conventional nanocrystalline range." if language == "English" else "Ukuran kristal berada di atas rentang nanokristalin konvensional.")
            st.caption("The Scherrer equation provides an approximate crystallite size and does not directly represent particle size." if language == "English" else "Persamaan Scherrer memberikan perkiraan ukuran kristal dan tidak merepresentasikan ukuran partikel secara langsung.")

if st.session_state.calculator=="corrected_scherrer":
    st.header("Instrument Corrected Scherrer Calculator" if language == "English" else "Kalkulator Scherrer Terkoreksi Instrumen")
    if language == "English":
        st.markdown("""
        ### Instrument Corrected Scherrer Equation
        Experimental peak broadening contains contributions from both the sample and the instrument. Therefore instrumental broadening correction is recommended before crystallite size calculation.
        ### Step 1: Corrected FWHM
        β = √(βobs² − βinst²)
        ### Step 2: Scherrer Equation
        D = Kλ / βcosθ
        """)
    else:
        st.markdown("""
        ### Persamaan Scherrer Terkoreksi Instrumen
        Pelebaran puncak yang terukur pada alat XRD mengandung kontribusi dari sampel sekaligus dari instrumen itu sendiri. Oleh karena itu, koreksi instrumental sangat direkomendasikan sebelum menghitung ukuran kristal.
        ### Langkah 1: FWHM Terkoreksi
        β = √(βobs² − βinst²)
        ### Langkah 2: Persamaan Scherrer
        D = Kλ / βcosθ
        """)

    k = st.number_input("Shape Factor (K)", min_value=0.1, value=0.9)
    wavelength = st.number_input("X-ray Wavelength λ (nm)", min_value=0.0001, value=0.15406)
    beta_obs = st.number_input("Observed FWHM βobs (degrees)" if language == "English" else "FWHM Teramati βobs (derajat)", min_value=0.0)
    beta_inst = st.number_input("Instrumental FWHM βinst (degrees)" if language == "English" else "FWHM Instrumen βinst (derajat)", min_value=0.0)
    theta = st.number_input("Bragg Angle θ (degrees)" if language == "English" else "Sudut Bragg θ (derajat)", min_value=0.0)

    if st.button("Calculate Corrected Scherrer" if language == "English" else "Hitung Scherrer Terkoreksi"):
        if beta_obs <= beta_inst:
            st.error("Observed FWHM must be greater than Instrumental FWHM." if language == "English" else "FWHM teramati harus lebih besar dari FWHM instrumen.")
        else:
            beta_corr_deg = math.sqrt(beta_obs**2 - beta_inst**2)
            beta_corr_rad = math.radians(beta_corr_deg)
            theta_rad = math.radians(theta)
            d = (k * wavelength) / (beta_corr_rad * math.cos(theta_rad))
            st.success(f"Corrected FWHM = {beta_corr_deg:.4f}°" if language == "English" else f"FWHM Terkoreksi = {beta_corr_deg:.4f}°")
            st.success(f"Crystallite Size = {d:.2f} nm" if language == "English" else f"Ukuran Kristal = {d:.2f} nm")

if st.session_state.calculator=="dspacing":
    st.header("Bragg d-Spacing Calculator" if language == "English" else "Kalkulator d-Spacing Bragg")
    if language == "English":
        st.markdown("""
        ### Bragg's Law
        Bragg's Law relates diffraction angle and crystal lattice spacing.
        nλ = 2d sinθ (For most XRD analyses, n = 1, so d = λ / (2 sinθ))
        ### Where
        - d = Interplanar spacing (nm)
        - λ = X-ray wavelength (nm)
        - θ = Bragg angle
        """)
    else:
        st.markdown("""
        ### Hukum Bragg
        Hukum Bragg menghubungkan antara sudut difraksi dengan jarak antar bidang kisi kristal (lattice spacing).
        nλ = 2d sinθ (Untuk analisis XRD standar, n = 1, sehingga d = λ / (2 sinθ))
        ### Keterangan
        - d = Jarak antar bidang / d-spacing (nm)
        - λ = Panjang gelombang sinar-X (nm)
        - θ = Sudut Bragg
        """)

    wavelength = st.number_input("X-ray Wavelength λ (nm)", min_value=0.0001, value=0.15406, key="d_lambda")
    two_theta = st.number_input("2θ (degrees)" if language == "English" else "2θ (derajat)", min_value=0.0, key="d_2theta")

    if st.button("Calculate d-Spacing" if language == "English" else "Hitung d-Spacing"):
        if two_theta <= 0:
            st.error("2θ must be greater than zero." if language == "English" else "Nilai 2θ harus lebih besar dari nol.")
        else:
            theta = two_theta / 2
            theta_rad = math.radians(theta)
            d = wavelength / (2 * math.sin(theta_rad))
            st.success(f"d-Spacing = {d:.4f} nm")
            st.success(f"d-Spacing = {d*10:.4f} Å")

if st.session_state.calculator=="pdi":
    st.header("Polydispersity Index (PDI) Interpreter" if language == "English" else "Interpreter Indeks Polidispersitas (PDI)")
    if language == "English":
        st.markdown("""
        ### Polydispersity Index (PDI)
        PDI describes the width of particle size distribution measured by Dynamic Light Scattering (DLS). Lower PDI values indicate a narrower and more uniform particle size distribution.
        """)
    else:
        st.markdown("""
        ### Indeks Polidispersitas (Polydispersity Index - PDI)
        PDI menggambarkan lebar distribusi ukuran partikel yang diukur menggunakan Dynamic Light Scattering (DLS). Nilai PDI yang lebih rendah menunjukkan distribusi ukuran partikel yang lebih sempit dan seragam (monodispers).
        """)

    pdi = st.number_input("PDI Value" if language == "English" else "Nilai PDI", min_value=0.0, max_value=1.0, value=0.20)
    if st.button("Interpret PDI" if language == "English" else "Interpretasikan PDI"):
        st.metric("PDI", f"{pdi:.3f}")
        if pdi < 0.10:
            st.success("Highly Monodisperse System" if language == "English" else "Sistem Sangat Monodispers")
        elif pdi < 0.20:
            st.success("Monodisperse System" if language == "English" else "Sistem Monodispers")
        elif pdi < 0.30:
            st.info("Acceptable Distribution" if language == "English" else "Distribusi Dapat Diterima (Cukup Baik)")
        elif pdi < 0.50:
            st.warning("Broad Particle Size Distribution" if language == "English" else "Distribusi Ukuran Partikel Lebar")
        else:
            st.error("Very Broad Particle Size Distribution" if language == "English" else "Distribusi Ukuran Partikel Sangat Lebar")

if st.session_state.calculator=="zeta":
    st.header("Zeta Potential Analysis" if language == "English" else "Analisis Potensial Zeta")
    if language == "English":
        st.markdown("""
        ### Zeta Potential
        Zeta potential reflects the electrostatic stability of colloidal systems and nanoparticle dispersions. Dispersion stability is generally related to the absolute value of zeta potential.
        """)
    else:
        st.markdown("""
        ### Potensial Zeta (Zeta Potential)
        Potensial zeta mencerminkan stabilitas elektrostatik dari sistem koloid dan dispersi nanopartikel. Stabilitas dispersi umumnya berkaitan dengan nilai absolut (mutlak) dari potensial zeta, baik bermuatan positif maupun negatif.
        """)

    zeta = st.number_input("Measured Zeta Potential (mV)" if language == "English" else "Potensial Zeta Terukur (mV)", key="zeta_value")
    if st.button("Interpret Stability" if language == "English" else "Interpretasikan Stabilitas", key="zeta_btn"):
        st.metric("Zeta Potential", f"{zeta:.2f} mV")
        z = abs(zeta)
        if z < 10:
            st.error("Very Unstable Dispersion" if language == "English" else "Dispersi Sangat Tidak Stabil")
        elif z < 20:
            st.warning("Relatively Unstable Dispersion" if language == "English" else "Dispersi Relatif Tidak Stabil")
        elif z < 30:
            st.info("Moderately Stable Dispersion" if language == "English" else "Dispersi Cukup Stabil")
        elif z < 40:
            st.success("Stable Dispersion" if language == "English" else "Dispersi Stabil")
        elif z < 60:
            st.success("Very Stable Dispersion" if language == "English" else "Dispersi Sangat Stabil")
        else:
            st.success("Highly Stable Dispersion" if language == "English" else "Dispersi Luar Biasa Stabil")

if st.session_state.category=="packaging":
    st.subheader("Food Packaging Calculators" if language == "English" else "Kalkulator Kemasan Pangan")
    c1,c2,c3 = st.columns(3)
    with c1:
        if st.button("WVTR Calculator"):
            st.session_state.calculator="wvtr"
    with c2:
        if st.button("Moisture Content"):
            st.session_state.calculator="moisture"
    with c3:
        if st.button("Swelling Index"):
            st.session_state.calculator="swelling"

if st.session_state.calculator=="wvtr":
    st.header("WVTR Calculator" if language == "English" else "Kalkulator WVTR")
    if language == "English":
        st.markdown("""
        ### Water Vapor Transmission Rate (WVTR)
        WVTR measures the rate at which water vapor passes through a packaging material over a specified area and time.
        ### Formula
        WVTR = Δm / (A × t) (Unit: g/m²/day)
        """)
    else:
        st.markdown("""
        ### Water Vapor Transmission Rate (WVTR)
        WVTR (Laju Transmisi Uap Air) mengukur kecepatan uap air menembus material kemasan pada luasan area dan waktu tertentu.
        ### Rumus
        WVTR = Δm / (A × t) (Satuan: g/m²/hari)
        ### Keterangan
        - Δm = Kehilangan/penambahan massa air (g)
        - A = Luas area film yang terpapar (m²)
        - t = Waktu pengujian (hari)
        """)

    mass_loss = st.number_input("Water Mass Loss (g)" if language == "English" else "Massa Air yang Hilang/Berpindah (g)", min_value=0.0)
    area = st.number_input("Exposed Area (m²)" if language == "English" else "Luas Area Terpapar (m²)", min_value=0.0)
    time = st.number_input("Time (day)" if language == "English" else "Waktu (hari)", min_value=0.0)

    if st.button("Calculate WVTR" if language == "English" else "Hitung WVTR"):
        if area <= 0 or time <= 0:
            st.error("Area and Time must be greater than zero." if language == "English" else "Area dan Waktu harus lebih besar dari nol.")
        else:
            wvtr = mass_loss / (area * time)
            st.success(f"WVTR = {wvtr:.4f} g/m²/day" if language == "English" else f"WVTR = {wvtr:.4f} g/m²/hari")

if st.session_state.calculator=="moisture":
    st.header("Moisture Content Calculator" if language == "English" else "Kalkulator Kadar Air")
    if language == "English":
        st.markdown("""
        ### Moisture Content (MC)
        Moisture Content represents the amount of water present in a material (e.g., edible films, biopolymers).
        ### Formula
        MC (%) = [(Initial Weight − Dry Weight) / Initial Weight] × 100
        """)
    else:
        st.markdown("""
        ### Kadar Air (Moisture Content - MC)
        Kadar Air merepresentasikan jumlah kandungan air yang berada di dalam suatu material (seperti edible film, biopolimer, dsb).
        ### Rumus
        MC (%) = [(Bobot Awal − Bobot Kering) / Bobot Awal] × 100
        """)

    initial_weight = st.number_input("Initial Weight (g)" if language == "English" else "Bobot Awal (g)", min_value=0.0, key="mc_initial")
    dry_weight = st.number_input("Dry Weight (g)" if language == "English" else "Bobot Kering (g)", min_value=0.0, key="mc_dry")

    if st.button("Calculate Moisture Content" if language == "English" else "Hitung Kadar Air", key="mc_btn"):
        if initial_weight <= 0:
            st.error("Initial weight must be greater than zero." if language == "English" else "Bobot awal harus lebih besar dari nol.")
        elif dry_weight > initial_weight:
            st.error("Dry weight cannot exceed initial weight." if language == "English" else "Bobot kering tidak boleh melebihi bobot awal.")
        else:
            mc = ((initial_weight - dry_weight) / initial_weight) * 100
            st.success(f"Moisture Content = {mc:.2f}%" if language == "English" else f"Kadar Air = {mc:.2f}%")

if st.session_state.calculator=="swelling":
    st.header("Swelling Index Calculator" if language == "English" else "Kalkulator Indeks Pengembangan (Swelling)")
    if language == "English":
        st.markdown("""
        ### Swelling Index (SI)
        Swelling Index describes the ability of a material to absorb water and expand.
        ### Formula
        SI (%) = [(Swollen Weight − Dry Weight) / Dry Weight] × 100
        """)
    else:
        st.markdown("""
        ### Indeks Pengembangan (Swelling Index - SI)
        Swelling Index menggambarkan kemampuan suatu material (hidrogel, biopolimer, film kemasan) untuk menyerap air dan mengembang.
        ### Rumus
        SI (%) = [(Bobot Basah/Mengembang − Bobot Kering) / Bobot Kering] × 100
        """)

    dry_weight = st.number_input("Dry Weight (g)" if language == "English" else "Bobot Kering (g)", min_value=0.0, key="swelling_dry")
    swollen_weight = st.number_input("Swollen Weight (g)" if language == "English" else "Bobot Basah / Setelah Mengembang (g)", min_value=0.0, key="swelling_wet")

    if st.button("Calculate Swelling Index" if language == "English" else "Hitung Swelling Index", key="swelling_btn"):
        if dry_weight <= 0:
            st.error("Dry weight must be greater than zero." if language == "English" else "Bobot kering harus lebih besar dari nol.")
        elif swollen_weight < dry_weight:
            st.error("Swollen weight must be greater than or equal to dry weight." if language == "English" else "Bobot basah harus lebih besar atau sama dengan bobot kering.")
        else:
            si = ((swollen_weight - dry_weight) / dry_weight) * 100
            st.success(f"Swelling Index = {si:.2f}%" if language == "English" else f"Indeks Pengembangan = {si:.2f}%")

if st.session_state.category=="microbiology":
    st.subheader("Microbiology Calculators" if language == "English" else "Kalkulator Mikrobiologi")
    if st.button("CFU Calculator"):
        st.session_state.calculator="cfu"

if st.session_state.calculator=="cfu":
    st.header("CFU Calculator" if language == "English" else "Kalkulator CFU (Colony Forming Unit)")
    if language == "English":
        st.markdown("""
        ### Colony Forming Unit (CFU)
        CFU estimates the number of viable microorganisms capable of forming colonies under specified culture conditions.
        ### Formula
        CFU/mL = (Number of Colonies × Dilution Factor) / Volume Plated
        """)
    else:
        st.markdown("""
        ### Colony Forming Unit (CFU)
        CFU digunakan untuk mengestimasi jumlah mikroorganisme hidup (viabel) yang mampu membentuk koloni di bawah kondisi kultur tertentu.
        ### Rumus
        CFU/mL = (Jumlah Koloni × Faktor Pengenceran) / Volume Plated (mL)
        ### Keterangan
        - Jumlah Koloni = Koloni terhitung pada cawan petri
        - Faktor Pengenceran = Kebalikan dari pengenceran (misal, 10000 jika pengencerannya 10⁻⁴)
        - Volume Plated = Volume sampel yang dituang/disebar ke agar (mL)
        """)
    
    colonies = st.number_input("Number of Colonies" if language == "English" else "Jumlah Koloni Terhitung", min_value=0, step=1)
    dilution = st.number_input("Dilution Factor (e.g., 10000 for 10⁻⁴)" if language == "English" else "Faktor Pengenceran (misal: 10000 untuk pengenceran 10⁻⁴)", min_value=1)
    volume = st.number_input("Volume Plated (mL)" if language == "English" else "Volume yang Ditumbuhkan (mL)", min_value=0.0)

    if st.button("Calculate CFU" if language == "English" else "Hitung CFU"):
        if volume <= 0:
            st.error("Volume plated must be greater than zero." if language == "English" else "Volume plated harus lebih besar dari nol.")
        else:
            cfu = (colonies * dilution) / volume
            st.success(f"{cfu:.2e} CFU/mL")
            if colonies < 30:
                st.warning("Colony count is below the recommended countable range (30–300 colonies)." if language == "English" else "Jumlah koloni di bawah kisaran ideal perhitungan yang direkomendasikan (30-300 koloni).")
            elif colonies > 300:
                st.warning("Colony count exceeds the recommended countable range (30–300 colonies)." if language == "English" else "Jumlah koloni melebihi kisaran ideal perhitungan yang direkomendasikan (30-300 koloni).")

if st.session_state.category=="bioactivity":
    st.subheader("Bioactivity Calculators" if language == "English" else "Kalkulator Bioaktivitas")
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        if st.button("DPPH/ABTS Inhibition"):
            st.session_state.calculator="inhibition"
    with c2:
        if st.button("IC50"):
            st.session_state.calculator="ic50"
    with c3:
        if st.button("EC50"):
            st.session_state.calculator="ec50"
    with c4:
        if st.button("Release Efficiency"):
            st.session_state.calculator="release"

if st.session_state.calculator=="inhibition":
    st.header("DPPH / ABTS Inhibition Calculator" if language == "English" else "Kalkulator Inhibisi DPPH / ABTS")
    if language == "English":
        st.markdown("""
        ### Radical Scavenging Activity
        DPPH and ABTS assays are widely used to evaluate antioxidant activity.
        ### Formula
        % Inhibition = [(Ablank − Asample) / Ablank] × 100
        """)
    else:
        st.markdown("""
        ### Aktivitas Penangkal Radikal Bebas
        Uji DPPH dan ABTS digunakan secara luas untuk mengevaluasi aktivitas antioksidan suatu sampel.
        ### Rumus
        % Inhibisi (Persentase Hambatan) = [(A_blanko − A_sampel) / A_blanko] × 100
        ### Keterangan
        - A_blanko = Absorbansi larutan blanko (tanpa sampel)
        - A_sampel = Absorbansi larutan sampel
        """)

    blank = st.number_input("Blank Absorbance" if language == "English" else "Absorbansi Blanko", min_value=0.0)
    sample = st.number_input("Sample Absorbance" if language == "English" else "Absorbansi Sampel", min_value=0.0)

    if st.button("Calculate Inhibition" if language == "English" else "Hitung Inhibisi"):
        if blank <= 0:
            st.error("Blank absorbance must be greater than zero." if language == "English" else "Absorbansi blanko harus lebih besar dari nol.")
        else:
            inhibition = ((blank - sample) / blank) * 100
            st.success(f"Inhibition = {inhibition:.2f}%" if language == "English" else f"Inhibisi = {inhibition:.2f}%")

if st.session_state.calculator=="ic50":
    st.header("DPPH / ABTS IC50 Calculator" if language == "English" else "Kalkulator IC50 DPPH / ABTS")
    if language == "English":
        st.markdown("""
        ### IC50 (Inhibitory Concentration 50)
        IC50 represents the concentration required to inhibit 50% of radicals. Linear regression is commonly used for preliminary estimation ($y = ax + b$).
        """)
    else:
        st.markdown("""
        ### IC50 (Inhibitory Concentration 50)
        IC50 merepresentasikan konsentrasi sampel yang dibutuhkan untuk menghambat/menangkal 50% radikal bebas. Regresi linear digunakan secara umum untuk estimasi awal ($y = ax + b$).
        """)

    blank = st.number_input("Blank Absorbance" if language == "English" else "Absorbansi Blanko", value=1.000, key="ic50_blank")
    concentration = st.text_input("Concentrations (comma separated)" if language == "English" else "Konsentrasi (pisahkan dengan koma)", "50,100,150,200,250")
    absorbance = st.text_input("Sample Absorbance (comma separated)" if language == "English" else "Absorbansi Sampel (pisahkan dengan koma)", "0.90,0.75,0.60,0.45,0.30")

    if st.button("Calculate IC50" if language == "English" else "Hitung IC50"):
        try:
            conc = np.array([float(x) for x in concentration.split(",")])
            abs_sample = np.array([float(x) for x in absorbance.split(",")])
            inhibition = ((blank - abs_sample) / blank) * 100
            df = pd.DataFrame({"Concentration": conc, "Absorbance": abs_sample, "% Inhibition": inhibition})
            st.dataframe(df)

            slope, intercept, r, p, std = linregress(conc, inhibition)
            r2 = r**2
            ic50 = (50 - intercept) / slope

            st.success(f"IC50 = {ic50:.2f} ppm")
            st.write(f"Regression: y = {slope:.4f}x + {intercept:.4f}")
            st.write(f"R² = {r2:.4f}")

            fig, ax = plt.subplots()
            ax.scatter(conc, inhibition)
            ax.plot(conc, slope*conc + intercept)
            ax.axhline(y=50, linestyle="--")
            ax.set_xlabel("Concentration (ppm)")
            ax.set_ylabel("% Inhibition")
            st.pyplot(fig)
        except:
            st.error("Invalid input." if language == "English" else "Input tidak valid.")

if st.session_state.calculator=="ec50":
    st.header("EC50 Calculator" if language == "English" else "Kalkulator EC50")
    if language == "English":
        st.markdown("""
        ### Effective Concentration 50
        EC50 is the concentration producing 50% of the maximal observed effect.
        """)
    else:
        st.markdown("""
        ### Effective Concentration 50 (EC50)
        EC50 adalah tingkat konsentrasi yang menghasilkan 50% dari efek maksimal yang teramati dalam pengujian.
        """)

    concentration = st.text_input("Concentrations" if language == "English" else "Konsentrasi", "10,20,40,80,100", key="ec50_conc")
    effect = st.text_input("Effect (%)" if language == "English" else "Efek (%)", "12,25,42,63,80", key="ec50_eff")

    if st.button("Calculate EC50" if language == "English" else "Hitung EC50"):
        try:
            conc = np.array([float(x) for x in concentration.split(",")])
            eff = np.array([float(x) for x in effect.split(",")])
            slope, intercept, r, p, std = linregress(conc, eff)
            ec50 = (50 - intercept) / slope
            st.success(f"EC50 = {ec50:.2f}")
            fig, ax = plt.subplots()
            ax.scatter(conc, eff)
            ax.plot(conc, slope*conc+intercept)
            ax.axhline(y=50, linestyle="--")
            st.pyplot(fig)
        except:
            st.error("Invalid input.")

if st.session_state.calculator=="release":
    st.header("Release Efficiency Calculator" if language == "English" else "Kalkulator Efisiensi Pelepasan (Release Efficiency)")
    if language == "English":
        st.markdown("""
        ### Release Efficiency
        Release efficiency represents the percentage of encapsulated compounds successfully released from a delivery system.
        ### Formula
        Release Efficiency (%) = (Released Compound / Loaded Compound) × 100
        """)
    else:
        st.markdown("""
        ### Efisiensi Pelepasan (Release Efficiency)
        Release efficiency merepresentasikan persentase zat aktif terenkapsulasi yang berhasil dilepaskan dari sistem penghantaran (delivery system) ke lingkungan medianya.
        ### Rumus
        Release Efficiency (%) = (Zat Terlepas / Zat Muatan Awal) × 100
        """)

    loaded = st.number_input("Loaded Compound" if language == "English" else "Zat Muatan Awal", min_value=0.0)
    released = st.number_input("Released Compound" if language == "English" else "Zat Terlepas", min_value=0.0)

    if st.button("Calculate Release Efficiency" if language == "English" else "Hitung Efisiensi Pelepasan"):
        if loaded <= 0:
            st.error("Loaded compound must be greater than zero.")
        elif released > loaded:
            st.warning("Released compound exceeds loaded amount.")
        else:
            release = (released / loaded) * 100
            st.success(f"Release Efficiency = {release:.2f}%")

if st.session_state.category=="analytical":
    st.subheader("Analytical Chemistry Calculators" if language == "English" else "Kalkulator Kimia Analitik")
    c1,c2 = st.columns(2)
    with c1:
        if st.button("Beer-Lambert Calculator"):
            st.session_state.calculator="beer"
    with c2:
        if st.button("Standard Curve Calculator"):
            st.session_state.calculator="standard_curve"

if st.session_state.calculator=="beer":
    st.header("Beer-Lambert Calculator" if language == "English" else "Kalkulator Beer-Lambert")
    if language == "English":
        st.markdown("""
        ### Beer-Lambert Law
        Beer-Lambert law describes the linear relationship between absorbance and concentration.
        Formula: A = εbc
        """)
    else:
        st.markdown("""
        ### Hukum Beer-Lambert
        Hukum Beer-Lambert mendeskripsikan hubungan linear antara absorbansi dengan konsentrasi suatu larutan zat penangkap cahaya.
        Rumus: A = εbc
        ### Keterangan
        - A = Absorbansi
        - ε = Absorptivitas molar (L/mol/cm)
        - b = Tebal kuvet / panjang jalur cahaya (cm)
        - c = Konsentrasi larutan (mol/L)
        """)

    absorbance = st.number_input("Absorbance (A)" if language == "English" else "Absorbansi (A)", min_value=0.0)
    epsilon = st.number_input("Molar Absorptivity ε (L/mol/cm)" if language == "English" else "Absorptivitas Molar ε (L/mol/cm)", min_value=0.000001, value=1000.0)
    path = st.number_input("Path Length (cm)" if language == "English" else "Tebal Kuvet / Panjang Jalur (cm)", min_value=0.0001, value=1.0)

    if st.button("Calculate Concentration" if language == "English" else "Hitung Konsentrasi"):
        concentration = absorbance / (epsilon * path)
        st.success(f"Concentration = {concentration:.6e} mol/L" if language == "English" else f"Konsentrasi = {concentration:.6e} mol/L")

if st.session_state.calculator=="standard_curve":
    st.header("Standard Curve Calculator" if language == "English" else "Kalkulator Kurva Standar")
    if language == "English":
        st.markdown("""
        ### Standard Calibration Curve
        A standard curve is used to determine the concentration of unknown samples based on the response obtained from standards. Linear model: $y = mx + b$.
        """)
    else:
        st.markdown("""
        ### Kurva Kalibrasi Standar
        Kurva standar digunakan untuk menentukan tingkat konsentrasi sampel tak diketahui (unknown sample) berdasarkan data respons deret larutan standar. Model linear: $y = mx + b$.
        """)

    concentration_text = st.text_input("Standard Concentrations" if language == "English" else "Konsentrasi Standar", "10,20,40,60,80,100")
    absorbance_text = st.text_input("Standard Absorbance" if language == "English" else "Absorbansi Standar", "0.102,0.205,0.402,0.601,0.810,1.012")
    unknown_abs = st.number_input("Unknown Sample Absorbance" if language == "English" else "Absorbansi Sampel Diketahui", min_value=0.0)

    if st.button("Calculate Standard Curve" if language == "English" else "Hitung Kurva Standar"):
        try:
            conc = np.array([float(x) for x in concentration_text.split(",")])
            absorb = np.array([float(x) for x in absorbance_text.split(",")])

            if len(conc) != len(absorb):
                st.error("Data length mismatch.")
            else:
                slope, intercept, r, p, std = linregress(conc, absorb)
                r2 = r**2
                unknown_conc = (unknown_abs - intercept) / slope

                st.success(f"Unknown Concentration = {unknown_conc:.4f}" if language == "English" else f"Konsentrasi Sampel = {unknown_conc:.4f}")
                st.write(f"Equation: y = {slope:.5f}x + {intercept:.5f}")
                st.write(f"R² = {r2:.5f}")

                fig, ax = plt.subplots()
                ax.scatter(conc, absorb)
                ax.plot(conc, slope*conc + intercept)
                ax.scatter(unknown_conc, unknown_abs, marker="x", s=100)
                st.pyplot(fig)
        except:
            st.error("Invalid numerical data.")