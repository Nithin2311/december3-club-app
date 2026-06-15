# December3.club — Next-Day Plan

_Last session: 2026-06-09 · Repo: https://github.com/Nithin2311/december3-club-app (private)_

## Done so far
- Dockerized 4-box foundation (`web` Next.js · `api` FastAPI · `db` pg16+pgvector · `caddy`).
- Working **Safe-Posting moderation** ported from the Gradio MVP → `POST /api/moderation`.
- Placeholder API routers + UI pages for all 12 remaining features.
- Live feature registry (`/api/features`) + `/status` roadmap page.
- Co-author kit: README setup guide, CONTRIBUTING, ARCHITECTURE/FEATURES docs, CI, PR/issue templates.
- Verified bootable from a fresh clone; pushed to GitHub (private), commits authored nithin2311 <palyam@usf.edu>.

## Open items (12 stub features — each = 1 router + 1 page + flip `implemented` flag)
Safety: scam · identity
Communication: writing · voice
Cognitive: readability · captioning
Community: feed · events · marketplace · profiles
Independence: carers
Platform: auth

## Priorities for tomorrow
1. **Auth** — signup/login + sessions. Unblocks profiles, carers, feed ownership. (`api/app/routers/auth.py`, `web/src/app` login/signup pages, `db/init` users table already stubbed.)
2. **Feed** — chronological post create + list (uses `posts` table). Most visible surface.
3. **Light up moderation** — add a valid `GEMINI_API_KEY` to `.env` so `/compose` works end-to-end; gate Submit on a 4xx/5xx path test.
4. **Invite teammates** — add collaborators on the private repo; confirm they can clone + `make up`.

## Open questions
- License? (USF/NSF IP — confirm before any public release.)
- Keep repo private or go public for the cohort?
- Which teammate owns which feature track (Safety / Communication / Community)?
- Gemini vs. a swappable provider for production (key cost / rate limits)?
