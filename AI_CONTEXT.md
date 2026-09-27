# AI context

## Purpose

A Nuxt 4 static site presenting the four reusable skills in this repository: Guidance, Web Design, Web Engineer, and SEO Production Audit.

## Current state

- Framework: Nuxt 4 / Vue 3 in `lime/`
- Package manager: pnpm, with `lime/pnpm-lock.yaml` as the web lockfile
- Production URL: `https://lime.isroot.in`
- Deployment: static generation via `cd lime && pnpm generate`; recommended on Cloudflare Pages, with GitHub Pages automation in `.github/workflows/lime-pages.yml`
- Environment variables: none
- Routes: `/`, `/guidance`, `/web-design`, `/web-engineer`, `/seo-production-audit`; unknown routes use `error.vue`
- Source of truth for skill copy: the matching `SKILL.md` files; the UI summary data lives in `data/skills.ts`

## Design decisions

- Palette: black, dark green, white, and a single acid-green accent; no gradients.
- Typography: Departure Mono for headings and UI labels; Handlee for paragraphs.
- Visual language: editorial field guide / terminal index with sharp edges, ruled lines, and restrained motion.
- SEO: canonical HTTPS URLs, explicit page metadata, robots, sitemap, and noindex for errors.

## Commands

```bash
cd lime
pnpm install --frozen-lockfile
pnpm typecheck
pnpm generate
pnpm dev
```

## Handoff notes

No backend, API, auth, storage, analytics, cookies, or personal-data collection was added. Re-read the repository `guidance`, `web-design`, `web-engineer`, and `seo-production-audit` skills before any future web change. Update `DEPLOYMENT.md` when runtime, domain, build, or environment requirements change.
