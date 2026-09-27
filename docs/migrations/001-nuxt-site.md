# Migration 001: Nuxt skills site

## Context

The repository previously contained skill packages and no public web application. This change adds a static Nuxt site that makes those packages discoverable at `lime.isroot.in`.

## Scope

- Add a Nuxt 4 / Vue 3 frontend under the `lime/` directory.
- Add public routes for the home page and each of the four skills.
- Add metadata, robots, sitemap, favicon, custom 404/error handling, and a MIT license.
- Add `DEPLOYMENT.md` and update `guidance/SKILL.md` so deployment notes are required for future projects.

## Compatibility and rollout

The existing skill directories remain the source of truth and are not renamed or moved. The site is static and introduces no backend, API, auth, database, cookies, or secrets.

## Ordered rollout

1. Install dependencies with `cd lime && pnpm install --frozen-lockfile`.
2. Run `cd lime && pnpm typecheck && pnpm generate`.
3. Connect the repository’s `main` branch to Cloudflare Pages or enable the GitHub Pages workflow using the settings in `DEPLOYMENT.md`.
4. Attach `lime.isroot.in` and verify canonical routes, sitemap, robots, and a true 404.

## Rollback / forward fix

Rollback is a normal Git revert of the site commit and redeploy. No data migration exists. If content becomes stale, update the summary data or source skill and redeploy.

## Validation

- Typecheck and static generation must pass.
- Direct routes must render.
- Unknown routes must return the framework’s 404 error response.
- No environment variable values or secrets may be committed.

## Risks and follow-up

Nuxt’s external Google Fonts request is optional presentation enhancement; the CSS includes local fallbacks. If a no-third-party policy is introduced, self-host the licensed font files and remove the external font requests.
