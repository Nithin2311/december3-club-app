"""Chronological, calm feed — no algorithm, no infinite scroll, no ads.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/feed", tags=["feed"])


@router.get("/status")
def status() -> dict:
    return {"feature": "feed", "implemented": False, "todo": "Chronological, calm feed — no algorithm, no infinite scroll, no ads."}
