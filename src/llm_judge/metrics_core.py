"""
metrics_core.py — core metric computations for LLM Judge.

This module defines the coherence-stability metrics used across
the L1–L3 viewers: ψ (psi), R∇ (reflective gradient), and MCI★
(moral coherence index).
"""

from typing import Dict, Any


def compute_metrics(forward: str, reflective: str) -> Dict[str, Any]:
    """
    Compute simple placeholder metrics comparing the forward vs reflective answers.
    The real RDL-based computations will replace this placeholder later.

    Returns a dictionary containing:
      - psi: coherence score between the two responses
      - rgrad: direction/magnitude of reflective correction
      - mci_star: early moral-coherence stability proxy
    """

    # Placeholder naive metric
    psi = 1.0 if forward.strip() == reflective.strip() else 0.5

    # Change in reasoning direction (very basic proxy)
    rgrad = len(reflective) - len(forward)

    # Stability proxy
    mci_star = max(0.0, 1.0 - abs(rgrad) / 500)

    return {
        "psi": psi,
        "rgrad": rgrad,
        "mci_star": mci_star,
    }
