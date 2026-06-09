"""Reading-level slider — rewrite any post Simple/Standard/Advanced, meaning preserved.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/readability", tags=["readability"])


@router.get("/status")
def status() -> dict:
    return {"feature": "readability", "implemented": False, "todo": "Reading-level slider — rewrite any post Simple/Standard/Advanced, meaning preserved."}
