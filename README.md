# December3.club

An **AI-powered, neuro-inclusive social platform**. Safe, accessible, and calm by design —
built for young adults with intellectual & developmental disabilities (IDD), and anyone left
behind by mainstream social media.

> USF College of Education · NSF I-Corps Spring 2026 · Team #2

This repository is the **foundation skeleton**: a Dockerized full-stack app you bring up with a
single command, with a working *Safe-Posting* moderation feature and placeholder surfaces for
every planned feature — a blank canvas to co-author the UI and the rest of the platform.

---

## Stack

| Box     | Tech                              | Path        |
|---------|-----------------------------------|-------------|
| `web`   | Next.js 14 (App Router, Tailwind) | `./web`     |
| `api`   | FastAPI (Python 3.12)             | `./api`     |
| `db`    | Postgres 16 + pgvector            | `./db`      |
| `caddy` | Reverse proxy (`/api/*` → api)    | `./caddy`   |

LLM provider: **Google Gemini** (swappable — isolated in `api/app/services/gemini.py`).

---

## Quick start

Prereqs: Docker Desktop, `make` (optional), a Gemini API key
(https://aistudio.google.com/app/apikey).

```bash
git clone <your-repo-url> december3-club-app
cd december3-club-app

cp .env.example .env
make gen-secrets        # prints POSTGRES_PASSWORD + SESSION_SECRET — paste into .env
# then edit .env and set GEMINI_API_KEY=...

make up                 # or: docker compose up -d --build
```

Open **http://localhost** → Feed shell. Click **Compose** to try Safe Posting.

| URL                          | What                              |
|------------------------------|-----------------------------------|
| http://localhost             | Web app (feed + features)         |
| http://localhost/compose     | Safe-Posting moderation (working) |
| http://localhost/api/health  | API health check                  |
| http://localhost/api/docs    | FastAPI interactive docs          |

Stop: `make down` · Wipe DB: `make reset`.

---

## What works today vs. placeholders

**Working:** Safe-Posting moderation — `POST /api/moderation` (Gemini), with kindness score +
kinder rewrite suggestions. Wired end-to-end through `web → caddy → api → Gemini`.

**Placeholders** (stub API + blank UI page, ready to build): Smart Writing, Scam/Bad-actor
warnings, Identity verification, Voice (TTS/STT), Reading-level slider, Auto-captioning, Feed,
Events, Marketplace, Profiles, Carer Accounts, Auth. See `docs/FEATURES.md`.

---

## Repo layout

```
december3-club-app/
├── docker-compose.yml      # one command brings up all 4 boxes
├── Makefile                # up / down / reset / gen-secrets
├── .env.example            # copy to .env (never commit .env)
├── caddy/Caddyfile         # routes /api/* → api, everything else → web
├── api/                    # FastAPI: app/routers/*  (moderation works, rest stubbed)
├── web/                    # Next.js: src/app/* pages, src/components/*
├── db/init/                # SQL run once on first DB boot
└── docs/                   # ARCHITECTURE, FEATURES, CONTRIBUTING
```

See `docs/ARCHITECTURE.md` and `CONTRIBUTING.md` before opening a PR.
