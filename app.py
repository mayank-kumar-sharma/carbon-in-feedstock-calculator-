import streamlit as st

st.set_page_config(page_title="Biochar Carbon Fraction Tool", layout="centered")

st.title("🌱 Biochar Carbon Fraction Calculator")

st.write("Select your feedstock and production type to estimate carbon fractions in biochar.")

# -----------------------------
# Feedstock Database
# -----------------------------

data = {
    "Rice husk": {
        "industrial": {"c": "0.60–0.70", "stable": "0.75–0.85"},
        "artisanal": {"c": "0.50–0.60", "stable": "0.65–0.75"},
    },
    "Wood chips": {
        "industrial": {"c": "0.70–0.80", "stable": "0.80–0.90"},
        "artisanal": {"c": "0.55–0.65", "stable": "0.65–0.75"},
    },
    "Corn cobs": {
        "industrial": {"c": "0.60–0.70", "stable": "0.75–0.85"},
        "artisanal": {"c": "0.50–0.60", "stable": "0.60–0.70"},
    },
    "Coconut shells": {
        "industrial": {"c": "0.46–0.64", "stable": "0.65–0.75"},
        "artisanal": {"c": "0.40–0.55", "stable": "0.55–0.65"},
    },
    "Bamboo": {
        "industrial": {"c": "0.65–0.75", "stable": "0.78–0.85"},
        "artisanal": {"c": "0.50–0.60", "stable": "0.65–0.75"},
    },
    "Sugarcane bagasse": {
        "industrial": {"c": "0.55–0.65", "stable": "0.70–0.82"},
        "artisanal": {"c": "0.45–0.55", "stable": "0.60–0.70"},
    },
    "Maize stalks": {
        "industrial": {"c": "0.60–0.72", "stable": "0.72–0.82"},
        "artisanal": {"c": "0.50–0.60", "stable": "0.60–0.70"},
    },
    "Cotton stalks": {
        "industrial": {"c": "0.60–0.70", "stable": "0.72–0.82"},
        "artisanal": {"c": "0.48–0.58", "stable": "0.60–0.70"},
    },
    "Wheat straw": {
        "industrial": {"c": "0.58–0.68", "stable": "0.70–0.80"},
        "artisanal": {"c": "0.45–0.55", "stable": "0.58–0.68"},
    },
    "Rice straw": {
        "industrial": {"c": "0.55–0.65", "stable": "0.70–0.78"},
        "artisanal": {"c": "0.45–0.55", "stable": "0.55–0.65"},
    },
    "Groundnut shells": {
        "industrial": {"c": "0.62–0.72", "stable": "0.75–0.85"},
        "artisanal": {"c": "0.50–0.60", "stable": "0.62–0.72"},
    },
    "Coffee husk": {
        "industrial": {"c": "0.60–0.70", "stable": "0.72–0.82"},
        "artisanal": {"c": "0.48–0.58", "stable": "0.60–0.70"},
    },
    "Palm kernel shells": {
        "industrial": {"c": "0.72–0.82", "stable": "0.82–0.90"},
        "artisanal": {"c": "0.58–0.68", "stable": "0.72–0.82"},
    },
    "Sewage sludge": {
        "industrial": {"c": "0.45–0.60", "stable": "0.65–0.78"},
        "artisanal": {"c": "0.35–0.50", "stable": "0.50–0.65"},
    },
}

# -----------------------------
# User Inputs
# -----------------------------

feedstock = st.selectbox("Select Feedstock", list(data.keys()))

production = st.radio(
    "Production Type",
    ["Industrial", "Artisanal"]
)

prod_key = production.lower()

# -----------------------------
# Output
# -----------------------------

st.subheader("📊 Estimated Carbon Fractions")

c_frac = data[feedstock][prod_key]["c"]
stable_frac = data[feedstock][prod_key]["stable"]

st.success(f"**Carbon Fraction:** {c_frac}")
st.success(f"**Stable Carbon Fraction:** {stable_frac}")

st.info(
    "Values are based on literature ranges. Actual values depend on pyrolysis temperature and process conditions."
)

# Footer
st.markdown("---")
st.caption("Biochar Carbon Fraction Tool | For estimation purposes only")
