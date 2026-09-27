# Web Quality, Security, and Privacy Readiness Audit — [Project]

**Audit date:** [YYYY-MM-DD]
**Scope:** [Repository, branch, deployment URL, or files]
**Requested operation:** [Audit / report / safe fixes / workflow / PRD / push]
**Framework/version:** [value or TBD]
**Fonts and design direction:** [value or TBD]
**Design and backend constraints:** [Preserve / explicitly authorized changes]
**Package manager and lockfile:** [pnpm/pnpm-lock.yaml, explicit exception, or TBD]
**Best-practice sources:** [source list/path]

## Executive summary

[One paragraph describing verified scope, highest-priority findings, completed fixes, blocked checks, policy flags, and important limitations. Do not call the system secure, conformant, or production-ready without evidence.]

## Clarifications, assumptions, and boundaries

| Item | Answer or status | Evidence / owner |
|---|---|---|
| Production URL | [URL or TBD] | [User/repository/live check] |
| Indexability policy | [Public/private/noindex or TBD] | [Route evidence] |
| Framework/fonts/design preferences | [value or TBD] | [User/project] |
| `web-design` | [Found/read or searched/unavailable] | [Path/date] |
| Design changes authorized? | [Yes/no] | [User instruction] |
| Backend/API/database changes authorized? | [Yes/no] | [User instruction] |
| Push authorized? | [Yes/no/branch] | [User instruction] |

## Scope and route/data classification

| Route or area | Classification | Data/trust boundary | Evidence | Indexable? | Tested? |
|---|---|---|---|---|---|
| [Route] | [Public/private/API/error] | [Client/server/third party/data store] | [File or URL] | [Yes/no/TBD] | [Yes/no] |

## Findings

| ID | Severity | Confidence | Area / trust boundary | Evidence | Impact | Safe reproduction | Recommendation | Status |
|---|---|---|---|---|---|---|---|---|
| [WEB-001] | [Critical/High/Medium/Low/Info] | [Confirmed/review signal/hypothesis] | [Client/server/CI/third party] | [File:line or URL] | [Concrete impact] | [Non-destructive steps or N/A] | [Action] | [Open/fixed/accepted/blocked] |

## SEO and accessibility verification

| Page or route | Title | Description | Canonical | Open Graph/Twitter | H1/alt/forms | Sitemap/robots | Result |
|---|---|---|---|---|---|---|---|

**Accessibility scope:** [WCAG version/level, full pages and flows, representative sample, variants, technologies, date]

**Automated checks:** [commands/results]

**Manual checks:** [keyboard, focus, contrast, zoom, mobile, screen reader, forms, reduced motion; mark Not tested unless performed]

Do not claim whole-site WCAG conformance from an isolated or automated sample. State the evaluated scope, applicable Success Criteria coverage, user-agent assumptions, and limitations.

## Security and business-logic verification

| Control | Result | Evidence | Notes / remaining risk |
|---|---|---|---|
| Secret scan | [Pass/Fail/Not tested] | [Command/output] | |
| Dependency and supply-chain audit | [Pass/Fail/Not tested] | [Evidence] | |
| Server authorization on every request | [Pass/Fail/Not applicable/Not tested] | [Evidence] | |
| Deny-by-default, least privilege, object/tenant/action checks | [Result] | [Evidence] | |
| Input and business-invariant validation | [Result] | [Evidence] | |
| Workflow state, replay, ordering, concurrency, and timing | [Result] | [Evidence] | |
| Rate/function-use limits, double submits, uploads, misuse | [Result] | [Evidence] | |
| CORS/CSRF/cookies | [Result] | [Evidence] | |
| Injection/XSS/path/command handling | [Result] | [Evidence] | |
| CI permissions and secret handling | [Result] | [Workflow] | |

## Privacy, cookies, terms, and legal-review readiness

| Area | Result | Evidence / caveat |
|---|---|---|
| Personal/sensitive data observed | [Result] | [Data flow] |
| Cookies/device storage/analytics/advertising inventory | [Result] | [Behavior] |
| Privacy notice/policy | [Needed/not observed/not assessed] | [Jurisdiction caveat] |
| Cookie disclosure/consent controls | [Needed/not observed/not assessed] | [Purpose/jurisdiction caveat] |
| Terms/service conditions | [Needed/not observed/not assessed] | [Business-model caveat] |
| Children’s, regulated, or cross-border processing | [Result] | [Legal/privacy review flag] |

## Validation evidence

| Command or URL | Result | Notes |
|---|---|---|
| `pnpm install --frozen-lockfile` | [Pass/Fail/Blocked/Not run] | [Relevant output] |
| `[pnpm test/lint/typecheck/build]` | [Pass/Fail/Blocked/Not run] | [Relevant output] |
| `[security/accessibility/SEO checks]` | [Pass/Fail/Blocked/Not run] | [Relevant output] |

## Changes made

| File | Change | Why safe under the stated scope |
|---|---|---|
| [Path] | [Description] | [Design/backend/API impact] |

## Remaining issues, not-tested items, assumptions, and deployment limitations

[Separate blocked checks, risks, assumptions, and legal-review needs.]

## Sources

- [URL and access date]

## Final verification

- [ ] Requested information was sufficient or missing details were explicitly recorded.
- [ ] Framework, fonts, design preferences, and taste reference were respected.
- [ ] Design and backend constraints were respected.
- [ ] pnpm and the authoritative lockfile were used consistently.
- [ ] Scanner and automation signals were reviewed for false positives.
- [ ] Business-logic and server-side authorization checks were considered.
- [ ] Tests, build, audit, and security checks passed or are clearly reported.
- [ ] Generated files exist and contain no secrets.
- [ ] Branch and remote state were verified.
