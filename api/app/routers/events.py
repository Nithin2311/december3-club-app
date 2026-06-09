"""Smart event matching — flag Sensory-Friendly / Hybrid / accessible events.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/events", tags=["events"])


@router.get("/status")
def status() -> dict:
    return {"feature": "events", "implemented": False, "todo": "Smart event matching — flag Sensory-Friendly / Hybrid / accessible events."}
