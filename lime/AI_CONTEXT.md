# AI Context

**Last updated:** 2026-09-27
**Maintainer:** `Haruki9767` (repository owner; further team details TBD)
**Project status:** Existing public static site; refreshed implementation ready for GitHub Pages deployment

## Purpose and current state

Lime Skills is a public field guide for four reusable web-work skills. The site uses a solid black/light-pink/white theme, Vue SFCs with plain JavaScript, route-specific metadata, local search, and optional GSAP ScrollTrigger motion. The static build includes a script-free custom 404 derived from Vue-rendered markup.

## Source of truth

- Repository: [Haruki9767/lime-skills](https://github.com/Haruki9767/lime-skills), branch `main`
- Product requirements: [`PRD.md`](./PRD.md)
- Quality/security/privacy findings: [`SEO-SECURITY-AUDIT.md`](./SEO-SECURITY-AUDIT.md)
- Migration: [`docs/migrations/2026-09-27-vue-javascript-gsap.md`](./docs/migrations/2026-09-27-vue-javascript-gsap.md)
- Deployment: [`DEPLOYMENT.md`](./DEPLOYMENT.md)
- Production URL: `https://lime.isroot.in` (from `public/CNAME`; verify live settings after deploy)
- Framework/runtime: Nuxt 4.5.2, Vue 3.5.43, Node.js 22, GSAP 3.15.0
- Package manager/lockfile: pnpm 11, `pnpm-lock.yaml`

## Architecture map

```text
Nuxt static routes (Vue SFCs)
  ├── pages/index.vue          -> local skill search and index
  ├── pages/[slug].vue         -> route-validated skill detail pages
  ├── pages/404.vue            -> prerendered noindex error route
  ├── data/skills.js           -> static skill records
  └── composables/useScrollAnimations.js -> dynamic GSAP + ScrollTrigger
          ↓
 pnpm generate -> .output/public -> GitHub Pages artifact
          └── scripts/finalize-static.mjs -> script-free root 404.html
```

There is no API server, database, authentication, authorization boundary, background job, or user data. The existing Handlee font is served by Google Fonts; Departure Mono is stored under `public/fonts/`.

## Commands

```text
Install:  pnpm install --frozen-lockfile
Dev:      pnpm dev --host 0.0.0.0
Lint:     not configured
Typecheck:not configured (authored code is JavaScript)
Test:     not configured
Build:    pnpm generate
Static preview after generate: python3 -m http.server 4176 --bind 127.0.0.1 --directory .output/public
```

## Configuration

No environment variables or secrets are required. `runtimeConfig.public.siteUrl` in `nuxt.config.mjs` is the public canonical URL; change it only with a domain migration.

## Decisions and constraints

- Vue/Nuxt was retained as the healthy existing stack; React was not introduced.
- Authored site code is JavaScript in `.vue`, `.js`, and `.mjs` files; TypeScript-specific tools/config were removed.
- Solid black, pink, and white only; no gradients/green. Keep reduced-motion behavior and the static readable fallback.
- Keep public route slugs and the custom domain stable. Do not add APIs, analytics, cookies, auth, or a backend without explicit authorization and privacy review.
- Keep `404.html` script-free and remove the unused `200.html` shell through the post-generation finalizer.

## Recent work and verification

- Changed areas: app shell/styles, Vue pages/error handling, JS skill data/Nuxt config, GSAP composable, static finalizer, Pages workflow, audit/PRD/deployment/migration docs.
- Checks: frozen-lockfile install; `pnpm generate`; five-page title/H1/canonical/OG checks; sitemap validation; 404 no-JS check; one-main error landmarks; search empty/recovery and direct detail route; contrast calculations; `pnpm audit --audit-level=high`; source-only web-quality scan (0 findings); `git diff --check`; real 390px viewport has no overflow, fully visible H1, and all four cards become visible after scroll.
- Known limitations: no lint/unit/typecheck scripts; full WCAG testing, OS reduced-motion emulation, live DNS/headers, and social image are not covered. See `SEO-SECURITY-AUDIT.md`.
- Migration/security/privacy notes: Google Fonts remains a third party; see audit. GitHub Pages workflow grants deploy permissions only to its deploy job.

## Safe next steps

1. For future deploys, verify the GitHub Pages Actions run, HTTPS, and a real unknown path’s HTTP 404 response using `DEPLOYMENT.md`.
2. Consider a public Open Graph image and whether to self-host Handlee after checking actual audience/privacy requirements.
3. Run the documented frozen install and static generation after future route, package, or theme changes.

## Handoff rules

Read the current relevant repository skills before acting. Preserve the public routes, static architecture, canonical host, no-green/no-gradient palette, reduced-motion behavior, and script-free 404. Do not introduce backend/API/auth/schema or tracking changes without explicit authorization.
