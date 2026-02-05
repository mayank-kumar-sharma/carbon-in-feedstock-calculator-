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
