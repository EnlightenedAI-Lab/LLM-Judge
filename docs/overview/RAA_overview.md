# Reflective Alignment Architecture (RAA) — Overview

The Reflective Alignment Architecture (RAA) is a layered framework for evaluating and improving large language models along **moral coherence**, not just accuracy.

It treats a model as something that can:

1. Act — produce an answer  
2. Reflect — critique or evaluate its own answer  
3. Update — converge toward consistent, stable behavior over time  

RAA organizes this into seven layers (L1–L7). Each layer:

- performs specific evaluations  
- exposes interpretable metrics  
- feeds into the global stability picture (Ψ, R∇, MCI★)  

---

## Why “reflective”?

Standard evaluations only check a model’s *first output*.

RAA introduces a second dimension:

- **Forward answer** — what the model says  
- **Reflective answer** — what the model says *about what it said*  

Comparing the two reveals:

- contradictions  
- rationalization vs. genuine correction  
- drift or collapse  
- stability under pressure  

This dual-process is the core of the **Reflective Duality Layer (RDL)**.

---

## Connection to Mirror-H

Mirror-H provides a structured loop:

1. Forward pass  
2. Reflective pass  
3. Comparison  
4. History over time  

This produces the signals used in L2–L7 dashboards.

See: [Mirror-H overview](MirrorH_overview.md)

---

## Repository links

- Theory → this folder  
- Implementation → `/src/llm_judge/`  
- Dashboards → `/docs/dashboards/`  
- Diagrams → `/docs/diagrams/`
