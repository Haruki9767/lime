# Clarification and Scope Rules

## Table of contents

1. [Ask before acting](#ask-before-acting)
2. [Preference intake](#preference-intake)
3. [Design-preservation rule](#design-preservation-rule)
4. [Backend and trust-boundary rule](#backend-and-trust-boundary-rule)
5. [Policy readiness](#policy-readiness)
6. [Assumptions and stop conditions](#assumptions-and-stop-conditions)

## Ask before acting

Ask one concise consolidated question and pause when any of these are missing and materially affects the result:

- repository or website target;
- requested operation: audit, report, fix, build, workflow, PRD, commit, or push;
- permission to modify or push;
- route indexability, authentication, or data-handling policy;
- framework/version and package-manager choice where lockfiles conflict;
- font, brand, design direction, references, and accessibility target;
- whether design, backend, API, database, auth, or deployment configuration may change.

Use `TBD` in reports only after the user has authorized a report despite missing information. Do not use `TBD` as a reason to make an implementation guess.

## Preference intake

Before making a web experience, collect and follow the framework/version, font preferences and fallbacks, visual taste, layout/density, color, motion, imagery, examples the user likes/dislikes, audience, product goal, responsive behavior, and accessibility expectations. Search for the current `web-design` skill before visual/frontend work; if absent, record that it was searched for and unavailable.

## Design-preservation rule

Treat layout, spacing, typography, colors, imagery, animation, responsive breakpoints, interaction behavior, visible copy, brand identity, API contracts, database schema, authentication, authorization, cookies, encryption, secrets, hosting, routing, build output, and deployment bindings as protected by default.

SEO metadata, crawler files, static 404 pages, semantic labels, tests, documentation, and CI are usually safe additions, but inspect context first. Do not make visual changes while claiming “no design changes.”

## Backend and trust-boundary rule

Never make a private route public, relax CORS, remove authentication, expose a database, trust client-calculated business values, or move an authorization check to the client to improve SEO or make a check pass. Report the boundary and ask for explicit authorization if a backend change is actually required.

## Policy readiness

Flag the likely need for privacy, cookie, terms, consent, retention, deletion, or legal review based on observed data practices and business model. Do not claim a policy is legally required without jurisdiction-specific evidence. A privacy notice is commonly relevant to personal-data processing; cookie consent may apply to non-essential device storage/access; terms are commonly relevant to accounts, contracts, paid services, user content, and sales.

## Assumptions and stop conditions

Record assumptions in the audit and PRD. Stop and ask instead of guessing when:

- the repository has `package-lock.json` and `pnpm-lock.yaml` with different dependency specs;
- the package-manager version is not declared or is incompatible with the lockfile;
- a URL is supplied but its ownership or canonical status is unclear;
- a page could be public or private;
- a finding could require a breaking dependency or framework upgrade;
- a proposed fix could alter appearance, runtime behavior, security posture, or policy behavior;
- a cookie/consent recommendation depends on unknown jurisdictions or processing purposes;
- the user asks to push but the target branch/remote is unclear.

A safe final report distinguishes **confirmed**, **review signal**, **not tested**, **assumption**, **legal review needed**, and **blocked**.
