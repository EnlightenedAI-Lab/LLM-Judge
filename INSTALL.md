# Installation & Usage Guide

This document explains how to install and run the **LLM Judge – Reflective Coherence Evaluation** system.

It covers:
- Environment and dependencies
- Installing the package
- Running a basic evaluation
- Viewing results in the dashboards
- Repository structure

---

## 1. Requirements

- **Python** 3.10 or later
- A Unix-like shell or PowerShell / Command Prompt
- An OpenAI-compatible API key for running models
- Recommended: use a virtual environment (`venv`)

Clone the repository:

    git clone https://github.com/EnlightenedAI-Lab/LLM-Judge.git
    cd LLM-Judge

---

## 2. Environment Setup

### 2.1 Create and activate a virtual environment

macOS / Linux:

    python3 -m venv .venv
    source .venv/bin/activate

Windows (PowerShell):

    python -m venv .venv
    .venv\Scripts\Activate.ps1

### 2.2 Install Python dependencies

    pip install -r requirements.txt

---

## 3. Configuration

Set your model API key.

macOS / Linux:

    export OPENAI_API_KEY="your_api_key_here"

Windows (PowerShell):

    $env:OPENAI_API_KEY="your_api_key_here"

---

## 4. Repository Layout

    LLM-Judge/
    ├─ src/llm_judge/
    │  ├─ client.py
    │  ├─ runner.py
    │  ├─ tests.jsonl
    │  └─ __init__.py
    ├─ results/
    ├─ docs/
    ├─ ABOUT.md
    ├─ CONTRIBUTING.md
    ├─ FUNDING.md
    ├─ ROADMAP.md
    ├─ SCIENCE.md
    ├─ VISION.md
    ├─ INSTALL.md
    ├─ LICENSE
    └─ requirements.txt

---

## 5. Running an Evaluation

    python src/llm_judge/runner.py \
        --model gpt-4o-mini \
        --tests src/llm_judge/tests.jsonl \
        --out results/run1.jsonl

Output file appears under:

    results/run1.jsonl

Contains:
- forward reasoning
- reflective reasoning
- stability metrics
- metadata

---

## 6. tests.jsonl Structure

Example entry:

    {
      "id": "ethical_001",
      "category": "ethical_ambiguity",
      "prompt": "You are given a morally ambiguous situation...",
      "reflective_prompt": "Re-evaluate your reasoning and check for drift.",
      "metadata": {
        "layer": "L2",
        "tags": ["ethics", "drift_check"]
      }
    }

---

## 7. Viewing Results (L2 Viewer)

Once `streamlit_app_L2.py` exists (per ROADMAP):

Run:

    streamlit run src/llm_judge/streamlit_app_L2.py

Viewer shows:
- divergence
- drift
- collapse signatures
- forward vs reflective comparisons

---

## 8. Troubleshooting

**ModuleNotFoundError**  
Ensure you run from repo root:

    export PYTHONPATH=$PYTHONPATH:$(pwd)/src

**API key errors**  
Check environment variable spelling.

**Missing files**  
Confirm under `src/llm_judge/`.

---

## 9. Contact

Website: https://www.enlightenedai.ai  
Email: research@enlightenedai.ai  
GitHub: https://github.com/EnlightenedAI-Lab

See also: SCIENCE.md, ROADMAP.md, FUNDING.md.
