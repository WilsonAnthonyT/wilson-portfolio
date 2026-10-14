# Wilson Antony Thang — Portfolio V3

An interactive portfolio for software engineering, applied AI, mobile, and embedded systems, using a restrained Neo-Tokyo-inspired dark aesthetic and Traditional Chinese section accents.

## What is in this package?

- **`src/`** — Next.js App Router / React / TypeScript production source.
- **`public/assets/`** — self-contained, original illustrative SVG art (not screenshots from the repositories).
- **`preview/`** — a standalone HTML/CSS/JavaScript approximation with functional interaction demos. It does not require npm; open `preview/index.html` in a browser. The preview and Next implementation are separate, so some detailed case-study prose differs; `src/` is the authoritative source.
- **`tools/`** — scripts generating the SVG art and standalone preview, plus offline browser interaction tests.
- **`Wilson_Antony_Thang_Resume_Public.pdf`** in `public/` and `preview/` — a public copy of the supplied résumé with the phone number redacted. Your supplied original is not distributed in this project.
- **`desktop-first-screen.png`** / **`mobile-first-screen.png`** and longer screenshots — inspected standalone preview renders.

## Install and run the real Next.js website

Prerequisites: Node.js 20+ and npm with an internet connection for installing dependencies.

```bash
npm install
npm run dev
```

Open http://localhost:3000. To verify the actual production code:

```bash
npm run typecheck
npm run build
```

With `output: 'export'`, the build produces the `out/` directory.

**Verification limitation for this delivery:** npm registry access is unavailable in the authoring environment. Consequently the dependencies could not be installed and the Next.js build/type check has **not** been run successfully. All 8 authored TypeScript/TSX files passed a syntax-transpilation check using the globally installed TypeScript compiler. The **separate standalone preview** was rendered with Chromium and its interactions tested.

## Deploy on Cloudflare Pages

1. Push this source repository to GitHub.
2. Create a Cloudflare Pages project and connect the repository.
3. Framework preset: Next.js (Static HTML Export) or none.
4. Build command: `npm run build`.
5. Output directory: `out`.
6. Confirm deployment and the real domain's links, metadata, mobile rendering, and accessibility.

No database or public AI API key is required. Terminal and project labs are local UI interactions, not backend services.

## Architecture

- `src/content/projects.ts` — typed project content and facts. Update this file when correcting descriptions or adding case studies.
- `src/components/Portfolio.tsx` — homepage sections, archive, and footer.
- `src/components/Interactive.tsx` — terminal, pointer-reactive cards, focus tabs, simulations, theme, galleries.
- `src/components/CaseStudy.tsx` — reusable project detail layout.
- `src/app/globals.css` — custom responsive design system; Tailwind included for future expansion.
- `src/app/projects/[slug]/page.tsx` — statically generated project routes.

## Projects and authenticity

Project descriptions draw from the provided résumé and the user's supplied GitHub profile. The original supplied résumé describes a top-scoring C++ project (among 30 teams), 8051 multithreading, SaveWiser, and Goal Digger work.

**Artwork disclaimer:** Each project visual is an original explanatory **concept illustration**, not a real application screenshot or proof of project performance. Replace these with your own screenshots before public launch, then update the alt text and gallery captions.

**Contribution disclaimer:** Goal Digger is a team project. The résumé supports general contributions to architecture, UI/UX, integration, debugging, and demo preparation, not ownership of individual modules. Confirm module-level responsibility before expanding the case study.

**Technical simulations:** The Goal Digger fallback explorer visualizes repository-described paths; it is not a live call to Firebase or Gemini. The 8051 thread simulation is not an instruction-accurate emulator. The RPG mini interaction is not the original game's code or assets.

**Pending items:** Actual screenshots, exact team contributions, 8051 repository link if available, and a final review of portfolio public contact information.

## Known gaps to close before publication

- Run `npm install`, `npm run typecheck`, and `npm run build` on a connected machine.
- Replace project concept art with actual screenshots and refine the deeper writeups from source code and your individual work.
- Conduct Lighthouse, keyboard-only and screen-reader checks on a **deployed** Next.js build.
- Verify every link after deployment.

## Static standalone preview browser tips

Some browsers restrict `file://` access or clipboard permissions. If an interaction fails in a file tab, run a local HTTP server:

```bash
cd preview
python -m http.server 8080
```

Then open http://localhost:8080.
