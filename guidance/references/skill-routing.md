# Skill Routing

Load the smallest current set of skills that covers the task. Search the project’s configured skill directories and repository before reading; a missing or renamed skill must be recorded rather than guessed.

| Task signal | Load first | Then load |
|---|---|---|
| New feature, architecture, agent handoff, migration, unclear scope | `guidance` | `web-design`, `web-engineer`, `seo-production-audit` as applicable |
| New page, redesign, visual polish, anti-slop review, motion | `web-design` | `accessibility` and `web-engineer` when applicable |
| API, auth, database, server logic, deployment, security | `guidance` then `web-engineer` | `systematic-debugging`, SQL, observability, or CI skills as applicable |
| SEO, routes, metadata, structured data, crawl/indexability | `seo-production-audit` | `web-engineer` for implementation boundaries |
| Build/test failure or unexpected behavior | `systematic-debugging` | `debugging-and-error-recovery`, then the domain skill |
| GitHub quality gates, CI, release automation | `ci-cd-and-automation` | `guidance`, `git-workflow-and-versioning` |
| Dependency update | `dependency-updater` | `guidance` and the affected domain skill |
| Repository commit/push/PR | `git-workflow-and-versioning` and `make-repo-contribution` | `guidance` when scope or docs are affected |

After implementation, re-read `web-design`, `web-engineer`, and `seo-production-audit` when the work touches a web experience. Apply their findings only within approved scope and report unavailable tools or checks.
