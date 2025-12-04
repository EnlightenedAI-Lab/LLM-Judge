# Reflective Alignment Architecture (RAA) — Documentation

This `docs/` folder is the human-readable map of the project.

It explains:

- What the Reflective Alignment Architecture (RAA) is,
- How the LLM Judge layers (L1–L7) work,
- How Mirror-H and the Reflective Duality Layer (RDL) measure stability and care,
- How to run the dashboards and experiments.

---

## 1. Conceptual overview

- [RAA overview](overview/RAA_overview.md)  
- [Mirror-H overview](overview/MirrorH_overview.md)

---

## 2. Dashboards

- [L1 — Continuity Viewer](dashboards/L1_continuity_viewer.md)
- [L2 — Reflective Viewer](dashboards/L2_reflective_viewer.md)
- [L3 — Stability Viewer](dashboards/L3_stability_viewer.md)

---

## 3. Diagrams

All core diagrams live in `docs/diagrams/`:

- `mirror_layers_stack.svg`
- `mirror_loop_map.svg`
- `tri_system_axes.svg`

Placeholders for now—will be replaced with production SVG diagrams later.

---

## 4. Running the tools

See: `api/run_llm_judge_cli.md`

---

## 5. Roadmap

- Add SVG diagrams (Mirror-H, seven-layer architecture, RDL geometry)
- Extend dashboards L4–L7
- Release v1.0 aligned with RAA whitepaper
