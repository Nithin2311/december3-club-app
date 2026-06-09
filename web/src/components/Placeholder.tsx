export default function Placeholder({
  title,
  blurb,
  todo,
}: {
  title: string;
  blurb: string;
  todo: string[];
}) {
  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold text-slate-900">{title}</h1>
      <p className="text-slate-700">{blurb}</p>
      <div className="rounded-xl border border-dashed bg-white p-6">
        <p className="mb-2 text-sm font-semibold uppercase tracking-wide text-slate-500">
          Placeholder — to build
        </p>
        <ul className="list-inside list-disc space-y-1 text-slate-700">
          {todo.map((t) => (
            <li key={t}>{t}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}
