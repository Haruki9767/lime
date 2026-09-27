# Product Requirements Document — Lime Skills

**Status:** Implemented
**Owner:** Repository maintainer (GitHub: `Haruki9767`)
**Date:** 2026-09-27
**Source:** User request for the `Haruki9767/lime-skills` repository
**Canonical production URL:** `https://lime.isroot.in` (from `public/CNAME`)
**Framework/version:** Vue 3.5.43 with Nuxt 4.5.2 static generation
**Fonts and fallbacks:** Existing Departure Mono (local), Handlee (Google Fonts), monospace/cursive fallbacks
**Design direction/references:** Solid black, light pink, and white; no gradients and no remaining green UI; preserve the existing site content and character
**Package manager and lockfile:** pnpm 11; `pnpm-lock.yaml`

## 1. Summary

The user asked to refresh the existing Lime site’s colors, move authored application code from TypeScript to plain JavaScript in Vue single-file components, add smooth GSAP scroll animation, find and fix bugs, and push the result to `main`. The site is a small, public Nuxt static field guide. The approved work preserves its public routes, copy intent, fonts, and static architecture while addressing route metadata, source links, navigation, CI permission scope, and the GitHub Pages 404 fallback.

## 2. Goals

| Goal | Measure | Evidence / owner |
|---|---|---|
| Apply the requested solid black/light-pink/white palette | Authored site CSS contains no green palette or gradient styles | Source scan and rendered screenshots |
| Use Vue SFCs and JavaScript rather than authored TypeScript | No authored `.ts`/`.tsx`, no `lang="ts"`, and config/data use `.mjs`/`.js` | Source inventory and static build |
| Add smooth, purposeful scroll motion | ScrollTrigger reveal/progress; context cleanup; reduced-motion alternative | `useScrollAnimations.js`, browser smoke check |
| Preserve public routes and make SEO metadata route-specific | Five indexable pages have unique title, H1, canonical, and `og:url` | Generated HTML assertions and sitemap check |
| Make errors actionable and correct for static hosting | Root Pages `404.html` contains visible no-JS error copy and a home link | Generated artifact parser and headless Chromium without JS |
| Fix confirmed navigation/source/CI issues | Home links resolve, public repository links are correct, PR build is non-deploying, deploy permissions are scoped | Browser/source review and workflow inspection |

## 3. Non-goals and protected boundaries

- No backend/API, database, authentication, authorization, storage, secret, or user-data changes.
- No new accounts, forms, analytics, advertising, or third-party integrations beyond the existing Google Fonts request.
- No route/content expansion beyond the utility `/404` route; it is `noindex` and excluded from the sitemap.
- No promise of SEO ranking improvement, legal compliance, or full WCAG conformance.
- Preserve existing font choices and core content; do not introduce gradients or green UI.

## 4. Users and use cases

| User | Need | Evidence | Priority |
|---|---|---|---|
| Readers of the public Lime field guide | Browse the four skills and search/filter the index | Existing public site content; exact demographic is TBD | Must |
| Visitors following a broken link | Understand the missing route and recover to the index/source | Confirmed empty static 404 fallback | Must |
| Site maintainer | Build and deploy a consistent static site from `main` | Existing GitHub Pages workflow and CNAME | Must |

## 5. Current state and findings

| Finding ID | Area | Severity | Confidence | Current behavior before fix | Evidence |
|---|---|---|---|---|---|
| WEB-001 | SEO | Medium | Confirmed | Detail routes used the home URL as canonical | Corrected in `pages/[slug].vue` |
| WEB-002 | Navigation | Low | Confirmed | Source links targeted a repository confirmed private | Corrected to public `Haruki9767/lime-skills` |
| WEB-003 | Navigation | Low | Confirmed | Detail route fragment links did not return to the home anchors | Corrected with root-route Nuxt links |
| WEB-004 | Error handling | Medium | Confirmed | Generated `404.html` was a blank Nuxt shell without visible error text when JS was absent | Corrected by prerendering Vue `/404` and producing script-free root fallback |
| WEB-005 | CI security | Low | Confirmed | Build job inherited Pages write/OIDC permissions | Scoped permissions to deploy job; PRs build without deployment |
| WEB-006 | Social metadata | Low | Confirmed | No Open Graph image configured | Backlog; not required to fulfill the requested palette/migration |
| WEB-008 | Motion/accessibility | Low | Confirmed | At 390px, a screenshot during page initialization showed primary copy mid-fade from transparent | Keep primary copy opaque during positional reveals; retain staggered fade on the skill cards |
| WEB-009 | HTML semantics | Low | Confirmed | Vue 404/error views nested a `<main>` inside the app’s shared `<main>` | Replaced with named sections; generated error routes now have one main landmark |

## 6. Requirements

### Functional

| ID | Requirement | Priority | Acceptance criteria | Verification |
|---|---|---|---|---|
| FR-001 | The site shall use a solid black, light-pink, and white visual palette. | Must | No green palette or gradient CSS remains in authored site files. | Source scan; desktop/mobile render review |
| FR-002 | The site shall use Vue SFCs with plain JavaScript for authored app/config/data code. | Must | No authored `.ts`/`.tsx` source, `lang="ts"`, or TypeScript-specific config remains. | Source inventory; `pnpm generate` |
| FR-003 | The site shall provide calm GSAP scroll reveals and reading progress. | Must | GSAP/ScrollTrigger is dynamically loaded on mount, cleaned up on unmount, and only animated for `prefers-reduced-motion: no-preference`. | Browser smoke check and source review |
| FR-004 | Search shall show an accessible empty state and recover when the query is cleared. | Must | A no-match query shows status text; clearing restores all four cards. | Browser console interaction smoke test |
| FR-005 | Detail pages shall keep unique SEO URLs and public source links. | Must | Each generated route has its correct canonical/`og:url`; source link resolves under the public repository. | Generated HTML and browser link inspection |
| FR-006 | GitHub Pages shall show a useful 404 document without client JavaScript. | Must | Root `404.html` has title, `noindex`, error heading, recovery links, and no `<script>` dependency; `200.html` is not shipped. | Finalizer checks and no-JS headless render |

### Non-functional

| ID | Requirement | Target or constraint | Verification |
|---|---|---|---|
| NFR-001 | Honor reduced-motion preferences | Static content remains readable; ScrollTrigger runs only when no reduced-motion preference is active; CSS smooth scrolling is disabled for reduced motion | Source review; OS-level emulation not performed |
| NFR-002 | Preserve accessible contrast in selected core text pairs | WCAG AA text contrast threshold (4.5:1) for tested pairs | Calculated ratios: 9.27:1–20.01:1 |
| NFR-003 | Keep the static build reproducible | Node 22, pnpm 11, frozen lockfile | `pnpm install --frozen-lockfile && pnpm generate` |
| NFR-004 | Avoid high-severity dependency findings | No known high-severity audit results | `pnpm audit --audit-level=high` |

## 7. Design, SEO, and accessibility

- Preserve Departure Mono and Handlee; use solid black `#08080a`, pink `#ffb8d2`, white `#ffffff`, and neutral text/lines.
- No gradients or green UI. Keep the existing layout/content rather than introducing an unrelated redesign.
- Public/indexable routes: `/`, `/guidance`, `/web-design`, `/web-engineer`, `/seo-production-audit`.
- Error route `/404` and root static `/404.html` are `noindex`; neither is listed in the sitemap.
- Each indexable page gets a unique title/description/canonical/Open Graph URL; no `og:image` is available yet.
- WCAG 2.2 AA-informed spot checks only; no whole-site conformance claim. See `SEO-SECURITY-AUDIT.md` for scope/limits.

## 8. Security, privacy, and policy

The site is static, with no API, accounts, forms, user-generated HTML, analytics, advertising, cookies, or local storage observed. Skill data is bundled from repository files. Google Fonts remains a third-party request; assess whether self-hosting or a privacy notice is appropriate for actual visitor jurisdictions with qualified review if needed. Do not add tracking/consent vendors silently. The deploy workflow grants Pages/OIDC permissions only to its deploy job. No server authorization controls are relevant to the static content.

## 9. Pull-request and workflow requirements

- Pull requests targeting `main` with Lime/workflow changes run frozen-lockfile install and `pnpm generate`, upload a build artifact, and do not deploy.
- Pushes to `main` and manual dispatch can deploy through the existing GitHub Pages environment.
- Default workflow permission is `contents: read`; Pages write and OIDC token permissions belong only to `deploy`.
- The project has no lint, unit-test, or typecheck scripts; static generation is the build gate. Source scanners and dependency audit were run locally.

## 10. Compatibility constraints

| Boundary | Constraint | Explicit authorization needed for change? |
|---|---|---|
| Visual design | Use the requested black/pink/white solid palette; preserve content and existing font choices | Yes, for broader redesign |
| Backend/API/database | No backend or schema; remain static | Yes |
| Auth/security | No auth or private data | Yes |
| Deployment | Keep GitHub Pages, `main`, custom domain, and static output | Yes, to change provider/domain |
| Package manager | pnpm and one lockfile | Yes, to switch |

## 11. Rollout and rollback

- Rollout: push the reviewed commit to `main`; existing workflow builds and deploys Pages.
- Monitoring: check the workflow run and make non-mutating HTTP checks for public routes and unknown-path status.
- Rollback: revert the commit on `main`; the same workflow publishes the reverted site. No database/data restore is needed.
- Post-deploy verification: HTTPS home/detail routes, route-specific canonical tags, and unknown path returning HTTP 404 with the custom error body.

## 12. Risks and dependencies

| Risk/dependency | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| External Google Fonts request | Medium | Low/Medium, depending on visitor jurisdiction | Consider local hosting and privacy review | Maintainer |
| No social image metadata | Medium | Low | Add a branded OG image if desired | Maintainer |
| GitHub Pages settings/domain state not source-verifiable | Low/Medium | High if misconfigured | Verify Actions run, Pages custom domain, and HTTPS after push | Maintainer |
| Optional animation code/network loading fails | Low | Low | Content is prerendered; composable catches load failure; reduced-motion skips animation | Implemented |

## 13. Open questions and assumptions

- Primary audience/markets and any privacy-policy obligations remain `TBD`.
- Whether the owner wants a branded Open Graph image remains `TBD`.
- The site’s intended Google Fonts privacy posture remains an owner/legal-review decision.

## 14. Traceability

| Requirement | Finding / test / workflow |
|---|---|
| FR-001 | `assets/css/main.css`; source scan; rendered desktop/mobile spot check |
| FR-002 | `.vue`, `.js`, `.mjs` sources; no-TypeScript inventory; `pnpm generate` |
| FR-003 | `composables/useScrollAnimations.js`; W3C/GSAP/Vue source review |
| FR-004 | Browser test: empty-state text shown; four cards restored |
| FR-005 | Generated title/canonical/OG URL assertions; correct public source link |
| FR-006 | `pages/404.vue`; `scripts/finalize-static.mjs`; no-JS headless output test |
| NFR-003 | Frozen install and generation |
| NFR-004 | pnpm dependency audit |

## 15. Final acceptance checklist

- [x] User supplied framework/color/motion scope and authorized a push to `main`.
- [x] Current `web-design` guidance was read.
- [x] Backend/API/auth/database boundaries were preserved.
- [x] pnpm and the single lockfile were used consistently.
- [x] Confirmed route, link, fallback, and workflow findings were addressed.
- [x] Local build, static metadata, dependency audit, and source checks passed.
- [x] Policy caveats and not-tested items are recorded in the audit.
