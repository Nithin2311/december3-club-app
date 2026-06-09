# Feature map

Status legend: ✅ working · 🟡 stub (API returns `implemented:false`, UI is a placeholder)

## Safety
- ✅ **Moderation / Safe Posting** — `POST /api/moderation`, `web/src/app/compose`
- 🟡 **Scam & bad-actor warning** — `/api/scam/status` · proactive phishing/romance-scam alerts
- 🟡 **Identity verification** — `/api/identity/status` · reveal who's really behind an account

## Communication support
- 🟡 **Smart Writing Assistant** — `/api/writing/status` · grammar/tone/caption help
- 🟡 **Voice** — `/api/voice/status` · Listen Anywhere (TTS), Speak Naturally (STT)

## Cognitive accessibility
- 🟡 **Reading-level slider** — `/api/readability/status` · Simple / Standard / Advanced
- 🟡 **Auto-captioning** — `/api/captioning/status` · describe/caption/summarize media

## Community & independence
- 🟡 **Feed** — `/api/feed/status` · chronological, no algorithm, no infinite scroll
- 🟡 **Events** — `/api/events/status` · sensory-friendly / hybrid / accessible matching
- 🟡 **Marketplace** — `/api/marketplace/status` · disability-first, members-only store
- 🟡 **Profiles** — `/api/profiles/status` · personal + business profiles
- 🟡 **Carer Accounts** — `/api/carers/status` · link up to 5, opt-in, non-surveillance
- 🟡 **Auth** — `/api/auth/status` · 18+ (13-17 via verified carer), sessions

> Design principle: tools must feel like an *empowering private assistant*, never a
> *digital babysitter*. (See the customer-discovery pivot in the project notes.)
