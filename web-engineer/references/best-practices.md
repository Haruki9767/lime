# Researched Best Practices

Use this reference to ground recommendations and record updates. Re-check official sources when the task depends on a newer framework, package-manager major, browser behavior, regulation, or jurisdiction.

## Package management and CI

- Prefer pnpm. Commit `pnpm-lock.yaml` and use `pnpm install --frozen-lockfile` in CI so manifest/lockfile drift fails instead of rewriting dependencies.
- Declare the package-manager version in `package.json` with `packageManager` (exact) or `devEngines.packageManager` (range/resolved version), and keep CI compatible with the lockfile writer.
- Treat pnpm store and metadata caches as trusted data. Cache only when useful, key by lockfile plus relevant runtime/platform dimensions, and prevent untrusted jobs from poisoning caches restored by trusted jobs.
- Treat integrity failures as hard failures. Do not bypass them with `--force`, `--offline`, or checksum updates without independently verifying the cause.

Sources:

- [pnpm Continuous Integration](https://pnpm.io/continuous-integration)
- [pnpm install](https://pnpm.io/cli/install)
- [pnpm package.json settings](https://pnpm.io/package_json)
- [pnpm supply-chain security](https://pnpm.io/supply-chain-security)

## Security and logic flaws

- Enforce authorization server-side on every request, for the specific object, tenant, action, and workflow state. Do not rely on client checks, guess-resistant IDs, referrers, or hidden fields.
- Use explicit deny-by-default and least privilege. Test an authorization matrix, including horizontal and vertical escalation, missing permissions, cross-tenant access, and guessed/tampered identifiers.
- Validate untrusted values and business invariants on the server. Recompute ownership, prices, totals, discounts, limits, and state from trusted data.
- Model multi-step workflows as server-side state machines. Reject skipped, out-of-order, repeated, expired, forged, replayed, or concurrent transitions.
- Test business logic beyond the happy path: forged requests, negative/edge values, timing/races, function-use limits, double submits, partial failures, uploads, and misuse defenses. Use safe non-destructive tests and report evidence without accessing other users’ data.

Sources:

- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [OWASP Business Logic Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Business_Logic_Security_Cheat_Sheet.html)
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- [OWASP Web Security Testing Guide: Business Logic](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/10-Business_Logic/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)

## Accessibility

- Use WCAG 2.2 as the current standards reference when applicable. Evaluate the four principles—perceivable, operable, understandable, robust—with automated checks plus human/functional review.
- Define scope, representative pages/views, process steps, variants, third-party content, technology baseline, date, and target level before making a conformance statement.
- Test full pages and complete user flows. Do not generalize a partial sample into a whole-site claim. Report unmet success criteria, reproducible evidence, manual coverage, and limitations.
- Treat WCAG conformance as distinct from usability. Supplement conformance checks with user research/usability testing involving disabled users where appropriate. Do not claim legal compliance from an automated scan.

Sources:

- [W3C WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C WCAG overview](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [W3C WCAG-EM 2.0](https://www.w3.org/TR/wcag-em-2/)

## Privacy, cookies, and terms

- Do not assume a universal requirement. Whether privacy notices, cookie controls, terms, or consent are needed depends on data practices, technologies, audience, business model, and applicable jurisdictions.
- Inventory personal-data collection, analytics/advertising, cookies and similar device access, accounts, transactions, user content, children’s access, and sensitive/regulated data before making a policy recommendation.
- When applicable, provide clear privacy information at or before collection, explain purposes/retention/sharing/rights, and update it before materially new uses.
- Where applicable e-privacy rules require consent, disclose non-essential cookies/device technologies and obtain affirmative, informed consent before setting/accessing them. Keep refusal and withdrawal usable; strictly necessary exceptions are narrow and should still be explained.
- Surface terms/conditions for contracts, paid services, accounts, subscriptions, marketplaces, user content, or sales. Flag jurisdiction-specific legal review rather than drafting legal text as fact.

Sources:

- [ICO: Right to be informed](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/)
- [ICO: Cookies and similar technologies](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/cookies-and-similar-technologies/)
- [California Attorney General: CCPA](https://oag.ca.gov/privacy/ccpa)
- [European Union: consumer contracts](https://europa.eu/youreurope/business/selling-in-eu/consumer-contracts-guarantees/consumer-contracts/index_en.htm)
- [FTC: COPPA FAQ](https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions)

## Research caveats

- Official documentation changes. Record the date and version relevant to each project.
- Standards and regulator guidance do not replace legal advice or a complete penetration test.
- Framework defaults and third-party actions can change; inspect the project’s actual configuration and pin/review dependencies and CI actions.
