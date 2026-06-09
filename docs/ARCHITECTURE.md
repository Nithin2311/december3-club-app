# Architecture

```
Browser ──HTTP──> Caddy ──┬── /api/*  ─(strip /api)─> api  (FastAPI :8000) ──> Postgres
                          └── else                  ─> web  (Next.js :3000)
                                                       api ──> Google Gemini
```

- **caddy** is the only box with published ports (80/443). It proxies `/api/*` to the API
  (stripping the `/api` prefix via `handle_path`) and everything else to the web app.
- **web** (Next.js standalone) renders pages. Browser-side calls hit the relative `/api/...`
  path; server-side rendering can use `API_INTERNAL_URL=http://api:8000`.
- **api** (FastAPI) owns business logic + all AI calls. Each feature is one router under
  `api/app/routers/`. The LLM is isolated in `api/app/services/gemini.py` (swap providers there).
- **db** is Postgres 16 with the `pgvector` extension available (for future embeddings/search).

## Request example
`POST http://localhost/api/moderation` → Caddy strips `/api` → `api:8000/moderation` →
`routers/moderation.py` → `services/gemini.py` → Gemini → JSON verdict back to the browser.

## Adding a service later
The current shape is intentionally compact. If a feature needs to scale independently (e.g.
media/auto-captioning), split it into its own box in `docker-compose.yml` and route it in the
Caddyfile — same pattern the team used on the NCCN healthcare app.
