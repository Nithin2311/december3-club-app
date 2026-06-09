import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        // Calm, low-stimulation palette (accessibility-first).
        brand: { DEFAULT: "#4f46e5", soft: "#eef2ff" },
      },
    },
  },
  plugins: [],
};
export default config;
