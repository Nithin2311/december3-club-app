"""Thin Google Gemini wrapper. Single place to swap the LLM provider later."""
from __future__ import annotations

from google import genai
from google.genai import types

from app.config import settings

_client: genai.Client | None = None


def get_client() -> genai.Client:
    """Lazily build and cache the Gemini client."""
    global _client
    if not settings.gemini_api_key:
        raise RuntimeError("GEMINI_API_KEY not set. Add it to .env.")
    if _client is None:
        _client = genai.Client(api_key=settings.gemini_api_key)
    return _client


def generate(prompt: str, system: str, temperature: float = 0.4) -> str:
    """Run one generation and return the raw text."""
    client = get_client()
    resp = client.models.generate_content(
        model=settings.gemini_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=system,
            temperature=temperature,
        ),
    )
    return (resp.text or "").strip()
