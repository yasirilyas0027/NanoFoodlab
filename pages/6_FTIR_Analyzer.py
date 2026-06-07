import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("🔬 FTIR Functional Group Analyzer")

st.markdown("""
Analyze FTIR peaks, identify functional groups,
predict material composition, and learn FTIR theory
used in nanotechnology and food science.
""")

st.subheader("📥 FTIR Peak Input")

peak_input = st.text_input(
    "Enter FTIR Peaks (cm⁻¹)",
    "3400,2920,1730,1630,1050"
)

analyze = st.button("🔍 Analyze Spectrum")

ftir_db = [

("O-H Stretching",3200,3550,"Alcohol / Phenol"),
("N-H Stretching",3250,3550,"Amine"),
("≡C-H Stretching",3200,3310,"Alkyne"),
("C-H Stretching",2850,2990,"Alkane"),
("Aldehyde C-H",2700,2900,"Aldehyde"),
("S-H Stretching",2550,2600,"Thiol"),

("C≡N Stretching",2200,2280,"Nitrile"),
("C≡C Stretching",2100,2250,"Alkyne"),

("Anhydride C=O",1740,1850,"Anhydride"),
("Ester C=O",1735,1765,"Ester"),
("Carbonyl C=O",1700,1750,"Carbonyl"),
("Carboxylic Acid",1700,1725,"Carboxylic Acid"),
("Amide",1630,1700,"Amide"),
("C=C Stretching",1620,1680,"Alkene"),

("Aromatic Ring",1495,1615,"Aromatic"),
("Nitro Group",1300,1570,"Nitro"),

("C-O Stretching",1000,1300,"Alcohol/Ether"),

("C-F",1000,1400,"Fluoride"),
("C-Cl",600,800,"Chloride"),
("C-Br",500,700,"Bromide")
]

if analyze:

    peaks = [
        float(x.strip())
        for x in peak_input.split(",")
    ]

    functional_groups = []

    for peak in peaks:

        for name,minv,maxv,group in ftir_db:

            if minv <= peak <= maxv:

                functional_groups.append(
                    [peak,name,group]
                )

st.subheader("🧬 Spectrum Complexity")

if len(peaks) < 5:

    st.success(
        f"{len(peaks)} Peaks → Simple Compound"
    )

else:

    st.warning(
        f"{len(peaks)} Peaks → Complex Compound"
    )

df = pd.DataFrame(
    functional_groups,
    columns=[
        "Peak (cm⁻¹)",
        "Vibration",
        "Functional Group"
    ]
)

st.subheader("📊 Functional Group Identification")

st.dataframe(
    df,
    use_container_width=True
)

groups = df["Functional Group"].tolist()

interpretation = []

if "Alcohol / Phenol" in groups:

    interpretation.append(
        "Hydroxyl groups detected."
    )

if "Carbonyl" in groups:

    interpretation.append(
        "Carbonyl compounds detected."
    )

if "Amide" in groups:

    interpretation.append(
        "Protein or amide structure detected."
    )

if "Aromatic" in groups:

    interpretation.append(
        "Aromatic ring present."
    )

st.subheader("🧠 Interpretation")

for item in interpretation:

    st.write("✔", item)

peakset = set(
    [round(x) for x in peaks]
)

if (
3400 in peakset and
2920 in peakset and
1050 in peakset
):

    st.success(
        "Possible Material: Cellulose"
    )

elif (
1730 in peakset and
2920 in peakset
):

    st.success(
        "Possible Material: PLA Film"
    )

elif (
3400 in peakset and
1630 in peakset
):

    st.success(
        "Possible Material: Protein-Based Film"
    )

elif (
3400 in peakset and
1650 in peakset and
1550 in peakset
):

    st.success(
        "Possible Material: Chitosan"
    )

fig = go.Figure()
fig.add_vrect(
    x0=2500,
    x1=4000,
    annotation_text="Single Bond"
)

fig.add_vrect(
    x0=2000,
    x1=2500,
    annotation_text="Triple Bond"
)

fig.add_vrect(
    x0=1500,
    x1=2000,
    annotation_text="Double Bond"
)

fig.add_vrect(
    x0=500,
    x1=1500,
    annotation_text="Fingerprint"
)

for peak in peaks:

    fig.add_scatter(
        x=[peak],
        y=[1],
        mode="markers+text",
        text=[str(peak)]
    )

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("📚 FTIR Theory Library")

topic = st.selectbox(
    "Select Topic",
    [
        "O-H",
        "N-H",
        "Carbonyl",
        "Amide",
        "Aromatic",
        "Fingerprint Region"
    ]
)

if topic == "Carbonyl":

    st.info("""
Carbonyl stretching generally appears
between 1750–1700 cm⁻¹.

Common in:
• PLA
• Ester
• Ketone
• Aldehyde
• Carboxylic Acid
""")
    
with st.expander(
    "📖 Complete FTIR Functional Group Table"
):
    st.dataframe(
        pd.DataFrame(
            ftir_db,
            columns=[
                "Vibration",
                "Min",
                "Max",
                "Group"
            ]
        )
    )

