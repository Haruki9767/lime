---
name: lime
description: Coordinate the reusable Lime Skills for web projects by routing each task to the appropriate guidance, design, engineering, or SEO workflow.
---

# Lime Skills

Use this repository as the entrypoint for the reusable Lime skill collection. Select the focused workflow before acting:

- `guidance/SKILL.md` — project coordination, scope, architecture, migrations, deployment, and AI handoffs.
- `web-design/SKILL.md` — distinctive frontend creation, visual direction, responsive behavior, motion, and accessibility.
- `web-engineer/SKILL.md` — implementation, maintainability, security, accessibility, SEO, testing, and deployment readiness.
- `seo-production-audit/SKILL.md` — technical SEO, structured data, accessibility, AI-search discoverability, and production audits.

## Routing rules

1. Read this file first, then read the one or more focused `SKILL.md` files relevant to the task.
2. For frontend creation or visual changes, use `web-design` and complete the `web-engineer` handoff it requires.
3. For implementation, debugging, or deployment, use `web-engineer` and consult `guidance` when project structure or scope is involved.
4. For search visibility, metadata, structured data, or launch audits, use `seo-production-audit` and apply its engineering and accessibility checks.
5. Treat `lime/` as the repository's Nuxt/Vue website. Do not load it as a skill package or modify it unless the task explicitly concerns the website.

The focused packages contain their own references, scripts, and templates. Load those resources progressively as instructed by the selected workflow.
