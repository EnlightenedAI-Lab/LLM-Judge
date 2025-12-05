# Datasets & Artifacts

This page summarizes the datasets, evaluation logs, and related artifacts produced by the **Enlightened AI Research Lab** for the LLM Judge / Reflective Alignment Architecture (RAA) program.

We distinguish between:

- **Core alignment datasets** — curated for reflective coherence and stability analysis.  
- **Supporting artifacts** — logs, traces, diagrams, and documentation that make experiments auditable.  
- **Planned releases** — clearly marked as *In preparation*.

---

## 1. Released Datasets

### 1.1 Reflective Alignment Lexicon (v1.0)

- **Type:** Conceptual / terminological dataset  
- **Scope:** Core vocabulary for reflective alignment, coherence, and moral intelligence  
- **Entries:** ~300+ terms (v1.0)  
- **Format:** PDF (primary), with planned structured exports (CSV / JSON)  
- **Host:** Zenodo  
- **DOI / Link:** https://zenodo.org/records/17751263  

**Description**

The Reflective Alignment Lexicon defines the conceptual backbone of the RAA and LLM Judge work.  
It provides:

- Canonical names and short definitions  
- Groupings around reflection, coherence, care, and stability  
- A shared language for research papers, dashboards, and future datasets  

**Intended use**

- To standardize terminology in alignment research  
- To annotate prompts, failure modes, and reasoning traces in later datasets  
- To support interpretable metrics and model-internal audits  

If you use the Lexicon in a paper or project, please cite the Zenodo record above.

---

## 2. Evaluation Logs & Traces

These artifacts are produced when running the L2 Reflective Viewer and related tools.  
Public versions will be released incrementally as we stabilize formats and privacy constraints.

### 2.1 L2 Reflective Coherence Runs (*Planned public sample*)

- **Type:** JSONL evaluation traces  
- **Contents (per row):**
  - Prompt metadata (ID, category, scenario description)  
  - Forward response  
  - Reflective response  
  - Coherence / stability metrics  
  - Tags for drift, collapse, rationalization, and self-correction  
- **Status:** In preparation (selected runs will be anonymized and published)  
- **Planned host:** Zenodo + GitHub `results/` samples  

When released, a dedicated section here will describe:

- Exact schema of each JSONL file  
- Example analysis notebooks  
- How to reproduce the runs with `runner.py` and the dashboards.

---

## 3. Future Dataset Roadmap

We are actively designing the following public releases.  
Details may evolve as the research matures.

### 3.1 Reflective Alignment Dataset (RAA-Eval v1)

- **Goal:** A benchmark dataset for *reasoning-trajectory stability*, not just final answers.  
- **Planned components:**
  - 500–1,000+ prompts spanning ethical ambiguity, temporal drift, constraint-pressure, and self-critique chains  
  - Paired forward + reflective calls per model  
  - Human-curated tags for failure modes and repair patterns  
- **Planned formats:** JSONL + documentation in `docs/`  
- **Status:** Design and pilot phase.

### 3.2 Coherence Metrics Sandbox

- **Goal:** Open repository of derived metrics for:
  - Divergence, collapse, and rationalization patterns  
  - Rigidity and hallucination signatures  
  - Long-horizon self-consistency  
- **Planned artifacts:**
  - CSV/Parquet tables with per-run metrics  
  - Lightweight plotting / analysis notebooks  

---

## 4. Access & Use

Unless otherwise noted, datasets and artifacts released under this repository will be:

- **Free to use for research and safety work**, subject to the license specified in each record.  
- Documented with:
  - Clear schema descriptions  
  - Example code snippets  
  - Versioning notes (v1.0, v1.1, …)  

If you are:

- A **lab or safety team** interested in early access, or  
- A **funder** exploring support for larger-scale dataset curation,

please contact:

- **Email:** research@enlightenedai.ai  
- **Website:** https://www.enlightenedai.ai

We welcome collaboration on joint dataset design, annotation, and validation.

---
