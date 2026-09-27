# Product Requirements Document — [Project]

**Status:** Draft / Proposed / Implemented / Blocked
**Owner:** [Owner or TBD]
**Date:** [YYYY-MM-DD or TBD]
**Source:** [Audit path, issue, URL, or user request]
**Canonical production URL:** [URL or TBD]
**Framework/version:** [choice or TBD]
**Fonts and fallbacks:** [choice or TBD]
**Design direction/references:** [choice or TBD]
**Package manager and lockfile:** [pnpm/pnpm-lock.yaml preferred, explicit exception, or TBD]

## 1. Summary

[Describe the verified user or product problem in one paragraph. Separate evidence from assumptions and mark unknowns `TBD`.]

## 2. Goals

| Goal | Measure | Evidence / owner |
|---|---|---|
| [Goal] | [Pass condition] | [Audit/test/TBD] |

## 3. Non-goals and protected boundaries

This work must not change the visual design, layout, typography, colors, imagery, animation, responsive behavior, visible product copy, API contracts, database schema, authentication, authorization, encryption, secrets, or deployment configuration unless the user explicitly authorizes the specific change.

- [Explicitly excluded behavior, redesign, migration, provider change, or backend change]

## 4. Users and use cases

| User | Need | Evidence | Priority |
|---|---|---|---|
| [User or TBD] | [Need] | [Audit/source/TBD] | Must/Should/Could |

## 5. Current state and findings

| Finding ID | Area | Severity | Confidence | Current behavior | Evidence |
|---|---|---|---|---|---|
| [ID] | [SEO/security/accessibility/CI/privacy/design] | [Level] | [Confirmed/review signal] | [Fact] | [File:line or URL] |

## 6. Requirements

### Functional

| ID | Requirement | Priority | Acceptance criteria | Verification |
|---|---|---|---|---|
| FR-001 | [The system shall...] | Must | [Observable pass condition] | [Test/command/review] |

### Non-functional

| ID | Requirement | Target or constraint | Verification |
|---|---|---|---|
| NFR-001 | [Security/SEO/accessibility/compatibility requirement] | [Target or TBD] | [Command/test/review] |

## 7. Design, SEO, and accessibility

Follow the supplied framework, font, and design direction. Search for and follow the current `ai-slop-pattern-looker` skill when available. Define route classification, indexability, title/description/canonical policy, Open Graph/Twitter metadata, sitemap/robots rules, heading/image/form requirements, WCAG 2.2 scope and target, manual checks, and deployment URL. Never make private data indexable to improve SEO.

## 8. Security, privacy, and policy

Describe trust boundaries, server-side authentication/authorization expectations, deny-by-default and least privilege, input/business validation, workflow/replay/rate-limit checks, data minimization, logging/redaction, dependency policy, CI permissions, third-party resources, and confirmed versus hypothetical risks. Record whether privacy notices, cookie disclosures/consent, terms, retention/deletion controls, children’s-data safeguards, or qualified legal review appear necessary; jurisdictional conclusions must be marked as needing counsel.

## 9. Pull-request and workflow requirements

Define PR and default-branch triggers, least-privilege permissions, pnpm-first frozen-lockfile installation, typecheck/lint/tests/build, SEO/accessibility scanner, dependency audit, secret checks, changed-file/design-boundary checks, safe artifacts, and fork-PR secret behavior.

## 10. Compatibility constraints

| Boundary | Constraint | Explicit authorization needed for change? |
|---|---|---|
| Visual design | Preserve existing appearance and interaction | Yes |
| Backend/API/database | Preserve contracts and data rules | Yes |
| Auth/security | Do not weaken trust boundaries | Yes |
| Deployment | Preserve provider/build bindings unless requested | Yes |
| Package manager | Prefer pnpm; follow packageManager/devEngines and lockfile authority | Yes if switching |

## 11. Rollout and rollback

- Rollout: [Phased release or TBD]
- Monitoring: [Metrics/logs/alerts or TBD]
- Rollback: [Revert/deploy procedure or TBD]
- Post-deploy verification: [URLs, status codes, headers, build artifact, or TBD]

## 12. Risks and dependencies

| Risk/dependency | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| [Risk] | [Low/Medium/High] | [Low/Medium/High] | [Mitigation] | [Owner/TBD] |

## 13. Open questions and assumptions

Record missing information here, but ask the user before implementation when the answer would materially change scope, security, design, indexability, package-manager choice, policy, or deployment behavior.

- [Question or assumption marked TBD]

## 14. Traceability

| Requirement | Finding / test / workflow |
|---|---|
| [FR/NFR ID] | [Finding ID, command, workflow job, or manual check] |

## 15. Final acceptance checklist

- [ ] User supplied or confirmed framework, fonts, design direction, and other material inputs.
- [ ] Current `ai-slop-pattern-looker` skill was searched and read if available.
- [ ] Protected design/backend/auth/deployment boundaries were respected.
- [ ] pnpm or an explicit repository exception was used consistently with the authoritative lockfile.
- [ ] PR checks run on proposed changes and default-branch changes.
- [ ] Audit findings have evidence, severity, confidence, remediation, and status.
- [ ] Verification commands pass, or failures are explicitly documented.
- [ ] Policy/legal review needs are surfaced without presenting legal advice as fact.
