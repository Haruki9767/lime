# Migration: [short name]

**Status:** Draft / Approved / In progress / Complete
**Owner:** [person or team]
**Date:** [YYYY-MM-DD]
**Related change:** [issue, PR, or decision link]

## Context

What is changing, why is it changing, and what problem or risk does it address?

## Current state

- Architecture/data/API/auth/deployment state:
- Consumers and dependencies:
- Known constraints:

## Target state

Describe the desired architecture, schema, API contract, workflow, or deployment state. Include compatibility requirements.

## Scope and compatibility

- In scope:
- Explicitly out of scope:
- Backward-compatible window:
- Deprecation/removal dates:
- Feature flag or staged rollout:

## Ordered migration plan

1. [Preflight and backup]
2. [Expand/additive change]
3. [Backfill or dual-read/write, if needed]
4. [Switch consumers]
5. [Validate and observe]
6. [Contract/dead-code cleanup]

## Data and safety

Describe validation, idempotency, batching, transaction boundaries, privacy/retention effects, and how partial failure is detected.

## Rollback or recovery

State what can be rolled back, how, by whom, and within what window. If destructive data changes cannot be reversed, document the forward-fix or restore procedure instead of claiming rollback.

## Verification

- [ ] Local tests:
- [ ] Migration dry run:
- [ ] Production-like validation:
- [ ] API/client compatibility:
- [ ] Monitoring and alerts:
- [ ] Security/privacy review:

## Risks and ownership

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| [risk] | [impact] | [mitigation] | [owner] |

## Cleanup and follow-up

List flags, compatibility shims, old columns/routes, documentation, and monitoring that must be removed or updated.
