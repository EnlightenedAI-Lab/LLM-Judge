"""
runner.py — executes forward + reflective evaluation loops for LLM Judge.

This module loads:
- prompts from a JSONL file
- runs forward and reflective calls (placeholder for now)
- computes metrics using metrics_core.py
- writes outputs to results_L2.jsonl
"""

import json
from typing import Dict, Any
from .metrics_core import compute_metrics


def run_single_test(prompt: str) -> Dict[str, Any]:
    """
    Placeholder forward + reflective calls.
    Replace later with actual API calls.

    forward_answer: model answers normally
    reflective_answer: model re-evaluates under a reflective prompt
    """

    # Placeholder behavior:
    forward_answer = f"Forward: {prompt}"
    reflective_answer = f"Reflective: {prompt}"

    # Compute metrics
    metrics = compute_metrics(forward_answer, reflective_answer)

    return {
        "prompt": prompt,
        "forward": forward_answer,
        "reflective": reflective_answer,
        "metrics": metrics,
    }


def run_all_tests(input_file: str = "tests.jsonl", output_file: str = "results_L2.jsonl"):
    """Run all prompts in tests.jsonl and save results."""
    results = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            prompt = entry.get("prompt", "")
            result = run_single_test(prompt)
            results.append(result)

    with open(output_file, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    print(f"✓ Saved results to {output_file}")


if __name__ == "__main__":
    run_all_tests()
