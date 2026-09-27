# Security checklist and severity guidance

Use this reference for source review and safe verification. This checklist is not a penetration-testing authorization.

## Trust boundaries

- Identify browser, API, worker/server, database, storage, queue, third-party, and admin boundaries.
- Trace identity, session, authorization, tenant/resource ownership, and privileged operations.
- Confirm server-side authorization for every read/write; do not rely on hidden UI or robots rules.
- Review CORS, CSRF, cookies, tokens, redirects, rate limits, and error responses at the boundary.

## Common bug classes

- Secrets committed in source, bundles, logs, fixtures, or CI output.
- XSS/HTML injection through unsafe HTML, URL, Markdown, templates, or DOM sinks.
- SQL/NoSQL/command/path injection and unsafe deserialization.
- IDOR/BOLA, privilege escalation, missing tenant checks, and insecure direct object references.
- Weak session handling, missing expiry/revocation, insecure cookie flags, and token leakage.
- CSRF on cookie-authenticated state changes; CORS allowing credentials to arbitrary origins.
- Open redirects, SSRF, unrestricted file upload, path traversal, debug/admin endpoints, verbose errors.
- Vulnerable or unpinned dependencies, insecure third-party scripts, and missing security headers.

## Evidence rules

- Use static evidence, tests, dependency advisories, and non-destructive requests.
- Mask tokens, personal data, database rows, and secret values in reports.
- Reproduce only against authorized local/test targets and never bypass controls.
- Separate confirmed findings from hypotheses. State what was not tested.

## Severity

- **Critical:** reliable remote compromise, arbitrary code execution, broad secret exposure, or unauthenticated access to all sensitive data.
- **High:** authentication/authorization bypass, cross-tenant access, stored XSS, significant secret exposure, or destructive injection.
- **Medium:** meaningful impact requiring conditions, such as CSRF, reflected XSS, SSRF with limited reach, weak isolation, or risky dependency exposure.
- **Low:** defense-in-depth gaps with limited direct impact, such as missing headers or verbose but non-sensitive errors.
- **Informational:** hygiene, maintainability, or unverified suspicion.

Every finding should include: ID, severity, affected asset, evidence, impact, safe reproduction or reasoning, remediation, regression test, and status.
