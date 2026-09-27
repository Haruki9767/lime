# Feature Plan: [name]

**Request:** [short description]
**Status:** Draft / Approved / In progress / Verified

## Scope classification

- [ ] Frontend-only
- [ ] Backend-required
- [ ] Hybrid
- **Evidence:** [routes, APIs, data, auth, schema, deployment, or why none are changing]

If backend or hybrid, record the user-approved backend configuration before implementation. Never invent secrets; record environment variable names only.

## Skill routing

- [ ] `guidance`
- [ ] `web-design`
- [ ] `web-engineer`
- [ ] `seo-production-audit`
- [ ] Other specialist skills: [names and reasons]

## Skeleton

- Route/page/component boundaries:
- Data states: loading / empty / success / validation / unauthorized / error / retry:
- API seam and typed contract:
- Permission and trust-boundary decisions:
- Responsive and accessibility structure:

## File plan

List the files/directories for presentation, state, transport, schemas, domain rules, server handlers/services/persistence, tests, styles, and docs. Avoid a new monolith.

## Refinement plan

1. Verify semantic skeleton and primary behavior.
2. Add approved design direction, tokens, typography, and content.
3. Add responsive, accessibility, error, and abuse-protection states.
4. Run focused tests, then lint/typecheck/build/security/specialist audits.

## Documentation impact

- [ ] Update `AI_CONTEXT.md`
- [ ] Create/update `docs/migrations/[name].md`
- [ ] Update API/schema/design docs
- [ ] No durable context change needed (explain why)

## Acceptance and verification

- [ ] Frontend behavior:
- [ ] Backend/API behavior:
- [ ] Logic/security checks:
- [ ] Accessibility/design checks:
- [ ] CI checks:
- [ ] SEO/policy checks, if applicable:
