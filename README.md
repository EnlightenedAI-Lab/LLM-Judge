# LLM Judge — Reflective Coherence Evaluation

**LLM Judge** is an experimental evaluation instrument for probing the **internal coherence stability** of large language models, rather than just their surface outputs.

It operationalizes the **Reflective Alignment Architecture (RAA)** and the **Reflective Duality Layer (RDL)** proposed in:

> Holm, N. (2025). *Reflective Alignment Architecture and the Reflective Duality Layer.*

The current prototype focuses on a **Level-2 Reflective Viewer (L2)** built in Streamlit.

---

## 1. Motivation

Frontier language models now show:

- multi-step reasoning  
- self-critique and “reflection”  
- long-horizon planning  
- context-dependent moral behavior  

Yet most alignment and safety work still evaluates **only final answers** on benchmarks or curated test sets.

This hides a critical failure mode:

> A model can look stable and “aligned” in its outputs while its **internal reasoning trajectory** is brittle, self-contradictory, or drifting under pressure.

**LLM Judge** is an attempt to make those internal dynamics **observable, measurable, and comparable**.

---

## 2. Core Idea

For each test prompt, LLM Judge runs two paired calls:

1. **Forward pass**  
   - The model answers normally.

2. **Reflective pass**  
   - The model is asked to reflect on, critique, or revise its own reasoning under a structured “reflective prompt.”

The RDL then compares the **forward trajectory** and the **reflective trajectory** along several axes:

- consistency and self-agreement  
- justification quality  
- value / constraint adherence  
- resistance to drift under perturbation  
- presence of rationalization vs. genuine correction  

These are summarized into **coherence-stability metrics**, which the dashboard displays and aggregates.

---

## 3. Current Features (v1 prototype)

- 🔹 **JSONL test harness**  
  - Define evaluation prompts and settings in `tests.jsonl`  
  - Supports multiple models / APIs (via simple adapter pattern)

- 🔹 **Paired forward + reflective evaluation loop**  
  - Saves full traces to `results_L2.jsonl` (or similar)  
  - Each record includes prompts, responses, scores, and metadata

- 🔹 **Level-2 Streamlit dashboard (`streamlit_app_L2.py`)**
  - Upload a results file and explore:
    - per-prompt metrics  
    - model-level aggregates  
    - failure signatures (drift, rationalization, collapse, etc.)  
  - Filter by model, test set, or tag  
  - Inspect individual traces (forward vs reflective)

- 🔹 **Early RDL-based metrics**
  - Coherence / divergence scores between trajectories  
  - Simple “stability index” visualizations  
  - Hooks for plugging in new metrics as the theory matures

- 🔹 **Model-agnostic design**
  - Anything callable via an API (OpenAI, Anthropic, local models) can be wired in through a small adapter.

---

## 4. Repository Structure

Suggested structure (adjust to match your local files):

```bash
LLM-Judge/
├─ app/
│  ├─ streamlit_app_L2.py        # L2 Reflective Viewer dashboard
│  ├─ requirements.txt           # Python dependencies
│  └─ config.example.yaml        # Example config for API keys, endpoints
│
├─ core/
│  ├─ judge.py                   # Main forward+reflective evaluation loop
│  ├─ rdl_metrics.py             # Coherence / stability metric implementations
│  ├─ models_openai.py           # Example model adapter(s)
│  └─ utils.py
│
├─ tests/
│  ├─ tests_example.jsonl        # Example test set
│  └─ results_example_L2.jsonl   # Sample results for trying the dashboard
│
├─ docs/
│  ├─ overview.md                # Longer conceptual description
│  ├─ architecture.png           # System diagram
│  └─ screenshots/               # Dashboard screenshots
│
└─ README.md
---

## 🚀 Installation / Quick Start

git clone https://github.com/EnlightenedAI-Lab/LLM-Judge.git
cd LLM-Judge
pip install -r requirements.txt

## 🧪 Run a Test Evaluation

python src/llm_judge/runner.py \
  --model gpt-4o-mini \
  --tests src/llm_judge/tests.jsonl \
  --out results/run1.jsonl

## 📊 View the Reflective Stability Metrics

from llm_judge.metrics_core import compute_metrics

forward = "Example forward answer."
reflective = "Revised answer after reflection."

compute_metrics(forward, reflective)

## 📁 Project Structure

LLM-Judge/
├── src/llm_judge/
│   ├── client.py
│   ├── runner.py
│   ├── metrics_core.py
│   ├── tests.jsonl
│   └── __init__.py
├── results/
│   └── .gitkeep
├── docs/
├── README.md
└── requirements.txt
