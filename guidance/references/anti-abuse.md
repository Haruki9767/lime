# Anti-Abuse Guidance

## Honeypot

Use a honeypot only on public, unauthenticated forms as a low-friction signal. The decoy control must be excluded from the accessible interaction model with `aria-hidden="true"` and `tabindex="-1"`, use a decoy field name and safe autocomplete behavior, and be visually hidden without creating a screen-reader or keyboard trap. Validate it on the server, reject or quarantine filled submissions, and record only a redacted reason. Do not reveal the detection rule in user-facing errors.

A honeypot is not proof that a request is automated. Combine it with schema validation, request size limits, rate limiting, abuse monitoring, duplicate/replay controls, and safe throttling. Avoid false positives and do not use it as authentication, authorization, or the only control protecting a sensitive action.

## Turnstile or CAPTCHA

Use an accessible challenge selectively on login/sign-in after suspicious or repeated failures, account creation, password reset, high-value actions, or abuse-prone public forms. Prefer a lower-friction option such as Turnstile when it fits the project’s vendor, privacy, accessibility, and regional requirements. Do not add a CAPTCHA wall to every form without evidence of abuse.

The backend—not the browser—must validate each token with the provider, enforce token expiry and single-use behavior, verify expected action/hostname where appropriate, time out safely, and keep the secret key out of the frontend. Treat provider failure as a controlled error with retry or a safe alternative; do not silently allow a risky action because a provider is unavailable.

## Authentication defense in depth

Challenge controls supplement, not replace, MFA, strong password handling, generic login/reset responses, server-side throttling, account-level protections, safe recovery, and monitoring. Avoid user enumeration and avoid lockout policies that let an attacker deny service to another user. Log failed validation and abuse signals without passwords, tokens, full request bodies, or unnecessary personal data.

## Privacy and accessibility

Explain third-party challenge, cookies, device/IP data, retention, and regional behavior in the project’s privacy/cookie review. Do not add a vendor that changes data flows or requires consent without authorization; queue the specific approval question and present it with any other applicable questions at the end after safe checks. Test keyboard and screen-reader operation, zoom, reduced motion, localization, error recovery, and users who cannot solve a visual/audio challenge. Provide an accessible alternative or support path where required.
