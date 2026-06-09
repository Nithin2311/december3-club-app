"""Proactive bad-actor / scam + phishing warning before the user engages.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/scam", tags=["scam"])


@router.get("/status")
def status() -> dict:
    return {"feature": "scam", "implemented": False, "todo": "Proactive bad-actor / scam + phishing warning before the user engages."}
