"""December3.club API — entrypoint.

Mounts every feature router under /api/* (Caddy strips nothing; routers own
their own prefixes). Moderation is the only fully-working feature today; the
rest are stubs that return {"implemented": false} so the web app can build
against a stable surface.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import (
    auth,
    captioning,
    carers,
    events,
    feed,
    features,
    health,
    identity,
    marketplace,
    moderation,
    profiles,
    readability,
    scam,
    voice,
    writing,
)

app = FastAPI(
    title="December3.club API",
    version="0.1.0",
    description="AI-powered neuro-inclusive social platform.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health at /api/health, features under their own prefixes.
for r in (
    health.router,
    moderation.router,   # WORKING
    writing.router,
    scam.router,
    identity.router,
    voice.router,
    readability.router,
    captioning.router,
    feed.router,
    features.router,
    events.router,
    marketplace.router,
    profiles.router,
    carers.router,
    auth.router,
):
    app.include_router(r)


@app.get("/")
def root() -> dict:
    return {"name": "December3.club API", "docs": "/docs", "health": "/health"}
