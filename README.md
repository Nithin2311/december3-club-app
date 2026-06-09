# December3.club

An **AI-powered, neuro-inclusive social platform** — safe, accessible, and calm by design.
Built for young adults with intellectual & developmental disabilities (IDD), and anyone left
behind by mainstream social media.

> USF College of Education · NSF I-Corps Spring 2026 · Team #2

This repo is the **foundation skeleton**: a Dockerized full-stack app you bring up with one
command. The *Safe-Posting* moderation feature works end-to-end; every other feature is a
placeholder (stub API + blank UI page) — a shared canvas to co-author.

---

## Stack

| Box     | Tech                              | Path      |
|---------|-----------------------------------|-----------|
| `web`   | Next.js 14 (App Router, Tailwind) | `./web`   |
| `api`   | FastAPI (Python 3.12)             | `./api`   |
| `db`    | Postgres 16 + pgvector            | `./db`    |
| `caddy` | Reverse proxy (`/api/*` → api)    | `./caddy` |

LLM provider: **Google Gemini** (isolated in `api/app/services/gemini.py` — swappable).

---

## Prerequisites

Install once:
- **Docker Desktop** — https://www.docker.com/products/docker-desktop/ (must be **running**)
- **Git**
- A **Google Gemini API key** (free) — https://aistudio.google.com/app/apikey
  *(Only needed for the moderation feature. Everything else boots without it.)*

`make` is optional — every `make` target has a plain `docker compose` equivalent below.

---

## First-time setup (teammates start here)

```bash
# 1. Clone
git clone <REPO_URL> december3-club-app
cd december3-club-app

# 2. Create your local env file (never committed)
cp .env.example .env

# 3. Generate secrets and paste them into .env
make gen-secrets          # prints POSTGRES_PASSWORD=... and SESSION_SECRET=...
#   no make? run:  openssl rand -hex 24   (for POSTGRES_PASSWORD)
#                  openssl rand -hex 32   (for SESSION_SECRET)

# 4. Open .env and set:
#      POSTGRES_PASSWORD=<paste>
#      SESSION_SECRET=<paste>
#      GEMINI_API_KEY=<your key>     # optional; moderation returns 503 without it

# 5. Build + run the whole stack
make up                   # or: docker compose up -d --build
```

Open **http://localhost** 🎉

| URL                          | What                                  |
|------------------------------|---------------------------------------|
| http://localhost             | Web app — feed shell                   |
| http://localhost/compose     | Safe-Posting moderation (works w/ key) |
| http://localhost/status      | Live build roadmap (1/13 features)     |
| http://localhost/api/health  | API health check                       |
| http://localhost/api/features| Feature registry (JSON)                |
| http://localhost/api/docs    | FastAPI interactive docs               |

---

## Everyday commands

| Task                    | make            | docker compose                       |
|-------------------------|-----------------|--------------------------------------|
| Start / rebuild         | `make up`       | `docker compose up -d --build`       |
| Stop (keep data)        | `make down`     | `docker compose down`                |
| Wipe DB + stop          | `make reset`    | `docker compose down -v`             |
| View logs               | `make logs`     | `docker compose logs -f`             |
| Service status          | `make ps`       | `docker compose ps`                  |

---

## Project layout

```
december3-club-app/
├── docker-compose.yml      # one command brings up all 4 boxes
├── Makefile                # up / down / reset / gen-secrets
├── .env.example            # copy to .env (NEVER commit .env)
├── caddy/Caddyfile         # /api/* → api, everything else → web
├── api/                    # FastAPI
│   └── app/
│       ├── main.py         # mounts every router
│       ├── routers/        # one file per feature (moderation works, rest stubbed)
│       ├── services/       # gemini.py — all LLM calls live here
│       └── schemas/        # pydantic request/response models
├── web/                    # Next.js
│   └── src/
│       ├── app/            # one folder per page (compose works, rest placeholder)
│       ├── components/     # shared UI (Nav, Card, Badge, Placeholder)
│       └── lib/            # api.ts — talks to the backend via /api
├── db/init/                # SQL run once on a fresh DB volume
├── docs/                   # ARCHITECTURE.md, FEATURES.md
└── .github/                # CI + PR/issue templates
```

---

## How to build a feature (claim one)

Every placeholder feature = **one API router + one web page**. To make `events` real:

1. **API:** edit `api/app/routers/events.py` — return real data.
2. **UI:** edit `web/src/app/events/page.tsx` — replace the placeholder.
3. **Registry:** flip `implemented: true` for `events` in `api/app/routers/features.py`
   (this updates the `/status` page automatically).
4. Talk to the API from the page via the relative `/api/events` path (Caddy proxies it).

See `docs/FEATURES.md` for the full list and `CONTRIBUTING.md` for the branch/PR workflow.

---

## Troubleshooting

| Symptom                                   | Fix                                                        |
|-------------------------------------------|------------------------------------------------------------|
| `Cannot connect to the Docker daemon`     | Start Docker Desktop, wait for it to say *Running*.        |
| `/compose` returns `GEMINI_API_KEY not set` | Add `GEMINI_API_KEY` to `.env`, then `make up`.          |
| Port 80 already in use                    | Stop the other server, or change the published port in `docker-compose.yml`. |
| Changed code but don't see it             | `make up` rebuilds images. For DB schema changes: `make reset`. |
| Want a clean slate                        | `make reset` (deletes the database volume).               |

---

## Security
- **Never commit `.env`** — it's gitignored. Secrets come from `.env` only.
- Rotate any key that lands in git history.
- The platform is built around *empowerment, not surveillance* — keep it that way.
