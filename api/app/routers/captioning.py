"""Auto-captioning — describe/caption/summarize images and video.

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/captioning", tags=["captioning"])


@router.get("/status")
def status() -> dict:
    return {"feature": "captioning", "implemented": False, "todo": "Auto-captioning — describe/caption/summarize images and video."}
