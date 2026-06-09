"""Disability-first marketplace — sell art/crafts/services from an accessible profile.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/marketplace", tags=["marketplace"])


@router.get("/status")
def status() -> dict:
    return {"feature": "marketplace", "implemented": False, "todo": "Disability-first marketplace — sell art/crafts/services from an accessible profile."}
