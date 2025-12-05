# LLM Judge — Overview

The LLM Judge is a multi-layer evaluation harness built on the Reflective Alignment Architecture (RAA).

It is designed to:
- Run structured tests against large language models
- Compare forward vs. reflective answers
- Measure reflective coherence (MCI★), stability, and drift
- Provide dashboards (L1–L7) for visual analysis

---

## Core Ideas

### Reflective Alignment Architecture (RAA)
A layered framework (L1–L7) that evaluates not only what a model answers, but how it *reflects* on its own answers over time.

### Reflective Duality Layer (RDL)
The key mechanism that compares:
- Forward answer (F): first response to a prompt  
- Reflective answer (R): response after reflection / critique  
The gap between them is turned into stability and coherence metrics.

### Coherence Metrics
Metrics such as MCI★ and R∇ summarize:
- How consistent the model is with its own prior answers  
- How much it “cares” about correcting mistakes  
- Whether it is drifting, collapsing, or stabilizing  

---

## Layers (L1–L7) in One Glance

- **L1 — Basic Integrity:** sanity checks, formatting, completeness  
- **L2 — Reflective Coherence:** forward vs. reflective answers (this repo’s main focus)  
- **L3 — Longitudinal Drift:** behavior over time / across runs  
- **L4 — Moral & Value Coherence:** consistency with declared principles  
- **L5 — Context & Memory Integrity:** consistency across long contexts  
- **L6 — Adversarial Robustness:** response to traps, jailbreaks, and pressure  
- **L7 — System-Level Stability:** global view, dashboards, and training feedback  

This repository currently implements **L2** in detail and provides scaffolding for **L3–L7**.

---

## Architecture

At a high level:

1. **Tests** → prompts in `tests/*.jsonl`  
2. **Judge** → Python harness (`judge_L2.py`) runs forward + reflective calls  
3. **Metrics** → computed by `metrics_core.py` and L2-specific metric functions  
4. **Results** → written to `results/*.jsonl`, `results/*.json`  
5. **Dashboard** → `streamlit_app_L2.py` visualizes metrics and diagrams (L2 view)

---

## Status

- L2: implemented (Reflective Coherence)  
- L3–L7: placeholders defined, design documented in `/docs/raa_layers.md`  

This is intended as a **research-grade evaluation tool** and a foundation for future alignment work.
