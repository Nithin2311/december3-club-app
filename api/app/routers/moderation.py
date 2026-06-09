"""Safe-Posting moderation — ported from the original Gradio MVP (app.py).

Evaluates a post and returns a structured verdict: safe vs blocked, a kindness
score (1-5), and kinder rewrite suggestions when blocked.
"""
from __future__ import annotations

import json
import re

from fastapi import APIRouter, HTTPException

from app.schemas.moderation import ModerationRequest, ModerationResponse
from app.services import gemini

router = APIRouter(prefix="/moderation", tags=["moderation"])

SYSTEM_PROMPT = """You are a content moderation assistant for a social media platform focused on safe, respectful communication for neurodivergent users.

Your job is to evaluate user-submitted post text and respond ONLY with a valid JSON object — no markdown fences, no extra text.

Rules:
1. If the post is positive, neutral, constructive, or safe -> return:
   {"status": "safe", "message": "Post looks good!", "kindness_score": <integer 1-5>}

2. If the post contains insults, harassment, hate speech, bullying, scam language, threats, or is otherwise harmful/inappropriate -> return:
   {"status": "blocked", "reason": "<short phrase>", "kindness_score": <integer 1-5>, "suggestions": ["<alt 1>", "<alt 2>", "<alt 3>"]}
   - Each suggestion must preserve the original core intent but rephrase it to be respectful, constructive, and kind.

kindness_score: rate the post's tone from 1 (very hostile) to 5 (very kind).

Respond with ONLY the JSON object."""


def _parse(raw: str) -> dict:
    raw = re.sub(r"^```[a-z]*\n?", "", raw, flags=re.IGNORECASE)
    raw = re.sub(r"\n?```$", "", raw, flags=re.IGNORECASE)
    return json.loads(raw)


@router.post("", response_model=ModerationResponse)
def moderate(req: ModerationRequest) -> ModerationResponse:
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code=422, detail="Post text is empty.")

    try:
        raw = gemini.generate(text, system=SYSTEM_PROMPT, temperature=0.4)
        data = _parse(raw)
    except RuntimeError as e:           # missing key / config
        raise HTTPException(status_code=503, detail=str(e))
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="Moderator returned malformed output.")
    except Exception as e:              # upstream API error
        raise HTTPException(status_code=502, detail=f"Moderation failed: {e}")

    return ModerationResponse(
        status=data.get("status", "safe"),
        kindness_score=int(data.get("kindness_score", 3)),
        message=data.get("message"),
        reason=data.get("reason"),
        suggestions=data.get("suggestions", []) or [],
    )
