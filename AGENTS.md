# Repository guidance for AI agents

## Skill discovery boundary

- Treat only top-level directories containing a `SKILL.md` file as skill packages.
- **Ignore `lime/` when discovering, loading, indexing, or validating skills.** It is the Nuxt/Vue website and deployment project, not a skill package.
- Do not infer skill instructions from files inside `lime/`.
- The authoritative skill packages are `guidance/`, `web-design/`, `web-engineer/`, and `seo-production-audit/`.

## Web project boundary

The `lime/` directory contains the public Nuxt site. Work on it only when the task explicitly concerns the website, its deployment, or its GitHub Pages workflow. Use `lime/README.md` and the root `DEPLOYMENT.md` when available for web-project context.
