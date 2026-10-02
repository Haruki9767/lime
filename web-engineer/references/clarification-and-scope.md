# Clarification and Scope Rules

Use the shared [`../../guidance/references/final-questions.md`](../../guidance/references/final-questions.md) protocol. This file adds engineering-specific boundaries; it is not a questionnaire to send wholesale.

## 1. Inspect, scope, and queue

- Read the request, existing conversation, repository instructions, code, tests, and deployment config before asking the user anything. Reuse every applicable answer already given.
- Ask only about missing information that changes the specific code, content, test, or deployment work in scope. Do not ask about untouched design, framework, backend, analytics, legal, or operations topics.
- Prefer existing project behavior and configuration as the default. Preserve architecture, UI, data, API contracts, auth, dependencies, and deployment behavior unless change is requested.
- Queue non-urgent questions and ask them together after completing and verifying safe independent work. If a question blocks one slice, leave that slice unchanged and continue other authorized work.
- Ask earlier only if no useful safe work can proceed without an answer or proceeding would cross a security, privacy, legal, deployment, destructive-change, financial, or other consequential boundary. Ask one concise batch, not repeated single questions.

## 2. Candidate questions (select only if applicable)

- **Target and operation:** repository/site or requested deliverable only when not identifiable from the request.
- **Permission:** modification, deployment, push, or an external action only when it was not already requested or authorized and the action needs it.
- **Framework/package manager:** only for a new project, requested stack change, or a real lockfile/runtime conflict; otherwise follow the healthy declared stack.
- **Visual preferences:** only when creating or changing visual design. Do not ask for fonts, layout, color, or references during design-preserving, backend-only, docs-only, or SEO-only work.
- **Routes, content, and SEO:** ask about indexability, canonical host, audience, market, copy, or business facts only if the requested implementation depends on the missing value. A structural audit can proceed without inventing any of these.
- **Backend/API/data/auth/deployment:** ask only for contract, ownership, provider, migration, auth, rollout, privacy/retention, or environment-variable **names** required for an actual in-scope change. Never ask for secret values in chat.
- **Policy:** surface privacy, cookie, terms, and legal review only when observed processing/business behavior makes it relevant; do not request jurisdiction details for work that does not rely on a legal conclusion.
- **Release or push target:** ask for branch, remote, or version only if it is genuinely ambiguous and required by the requested action.

## 3. Design-preservation rule

Treat layout, spacing, typography, colors, imagery, animation, responsive breakpoints, interaction behavior, visible copy, brand identity, API contracts, database schema, authentication, authorization, cookies, encryption, secrets, hosting, routing, build output, and deployment bindings as protected by default.

SEO metadata, crawler files, static 404 pages, semantic labels, tests, documentation, and CI are usually safe additions, but inspect context first. Do not make visual changes while claiming “no design changes.”

## 4. Backend and trust-boundary rule

Never make a private route public, relax CORS, remove authentication, expose a database, trust client-calculated business values, or move an authorization check to the client to improve SEO or make a check pass. If an actual backend change requires missing authorization or configuration, leave that slice untouched and queue the specific blocking question; continue independent work where safe.

## 5. Policy readiness

Flag the likely need for privacy, cookie, terms, consent, retention, deletion, or legal review based on observed data practices and business model. Do not claim a policy is legally required without jurisdiction-specific evidence. A privacy notice is commonly relevant to personal-data processing; cookie consent may apply to non-essential device storage/access; terms are commonly relevant to accounts, contracts, paid services, user content, and sales.

## 6. Assumptions and stop conditions

Use existing project evidence and reversible defaults when safe; state material assumptions in the report. Leave only the affected change blocked and queue a question instead of guessing when:

- the repository has conflicting `package-lock.json` and `pnpm-lock.yaml` dependency specifications;
- the package-manager version is undeclared or incompatible with the lockfile;
- a URL’s ownership or canonical status is unclear and a requested change depends on it;
- a page could be public or private;
- a proposed fix needs a breaking dependency/framework upgrade;
- a proposed fix could materially alter appearance, runtime behavior, security posture, or policy behavior;
- cookie/consent guidance depends on unknown jurisdictions or processing purposes;
- a requested push/release target is genuinely unclear.

Do not stop unrelated safe work. Run final verification, fix authorized failures, and rerun affected checks before reporting. Distinguish **confirmed**, **failed**, **not tested**, **assumption**, **legal review needed**, **blocked**, and **question**. Put all remaining applicable questions together at the end; omit irrelevant questions.
