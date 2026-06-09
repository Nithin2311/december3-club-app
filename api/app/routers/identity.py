"""Identity verification — reveal who is really behind an account (anti-catfish).

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/identity", tags=["identity"])


@router.get("/status")
def status() -> dict:
    return {"feature": "identity", "implemented": False, "todo": "Identity verification — reveal who is really behind an account (anti-catfish)."}
