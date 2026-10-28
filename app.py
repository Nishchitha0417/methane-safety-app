from datetime import datetime
import os
from fpdf import FPDF
import streamlit as st

st.set_page_config(
    page_title="Methane Lab Safety", page_icon="🛡️", layout="wide"
)

st.title("🛡️ Methane System: Full Integration & Sealing Guide")
st.write(
    "**Researcher:** Nishchitha N K | **Location:** DTU Mechanical Engineering"
)

# --- SECTION 1: SYSTEM TOPOLOGY ---
st.header("1. Component Interconnection")
st.info(
    "Follow this order to maintain the pressure gradient and protect"
    " sensitive sensors."
)
st.markdown("""
1. **Source:** Methane Cylinder → **Regulator** (HBS 200-3-2.5)
2. **Flow Control:** Regulator → **6mm PFA Tubing** → **MFC** (Sensirion SFC5500)
3. **Saturation:** MFC → **Check Valve** (CV-3330) → **Saturation Bottles** (x2)
4. **Analysis:** Saturation Bottles → **4-Way PEEK Valve** → **Sensor Chamber** (QCM/MOF)
5. **Exhaust:** Chamber → **3.2mm PFA Tubing** → **SCAT Safety Cap** → **Vacuum Pump/Fume Hood**
""")

# --- SECTION 2: THE 15-POINT CHECKLIST ---
st.header("2. 15-Point Verification")
col1, col2 = st.columns(2)
with col1:
  v1 = st.checkbox("1. Cylinder secured")
  v2 = st.checkbox("2. Regulator at 0.3 bar")
  v3 = st.checkbox("3. Main valve cracked slowly")
  v4 = st.checkbox("4. MFC Powered (EK-F5X)")
  v5 = st.checkbox("5. 6mm PFA Tubing secure")
  v6 = st.checkbox("6. KQ2H23-06A Adapters seated")
  v7 = st.checkbox("7. Bottle 1 Cap hand-tight")
  v8 = st.checkbox("8. Bottle 2 Cap hand-tight")
with col2:
  v9 = st.checkbox("9. CV-3330 Check Valve (MFC Protection)")
  v10 = st.checkbox("10. PEEK Valve in 'L' path")
  v11 = st.checkbox("11. Sensor Chamber sealed")
  v12 = st.checkbox("12. 3.2mm Outlet to exhaust")
  v13 = st.checkbox("13. SCAT Safety Cap clear")
  v14 = st.checkbox("14. Methane Detector: ON")
  v15 = st.checkbox("15. Pump vented to hood")

# --- SECTION 3: THREAD SEALING & LEAK LOCKDOWN ---
st.header("3. Sealing & Leak Remediation")
t1, t2 = st.columns(2)

with t1:
  st.subheader("How to Seal Threads")
  st.markdown("""
    * **PTFE Tape:** Wrap **clockwise** 3-4 times around male NPT threads (Regulator/Adapters).
    * **Ferrule Alignment:** For **SMC KQ2** or **PEEK** fittings, ensure the tubing is cut square (90°) using a dedicated cutter.
    * **Hand Tight + 1/4 Turn:** Do not over-torque PEEK fittings; they rely on the compression of the cone, not the thread friction.
    """)

with t2:
  st.subheader("How to Lock Down Leaks")
  st.warning(
      "If a leak is detected during the 0.2 bar pressure decay test:"
  )
  st.markdown("""
    1. **Depressurize:** Never tighten a fitting under 0.3 bar pressure.
    2. **Reseat Tubing:** Push the **Saint-Gobain PFA tubing** deeper into the **KQ2 adapter**.
    3. **Replace Ferrule:** If PEEK fittings leak, the plastic ferrule may be deformed; replace with a new one.
    4. **Snoop Test:** Use a certified leak detection spray (e.g., Swagelok Snoop) to confirm zero bubbles.
    """)

# --- SECTION 4: HARDWARE INVENTORY ---
st.header("4. Items & Equipment")
items = {
    "Regulator": "HBS 200-3-2.5 (Set to 0.3 Bar max)",
    "Mass Flow Controller": "Sensirion SFC5500 with EK-F5X",
    "Adapter (6mm to 3.2mm)": "SMC KQ2H23-06A",
    "Check Valve": "IDEX CV-3330 (Prevents backflow to MFC)",
    "Tubing": "Saint-Gobain PFA (6mm and 3.2mm)",
    "Safety Cap": "SCAT Exhaust Filter System",
}
st.table(items)

# --- SECTION 5: REPORT GENERATION ---
if st.button("Generate Compliance PDF"):
  if all([
      v1,
      v2,
      v3,
      v4,
      v5,
      v6,
      v7,
      v8,
      v9,
      v10,
      v11,
      v12,
      v13,
      v14,
      v15,
  ]):
    output_dir = r"M:\Offshore Project\Softwares\Risk assesment"
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, "Methane_Safety_Compliance.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(
        200, 10, txt="Methane System Safety Compliance Report", ln=1, align="C"
    )
    pdf.cell(200, 10, txt=f"Researcher: Nishchitha N K", ln=1)
    pdf.cell(200, 10, txt=f"Location: DTU Mechanical Engineering", ln=1)
    pdf.cell(
        200,
        10,
        txt=f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        ln=1,
    )
    pdf.cell(200, 10, txt="Status: ALL 15 CHECKPOINTS VERIFIED PASSED", ln=1)

    pdf.output(filename)

    st.success(f"✅ Compliance PDF saved successfully to:\n`{filename}`")

    with open(filename, "rb") as file:
      st.download_button(
          label="📥 Download Copy",
          data=file,
          file_name="Methane_Safety_Compliance.pdf",
          mime="application/pdf",
      )
  else:
    st.error(
        "❌ Please complete all 15 checkpoints before generating the report."
    )