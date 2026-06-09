import Placeholder from "@/components/Placeholder";

export default function Page() {
  return (
    <Placeholder
      title="Settings"
      blurb="Accessibility and account settings."
      todo={["Reading-level default (Simple / Standard / Advanced)", "Voice input/output (Listen Anywhere / Speak Naturally)", "Calm-mode toggles (no autoplay, no infinite scroll)", "API: /readability, /voice, /auth"]}
    />
  );
}
