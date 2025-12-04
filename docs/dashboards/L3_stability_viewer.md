# L3 – Stability Viewer (Long-Horizon Coherence Dashboard)

The L3 dashboard tracks coherence stability across long reasoning horizons and multiple reflective cycles.

---

## What it shows

- Long-horizon drift
- Collapse or stabilization patterns
- Coherence trajectories (Ψ, RV, MCI★)
- Forward vs. reflective separation over many steps
- Stability index over extended runs

---

## Input format

The dashboard expects a results file such as:

results_L3.jsonl

Each entry contains:

- prompt
- forward response
- reflective response
- metrics
- metadata

---

## How to run

streamlit run src/apps/streamlit_app_L3.py

Select a results file in the UI.

---

## Notes

A placeholder diagram (stability trajectory) will appear on this page later.
