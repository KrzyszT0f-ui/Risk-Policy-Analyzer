# Porter's Five Forces Timeline Engine

An interactive, bilingual (**EN / PL**) Progressive Web App (PWA) for multi-decade competitive strategy and financial trajectory analysis, powered by an **in-browser Edge AI analyst (WebGPU + WebLLM)**.

**Live Demo:** [porter-timeline.vercel.app](https://porter-timeline.vercel.app)

---

## Why This Project Exists

Most strategy frameworks are presented as static snapshots, while most AI wrappers suffer from recurring API costs, data privacy trade-offs, and numerical hallucinations. 

This engine bridges **corporate financial analysis** and **client-side AI engineering**:
1. **Longitudinal Strategic Tracking:** Maps up to 30+ years of historical financial KPIs alongside year-by-year **Porter's Five Forces** scoring (`1–5`), segment breakdowns, and strategic catalysts derived from primary SEC filings (Form 10-K / 20-F) and annual reports.
2. **Zero-Cost Edge AI Analyst:** Runs a quantized **Qwen 2.5 3B Instruct** model (`q4f16_1-MLC`) directly on the user's GPU inside a dedicated Web Worker—requiring zero backend servers, zero API keys, and zero inference fees.

---

## Covered Companies & Datasets

Each company dataset is structured in a modular JSON registry (`src/data/companies/`) with custom brand theming and full Polish/English localization:

| Ticker | Company | Coverage | Key Strategic Arcs |
| :--- | :--- | :--- | :--- |
| **NVDA** | NVIDIA Corporation | **1995 – FY2027 YTD** (33 periods) | Pre-IPO multimedia chips → GeForce 256 & Xbox → ATI duopoly & nForce → CUDA & Tegra pivot → Deep Learning inflection (Pascal/Volta) → Generative AI & Blackwell/Rubin full-stack dominance. |
| **RYA / RYAAY** | Ryanair Holdings plc | **1997 – FY2026** (30 years) | Dublin/NASDAQ IPO → Post-9/11 & EU deregulation expansion → Fuel hedging & ancillary unbundling → COVID-19 grounding trough (`FY2021`) → Post-pandemic fare & load factor recovery (`94%`). |
| **SPOT** | Spotify Technology S.A. | **2014 – 2026** (13 years) | Pre-IPO hypergrowth & label supplier power (`5/5`) → Direct Listing (`2018`) → Podcast/audiobook diversification → Margin inflection & first full-year operating profit (`2024–2026`). |

---

## Key Features

* **Interactive Timeline & Radar Comparison:** Scrub across decades with synchronized SVG revenue trajectories (Log & Linear scales), segment mix bars, and an overlaid 5-axis radar chart comparing any two historical years side-by-side.
* **Hybrid Edge AI Chat (`ChatWidget.jsx`):**
  * **Hardware Detection & Explicit Consent:** Automatically probes `navigator.gpu` and `navigator.deviceMemory`. Desktop WebGPU users receive an explicit opt-in prompt before caching the ~1.9 GB model weights in the browser's Cache API.
  * **Graceful Fallback:** On mobile devices or browsers without WebGPU support, the widget degrades cleanly into a one-click structured prompt exporter for external LLMs.
  * **Deterministic Context Injection:** Instead of feeding an entire 30-year JSON file into a small context window (which degrades 3B model accuracy), a regex parser extracts specific years mentioned in the user's query and injects only the matching periods plus active slider selections at `temperature: 0.01`.
* **Dynamic Brand Theming & Full i18n:** Switching companies dynamically updates CSS custom properties (`--accent`, `--bg-main`, `--bg-card`) and resets chat context to prevent cross-company data bleed.
* **Offline-Ready PWA:** Configured with `vite-plugin-pwa` and custom Workbox `globIgnores` so the core application precaches in ~520 KiB while heavy WebLLM runtime chunks load lazily on demand.

---

## Tech Stack

* **Frontend:** React 19, Vite, Tailwind CSS (`@tailwindcss/vite`), Lucide Icons
* **In-Browser AI:** `@mlc-ai/web-llm` (`Qwen2.5-3B-Instruct-q4f16_1-MLC`), WebGPU, Web Workers (`llm.worker.js`), Browser Cache API
* **PWA & Deployment:** `vite-plugin-pwa` (Workbox), Vercel CI/CD via GitHub

---

## Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/KrzyszT0f-ui/porter-timeline.git
cd porter-timeline

# 2. Install dependencies
npm install

# 3. Start local development server
npm run dev

# 4. Build production bundle
npm run build
