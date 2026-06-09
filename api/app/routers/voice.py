"""Voice I/O — Listen Anywhere (TTS) and Speak Naturally (STT).

PLACEHOLDER — not yet implemented. Returns a stub so the UI can wire against
a stable contract. Replace the body when building this feature.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/voice", tags=["voice"])


@router.get("/status")
def status() -> dict:
    return {"feature": "voice", "implemented": False, "todo": "Voice I/O — Listen Anywhere (TTS) and Speak Naturally (STT)."}
