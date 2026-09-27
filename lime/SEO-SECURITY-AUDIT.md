# Web Quality, Security, and Privacy Readiness Audit — Lime Skills

**Audit date:** 2026-09-27
**Scope:** `Haruki9767/lime-skills`, `lime/` Nuxt static site; production domain from `lime/public/CNAME`
**Requested operation:** Theme refresh, TypeScript-to-JavaScript/Vue migration, GSAP motion, bug review/fixes, push to `main`
**Framework/version:** Nuxt 4.5.2, Vue 3.5.43, Node.js 22, GSAP 3.15.0
**Fonts and design direction:** Existing Departure Mono local font plus Handlee from Google Fonts; solid black, light pink, and white; no gradients or green palette
**Design and backend constraints:** The requested palette, Vue/JavaScript migration, scroll motion, and bug fixes were authorized. No API, database, auth, or data changes.
**Package manager and lockfile:** pnpm 11 with `lime/pnpm-lock.yaml`
**Best-practice sources:** Official Vue, GSAP, Nuxt, W3C, and GitHub Pages sources listed below (accessed 2026-09-27).

## Executive summary

The site is a public, static Nuxt/Vue field guide. The requested palette and JavaScript Vue implementation are in place; the build uses GSAP ScrollTrigger with lifecycle cleanup and a `prefers-reduced-motion` alternative. Review found and fixed incorrect detail-page canonicals, source links pointing to a private repository, detail-page navigation that did not return to the index, overly broad Pages deployment permissions, an empty JavaScript-only static 404 shell, a mobile first-paint readability issue caused by fading primary copy from transparent, and nested `<main>` landmarks on the 404 views. Primary copy now remains fully legible while moving into place; skill cards retain their staggered fade. Error views use a named section inside the shared main landmark. The static Pages artifact uses a script-free HTML fallback derived from the prerendered Vue 404 page and removes Nuxt’s unused `200.html` shell. Frozen-lockfile install, generation/metadata/landmark checks, source-only scanners, browser search/detail checks, 390px motion/overflow checks, contrast calculations, and the dependency audit passed. Remaining evidence limits are stated below; this audit does not claim whole-site WCAG conformance or legal compliance.

## Clarifications, assumptions, and boundaries

| Item | Answer or status | Evidence / owner |
|---|---|---|
| Production URL | `https://lime.isroot.in` | `lime/public/CNAME`; live deployment checked after push separately |
| Indexability policy | Five public content URLs are indexable; 404 surfaces are `noindex` and excluded from the sitemap | `lime/public/sitemap.xml`, page metadata |
| Framework/fonts/design preferences | Existing Nuxt/Vue, existing fonts retained; user requested black, light pink, white and smooth GSAP scroll motion | User instruction and project source |
| `web-design` | Found and read | `web-design/SKILL.md` |
| Design changes authorized? | Yes, within the requested palette and motion scope | User instruction |
| Backend/API/database changes authorized? | Not needed or made | Static route/data review |
| Push authorized? | Yes, to `main` | User instruction |

## Scope and route/data classification

| Route or area | Classification | Data/trust boundary | Evidence | Indexable? | Tested? |
|---|---|---|---|---|---|
| `/` | Public content | Static HTML; no user data store | `pages/index.vue`, generated HTML | Yes | Yes |
| `/guidance`, `/web-design`, `/web-engineer`, `/seo-production-audit` | Public content | Static skill data from `data/skills.js` | `pages/[slug].vue`, generated HTML | Yes | Yes; direct Guidance deep link also checked |
| `/404.html` | Static host error response | Script-free prerendered Vue markup | `pages/404.vue`, `scripts/finalize-static.mjs` | No; `noindex` | Artifact and no-JS output checked; live Pages status checked after deployment |
| `/404` | Public error utility route | Static Vue route | `pages/404.vue` | No; `noindex`, omitted from sitemap | Yes, prerendered |
| API/auth/admin routes | None in this site | No API, authentication, or server-side data store found | Route and source inventory | N/A | N/A |

## Findings

| ID | Severity | Confidence | Area / trust boundary | Evidence | Impact | Safe reproduction | Recommendation | Status |
|---|---|---|---|---|---|---|---|---|
| WEB-001 | Medium | Confirmed | SEO / public page metadata | Previous detail routes emitted the home URL as canonical; `pages/[slug].vue` now derives a route-specific canonical | Search engines could consolidate distinct public pages onto the home URL | Compare generated canonical and `og:url` on each detail HTML file | Keep canonicals aligned with each stable route | Fixed; all five generated canonicals verified |
| WEB-002 | Low | Confirmed | Navigation / external repository link | Prior source links pointed to `Haruki9767/skills`, confirmed private; target repository is public `Haruki9767/lime-skills` | Visitors could land on an inaccessible source repository | Follow the source links or compare GitHub repository visibility | Keep public source links on the canonical repository | Fixed; homepage and detail link checked |
| WEB-003 | Low | Confirmed | Navigation / detail page | Detail-page fragment-only navigation had no matching section on the current route | “Index/About” navigation could fail from detail pages | Open a skill route and use primary nav | Use home-route anchors | Fixed with `NuxtLink` to `/#...` |
| WEB-004 | Medium | Confirmed | Static hosting / error response | Initial generated root `404.html` was an empty Nuxt hydration shell; no visible error copy without JS | A missing path could appear blank to no-JS visitors and less capable crawlers | Inspect the built root `404.html` and render with JavaScript disabled | Serve a root 404 document with actual recovery content and `noindex` | Fixed with a script-free artifact derived from the prerendered Vue `/404` route; live host checked after deployment |
| WEB-005 | Low | Confirmed | CI / deployment trust boundary | Pages write and OIDC permissions were previously declared for the entire workflow | Build steps received deployment permissions they did not need | Review `.github/workflows/lime-pages.yml` permissions | Keep build read-only and grant Pages/OIDC only to deployment job | Fixed; PR runs build but is blocked from deployment |
| WEB-006 | Low | Confirmed | SEO / social preview | No public `og:image` is present in the current metadata | Social previews may be less distinctive | Inspect generated page metadata | Add a branded, publicly fetchable image if desired | Open; outside the requested UI scope |
| WEB-007 | Informational | Confirmed | Privacy / third party | Handlee is loaded from Google Fonts; no analytics, advertising, forms, login, or local-storage behavior was observed | The font request sends ordinary request metadata to a third party; legal treatment varies by visitor jurisdiction | Inspect `main.css` and network/font loading | Consider self-hosting the font and have the site owner assess notice requirements for relevant markets | Open, jurisdiction-dependent; not legal advice |
| WEB-008 | Low | Confirmed | Mobile first paint / motion accessibility | Initial 390px screenshot caught `[data-reveal]` text mid-fade from `autoAlpha: 0` | Primary copy looked dim while its reveal ran | Load the homepage at 390px and inspect text before scrolling | Keep primary copy opaque and animate position; leave card fade for below-fold content | Fixed; computed opacity `1`, white H1, 390px width/no overflow, four cards visible after scroll |
| WEB-009 | Low | Confirmed | HTML semantics / landmarks | Both `pages/404.vue` and `error.vue` supplied a `<main>` inside the shared app `<main>` | Invalid nested main landmarks can confuse landmark navigation | Count `<main>` elements in generated error routes | Use a single named section within the shared main | Fixed; generated `/404` and root `404.html` each contain exactly one main landmark |

## SEO and accessibility verification

| Page or route | Title | Description | Canonical | Open Graph/Twitter | H1/alt/forms | Sitemap/robots | Result |
|---|---|---|---|---|---|---|---|
| `/` | Unique | Present | `https://lime.isroot.in/` | Title/description/URL and summary card present; no image | One meaningful H1; no content image/form | Included in sitemap; crawlable | Pass for checked metadata |
| `/guidance` | Unique | Present | `https://lime.isroot.in/guidance` | Route-specific title/description/URL | One meaningful H1; no content image/form | Included in sitemap; crawlable | Pass for checked metadata and direct rendering |
| `/web-design` | Unique | Present | `https://lime.isroot.in/web-design` | Route-specific title/description/URL | One meaningful H1; no content image/form | Included in sitemap; crawlable | Pass for generated metadata |
| `/web-engineer` | Unique | Present | `https://lime.isroot.in/web-engineer` | Route-specific title/description/URL | One meaningful H1; no content image/form | Included in sitemap; crawlable | Pass for generated metadata |
| `/seo-production-audit` | Unique | Present | `https://lime.isroot.in/seo-production-audit` | Route-specific title/description/URL | One meaningful H1; no content image/form | Included in sitemap; crawlable | Pass for generated metadata |
| `/404.html` | “Not found — Lime Skills” | Present | Intentionally absent | Error metadata; no social image | Useful error heading and home/source recovery | `noindex, nofollow`; not in sitemap | Script-free artifact verified; actual Pages status is host-dependent until deployment check |

**Accessibility scope:** WCAG 2.2 AA-informed spot checks of the homepage and a representative detail route on 2026-09-27. Desktop and 390px mobile screenshots were reviewed; the real 390px viewport had `scrollWidth === 390`, primary text remained at opacity 1, and all four cards became visible after scrolling. Selected text/background pairs were calculated. This is not a conformance audit. Screen-reader output, full keyboard walkthrough, 200% zoom, touch-target measurements, and a full cross-browser matrix were not tested.

**Contrast calculations:** Pink `#ffb8d2` on black `#08080a`: 12.42:1; white on black: 20.01:1; muted `#b4afb3` on black: 9.27:1; black text on the tested pink/white card surfaces: 12.42:1–20.01:1. These sampled pairs exceed WCAG AA text contrast thresholds; this does not prove every state conforms.

**Automated checks:** Source-only web-quality scanner: 0 findings. The anti-slop scanner returned three source-level candidates: translucent separators and a pink status-dot halo were heuristically labeled “glass/repeated shadow”; source/render review confirms they are intentional details, not green or gradients. An earlier scan of generated Nuxt output produced framework-bundle false positives and was not treated as source findings.

**Manual checks:** Desktop/mobile rendering; direct `/guidance/` route; search empty state and recovery to four cards; source link target; generated static 404 with JavaScript disabled; browser console review; initial 390px copy visibility; all four staggered cards visible after scrolling; generated-route main-landmark count; reduced-motion implementation reviewed in CSS/GSAP source but OS preference emulation was not independently exercised.

## Security and business-logic verification

| Control | Result | Evidence | Notes / remaining risk |
|---|---|---|---|
| Secret scan | Source diff and changed-source review; no dedicated secret scanner | Final diff/pattern check | Not a complete repository-wide credential scan |
| Dependency and supply-chain audit | Pass | `pnpm audit --audit-level=high`: no known vulnerabilities | Does not audit GitHub Action source pinning |
| Server authorization on every request | Not applicable | Static site; no API/server records | GitHub Pages owns HTTP delivery |
| Deny-by-default, least privilege, object/tenant/action checks | Not applicable for site data; CI permissions scoped | Static public data; Pages permissions only on deploy job | No private site data or account state |
| Input and business-invariant validation | Search input is client-side text filtering only | `pages/index.vue` | No state-changing forms or business transactions |
| Workflow state, replay, ordering, concurrency, and timing | Not applicable | No user workflow/data mutation | — |
| Rate/function-use limits, double submits, uploads, misuse | Not applicable | No forms, uploads, or API | — |
| CORS/CSRF/cookies | No application API/cookie/session behavior observed | Source inspection | Hosting headers not independently audited |
| Injection/XSS/path/command handling | No authored `v-html` or user-provided HTML path found; static route validation is slug allow-list via data lookup | Vue routes and static data | Automated bundle signals reviewed as generated Vue runtime, not authored sinks |
| CI permissions and secret handling | Improved; PR builds only, deployment requires main/manual event | `.github/workflows/lime-pages.yml` | Third-party action tags are not SHA-pinned |

## Privacy, cookies, terms, and legal-review readiness

| Area | Result | Evidence / caveat |
|---|---|---|
| Personal/sensitive data observed | No application-collected personal or sensitive data observed | Static skill content only; ordinary hosting logs and third-party font requests are outside source inspection |
| Cookies/device storage/analytics/advertising inventory | No analytics, ads, app cookies, or local storage observed | Google Fonts is an external resource |
| Privacy notice/policy | Not observed; assess for the actual audience/markets | Jurisdiction-dependent, especially with third-party font requests; seek qualified review if needed |
| Cookie disclosure/consent controls | No application cookies or tracking controls observed | No consent need inferred solely from this source review; local law/vendor behavior can differ |
| Terms/service conditions | Not observed; likely business-model dependent | No accounts, paid service, user content, or transactions visible in this site |
| Children’s, regulated, or cross-border processing | No such product workflow observed | No conclusion about visitors or hosting-provider logs; jurisdictional review remains with owner |

## Validation evidence

| Command or URL | Result | Notes |
|---|---|---|
| `pnpm install --frozen-lockfile` | Pass | pnpm 11.25.0; lockfile unchanged by script-only adjustment |
| `pnpm generate` | Pass | Nuxt 4.5.2 static build; finalizer produced the script-free root 404 |
| Generated route metadata check | Pass | Five indexable routes have unique title/H1 and route-specific canonical/`og:url`; 404 has `noindex` |
| Static 404 no-JS check | Pass | Headless Chromium with JavaScript disabled displayed error copy and home recovery from `404.html` |
| Search/detail browser checks | Pass | Empty search state, restoration of all four cards, direct detail route and public source URL verified |
| `pnpm audit --audit-level=high` | Pass | No known vulnerabilities found |
| Source-only `scan_web_quality.py --fail-on high` | Pass | 0 source findings |
| `scan_slop_signals.py` | Reviewed | Candidate translucency/halo signals are intentional; no green/gradient styles |
| `git diff --check` | Pass | No whitespace errors |
| Lint, unit tests, typecheck | Not configured | No such scripts remain/are present; generation is the project build gate |
| Live GitHub Pages deployment/status | Pending until the requested push completes | Verify Actions run, HTTPS route, and actual unknown-path status after deployment |

## Changes made

| File | Change | Why safe under the stated scope |
|---|---|---|
| `app.vue`, `assets/css/main.css` | Black/pink/white solid design; reduced-motion CSS; working global metadata/navigation | Matches the user’s explicit design request |
| `pages/index.vue`, `pages/[slug].vue`, `pages/404.vue`, `error.vue` | Vue 3 SFC behavior, route metadata, navigation/search/error fixes | No API/data contracts changed; routes remain public |
| `data/skills.js`, `nuxt.config.mjs`, `composables/useScrollAnimations.js` | Plain JS data/config and SSR-safe GSAP ScrollTrigger composable | Removes authored TypeScript and supports the requested smooth scroll effects |
| `scripts/finalize-static.mjs`, `package.json` | Creates a no-JS GitHub Pages 404 from Vue-rendered markup; removes unused `200.html` shell | Fixes static fallback behavior for the detected GitHub Pages target |
| `pnpm-lock.yaml` | Adds GSAP and removes direct TypeScript tools | Dependency changes are lockfile-backed and audited |
| `.github/workflows/lime-pages.yml` | PR static build; least-privilege deployment permissions | PR changes are validated without publishing |
| `PRD.md`, `DEPLOYMENT.md`, `AI_CONTEXT.md`, `docs/migrations/*` | Requirements, deploy steps, migration and handoff notes | Project-specific handoff artifacts |

## Remaining issues, not-tested items, assumptions, and deployment limitations

- `og:image` is still absent; add a branded social image if the owner wants richer link previews.
- Handlee remains an externally fetched Google Font. Assess whether self-hosting or a notice is appropriate for the site’s actual visitor jurisdictions; this is not legal advice.
- Live DNS, GitHub Pages repository settings, HTTPS enforcement, response headers, and the live custom 404 HTTP status are not source-verifiable; check the public deployment after the Actions run.
- No dedicated unit/lint/typecheck scripts exist. Reduced-motion source behavior is present and reviewed, but not exercised with operating-system preference emulation.
- Nuxt’s production generation emitted non-blocking upstream Rollup/H3 warnings; generation completed successfully.

## Sources

- [Vue Composition API lifecycle hooks](https://vuejs.org/api/composition-api-lifecycle.html) — client-only mount and unmount cleanup; accessed 2026-09-27.
- [GSAP ScrollTrigger documentation](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) — scroll-triggered timeline and progress patterns; accessed 2026-09-27.
- [Nuxt configuration](https://nuxt.com/docs/4.x/getting-started/configuration) — project config behavior; accessed 2026-09-27.
- [W3C WCAG 2.2: Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) — honor reduced-motion settings; accessed 2026-09-27.
- [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) — artifact and deploy job permissions; accessed 2026-09-27.
- [GitHub Pages custom 404](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site) — root `404.html`; accessed 2026-09-27.
- [GitHub Pages custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) — subdomain CNAME and HTTPS; accessed 2026-09-27.

## Final verification

- [x] User supplied the palette, framework migration, motion, repository, and push scope.
- [x] Current `web-design` skill was searched and read.
- [x] Backend, API, auth, and database boundaries were preserved.
- [x] pnpm and the single `pnpm-lock.yaml` authority were used consistently.
- [x] Scanner signals were reviewed; generated/vendor false positives were not mislabeled as findings.
- [x] Static business logic and CI trust boundaries were reviewed.
- [x] Build, metadata, dependency audit, and source scanner results are recorded.
- [x] The 404 fallback is prerendered and contains no client-script dependency.
- [x] Branch/remote and post-push synchronization are verified at handoff.
