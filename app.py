import streamlit as st

st.set_page_config(page_title="Biochar Carbon Calculator", layout="centered")

# -----------------------------
# Header
# -----------------------------
st.title("🌱 Biochar Carbon Credit Calculator")
st.markdown("Estimate **stable carbon storage** and **CO₂ removal potential** from biochar.")

st.divider()

# -----------------------------
# Constants
# -----------------------------
BIOCHAR_MASS = 1
CO2_CONVERSION = 3.67
EMISSION_DEDUCTION = 0.15

# -----------------------------
# Feedstock Data
# -----------------------------
data = {
    "Rice husk": {"industrial": (0.60, 0.75), "artisanal": (0.50, 0.65)},
    "Wood chips": {"industrial": (0.55, 0.80), "artisanal": (0.55, 0.65)},
    "Corn cobs": {"industrial": (0.71, 0.75), "artisanal": (0.50, 0.60)},
    "Coconut shells": {"industrial": (0.45, 0.65), "artisanal": (0.40, 0.55)},
    "Bamboo": {"industrial": (0.62, 0.78), "artisanal": (0.50, 0.65)},
    "Sugarcane bagasse": {"industrial": (0.58, 0.70), "artisanal": (0.45, 0.60)},
    "Maize stalks": {"industrial": (0.73, 0.72), "artisanal": (0.50, 0.60)},
    "Cotton stalks": {"industrial": (0.49, 0.72), "artisanal": (0.38, 0.60)},
    "Wheat straw": {"industrial": (0.62, 0.70), "artisanal": (0.45, 0.58)},
    "Rice straw": {"industrial": (0.61, 0.70), "artisanal": (0.45, 0.55)},
    "Groundnut shells": {"industrial": (0.62, 0.75), "artisanal": (0.50, 0.62)},
    "Coffee husk": {"industrial": (0.60, 0.72), "artisanal": (0.48, 0.60)},
    "Palm kernel shells": {"industrial": (0.65, 0.82), "artisanal": (0.58, 0.72)},
    "Sewage sludge": {"industrial": (0.42, 0.65), "artisanal": (0.35, 0.50)},
}

# -----------------------------
# Inputs Section
# -----------------------------
st.subheader("🔧 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    feedstock = st.selectbox("Feedstock Type", list(data.keys()))

with col2:
    production = st.radio("Production Method", ["Industrial", "Artisanal"])

prod_key = production.lower()

st.divider()

# -----------------------------
# Button
# -----------------------------
if st.button("Calculate Carbon Impact"):

    c_frac, stable_frac = data[feedstock][prod_key]

    stable_carbon = BIOCHAR_MASS * c_frac * stable_frac
    gross_co2 = stable_carbon * CO2_CONVERSION
    net_credits = gross_co2 * (1 - EMISSION_DEDUCTION)

    st.subheader("📊 Results")

    # Metrics Row
    c1, c2, c3 = st.columns(3)

    c1.metric("🌿 Stable Carbon", f"{stable_carbon:.2f} t C")
    c2.metric("🌍 CO₂ Removed", f"{gross_co2:.2f} tCO₂e")
    c3.metric("💰 Net Credits", f"{net_credits:.2f} tCO₂e")

    st.divider()

    # Details Expander
    with st.expander("📘 Calculation Details"):
        st.write(f"**Carbon fraction used:** {c_frac}")
        st.write(f"**Stable carbon fraction:** {stable_frac}")
        st.write(f"**Biochar mass assumed:** {BIOCHAR_MASS} tonne")
        st.write(f"**CO₂ conversion factor:** 3.67")
        st.write(f"**Emission deduction:** 15%")

    st.success("✅ Calculation complete!")

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Biochar MRV Calculator | Demo Tool 🌱")
st.markdown("💡 Made with ❤️ by **Mayank Kumar Sharma**")
