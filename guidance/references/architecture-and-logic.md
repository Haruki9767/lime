# Architecture and Logic Checks

## Boundary map

Record browser/UI, API/worker/server, database, storage, queue, webhook, third-party, and admin boundaries. Identify authentication, authorization, tenant/object ownership, secrets, personal data, trust transitions, and public/private routes.

## Frontend checks

Verify state ownership, route guards, loading/empty/error/retry states, form validation, cancellation, stale-response handling, optimistic-update rollback, keyboard behavior, and clear API status handling. Client checks improve UX but never replace server authorization or validation.

## API and backend checks

Verify request size/type/schema validation, authentication, server-side authorization for the exact object/action/tenant, business invariants, transaction boundaries, idempotency, replay protection, concurrency handling, pagination, rate limits, CORS/CSRF, safe errors, redacted logs, and dependency timeouts. Compare client/server schemas, status codes, versioning, defaults, nullability, and backward compatibility.

For multi-step workflows, model allowed server-side states and transitions. Reject skipped, repeated, expired, forged, out-of-order, unauthorized, and concurrent transitions. Test duplicate requests, retries, partial failures, and a user attempting to change another user’s object.

## Change evidence

For each finding, record the file/route, trust boundary, observed behavior, expected invariant, test or command, confidence, and whether the change was authorized. Never call a client-side appearance check, hidden field, status code, or successful build proof of security.
