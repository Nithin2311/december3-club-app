# Contributing to December3.club

Welcome, co-author! This is a shared foundation. Keep it bootable and easy for the next person.

## Setup
1. `cp .env.example .env`, run `make gen-secrets`, set `GEMINI_API_KEY`.
2. `make up`, confirm http://localhost and http://localhost/api/health work.

## Workflow
- Branch off `main`: `git checkout -b feat/<feature>` (e.g. `feat/events-api`).
- One feature per branch. Keep `main` always bootable (`make up` must succeed).
- Open a PR; describe what works and how to test it.

## Where things go
- **New API feature:** replace the stub in `api/app/routers/<feature>.py`. Add schemas in
  `api/app/schemas/`. Keep all LLM calls inside `api/app/services/`.
- **New UI:** replace the placeholder page in `web/src/app/<feature>/page.tsx`. Shared UI in
  `web/src/components/`. Talk to the API via the relative `/api/...` path (Caddy proxies it).
- **DB schema:** add a numbered file in `db/init/` (runs only on a fresh volume; use `make reset`
  to re-init in dev).

## Conventions
- Python: type hints, small routers, no secrets in code.
- TypeScript: `strict` mode, components in PascalCase.
- **Never commit `.env` or API keys.** Secrets come from `.env` only.

## Accessibility is the product
Every UI change must keep it calm and inclusive: high contrast, large tap targets, keyboard
navigable, no autoplay, no infinite scroll, plain language.
