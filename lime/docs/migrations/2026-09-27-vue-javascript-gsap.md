# Migration: Lime Vue/JavaScript, GSAP, and GitHub Pages fallback

**Status:** Complete
**Owner:** Repository maintainer
**Date:** 2026-09-27
**Related change:** `Haruki9767/lime-skills`, `main` (commit recorded in Git history)

## Context

The Lime site was an existing Nuxt/Vue static site with authored TypeScript configuration/data. The user requested an all-Vue/JavaScript frontend, a solid black/light-pink/white palette without gradients, smooth GSAP scroll motion, bug fixes, and a push to `main`. Review also found stale/incorrect canonical metadata, source links into a private repository, broken fragment navigation from detail pages, excess deployment permissions, and a root GitHub Pages `404.html` that was only a JavaScript hydration shell.

## Current state

- Architecture/data/API/auth/deployment state: Nuxt 4 static site; Vue pages; four static skill records; GitHub Pages custom workflow and custom-domain CNAME. No API, database, auth, or user records.
- Consumers and dependencies: Vue 3.5.43, Nuxt 4.5.2; GSAP 3.15.0 added for ScrollTrigger; direct TypeScript tooling removed.
- Known constraints: public URL is `https://lime.isroot.in`; root-relative asset paths; GitHub Pages artifact is `.output/public`; public routes must remain stable.

## Target state

- Authored site code uses Vue SFCs with plain JavaScript data and `.mjs` Nuxt configuration; no authored `.ts`/`.tsx` files remain.
- The solid black/light-pink/white visual system replaces green/gradient styles while preserving existing fonts and core content.
- GSAP reveals/progress are dynamically initialized after mount, scoped to the Vue page, cleaned up on unmount, and disabled when reduced motion is requested.
- Detail canonicals and source links target the correct public URLs; index navigation works from detail pages.
- `/404` is a noindex Vue route. `pnpm generate` derives a script-free root `404.html` from its prerendered markup and removes the unused `200.html` shell.
- Pages build checks run on pull requests; only the deployment job receives Pages write/OIDC permissions.

## Scope and compatibility

- In scope: `lime/` Vue/CSS/data/config/dependency/build changes and `.github/workflows/lime-pages.yml` CI permission/PR behavior.
- Explicitly out of scope: backend/API/database/auth, new analytics or cookies, user-data migration, changing the domain/provider, and unrelated skill package contents.
- Backward-compatible window: no API/data schema compatibility window is needed; existing five content URLs remain stable.
- Deprecation/removal dates: authored TypeScript files and direct TypeScript tools are removed in this change; no deferred compatibility layer.
- Feature flag or staged rollout: none; deploy is an atomic static artifact.

## Ordered migration plan

1. Preserve current Git history and verify clean baseline, branch, lockfile, domain, and Pages workflow.
2. Convert the authored skill data and Nuxt configuration to JavaScript; remove `tsconfig.json`, `typescript`, and `vue-tsc`.
3. Implement the requested palette, route metadata/navigation fixes, JavaScript error handling, and GSAP composable.
4. Add the Vue `/404` route and a finalization step that emits a script-free root Pages error file.
5. Run frozen-lockfile install, static generation, route/canonical/sitemap checks, no-JS 404 verification, dependency audit, source scanners, and browser smoke checks.
6. Review diff and commit; push to `main`; verify Pages Actions and live responses.

## Data and safety

There are no database tables, API records, secrets, or user-generated data to backfill. The only data module is a static JavaScript array. The finalizer is deterministic: it reads `.output/public/404/index.html`, strips script and module-preload tags from that Vue-rendered document, checks the error text exists, writes `.output/public/404.html`, and removes only Nuxt’s unused `.output/public/200.html`. A failed assertion stops generation before deployment.

## Rollback or recovery

The change is reversible through Git. Revert the change commit on `main` and allow the existing Pages workflow to regenerate/deploy. No destructive data migration or external state change exists. If the Pages workflow fails, retain the last deployed artifact and apply a forward fix to the generator/finalizer; no DNS or database restore is needed.

## Verification

- [x] Local tests: `pnpm install --frozen-lockfile`; `pnpm generate`; generated route/title/canonical/OG/H1 checks; sitemap parse; one-main error landmark assertion; script-free 404 and JavaScript-disabled render; search empty/recovery; direct detail route; real 390px viewport with no horizontal overflow, readable initial copy, and four cards visible after the GSAP scroll reveal; `git diff --check`.
- [x] Migration dry run: not applicable; no schema/data migration.
- [x] Production-like validation: static artifact served locally; final production host check occurs after deployment.
- [x] API/client compatibility: no API; five public URLs retained.
- [x] Monitoring and alerts: GitHub Actions Pages run is the rollout signal; no runtime telemetry added.
- [x] Security/privacy review: `pnpm audit --audit-level=high` clean; source scanner clean; Google Fonts third-party request remains noted in `SEO-SECURITY-AUDIT.md`.

## Risks and ownership

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| GSAP fails to load | Motion does not run | Dynamic import is caught; content is prerendered and readable | Maintainer |
| GitHub Pages domain/setting differs from source | Deployment or canonical URL mismatch | Verify custom domain, HTTPS, Actions, and live routes after push | Maintainer |
| External Google Fonts has jurisdiction-specific privacy implications | Potential disclosure/hosting concern | Consider self-hosting; owner to seek qualified review where needed | Maintainer |

## Cleanup and follow-up

- Keep `tsconfig.json`, `nuxt.config.ts`, `data/skills.ts`, `typescript`, and `vue-tsc` removed; do not reintroduce authored TypeScript without an explicit request.
- Ensure `200.html` remains excluded from the Pages artifact by the finalizer.
- Consider a public OG image and review whether to self-host Handlee.
- Verify the production unknown-path response is HTTP 404 with the custom body after the deploy succeeds.
