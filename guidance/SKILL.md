---
name: guidance
description: Coordinate web-project work across the repository’s skills, classify frontend versus backend scope, protect architecture and API logic, enforce maintainable file boundaries, document migrations and AI handoffs, and deliver a tested skeleton before visual refinement. Use before adding features, changing architecture, switching agents, or coordinating web-design, web-engineer, and SEO work.
---

# Guidance

Use this skill as the project coordinator before making or reviewing a meaningful web change. It keeps the work understandable to the user and to future developers or AI agents. It does not replace specialist skills; it routes work to them and preserves their current instructions.

## 1. Discover and route to the right skills

Before acting, search the current skill directories, repository, and configured skills for the latest `SKILL.md` files. Never rely on a cached copy, and never assume a named skill exists. Read the current package only when its domain is relevant.

Use the repository skills in this order for a typical web feature:

| Need | Skill to load | When to use |
|---|---|---|
| Project coordination, scope, architecture, handoff, migrations | `guidance` | First for feature work, architecture changes, agent switching, or unclear scope |
| Visual direction, anti-slop review, typography, interaction, motion | `web-design` | Before frontend design or UI changes; ask for user preferences before inventing a custom direction |
| Framework, code quality, accessibility, security, business logic, privacy/policy readiness | `web-engineer` | During implementation and again after the web experience is built |
| Search visibility, metadata, crawl/indexability, structured data, AI search | `seo-production-audit` | After implementation or whenever SEO/discoverability is in scope |

When a relevant specialist is available, read it and follow its workflow. If it is missing, record that it was searched for and unavailable. For adjacent installed skills, route deliberately: use `accessibility` for focused WCAG work, `systematic-debugging` or `debugging-and-error-recovery` for failures, `ci-cd-and-automation` for pipelines, `dependency-updater` for dependency changes, `sql-queries`/`sql-optimization-patterns` for database work, and `git-workflow-and-versioning`/`make-repo-contribution` for repository changes. Do not load every unrelated skill into context.

## 2. Classify every feature before implementation

Before changing files, classify the request as **frontend-only**, **backend-only**, or **hybrid**. Inspect routes, components, server handlers, API clients, schemas, database calls, auth, storage, queues, webhooks, and deployment bindings instead of trusting the feature label.

A feature is frontend-only only when it can be completed without changing server code, API contracts, authentication/authorization, database schema/data, storage, secrets, background jobs, webhooks, or deployment configuration. A feature is backend-required if it needs new or changed data, server validation, permissions, business rules, API endpoints, persistence, secrets, integrations, webhooks, or server-side rendering behavior. Treat uncertain work as hybrid until proven otherwise.

If backend or hybrid work is required, stop before editing and ask the user for backend configuration and authorization. Request only the information needed: backend/runtime and version, API contract or endpoint ownership, database/provider and migration policy, authentication and authorization model, environment variable **names** and safe local/test values (never request secrets in chat), storage/queue/webhook providers, deployment target, data retention/privacy constraints, rate limits, and whether schema/API changes are approved. Do not invent a database, auth provider, endpoint, secret, migration, or production configuration.

If the feature is genuinely frontend-only, continue with a typed/mock boundary where appropriate, document that no backend contract changed, and do not smuggle client-side checks in as security controls.

## 3. Inspect logic and trust boundaries

Map the change before implementation. For the frontend, inspect state ownership, route guards, loading/empty/error states, form validation, optimistic updates, cancellation, retries, stale responses, permissions shown in the UI, and keyboard/accessible behavior. For the backend, inspect input validation, authentication, server-side authorization for every object/action/tenant, business invariants, transaction boundaries, idempotency, replay and race handling, pagination, rate limits, CORS/CSRF, error disclosure, logging/redaction, and dependency boundaries. For APIs, compare request/response schemas, status codes, versioning, backward compatibility, timeout/retry behavior, and client/server assumptions.

Never trust hidden fields, client-calculated prices/roles/statuses, route obfuscation, referrers, or UI-only guards. Reject invalid, out-of-order, repeated, expired, forged, unauthorized, and concurrent workflow transitions on the server. Keep secrets and privileged decisions server-side. Add a focused regression test for every deterministic logic fix.

## 4. Protect users from automated abuse

For public unauthenticated forms, consider a low-friction honeypot as one signal in a layered defense. Add a decoy field that is excluded from the accessible interaction model (`aria-hidden="true"`, `tabindex="-1"`, an appropriate autocomplete strategy, and a visually hidden implementation that does not disrupt screen readers). Give it an ordinary-looking decoy name, reject or quarantine submissions that fill it on the server, and log a redacted reason. Do not punish legitimate users based on the honeypot alone; combine it with rate limiting, payload validation, abuse monitoring, and safe throttling. Never use a honeypot as authentication, authorization, or the only protection for sensitive actions.

Prefer Turnstile or another accessible challenge over a traditional CAPTCHA when the project’s privacy, vendor, and accessibility requirements allow it. Use it selectively for login/sign-in after suspicious or repeated failures, account creation, password reset, high-value actions, or abuse-prone public forms—not automatically on every form. CAPTCHA is defense in depth, not a replacement for MFA, secure password handling, generic authentication errors, server-side rate limiting, lockout/step-up policy, and monitoring. Validate the challenge token on the backend for the exact action and hostname where applicable; never trust a client-only result, never expose the secret key, enforce token expiry/single-use behavior, handle provider timeouts safely, and provide an accessible recovery path.

Surface privacy/cookie/third-party implications to the user. Do not add a bot-protection vendor silently when it changes data flows, consent, cost, or regional availability.

## 5. Keep the project maintainable

Use clear domain-oriented file boundaries instead of a single giant component, route, service, or stylesheet. Separate presentation, state/hooks, API clients, schemas/types, server handlers, domain/business logic, persistence, configuration, styles/tokens, tests, and fixtures according to the project’s framework. Co-locate tightly related feature files, but keep secrets/config, transport, and domain rules separate.

A typical feature may use:

```text
src/features/<feature>/
  components/       # presentational UI
  hooks/            # client state and data orchestration
  api/              # typed transport client only
  schemas/          # request/response and form validation
  domain/           # framework-independent rules
  routes/           # route composition and guards
  tests/            # unit/component/integration coverage
server/<feature>/
  handlers/         # transport and status mapping
  services/         # use cases and transactions
  repositories/     # persistence only
  policies/         # authorization and invariants
```

Adapt the layout to the existing repository; do not reorganize everything for aesthetics. Keep modules cohesive, APIs explicit, imports acyclic where practical, and tests next to the behavior they protect. Prefer pnpm over npm when the project uses Node, and preserve one intentional lockfile authority.

## 6. Build the skeleton before refinement

Start with a design and behavior skeleton: route map, page/frame hierarchy, content blocks, component boundaries, data states, API seams, permissions, and responsive structure. Use real semantic elements and representative content, but keep styling intentionally plain. Confirm the skeleton supports the primary task, correct navigation, states, and backend boundary before adding fonts, imagery, polished tokens, animation, glassmorphism, skeuomorphism, or other visual treatments.

Then refine in checkpoints: structure and behavior first; design direction and tokens second; responsive/accessibility/error states third; performance, polish, and specialist audits last. Keep each checkpoint runnable and reversible. Ask the user before a material design, backend, schema, API, auth, deployment, or dependency decision.

## 7. Document migrations and large changes

Create a migration document whenever a change alters database schema/data, public API or routes, authentication/authorization, deployment/environment configuration, dependencies with compatibility impact, file architecture, or a user workflow that requires coordinated rollout. Use `templates/MIGRATION.md` and place the completed document in the project’s agreed `docs/migrations/` directory (or a documented equivalent).

The migration must state context, current and target state, scope, compatibility window, ordered steps, data/backfill strategy, feature flags, rollback/forward-fix plan, validation queries/checks, ownership, risks, and follow-up cleanup. Never claim rollback is safe if a destructive data migration cannot be reversed; state the recovery path instead. Link the migration from the PR/change summary.

## 8. Maintain an AI handoff context

Create or update `AI_CONTEXT.md` at the project root when another AI may take over, after a major milestone, or whenever architecture/commands/constraints change. Use `templates/AI_CONTEXT.md`. Keep it concise and current: project purpose, current state, architecture map, source of truth, framework/package manager, commands, environment variable names (not values), routes/API contracts, data/auth boundaries, design decisions, active risks, files changed, checks run, known failures, and next safe steps.

Never put secrets, tokens, private customer data, or copied credentials in `AI_CONTEXT.md`. Treat it as a handoff document, not a dump of the entire codebase.

## 9. Verification workflow

1. Read the current relevant skills and repository contribution rules.
2. Classify frontend/backend/hybrid and collect backend configuration before backend work.
3. Inventory files, routes, data flows, trust boundaries, scripts, tests, lockfiles, and workflows.
4. Write or update `AI_CONTEXT.md` for a substantial task and a migration document when the change qualifies.
5. Implement the semantic skeleton with separate maintainable modules.
6. Run focused tests and logic checks; then run lint, typecheck, build, security, and relevant specialist audits.
7. Verify honeypot/challenge behavior server-side, accessibility, rate limits, error states, API status/schema compatibility, and secret redaction when abuse protection is in scope.
8. Re-read `web-design`, `web-engineer`, and `seo-production-audit` after implementation when relevant; fix authorized findings and re-run affected checks.
9. Inspect the diff, verify docs and files exist, check for secrets/generated artifacts, and report what was verified, what was not, and remaining decisions.

## References and templates

- `references/skill-routing.md` — repository skill map and specialist routing.
- `references/architecture-and-logic.md` — frontend/backend/API trust-boundary checks.
- `references/anti-abuse.md` — layered honeypot, Turnstile/CAPTCHA, accessibility, privacy, and authentication guidance.
- `references/best-practices.md` — sources and caveats for workflow and handoff decisions.
- `templates/MIGRATION.md` — migration and large-change context template.
- `templates/AI_CONTEXT.md` — AI-to-AI project handoff template.
- `templates/FEATURE_PLAN.md` — skeleton-first feature planning template.
- `templates/project-quality.yml` — provider-neutral project quality workflow to adapt after inspecting an existing CI setup.
- `scripts/check_skill_repo.py` — deterministic validation used by this repository’s GitHub workflow.

## Completion checklist

Before stopping, verify that current specialist skills and contribution rules were searched; feature scope was classified; backend configuration was requested before backend work; frontend/backend/API logic and trust boundaries were checked; honeypot/challenge choices are layered, server-validated, accessible, and privacy-reviewed; files are separated by responsibility; skeleton behavior was verified before refinement; migration and AI context docs were created when required; relevant specialist checks passed or limitations are explicit; and no secrets or unauthorized changes were introduced.
