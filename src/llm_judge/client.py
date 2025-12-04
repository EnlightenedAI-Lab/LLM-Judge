"""
client.py — Model adapter for LLM Judge.

This file defines `call_model`, which is the standard interface the
evaluation system uses to interact with any language model.

Today it uses a placeholder mock model.
Later you can replace this with:
  • OpenAI API
  • Anthropic API
  • Local model (Ollama, LM Studio)
  • Custom inference servers
"""

from typing import Dict

def call_model(prompt: str) -> str:
    """
    Placeholder model call.

    Returns a deterministic dummy response so the system works end-to-end.
    Replace this with a real model call later.
    """
    return f"[MOCK RESPONSE] Based on the prompt: {prompt}"
