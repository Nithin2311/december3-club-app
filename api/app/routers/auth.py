"""Auth — signup/login, 18+ (13-17 via verified carer), sessions.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/status")
def status() -> dict:
    return {"feature": "auth", "implemented": False, "todo": "Auth — signup/login, 18+ (13-17 via verified carer), sessions."}
