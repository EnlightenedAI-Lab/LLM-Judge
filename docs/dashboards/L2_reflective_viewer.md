# L2 — Reflective Viewer (Mirror-H Dashboard)

The L2 dashboard is the main interface for inspecting forward vs. reflective reasoning.

---

## What it shows

- Forward answer
- Reflective answer
- Comparison
- Metrics (Ψ, R∇, MCI★)
- Run-by-run trace
- Drift or stabilization patterns

---

## Input format

The dashboard expects a results file such as:

results_L2.jsonl

Each entry contains:

- prompt
- forward response
- reflective response
- metrics
- metadata

---

## How to run

streamlit run src/apps/streamlit_app_L2.py

Select a results file in the UI.

---

## Notes

A placeholder diagram (Mirror-H loop) will appear on this page later.
