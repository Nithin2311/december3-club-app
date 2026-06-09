import Link from "next/link";

export default function Home() {
  return (
    <div className="space-y-8">
      <section className="rounded-2xl bg-brand-soft p-6">
        <h1 className="text-2xl font-bold text-slate-900">Making social media truly social.</h1>
        <p className="mt-2 text-slate-700">
          A calm, safe, accessible space. AI helps you post kindly, spot bad actors,
          and understand anything — without surveillance.
        </p>
        <Link
          href="/compose"
          className="mt-4 inline-block rounded-lg bg-brand px-4 py-2 font-medium text-white hover:opacity-90"
        >
          Try Safe Posting →
        </Link>
      </section>

      <section>
        <h2 className="mb-3 text-lg font-semibold text-slate-900">Your feed</h2>
        <div className="rounded-xl border border-dashed bg-white p-8 text-center text-slate-500">
          Feed placeholder — chronological, no algorithm, no infinite scroll.
          <br />Posts will appear here once the feed API is built.
        </div>
      </section>
    </div>
  );
}
