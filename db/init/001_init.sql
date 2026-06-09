-- December3.club — initial schema (placeholder).
-- Runs once, only on a fresh database volume. Use `make reset` to re-run in dev.

CREATE EXTENSION IF NOT EXISTS vector;

-- Minimal users table so auth/profile work can start.
CREATE TABLE IF NOT EXISTS users (
    id          BIGSERIAL PRIMARY KEY,
    email       TEXT UNIQUE NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Posts will feed the chronological timeline. Expand as the feed feature is built.
CREATE TABLE IF NOT EXISTS posts (
    id          BIGSERIAL PRIMARY KEY,
    author_id   BIGINT REFERENCES users(id),
    body        TEXT NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
