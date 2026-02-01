import streamlit as st

st.set_page_config(page_title="Biochar Carbon Calculator", layout="centered")

st.title("🌱 Biochar Carbon Credit Calculator")

st.write("Estimate stable carbon and CO₂ removal from biochar.")

# -----------------------------
# Constants
# -----------------------------
BIOCHAR_MASS = 1  # tonne
CO2_CONVERSION = 3.67
EMISSION_DEDUCTION = 0.15

# -----------------------------
# Feedstock Data
# -----------------------------
data = {
    "Rice husk": {"industrial": (0.65, 0.80), "artisanal": (0.55, 0.70)},
    "Wood chips": {"industrial": (0.75, 0.85), "artisanal": (0.60, 0.70)},
    "Corn cobs": {"industrial": (0.65, 0.80), "artisanal": (0.55, 0.65)},
    "Coconut shells": {"industrial": (0.55, 0.70), "artisanal": (0.45, 0.60)},
    "Bamboo": {"industrial": (0.70, 0.82), "artisanal": (0.55, 0.70)},
    "Sugarcane bagasse": {"industrial": (0.60, 0.76), "artisanal": (0.50, 0.65)},
    "Maize stalks": {"industrial": (0.66, 0.77), "artisanal": (0.55, 0.65)},
    "Cotton stalks": {"industrial": (0.65, 0.77), "artisanal": (0.53, 0.65)},
    "Wheat straw": {"industrial": (0.63, 0.75), "artisanal": (0.50, 0.63)},
    "Rice straw": {"industrial": (0.60, 0.74), "artisanal": (0.50, 0.60)},
    "Groundnut shells": {"industrial": (0.67, 0.80), "artisanal": (0.55, 0.67)},
    "Coffee husk": {"industrial": (0.65, 0.77), "artisanal": (0.53, 0.65)},
    "Palm kernel shells": {"industrial": (0.77, 0.86), "artisanal": (0.63, 0.77)},
    "Sewage sludge": {"industrial": (0.52, 0.72), "artisanal": (0.42, 0.58)},
}

# -----------------------------
# Inputs
# -----------------------------
feedstock = st.selectbox("Select Feedstock", list(data.keys()))
production = st.radio("Production Type", ["Industrial", "Artisanal"])

prod_key = production.lower()

# -----------------------------
# Button
# -----------------------------
if st.button("Calculate Carbon Impact"):

    c_frac, stable_frac = data[feedstock][prod_key]

    # Calculations
    stable_carbon = BIOCHAR_MASS * c_frac * stable_frac
    gross_co2 = stable_carbon * CO2_CONVERSION
    net_credits = gross_co2 * (1 - EMISSION_DEDUCTION)

    st.subheader("📊 Results")

    st.write(f"**Carbon fraction used:** {c_frac}")
    st.write(f"**Stable carbon fraction used:** {stable_frac}")

    st.success(f"🌿 Stable carbon stored: **{stable_carbon:.2f} tonnes C**")
    st.success(f"🌍 Gross CO₂ removed: **{gross_co2:.2f} tCO₂e**")
    st.success(f"💰 Net carbon credits: **{net_credits:.2f} tCO₂e**")

    st.info("Assumptions: 1 tonne biochar, CO₂/C=3.67, 15% emission deduction.")

# Footer
st.markdown("---")
st.caption("Biochar calculator – estimation tool")
