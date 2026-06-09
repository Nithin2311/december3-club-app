"""Smart Writing Assistant — fix grammar/spelling, polish tone, suggest captions.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/writing", tags=["writing"])


@router.get("/status")
def status() -> dict:
    return {"feature": "writing", "implemented": False, "todo": "Smart Writing Assistant — fix grammar/spelling, polish tone, suggest captions."}
