# **ENLIGHTENED AI RESEARCH LAB**
### Advancing the science of reflective stability, internal coherence, and moral alignment in frontier AI systems.

---
# LLM Judge — Reflective Coherence Evaluation  
### A high-clarity, research-grade framework for measuring internal reasoning stability in advanced language models.

LLM Judge is an evaluation instrument designed to make the *internal coherence stability* of language models observable, measurable, and comparable.  
Rather than analyzing only surface responses, LLM Judge examines how a model’s internal reasoning trajectory behaves under reflective pressure.

It is built upon two components:

- **Reflective Alignment Architecture (RAA)**  
- **Reflective Duality Layer (RDL)**

Both originate from *Holm, N. (2025). Reflective Alignment Architecture and the Reflective Duality Layer.*

The current prototype includes a **Level-2 Reflective Viewer (L2)** implemented in Streamlit.

---

## 1. Motivation

Modern language models demonstrate:
- multi-step reasoning  
- self-critique and internal reflection  
- long-horizon planning  
- context-adaptive moral behavior  

Yet nearly all evaluation frameworks still measure **only the final answer**.

This creates a critical blind spot:

> A model can appear aligned and stable in its outputs while its **internal reasoning trajectory** is brittle, inconsistent, or drifting under pressure.

LLM Judge directly targets this gap by evaluating *how* the model thinks, not just *what* it outputs.

---

## 2. Method: Forward vs Reflective Duality

Each evaluation consists of two coordinated passes:

### **Forward Pass**  
The model answers the prompt normally.

### **Reflective Pass**  
The model is instructed to critique, revise, or re-express its reasoning using a structured reflective instruction.

The RDL then compares the **forward trajectory** and the **reflective trajectory** along several stability axes:

- self-agreement  
- justification quality  
- adherence to constraints and values  
- resistance to perturbation  
- rationalization vs. genuine correction  

These comparisons produce **coherence-stability metrics**, which feed into the dashboard and analytical tools.

---

## 3. Current Prototype Features (v1)

### JSONL Test Harness  
- Define evaluation prompts in `tests.jsonl`  
- Supports multiple model APIs through lightweight adapters  

### Paired Forward + Reflective Execution Loop  
- Saves full reasoning traces to `results/*.jsonl`  
- Captures prompts, responses, metadata, and metrics  

### Level-2 Reflective Dashboard  
Allows investigation into:
- per-prompt stability  
- model-level aggregates  
- drift/collapse/rationalization signatures  
- forward vs reflective comparison  

### Early RDL-Based Metrics  
- coherence and divergence measurement  
- basic stability index plots  
- extensible metric hook system  

### Model-Agnostic Design  
Compatible with OpenAI, Anthropic, and local hosted models.

---

## 4. Repository Structure

```
LLM-Judge/
│
├── src/llm_judge/
│   ├── client.py
│   ├── runner.py
│   ├── metrics_core.py
│   ├── tests.jsonl
│   └── __init__.py
│
├── results/
│   └── .gitkeep
│
├── docs/
│   ├── overview.md
│   ├── architecture.png
│   └── screenshots/
│
├── README.md
└── requirements.txt
```

---

## 5. Installation

```bash
git clone https://github.com/EnlightenedAI-Lab/LLM-Judge.git
cd LLM-Judge
pip install -r requirements.txt
```

---

## 6. Run a Test Evaluation

```bash
python src/llm_judge/runner.py \
  --model gpt-4o-mini \
  --tests src/llm_judge/tests.jsonl \
  --out results/run1.jsonl
```

---

## 7. Compute Metrics Programmatically

```python
from llm_judge.metrics_core import compute_metrics

forward = "Example forward answer."
reflective = "Revised answer after reflection."

compute_metrics(forward, reflective)
```

---

## 8. Purpose and Vision

LLM Judge is a step toward reflective-layer evaluation:  
a methodology for examining whether the *process* by which an AI system arrives at its outputs remains stable, interpretable, and alignable.

Future iterations incorporate:

- Reflective Duality Layer (full mathematical formulation)  
- richer trajectory comparisons  
- multi-model benchmarking  
- research-grade visualization modules  

LLM Judge aims to become a foundational instrument for studying the internal coherence properties of next-generation AI systems.
