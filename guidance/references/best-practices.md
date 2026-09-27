# Guidance Best Practices

## GitHub Actions

Use read-only `contents: read` permissions by default. Prefer `pull_request` for untrusted change validation and avoid privileged `pull_request_target` unless there is a documented need. Do not expose secrets to untrusted code. Pin third-party actions to reviewed versions or full commit SHAs where the repository’s maintenance policy supports it. Keep workflow checks deterministic, fail closed, and avoid interpolating untrusted event text directly into shell code.

Sources:

- [GitHub Actions workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)
- [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

## Turnstile and challenges

A client widget is not protection. Turnstile tokens must be validated by the backend through Siteverify, checked for expected action/hostname where used, treated as short-lived and single-use, and handled with timeouts and safe fallback behavior. Store the secret server-side. Add challenges selectively after risk signals or on abuse-sensitive flows; do not turn every form into a CAPTCHA wall.

Source: [Cloudflare Turnstile server-side validation](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)

## Authentication abuse

CAPTCHA is defense in depth, not a replacement for MFA, secure password handling, generic login/reset responses, server-side throttling, account-level protections, monitoring, and careful recovery flows. Avoid account-enumeration messages and avoid lockout designs that let attackers deny service to other users.

Source: [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

## Caveat

Honeypots are heuristic signals and can be bypassed. They should be server-enforced, accessible to assistive technology users, privacy-reviewed, and combined with rate limits, validation, monitoring, and step-up controls. Vendor choice, cookies, IP handling, and challenge data can create legal or consent obligations that require project-specific review.
