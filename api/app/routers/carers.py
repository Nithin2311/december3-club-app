"""Carer Accounts — link up to 5 trusted carers (opt-in, non-surveillance).

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/carers", tags=["carers"])


@router.get("/status")
def status() -> dict:
    return {"feature": "carers", "implemented": False, "todo": "Carer Accounts — link up to 5 trusted carers (opt-in, non-surveillance)."}
