"""Feature registry — single source of truth for what exists and its status.

The web app reads this to render the live roadmap (/status). Flip `implemented`
to true (and keep `endpoint` accurate) as each feature ships.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/features", tags=["features"])

FEATURES = [
    {"key": "moderation",  "name": "Safe Posting / Moderation", "category": "Safety",        "endpoint": "/moderation",  "implemented": True},
    {"key": "scam",        "name": "Scam & Bad-actor Warning",  "category": "Safety",        "endpoint": "/scam",        "implemented": False},
    {"key": "identity",    "name": "Identity Verification",     "category": "Safety",        "endpoint": "/identity",    "implemented": False},
    {"key": "writing",     "name": "Smart Writing Assistant",   "category": "Communication", "endpoint": "/writing",     "implemented": False},
    {"key": "voice",       "name": "Voice (TTS / STT)",         "category": "Communication", "endpoint": "/voice",       "implemented": False},
    {"key": "readability", "name": "Reading-level Slider",      "category": "Cognitive",     "endpoint": "/readability", "implemented": False},
    {"key": "captioning",  "name": "Auto-captioning",           "category": "Cognitive",     "endpoint": "/captioning",  "implemented": False},
    {"key": "feed",        "name": "Calm Chronological Feed",   "category": "Community",     "endpoint": "/feed",        "implemented": False},
    {"key": "events",      "name": "Inclusive Event Matching",  "category": "Community",     "endpoint": "/events",      "implemented": False},
    {"key": "marketplace", "name": "Disability-first Market",   "category": "Community",     "endpoint": "/marketplace", "implemented": False},
    {"key": "profiles",    "name": "Profiles (User + Business)","category": "Community",     "endpoint": "/profiles",    "implemented": False},
    {"key": "carers",      "name": "Carer Accounts",            "category": "Independence",  "endpoint": "/carers",      "implemented": False},
    {"key": "auth",        "name": "Auth & Sessions",           "category": "Platform",      "endpoint": "/auth",        "implemented": False},
]


@router.get("")
def list_features() -> dict:
    done = sum(1 for f in FEATURES if f["implemented"])
    return {"total": len(FEATURES), "implemented": done, "features": FEATURES}
