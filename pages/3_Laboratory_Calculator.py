import streamlit as st
import math

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

st.header("Select Category")
col1,col2,col3,col4,col5,col6,col7 = st.columns(7)

with col1:
    if st.button("Basic Chemistry"):
        st.session_state.category = "basic"

with col2:
    if st.button("Nano Synthesis"):
        st.session_state.category = "synthesis"

with col3:
    if st.button("Characterization"):
        st.session_state.category = "characterization"

with col4:
    if st.button("Food Packaging"):
        st.session_state.category = "packaging"

with col5:
    if st.button("Microbiology"):
        st.session_state.category = "microbiology"

with col6:
    if st.button("Bioactivity"):
        st.session_state.category = "bioactivity"

with col7:
    if st.button("Analytical Chemistry"):
        st.session_state.category = "analytical"

if st.session_state.category == "basic":

    st.subheader("Basic Chemistry Calculators")

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        if st.button("Dilution Calculator"):
            st.session_state.calculator="dilution"

    with c2:
        if st.button("PPM Calculator"):
            st.session_state.calculator="ppm"

    with c3:
        if st.button("Molarity Calculator"):
            st.session_state.calculator="molarity"
    
    with c4:
        if st.button("Density Calculator"):
            st.session_state.calculator="density"

if st.session_state.calculator == "dilution":

    st.header("Dilution Calculator")

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

    st.latex(r"C_1V_1=C_2V_2")

    c1 = st.number_input(
        "Initial Concentration (C₁)",
        min_value=0.0
    )

    v1 = st.number_input(
        "Initial Volume (V₁, mL)",
        min_value=0.0
    )

    c2 = st.number_input(
        "Final Concentration (C₂)",
        min_value=0.0
    )

    if st.button(
        "Calculate Dilution",
        key="dilution_btn"
    ):

        if c2 <= 0:

            st.error(
                "Final concentration must be greater than zero."
            )

        else:

            v2 = (c1 * v1) / c2

            st.success(
                f"Final Volume (V₂) = {v2:.2f} mL"
            )

if st.session_state.calculator == "ppm":

    st.header("PPM Calculator")

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

    1 ppm ≈ 1 mg/L

    (for dilute aqueous solutions where the density is approximately 1 kg/L)

    ### Scientific Note

    The equivalence between ppm and mg/L is generally valid only for dilute aqueous solutions.
    """)

    mass = st.number_input(
        "Mass (mg)",
        min_value=0.0
    )

    volume = st.number_input(
        "Volume (L)",
        min_value=0.0
    )

    if st.button(
        "Calculate PPM",
        key="ppm_btn"
    ):

        if volume <= 0:

            st.error(
                "Volume must be greater than zero."
            )

        else:

            ppm = mass / volume

            st.success(
                f"Concentration = {ppm:.2f} ppm"
            )

if st.session_state.calculator == "molarity":

    st.header("Molarity Calculator")

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

    mass = st.number_input(
        "Mass (g)",
        min_value=0.0,
        key="mol_mass"
    )

    molar_mass = st.number_input(
        "Molar Mass (g/mol)",
        min_value=0.0,
        key="mol_mw"
    )

    volume = st.number_input(
        "Volume (L)",
        min_value=0.0,
        key="mol_vol"
    )

    if st.button(
        "Calculate Molarity",
        key="molarity_btn"
    ):

        if molar_mass <= 0:

            st.error(
                "Molar mass must be greater than zero."
            )

        elif volume <= 0:

            st.error(
                "Volume must be greater than zero."
            )

        else:

            molarity = (
                (mass / molar_mass)
                /
                volume
            )

            st.success(
                f"Molarity = {molarity:.4f} M"
            )

if st.session_state.calculator == "density":

    st.header("Density Calculator")

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

    mass = st.number_input(
        "Mass (g)",
        min_value=0.0,
        key="dens_mass"
    )

    volume = st.number_input(
        "Volume (mL)",
        min_value=0.0,
        key="dens_vol"
    )

    if st.button(
        "Calculate Density",
        key="density_btn"
    ):

        if volume <= 0:

            st.error(
                "Volume must be greater than zero."
            )

        else:

            density = mass / volume

            st.success(
                f"Density = {density:.4f} g/mL"
            )

            if density < 1:

                st.info(
                    "Less dense than water."
                )

            elif density > 1:

                st.info(
                    "More dense than water."
                )

            else:

                st.info(
                    "Density is approximately equal to water."
                )

if st.session_state.category=="synthesis":

    st.subheader(
        "Nanomaterial Synthesis"
    )

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        if st.button("Yield Calculator"):
            st.session_state.calculator="yield"

    with c2:
        if st.button("Recovery Calculator"):
            st.session_state.calculator="recovery"

    with c3:
        if st.button("Encapsulation Efficiency"):
            st.session_state.calculator="ee"

    with c4:
        if st.button("Loading Capacity"):
            st.session_state.calculator="lc"
            
if st.session_state.calculator=="yield":

    st.header("Yield Calculator")

    if language == "English":
        st.markdown("""
        ### Percent Yield

        Percent yield indicates the efficiency of a synthesis or production process by comparing the actual amount of product obtained with the theoretical amount expected.

        ### Formula

        Percent Yield (%) =
        (Actual Yield / Theoretical Yield) × 100

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

        Persentase Rendemen (%) =
        (Produk Aktual / Produk Teoritis) × 100

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
        
    actual_yield = st.number_input(
        "Actual Yield",
        min_value=0.0,
        key="actual_yield"
    )

    theoretical_yield = st.number_input(
        "Theoretical Yield",
        min_value=0.0,
        key="theoretical_yield"
    )

    if st.button(
        "Calculate Yield",
        key="yield_btn"
    ):

        if theoretical_yield <= 0:

            st.error(
                "Theoretical Yield must be greater than zero."
            )

        else:

            yield_percent = (
                actual_yield
                /
                theoretical_yield
            ) * 100

            st.success(
                f"Percent Yield = {yield_percent:.2f}%"
            )

            if yield_percent > 100:

                st.warning(
                    "Yield exceeds 100%. Verify experimental data and purity of the product."
                )

            elif yield_percent >= 80:

                st.info(
                    "High synthesis efficiency."
                )

            elif yield_percent >= 50:

                st.info(
                    "Moderate synthesis efficiency."
                )

            else:

                st.info(
                    "Low synthesis efficiency."
                )
            
if st.session_state.calculator=="recovery":

    st.header("Recovery Calculator")

    if language == "English":

        st.markdown("""
        ### Recovery Percentage

        Recovery percentage indicates the proportion of material recovered relative to the original amount.

        ### Formula

        Recovery (%) =
        (Recovered Amount / Initial Amount) × 100

        ### Applications

        - Extraction processes
        - Adsorption studies
        - Nanomaterial purification
        - Bioactive compound recovery

        ## Interpretation

        Higher recovery values indicate more effective material retrieval.

        ### Scientific Note

        Recovery may be expressed using mass, concentration, or total amount depending on the analytical method employed.
        """)

    else:
        st.markdown("""
        ### Persentase Recovery

        Persentase recovery menunjukkan proporsi material yang berhasil diperoleh kembali dibandingkan dengan jumlah awal material tersebut.

        ### Rumus

        Recovery (%) =
        (Jumlah yang Direcovery / Jumlah Awal) × 100

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

    initial_amount = st.number_input(
        "Initial Amount",
        min_value=0.0,
        key="initial_amount"
    )

    recovered_amount = st.number_input(
        "Recovered Amount",
        min_value=0.0,
        key="recovered_amount"
    )

    if st.button(
        "Calculate Recovery",
        key="recovery_btn"
    ):

        if initial_amount <= 0:

            st.error(
                "Initial Amount must be greater than zero."
            )

        else:

            recovery = (
                recovered_amount
                /
                initial_amount
            ) * 100

            st.success(
                f"Recovery = {recovery:.2f}%"
            )

            if recovery > 100:

                st.warning(
                    "Recovery exceeds 100%. Check analytical measurements."
                )

            elif recovery >= 80:

                st.info(
                    "High recovery efficiency."
                )

            elif recovery >= 50:

                st.info(
                    "Moderate recovery efficiency."
                )

            else:

                st.info(
                    "Low recovery efficiency."
                )

if st.session_state.calculator=="ee":

    st.header(
        "Encapsulation Efficiency"
    )

    if language == "English":

        st.markdown("""
        ### Encapsulation Efficiency

        Encapsulation efficiency measures the percentage of active compounds successfully entrapped within a carrier system.

        ### Formula

        EE (%) =
        [(Total Compound − Free Compound)
        /
        Total Compound] × 100

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

        EE (%) =
        [(Senyawa Total − Senyawa Bebas)
        /
        Senyawa Total] × 100

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

    total_compound = st.number_input(
        "Total Compound",
        min_value=0.0,
        key="total_compound"
    )

    free_compound = st.number_input(
        "Free Compound",
        min_value=0.0,
        key="free_compound"
    )

    if st.button(
        "Calculate EE",
        key="ee_btn"
    ):

        if total_compound <= 0:

            st.error(
                "Total Compound must be greater than zero."
            )

        elif free_compound > total_compound:

            st.error(
                "Free Compound cannot exceed Total Compound."
            )

        else:

            ee = (
                (
                    total_compound
                    -
                    free_compound
                )
                /
                total_compound
            ) * 100

            st.success(
                f"Encapsulation Efficiency = {ee:.2f}%"
            )

            if ee >= 80:

                st.info(
                    "High encapsulation efficiency."
                )

            elif ee >= 50:

                st.info(
                    "Moderate encapsulation efficiency."
                )

            else:

                st.info(
                    "Low encapsulation efficiency."
                )

if st.session_state.calculator=="lc":

    st.header(
        "Loading Capacity Calculator"
    )

    if language == "English":

        st.markdown("""
        ### Loading Capacity (LC)

        Loading Capacity describes the amount of active compound successfully loaded into a carrier material relative to the mass of the carrier.

        ### Formula

        LC (%) =
        (Encapsulated Compound / Carrier Mass)
        × 100

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
        ### Loading Capacity (LC)

        Loading Capacity menunjukkan jumlah senyawa aktif yang berhasil dimuat ke dalam material pembawa dibandingkan dengan massa material pembawa tersebut.

        ### Rumus

        LC (%) =
        (Massa Senyawa Terenkapsulasi / Massa Carrier)
        × 100

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

        Loading Capacity biasanya dilaporkan bersama Encapsulation Efficiency (EE). EE menunjukkan efisiensi proses enkapsulasi, sedangkan LC menunjukkan jumlah senyawa aktif yang berhasil dimuat ke dalam sistem pembawa.
        """)

    encapsulated_compound = st.number_input(
        "Encapsulated Compound Mass (mg)",
        min_value=0.0,
        key="lc_compound"
    )

    carrier_mass = st.number_input(
        "Carrier Mass (mg)",
        min_value=0.0,
        key="lc_carrier"
    )

    if st.button(
        "Calculate Loading Capacity",
        key="lc_btn"
    ):

        if carrier_mass <= 0:

            st.error(
                "Carrier mass must be greater than zero."
            )

        else:

            lc = (
                encapsulated_compound
                /
                carrier_mass
            ) * 100

            st.success(
                f"Loading Capacity = {lc:.2f}%"
            )

            if lc >= 50:

                st.success(
                    "Very High Loading Capacity"
                )

            elif lc >= 25:

                st.info(
                    "Moderate Loading Capacity"
                )

            elif lc >= 10:

                st.warning(
                    "Low Loading Capacity"
                )

            else:

                st.error(
                    "Very Low Loading Capacity"
                )

            st.caption(
                """
Loading Capacity indicates the amount of active compound incorporated per unit mass of carrier material.
                """
            )

if st.session_state.category=="characterization":

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
        if st.button(
            "Zeta Potential"
        ):
            st.session_state.calculator="zeta"

if st.session_state.calculator=="scherrer":

    import math

    st.header(
        "Scherrer Equation Calculator"
    )

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

    - ZnO nanoparticles
    - TiO₂ nanoparticles
    - Silver nanoparticles
    - Silica nanoparticles
    - Nanocomposite materials

    ### Instrumental Broadening Correction
                
    Experimental peak broadening contains contributions from both the sample and the instrument.

    Corrected peak broadening is calculated as:

    β = √(βobs² − βinst²)

    Where:

    - βobs = Observed FWHM
    - βinst = Instrumental FWHM
    - β = Corrected FWHM

    ### Scientific Note

    Instrumental broadening correction is recommended for accurate crystallite size estimation in XRD analysis.
    """)

    k = st.number_input(
        "Shape Factor (K)",
        min_value=0.1,
        value=0.9,
        key="scherrer_k"
    )

    lam = st.number_input(
        "X-ray Wavelength λ (nm)",
        min_value=0.0001,
        value=0.15406,
        key="scherrer_lambda"
    )

    beta = st.number_input(
        "FWHM β (degrees)",
        min_value=0.0,
        key="scherrer_beta"
    )

    theta = st.number_input(
        "Bragg Angle θ (degrees)",
        min_value=0.0,
        key="scherrer_theta"
    )

    if st.button(
        "Calculate Crystallite Size",
        key="scherrer_btn"
    ):

        if beta <= 0:

            st.error(
                "FWHM β must be greater than zero."
            )

        else:

            beta_rad = math.radians(beta)

            theta_rad = math.radians(theta)

            d = (
                k * lam
            ) / (
                beta_rad *
                math.cos(theta_rad)
            )

            st.success(
                f"Crystallite Size = {d:.2f} nm"
            )

            if d < 100:

                st.info(
                    "Crystallite size falls within the nanocrystalline range."
                )

            else:

                st.info(
                    "Crystallite size is above the conventional nanocrystalline range."
                )

            st.caption(
                "The Scherrer equation provides an approximate crystallite size and does not directly represent particle size."
            )

if st.session_state.calculator=="corrected_scherrer":

    st.header(
        "Instrument Corrected Scherrer Calculator"
    )

    st.markdown("""
    ### Instrument Corrected Scherrer Equation

    The Scherrer equation is widely used to estimate crystallite size from X-ray diffraction peak broadening.

    Experimental peak broadening contains contributions from both the sample and the instrument.

    Therefore instrumental broadening correction is recommended before crystallite size calculation.

    ### Step 1: Corrected FWHM

    β = √(βobs² − βinst²)

    ### Step 2: Scherrer Equation

    D = Kλ / βcosθ

    ### Where

    - D = Crystallite size (nm)
    - K = Shape factor
    - λ = X-ray wavelength (nm)
    - βobs = Observed FWHM (radians)
    - βinst = Instrumental FWHM (radians)
    - β = Corrected FWHM
    - θ = Bragg angle

    ### Applications

    - ZnO nanoparticles
    - TiO₂ nanoparticles
    - Ag nanoparticles
    - Silica nanoparticles
    - Nanocomposite materials

    ### Scientific Note

    Instrumental correction is recommended by XRD characterization literature because measured peak broadening contains both sample and instrument contributions.
    """)

    k = st.number_input(
        "Shape Factor (K)",
        min_value=0.1,
        value=0.9
    )

    wavelength = st.number_input(
        "X-ray Wavelength λ (nm)",
        min_value=0.0001,
        value=0.15406
    )

    beta_obs = st.number_input(
        "Observed FWHM βobs (degrees)",
        min_value=0.0
    )

    beta_inst = st.number_input(
        "Instrumental FWHM βinst (degrees)",
        min_value=0.0
    )

    theta = st.number_input(
        "Bragg Angle θ (degrees)",
        min_value=0.0
    )

    if st.button("Calculate Corrected Scherrer"):

        import math

        if beta_obs <= beta_inst:

            st.error(
                "Observed FWHM must be greater than Instrumental FWHM."
            )

        else:

            beta_corr_deg = math.sqrt(
                beta_obs**2 -
                beta_inst**2
            )

            beta_corr_rad = math.radians(
                beta_corr_deg
            )

            theta_rad = math.radians(
                theta
            )

            d = (
                k *
                wavelength
            ) / (
                beta_corr_rad *
                math.cos(theta_rad)
            )

            st.success(
                f"Corrected FWHM = {beta_corr_deg:.4f}°"
            )

            st.success(
                f"Crystallite Size = {d:.2f} nm"
            )

            st.caption(
                "Calculated using instrumental broadening corrected Scherrer equation."
            )

if st.session_state.calculator=="dspacing":

    st.header(
        "Bragg d-Spacing Calculator"
    )

    st.markdown("""
    ### Bragg's Law

    Bragg's Law relates diffraction angle and crystal lattice spacing.

    nλ = 2d sinθ

    For most XRD analyses:

    n = 1

    Therefore:

    d = λ / (2 sinθ)

    ### Where

    - d = Interplanar spacing (nm)
    - λ = X-ray wavelength (nm)
    - θ = Bragg angle

    ### Applications

    - Crystal structure analysis
    - Lattice spacing determination
    - Nanoparticle characterization
    - Material identification

    ### Scientific Note

    d-spacing is one of the most important parameters reported in XRD studies.
    """)

    wavelength = st.number_input(
        "X-ray Wavelength λ (nm)",
        min_value=0.0001,
        value=0.15406,
        key="d_lambda"
    )

    two_theta = st.number_input(
        "2θ (degrees)",
        min_value=0.0,
        key="d_2theta"
    )

    if st.button(
        "Calculate d-Spacing"
    ):

        import math

        if two_theta <= 0:

            st.error(
                "2θ must be greater than zero."
            )

        else:

            theta = two_theta / 2

            theta_rad = math.radians(
                theta
            )

            d = wavelength / (
                2 *
                math.sin(theta_rad)
            )

            st.success(
                f"d-Spacing = {d:.4f} nm"
            )

            st.success(
                f"d-Spacing = {d*10:.4f} Å"
            )

            st.caption(
                "Calculated using Bragg's Law."
            )

if st.session_state.calculator=="pdi":

    st.header(
        "Polydispersity Index (PDI) Interpreter"
    )

    st.markdown("""
    ### Polydispersity Index (PDI)

    PDI describes the width of particle size distribution measured by Dynamic Light Scattering (DLS).

    Lower PDI values indicate a narrower and more uniform particle size distribution.

    ### General Interpretation

    | PDI | Interpretation |
    |------|---------------|
    | < 0.10 | Highly Monodisperse |
    | 0.10–0.20 | Monodisperse |
    | 0.20–0.30 | Acceptable |
    | 0.30–0.50 | Broad Distribution |
    | > 0.50 | Very Broad Distribution |

    ### Applications

    - Nanoparticle characterization
    - Nanoemulsions
    - Liposomes
    - Polymeric nanoparticles
    - Food nanotechnology systems

    ### Scientific Note

    PDI is obtained from DLS analysis and is commonly used to assess sample homogeneity.
    """)

    pdi = st.number_input(
        "PDI Value",
        min_value=0.0,
        max_value=1.0,
        value=0.20
    )

    if st.button(
        "Interpret PDI"
    ):

        st.metric(
            "PDI",
            f"{pdi:.3f}"
        )

        if pdi < 0.10:

            st.success(
                "Highly Monodisperse System"
            )

        elif pdi < 0.20:

            st.success(
                "Monodisperse System"
            )

        elif pdi < 0.30:

            st.info(
                "Acceptable Distribution"
            )

        elif pdi < 0.50:

            st.warning(
                "Broad Particle Size Distribution"
            )

        else:

            st.error(
                "Very Broad Particle Size Distribution"
            )

        st.caption(
            "Lower PDI values indicate greater particle size uniformity."
        )

if st.session_state.calculator=="zeta":

    st.header(
        "Zeta Potential Analysis"
    )

    st.markdown("""
    ### Zeta Potential

    Zeta potential reflects the electrostatic stability of colloidal systems and nanoparticle dispersions.

    ### Stability Classification

    | Zeta Potential (mV) | Stability |
    |---------------------|-----------|
    | 0 to ±10 | Very unstable |
    | ±10 to ±20 | Relatively unstable |
    | ±20 to ±30 | Moderately stable |
    | ±30 to ±40 | Stable |
    | ±40 to ±60 | Very stable |
    | > ±60 | Highly stable |

    ### Applications

    - Nanoparticle characterization
    - Nanoemulsions
    - Liposomes
    - Nanofood systems
    - Colloidal dispersions

    ### Scientific Note

    Dispersion stability is generally related to the absolute value of zeta potential, regardless of whether the surface charge is positive or negative.
    """)

    zeta = st.number_input(
        "Measured Zeta Potential (mV)",
        key="zeta_value"
    )

    if st.button(
        "Interpret Stability",
        key="zeta_btn"
    ):

        st.metric(
            "Zeta Potential",
            f"{zeta:.2f} mV"
        )

        z = abs(zeta)

        if z < 10:

            st.error(
                "Very Unstable Dispersion"
            )

        elif z < 20:

            st.warning(
                "Relatively Unstable Dispersion"
            )

        elif z < 30:

            st.info(
                "Moderately Stable Dispersion"
            )

        elif z < 40:

            st.success(
                "Stable Dispersion"
            )

        elif z < 60:

            st.success(
                "Very Stable Dispersion"
            )

        else:

            st.success(
                "Highly Stable Dispersion"
            )

        st.caption(
            "Higher absolute zeta potential values generally indicate stronger electrostatic repulsion and improved colloidal stability."
        )

if st.session_state.category=="packaging":

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

    st.header(
        "WVTR Calculator"
    )

    st.markdown("""
    ### Water Vapor Transmission Rate (WVTR)

    WVTR measures the rate at which water vapor passes through a packaging material over a specified area and time.

    ### Formula

    WVTR = Δm / (A × t)

    ### Where

    - Δm = Water mass loss (g)
    - A = Exposed area (m²)
    - t = Time (day)

    ### Unit

    g/m²/day

    ### Interpretation

    Lower WVTR values indicate better moisture barrier properties.

    ### Applications

    - Food packaging films
    - Biopolymer films
    - Nanocomposite packaging
    - Active packaging systems
    """)

    mass_loss = st.number_input(
        "Water Mass Loss (g)",
        min_value=0.0
    )

    area = st.number_input(
        "Exposed Area (m²)",
        min_value=0.0
    )

    time = st.number_input(
        "Time (day)",
        min_value=0.0
    )

    if st.button(
        "Calculate WVTR"
    ):

        if area <= 0 or time <= 0:

            st.error(
                "Area and Time must be greater than zero."
            )

        else:

            wvtr = (
                mass_loss
                /
                (area * time)
            )

            st.success(
                f"WVTR = {wvtr:.4f} g/m²/day"
            )

            st.info(
                "Lower WVTR values generally indicate better moisture barrier performance."
            )

            st.caption(
                "WVTR is affected by material composition, film thickness, temperature, and relative humidity."
            )

if st.session_state.calculator=="moisture":

    st.header(
        "Moisture Content Calculator"
    )

    st.markdown("""
    ### Moisture Content (MC)

    Moisture Content represents the amount of water present in a material.

    It is one of the most important physical properties evaluated in food packaging films, biopolymers, and nanocomposite materials.

    ### Formula

    MC (%) =
    [(Initial Weight − Dry Weight)
    /
    Initial Weight]
    × 100

    ### Where

    - Initial Weight = sample weight before drying
    - Dry Weight = sample weight after drying

    ### Applications

    - Edible films
    - Biopolymer packaging
    - Starch films
    - Chitosan films
    - Nanocomposite food packaging

    ### Interpretation

    Lower moisture content generally indicates better resistance to water absorption and improved storage stability.

    ### Scientific Note

    Moisture content is commonly determined by oven drying until constant weight according to standard gravimetric methods.
    """)

    initial_weight = st.number_input(
        "Initial Weight (g)",
        min_value=0.0,
        key="mc_initial"
    )

    dry_weight = st.number_input(
        "Dry Weight (g)",
        min_value=0.0,
        key="mc_dry"
    )

    if st.button(
        "Calculate Moisture Content",
        key="mc_btn"
    ):

        if initial_weight <= 0:

            st.error(
                "Initial weight must be greater than zero."
            )

        elif dry_weight > initial_weight:

            st.error(
                "Dry weight cannot exceed initial weight."
            )

        else:

            mc = (
                (initial_weight - dry_weight)
                /
                initial_weight
            ) * 100

            st.success(
                f"Moisture Content = {mc:.2f}%"
            )

            if mc < 5:

                st.success(
                    "Very Low Moisture Content"
                )

            elif mc < 15:

                st.info(
                    "Moderate Moisture Content"
                )

            else:

                st.warning(
                    "High Moisture Content"
                )

            st.caption(
                """
Moisture content influences mechanical properties, barrier performance, and storage stability of packaging materials.
                """
            )

if st.session_state.calculator=="swelling":

    st.header(
        "Swelling Index Calculator"
    )

    st.markdown("""
    ### Swelling Index (SI)

    Swelling Index describes the ability of a material to absorb water and expand.

    It is widely used for characterization of edible films, hydrogels, biopolymers, and nanocomposite packaging materials.

    ### Formula

    SI (%) =
    [(Swollen Weight − Dry Weight)
    /
    Dry Weight]
    × 100

    ### Where

    - Dry Weight = weight before immersion
    - Swollen Weight = weight after immersion

    ### Applications

    - Chitosan films
    - Starch films
    - Hydrogels
    - Nanocomposite packaging
    - Biopolymer materials

    ### Interpretation

    Higher swelling index indicates greater water uptake capacity.

    ### Scientific Note

    Swelling behavior is affected by polymer composition, crosslinking density, nanoparticle incorporation, and immersion medium.
    """)

    dry_weight = st.number_input(
        "Dry Weight (g)",
        min_value=0.0,
        key="swelling_dry"
    )

    swollen_weight = st.number_input(
        "Swollen Weight (g)",
        min_value=0.0,
        key="swelling_wet"
    )

    if st.button(
        "Calculate Swelling Index",
        key="swelling_btn"
    ):

        if dry_weight <= 0:

            st.error(
                "Dry weight must be greater than zero."
            )

        elif swollen_weight < dry_weight:

            st.error(
                "Swollen weight must be greater than or equal to dry weight."
            )

        else:

            si = (
                (swollen_weight - dry_weight)
                /
                dry_weight
            ) * 100

            st.success(
                f"Swelling Index = {si:.2f}%"
            )

            if si < 50:

                st.info(
                    "Low Water Uptake"
                )

            elif si < 150:

                st.info(
                    "Moderate Water Uptake"
                )

            else:

                st.success(
                    "High Water Uptake"
                )

            st.caption(
                """
Swelling Index reflects water absorption behavior and structural expansion of packaging materials.
                """
            )

if st.session_state.category=="microbiology":

    if st.button("CFU Calculator"):
        st.session_state.calculator="cfu"

if st.session_state.calculator=="cfu":

    st.header(
        "CFU Calculator"
    )

    st.markdown("""
    ### Colony Forming Unit (CFU)

    CFU estimates the number of viable microorganisms capable of forming colonies under specified culture conditions.

    ### Formula

    CFU/mL =
    (Number of Colonies × Dilution Factor)
    /
    Volume Plated

    ### Where

    - Number of Colonies = Counted colonies on the plate
    - Dilution Factor = Reciprocal of the dilution used
    - Volume Plated = Volume inoculated onto the agar plate (mL)

    ### Applications

    - Food microbiology
    - Antimicrobial testing
    - Shelf-life studies
    - Fermentation monitoring
    - Probiotic analysis

    ### Interpretation

    Higher CFU values generally indicate a greater microbial population.

    ### Scientific Note

    Interpretation depends on the product type, microbial species, culture conditions, and applicable microbiological standards.
    """)
    
    colonies = st.number_input(
        "Number of Colonies",
        min_value=0,
        step=1
    )

    dilution = st.number_input(
        "Dilution Factor (e.g., 10000 for 10⁻⁴ dilution)",
        min_value=1
    )

    volume = st.number_input(
        "Volume Plated (mL)",
        min_value=0.0
    )

    if st.button(
        "Calculate CFU"
    ):

        if volume <= 0:

            st.error(
                "Volume plated must be greater than zero."
            )

        else:

            cfu = (
                colonies *
                dilution
            ) / volume

            st.success(
                f"{cfu:.2e} CFU/mL"
            )

            if colonies < 30:

                st.warning(
                    "Colony count is below the recommended countable range (30–300 colonies)."
                )

            elif colonies > 300:

                st.warning(
                    "Colony count exceeds the recommended countable range (30–300 colonies)."
                )

            st.info(
                "Interpret CFU values according to the product type and microbiological standards."
            )

            st.caption(
                """
    CFU estimates viable microorganisms capable of forming colonies under specified culture conditions.
                """
            )

if st.session_state.category=="bioactivity":

    st.subheader("Bioactivity Calculators")

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

    st.header("DPPH / ABTS Inhibition Calculator")

    st.markdown("""
    ### Radical Scavenging Activity

    DPPH and ABTS assays are widely used to evaluate antioxidant activity.

    ### Formula

    % Inhibition =
    [(Ablank − Asample)/Ablank] × 100

    ### Where

    - Ablank = Blank absorbance
    - Asample = Sample absorbance

    ### Applications

    - Antioxidant activity
    - Plant extracts
    - Nanoencapsulated antioxidants
    - Functional foods

    ### Scientific Note

    Higher inhibition percentages indicate stronger radical scavenging activity.
    """)

    blank = st.number_input(
        "Blank Absorbance",
        min_value=0.0
    )

    sample = st.number_input(
        "Sample Absorbance",
        min_value=0.0
    )

    if st.button("Calculate Inhibition"):

        if blank <= 0:

            st.error(
                "Blank absorbance must be greater than zero."
            )

        else:

            inhibition = (
                (blank-sample)
                /
                blank
            )*100

            st.success(
                f"Inhibition = {inhibition:.2f}%"
            )

            if inhibition >= 80:
                st.success("Very High Antioxidant Activity")

            elif inhibition >= 50:
                st.info("High Antioxidant Activity")

            elif inhibition >= 20:
                st.warning("Moderate Antioxidant Activity")

            else:
                st.error("Low Antioxidant Activity")
           
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

if st.session_state.calculator=="ic50":

    st.header("DPPH / ABTS IC50 Calculator")

    st.markdown("""
    ### IC50

    IC50 represents the concentration required
    to inhibit 50% of radicals.

    ### Formula

    y = ax + b

    IC50 = (50 - b)/a

    ### Scientific Note

    Linear regression is commonly used for preliminary IC50 estimation.
    More advanced studies may use nonlinear dose-response fitting.
    """)

    blank = st.number_input(
        "Blank Absorbance",
        value=1.000,
        key="ic50_blank"
    )

    concentration = st.text_input(
        "Concentrations (comma separated)",
        "50,100,150,200,250"
    )

    absorbance = st.text_input(
        "Sample Absorbance",
        "0.90,0.75,0.60,0.45,0.30"
    )

    if st.button("Calculate IC50"):

        try:

            conc = np.array([
                float(x)
                for x in concentration.split(",")
            ])

            abs_sample = np.array([
                float(x)
                for x in absorbance.split(",")
            ])

            inhibition = (
                (blank - abs_sample)
                /
                blank
            ) * 100

            df = pd.DataFrame({
                "Concentration": conc,
                "Absorbance": abs_sample,
                "% Inhibition": inhibition
            })

            st.dataframe(df)

            slope, intercept, r, p, std = linregress(
                conc,
                inhibition
            )

            r2 = r**2

            ic50 = (
                50 - intercept
            ) / slope

            st.success(
                f"IC50 = {ic50:.2f} ppm"
            )

            st.write(
                f"Regression: y = {slope:.4f}x + {intercept:.4f}"
            )

            st.write(
                f"R² = {r2:.4f}"
            )

            if ic50 < 50:
                st.success("Very Strong")

            elif ic50 < 100:
                st.info("Strong")

            elif ic50 < 150:
                st.warning("Moderate")

            elif ic50 < 200:
                st.warning("Weak")

            else:
                st.error("Very Weak")

            fig, ax = plt.subplots()

            ax.scatter(
                conc,
                inhibition
            )

            ax.plot(
                conc,
                slope*conc + intercept
            )

            ax.axhline(
                y=50,
                linestyle="--"
            )

            ax.set_xlabel(
                "Concentration (ppm)"
            )

            ax.set_ylabel(
                "% Inhibition"
            )

            ax.set_title(
                "IC50 Regression Curve"
            )

            st.pyplot(fig)

        except:

            st.error(
                "Invalid input."
            )

if st.session_state.calculator=="ec50":

    st.header("EC50 Calculator")

    st.markdown("""
    ### Effective Concentration 50

    EC50 is the concentration producing
    50% of the maximal observed effect.

    ### Formula

    EC50 = (50 − b)/a

    obtained from linear regression.
    """)

    concentration = st.text_input(
        "Concentrations",
        "10,20,40,80,100",
        key="ec50_conc"
    )

    effect = st.text_input(
        "Effect (%)",
        "12,25,42,63,80",
        key="ec50_eff"
    )

    if st.button("Calculate EC50"):

        try:

            conc = np.array([
                float(x)
                for x in concentration.split(",")
            ])

            eff = np.array([
                float(x)
                for x in effect.split(",")
            ])

            slope, intercept, r, p, std = linregress(
                conc,
                eff
            )

            ec50 = (
                50 - intercept
            ) / slope

            r2 = r**2

            st.success(
                f"EC50 = {ec50:.2f}"
            )

            st.write(
                f"R² = {r2:.4f}"
            )

            fig, ax = plt.subplots()

            ax.scatter(
                conc,
                eff
            )

            ax.plot(
                conc,
                slope*conc+intercept
            )

            ax.axhline(
                y=50,
                linestyle="--"
            )

            ax.set_xlabel(
                "Concentration"
            )

            ax.set_ylabel(
                "Effect (%)"
            )

            ax.set_title(
                "EC50 Regression Curve"
            )

            st.pyplot(fig)

        except:

            st.error(
                "Invalid input."
            )

if st.session_state.calculator=="release":

    st.header("Release Efficiency Calculator")

    st.markdown("""
    ### Release Efficiency

    Release efficiency represents the percentage
    of encapsulated compounds successfully released
    from a delivery system.

    ### Formula

    Release Efficiency (%) =
    (Released Compound / Loaded Compound)
    ×100

    ### Applications

    - Nanoencapsulation
    - Liposomes
    - Polymeric nanoparticles
    - Active packaging
    - Controlled release systems

    ### Scientific Note

    Release efficiency is commonly reported in
    release kinetics and controlled delivery studies.
    """)

    loaded = st.number_input(
        "Loaded Compound",
        min_value=0.0
    )

    released = st.number_input(
        "Released Compound",
        min_value=0.0
    )

    if st.button(
        "Calculate Release Efficiency"
    ):

        if loaded <= 0:

            st.error(
                "Loaded compound must be greater than zero."
            )

        elif released > loaded:

            st.warning(
                "Released compound exceeds loaded amount."
            )

        else:

            release = (
                released
                /
                loaded
            ) * 100

            st.success(
                f"Release Efficiency = {release:.2f}%"
            )

            if release >= 80:

                st.success(
                    "High Release Efficiency"
                )

            elif release >= 50:

                st.info(
                    "Moderate Release Efficiency"
                )

            else:

                st.warning(
                    "Low Release Efficiency"
                )

if st.session_state.category=="analytical":

    st.subheader(
        "Analytical Chemistry Calculators"
    )

    c1,c2 = st.columns(2)

    with c1:
        if st.button(
            "Beer-Lambert Calculator"
        ):
            st.session_state.calculator="beer"

    with c2:
        if st.button(
            "Standard Curve Calculator"
        ):
            st.session_state.calculator="standard_curve"

if st.session_state.calculator=="beer":

    st.header(
        "Beer-Lambert Calculator"
    )

    st.markdown("""
    ### Beer-Lambert Law

    Beer-Lambert law describes the linear relationship
    between absorbance and concentration.

    Formula:

    A = εbc

    Where:

    - A = Absorbance
    - ε = Molar absorptivity
    - b = Path length (cm)
    - c = Concentration

    Applications:

    - UV-Vis spectrophotometry
    - Total phenolic content
    - Total flavonoid content
    - DPPH assay
    - ABTS assay
    - Protein analysis

    Scientific Note:

    The Beer-Lambert relationship is generally valid
    for dilute solutions where absorbance remains
    proportional to concentration.
    """)

    absorbance = st.number_input(
        "Absorbance (A)",
        min_value=0.0
    )

    epsilon = st.number_input(
        "Molar Absorptivity ε (L/mol/cm)",
        min_value=0.000001,
        value=1000.0
    )

    path = st.number_input(
        "Path Length (cm)",
        min_value=0.0001,
        value=1.0
    )

    if st.button(
        "Calculate Concentration"
    ):

        concentration = (
            absorbance
            /
            (epsilon * path)
        )

        st.success(
            f"Concentration = {concentration:.6e} mol/L"
        )

        st.caption(
            "Calculated according to the Beer-Lambert law."
        )

if st.session_state.calculator=="standard_curve":

    st.header(
        "Standard Curve Calculator"
    )

    st.markdown("""
    ### Standard Calibration Curve

    A standard curve is used to determine the
    concentration of unknown samples based on
    the response obtained from standards.

    Linear model:

    y = mx + b

    Where:

    - y = Absorbance
    - x = Concentration

    Applications:

    - Total Phenolic Content
    - Total Flavonoid Content
    - Protein Assay
    - Heavy Metal Analysis
    - UV-Vis Quantification

    Scientific Note:

    Good calibration curves typically show
    R² values approaching 1.000.
    """)

    concentration_text = st.text_input(
        "Standard Concentrations",
        "10,20,40,60,80,100"
    )

    absorbance_text = st.text_input(
        "Standard Absorbance",
        "0.102,0.205,0.402,0.601,0.810,1.012"
    )

    unknown_abs = st.number_input(
        "Unknown Sample Absorbance",
        min_value=0.0
    )

    if st.button(
        "Calculate Standard Curve"
    ):

        try:

            conc = np.array([
                float(x)
                for x in concentration_text.split(",")
            ])

            absorb = np.array([
                float(x)
                for x in absorbance_text.split(",")
            ])

            if len(conc) != len(absorb):

                st.error(
                    "Data length mismatch."
                )

            else:

                slope, intercept, r, p, std = linregress(
                    conc,
                    absorb
                )

                r2 = r**2

                unknown_conc = (
                    unknown_abs
                    -
                    intercept
                ) / slope

                st.success(
                    f"Unknown Concentration = {unknown_conc:.4f}"
                )

                st.write(
                    f"Equation: y = {slope:.5f}x + {intercept:.5f}"
                )

                st.write(
                    f"R² = {r2:.5f}"
                )

                df = pd.DataFrame({
                    "Concentration": conc,
                    "Absorbance": absorb
                })

                st.dataframe(df)

                fig, ax = plt.subplots()

                ax.scatter(
                    conc,
                    absorb
                )

                ax.plot(
                    conc,
                    slope*conc + intercept
                )

                ax.scatter(
                    unknown_conc,
                    unknown_abs,
                    marker="x",
                    s=100
                )

                ax.set_xlabel(
                    "Concentration"
                )

                ax.set_ylabel(
                    "Absorbance"
                )

                ax.set_title(
                    "Calibration Curve"
                )

                st.pyplot(fig)

                if r2 >= 0.99:

                    st.success(
                        "Excellent Linearity"
                    )

                elif r2 >= 0.95:

                    st.info(
                        "Good Linearity"
                    )

                else:

                    st.warning(
                        "Poor Linearity. Consider repeating calibration."
                    )

        except:

            st.error(
                "Invalid numerical data."
            )
