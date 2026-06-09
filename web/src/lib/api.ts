// Client + server helper for talking to the API through the Caddy proxy.
// Browser calls go to the relative /api path; SSR uses API_INTERNAL_URL.
const SERVER_BASE = process.env.API_INTERNAL_URL ?? "http://api:8000";

export function apiBase(): string {
  return typeof window === "undefined" ? SERVER_BASE : "/api";
}

export async function apiGet<T>(path: string): Promise<T> {
  const res = await fetch(`${apiBase()}${path}`, { cache: "no-store" });
  if (!res.ok) throw new Error(`GET ${path} -> ${res.status}`);
  return res.json() as Promise<T>;
}
