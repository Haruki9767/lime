# AI Skills

Reusable, platform-neutral AI skills maintained in this repository. Each package can be adapted to an assistant’s project instructions, system prompt, or local skill directory.

## Included skills

- [`guidance`](./guidance/) — project coordination, skill routing, frontend/backend classification, architecture and API logic checks, maintainable file boundaries, skeleton-first delivery, migration documentation, AI handoffs, deployment guidance, and layered anti-bot protection.
- [`web-engineer`](./web-engineer/) — design-preserving web engineering with framework/font/design preference intake, researched best practices, pnpm-first CI, accessibility and SEO, security and business-logic checks, and privacy/cookie/terms readiness.
- [`web-design`](./web-design/) — distinctive web creation and review with AI-slop detection, approved visual direction, React/Vue selection, custom 404/error handling, motion/accessibility safeguards, and mandatory post-build SEO and web-engineering handoff.
- [`seo-production-audit`](./seo-production-audit/) — production SEO, technical search, accessibility, structured data, GEO, AEO, LLMO, GSO, and AI SEO audits and implementations. See its [`PORTABLE.md`](./seo-production-audit/PORTABLE.md) for cross-assistant integration.

## Site

The public field guide is built with Nuxt 4 and Vue 3 at [lime.isroot.in](https://lime.isroot.in). It uses Departure Mono for headings and Handlee for paragraphs, with a black, dark green, white, and acid-green palette.

```bash
pnpm install --frozen-lockfile
pnpm dev
pnpm typecheck
pnpm generate
```

Deployment settings, environment variables, DNS, and post-deploy checks are documented in [`DEPLOYMENT.md`](./DEPLOYMENT.md).

## License

MIT — see [`LICENSE`](./LICENSE).
