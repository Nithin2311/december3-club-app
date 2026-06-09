"""User + business profiles.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/status")
def status() -> dict:
    return {"feature": "profiles", "implemented": False, "todo": "User + business profiles."}
