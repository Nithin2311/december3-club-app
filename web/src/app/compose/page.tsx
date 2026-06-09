"use client";

import { useState } from "react";

type Result = {
  status: "safe" | "blocked";
  kindness_score: number;
  message?: string | null;
  reason?: string | null;
  suggestions: string[];
};

const TONE: Record<number, { label: string; color: string }> = {
  1: { label: "Very Harsh", color: "#ef4444" },
  2: { label: "Harsh", color: "#f97316" },
  3: { label: "Neutral", color: "#eab308" },
  4: { label: "Kind", color: "#84cc16" },
  5: { label: "Very Kind", color: "#22c55e" },
};

export default function Compose() {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<Result | null>(null);

  async function submit() {
    setLoading(true);
    setError(null);
    setResult(null);
    try {
      const res = await fetch("/api/moderation", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail ?? `Error ${res.status}`);
      }
      setResult(await res.json());
    } catch (e) {
      setError(e instanceof Error ? e.message : "Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  const tone = result ? TONE[result.kindness_score] ?? TONE[3] : null;

  return (
    <div className="space-y-5">
      <div>
        <h1 className="text-2xl font-bold text-slate-900">Safe Posting</h1>
        <p className="text-slate-700">
          Write a post. Our AI checks it for harmful content and suggests kinder
          alternatives before anything goes live.
        </p>
      </div>

      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="What's on your mind?"
        rows={5}
        className="w-full rounded-lg border border-slate-300 p-3 focus:border-brand focus:outline-none"
      />

      <div className="flex gap-2">
        <button
          onClick={submit}
          disabled={loading || !text.trim()}
          className="rounded-lg bg-brand px-4 py-2 font-medium text-white hover:opacity-90 disabled:opacity-50"
        >
          {loading ? "Checking…" : "Submit Post"}
        </button>
        <button
          onClick={() => { setText(""); setResult(null); setError(null); }}
          className="rounded-lg border border-slate-300 px-4 py-2 text-slate-700 hover:bg-slate-100"
        >
          Clear
        </button>
      </div>

      {error && (
        <div className="rounded-lg bg-red-50 p-3 text-sm text-red-700">⚠️ {error}</div>
      )}

      {result && tone && (
        <div className="space-y-3 rounded-xl border bg-white p-4">
          <div>
            <div className="mb-1 text-sm text-slate-600">
              Kindness Score: <strong>{result.kindness_score}/5</strong> — {tone.label}
            </div>
            <div className="h-2 w-full rounded-full bg-slate-200">
              <div
                className="h-2 rounded-full"
                style={{ width: `${result.kindness_score * 20}%`, background: tone.color }}
              />
            </div>
          </div>

          {result.status === "safe" ? (
            <p className="font-medium text-green-700">✅ {result.message ?? "Post looks good!"}</p>
          ) : (
            <div className="space-y-2">
              <p className="font-medium text-red-700">
                🛑 Harmful content detected{result.reason ? ` — ${result.reason}` : ""}.
              </p>
              <p className="text-sm text-slate-600">Pick a kinder version:</p>
              <div className="space-y-2">
                {result.suggestions.map((s, i) => (
                  <button
                    key={i}
                    onClick={() => { setText(s); setResult(null); }}
                    className="block w-full rounded-lg border border-slate-300 p-2 text-left text-sm hover:bg-brand-soft"
                  >
                    ↑ Use: {s}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
