import { apiGet } from "@/lib/api";
import { Card, Badge } from "@/components/ui";

type Feature = {
  key: string;
  name: string;
  category: string;
  endpoint: string;
  implemented: boolean;
};
type Registry = { total: number; implemented: number; features: Feature[] };

export const dynamic = "force-dynamic";

export default async function Status() {
  let reg: Registry | null = null;
  let error: string | null = null;
  try {
    reg = await apiGet<Registry>("/features");
  } catch {
    error = "Could not reach the API. Is the stack up (make up)?";
  }

  if (error || !reg) {
    return (
      <div className="space-y-3">
        <h1 className="text-2xl font-bold text-slate-900">Build status</h1>
        <Card className="text-red-700">⚠️ {error}</Card>
      </div>
    );
  }

  const byCategory = reg.features.reduce<Record<string, Feature[]>>((acc, f) => {
    (acc[f.category] ??= []).push(f);
    return acc;
  }, {});

  return (
    <div className="space-y-5">
      <div>
        <h1 className="text-2xl font-bold text-slate-900">Build status</h1>
        <p className="text-slate-700">
          {reg.implemented} of {reg.total} features live. Live data from{" "}
          <code className="text-sm">/api/features</code>.
        </p>
      </div>

      {Object.entries(byCategory).map(([cat, feats]) => (
        <Card key={cat}>
          <h2 className="mb-3 text-lg font-semibold text-slate-900">{cat}</h2>
          <ul className="space-y-2">
            {feats.map((f) => (
              <li key={f.key} className="flex items-center justify-between gap-3">
                <span className="text-slate-800">{f.name}</span>
                <span className="flex items-center gap-2">
                  <code className="text-xs text-slate-500">/api{f.endpoint}</code>
                  <Badge ok={f.implemented} />
                </span>
              </li>
            ))}
          </ul>
        </Card>
      ))}
    </div>
  );
}
