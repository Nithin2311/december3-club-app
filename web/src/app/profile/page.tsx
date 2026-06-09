import Placeholder from "@/components/Placeholder";

export default function Page() {
  return (
    <Placeholder
      title="Profile"
      blurb="Your personal and optional business profile."
      todo={["Edit personal profile + accessibility preferences", "Business profile toggle (catalog, storefront)", "API: /profiles"]}
    />
  );
}
