# Porter's Five Forces Timeline Engine

**Live Application:** https://porter-timeline.vercel.app

An interactive, multi-company strategic analysis web application (PWA) designed to visualize how competitive dynamics and industry moats evolve over multi-decade financial trajectories.

---

## Core Capabilities

* **Multi-Company Portfolio & Dynamic Brand Theming:** Switch seamlessly between **NVIDIA (NVDA)**, **Spotify (SPOT)**, and **Ryanair (RYA / RYAAY)**, with real-time CSS variable injection matching each company's corporate visual identity.
* **Full Bilingual Localization (PL / EN):** Instant switching between Polish and English across both UI controls and all multi-decade historical datasets, KPIs, and strategic rationales.
* **Historical Timeline Scrubbing:** Navigate through distinct strategic eras (up to 2026) to observe structural shifts in competitive positioning alongside annual financial KPIs (revenue, gross margin, operating margin, net income, R&D / operational metrics).
* **Dynamic Five Forces Radar:** Interactive SVG pentagon chart scoring Competitive Rivalry, Supplier Power, Buyer Power, Threat of Substitution, and Threat of New Entry on a 1–5 scale, paired with historical rationale for each selected year.
* **Year-over-Year Strategic Comparison:** Overlay any two historical periods on the radar chart to quantify structural moat expansion or compression.
* **Financial & Segment Breakdown:** Multi-decade revenue trajectory chart supporting both linear and logarithmic scales, combined with revenue mix breakdowns by business segment.
* **Offline-First Progressive Web App (PWA):** Installable as a standalone application on desktop (Windows/macOS) and mobile devices (Android/iOS) with local service worker caching.

---

## Architecture & Extensibility

The engine decouples UI visualization from company datasets through a modular registry pattern:

* `src/data/companies/nvda.json` – NVIDIA Corporation dataset (1993–2026)
* `src/data/companies/spot.json` – Spotify Technology S.A. dataset (2014–2026)
* `src/data/companies/rya.json` – Ryanair Holdings plc dataset
* `src/data/registry.js` – Central company index and selector binding
* `src/i18n/translations.js` – Bilingual dictionary and `pickLang` localization helper
* `src/App.jsx` – Core state management, dynamic theme engine, radar visualization, and comparison engine

To add a new company, create a corresponding bilingual JSON file in `src/data/companies/` (including its `theme` palette) and register it in `src/data/registry.js`.

---

## Tech Stack

* **Frontend:** React, Vite 8, Tailwind CSS
* **Icons & Visualization:** Custom SVG rendering, `lucide-react`
* **PWA & Deployment:** `vite-plugin-pwa` (Workbox), Vercel CI/CD

---

## Local Development

1. Clone the repository: `git clone https://github.com/KrzyszT0f-ui/porter-timeline.git`
2. Enter the directory: `cd porter-timeline`
3. Install dependencies: `npm install`
4. Start development server: `npm run dev`
5. Build production bundle: `npm run build`

---

## License

This project is licensed under the [MIT License](LICENSE).
