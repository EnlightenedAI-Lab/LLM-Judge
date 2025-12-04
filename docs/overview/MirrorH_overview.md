# Mirror-H — Reflective Mirror Overview

Mirror-H is the structured loop that evaluates how a model reflects on its own reasoning.

---

## Core Loop

1. Forward pass  
2. Reflective pass  
3. Compare forward vs. reflective  
4. Track history over time  

This exposes stability, drift, collapse, and correction patterns.

---

## Metrics

Mirror-H produces the signals used in L2–L7 dashboards:

- Ψ (coherence)
- R∇ (reflective improvement)
- MCI★ (moral coherence index)

---

## Position in RAA

Mirror-H sits inside the full RAA architecture and powers:

- the reflective viewer (L2)
- the stability viewer (L3)
- higher-order layers

See: `RAA_overview.md`
