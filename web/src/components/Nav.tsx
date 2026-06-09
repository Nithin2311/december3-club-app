import Link from "next/link";

const LINKS: { href: string; label: string }[] = [
  { href: "/", label: "Feed" },
  { href: "/compose", label: "Compose" },
  { href: "/events", label: "Events" },
  { href: "/marketplace", label: "Marketplace" },
  { href: "/profile", label: "Profile" },
  { href: "/carers", label: "Carers" },
  { href: "/settings", label: "Settings" },
  { href: "/status", label: "Status" },
];

export default function Nav() {
  return (
    <header className="border-b bg-white">
      <nav className="mx-auto flex max-w-3xl flex-wrap items-center gap-4 px-4 py-3">
        <Link href="/" className="text-lg font-bold text-brand">December3.club</Link>
        <div className="flex flex-wrap gap-3 text-sm text-slate-600">
          {LINKS.map((l) => (
            <Link key={l.href} href={l.href} className="hover:text-brand">{l.label}</Link>
          ))}
        </div>
      </nav>
    </header>
  );
}
