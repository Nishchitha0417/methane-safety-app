# methane-safety-app
A risk assesment app for aqeous methane


# 🛡️ Methane Gas Handling & Safety Compliance App

An interactive, web-based laboratory safety checklist and integration workflow designed for experimental methane gas flow systems. Built with **Streamlit** and hosted on **Streamlit Community Cloud**, this tool guides researchers through component assembly, mandatory 15-point verification, leak remediation protocols, and standard compliance report generation.

---

## 🔬 Project Overview

* **Primary Investigator / Researcher:** Nishchitha N K
* **Affiliation:** DTU Mechanical Engineering
* **Purpose:** Ensure systematic verification and documentation of experimental methane gas setup integrity prior to execution.

---

## 🛠️ System Topology & Flow Sequence

To maintain proper pressure gradients and prevent backflow or sensor contamination, components must be assembled in the following sequence:

1. **Gas Source:** Methane Cylinder → **Regulator** (HBS 200-3-2.5)
2. **Flow Control:** Regulator → **6mm PFA Tubing** → **MFC** (Sensirion SFC5500)
3. **Saturation:** MFC → **Check Valve** (CV-3330) → **Saturation Bottles** (x2)
4. **Analysis:** Saturation Bottles → **4-Way PEEK Valve** → **Sensor Chamber** (QCM/MOF)
5. **Exhaust:** Sensor Chamber → **3.2mm PFA Tubing** → **SCAT Safety Cap** → **Vacuum Pump / Fume Hood**

---

## ✨ Features & Functionality

* **Interactive 15-Point Safety Verification:** Complete checklist covering cylinder stability, tubing seat depth, adapter checks, active leak detectors, and exhaust integrity.
* **Sealing & Leak Remediation Protocols:** Quick reference guides for NPT thread wrapping (PTFE tape rules), PEEK compression fitting limits, and 0.2 bar pressure decay lockdown steps.
* **Equipment & Fitting Inventory:** Itemized overview of active system hardware (SMC adapters, IDEX check valves, Saint-Gobain PFA tubing).
* **Automated Compliance Report:** Generates a timestamped PDF safety compliance report upon passing all 15 checklist criteria.

---

## 📦 System Hardware Inventory

| Component | Description / Specification |
| :--- | :--- |
| **Regulator** | HBS 200-3-2.5 (Set to 0.3 Bar max delivery) |
| **Mass Flow Controller** | Sensirion SFC5500 with EK-F5X evaluation kit |
| **Tubing Adapter** | SMC KQ2H23-06A (6mm to 3.2mm transition) |
| **Check Valve** | IDEX CV-3330 (Prevents backflow protection for MFC) |
| **Tubing** | Saint-Gobain PFA (6mm outer diameter & 3.2mm outer diameter) |
| **Exhaust Safety** | SCAT Exhaust Filter System with integrated safety cap |

---

## 🚀 Local Installation & Execution

If you wish to run this application locally on your PC:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Nishchitha0417/methane-safety-app.git](https://github.com/Nishchitha0417/methane-safety-app.git)
   cd methane-safety-app
