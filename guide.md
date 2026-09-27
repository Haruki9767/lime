# How to use Lime Skills

Lime Skills is a small set of reusable instructions for AI-assisted web work. The skills are designed to be routed—not pasted blindly into every task.

## 1. Start with the right skill

Read only the skill that matches the work, then load adjacent specialists when the workflow says to do so.

| Work | Start with | Add when relevant |
|---|---|---|
| Planning, architecture, handoffs, migrations, deployment | [`guidance/`](./guidance/) | `web-design`, `web-engineer`, `seo-production-audit` |
| Creating or redesigning a frontend | [`web-design/`](./web-design/) | `guidance`, `web-engineer`, `seo-production-audit` |
| Framework, accessibility, security, privacy, or launch quality | [`web-engineer/`](./web-engineer/) | `guidance`, `seo-production-audit` |
| Search visibility, crawlability, metadata, structured data | [`seo-production-audit/`](./seo-production-audit/) | `web-engineer`, `web-design` |

**Important:** ignore [`lime/`](./lime/) during skill discovery. It contains the public Nuxt website and deployment project, not a skill package. Only top-level directories containing `SKILL.md` are skills.

## 2. Use the normal web-project sequence

For a new or substantial website, use this order:

1. **Guidance** — discover the repository, classify frontend/backend/hybrid scope, map constraints, and define the skeleton.
2. **Web Design** — establish the visual direction, typography, layout, interaction, responsive behavior, and error states.
3. **Web Engineer** — review the framework implementation, accessibility, security, privacy readiness, logic, and launch configuration.
4. **SEO Production Audit** — verify metadata, canonical URLs, crawl controls, headings, images, routes, structured data, and indexability.
5. **Guidance again** — update deployment, migration, AI handoff, and next-step documentation.

Do not skip discovery. Read the current `SKILL.md` files from the repository rather than relying on a cached copy.

## 3. Keep the boundary between skills and the website

The skill packages are the source of truth for reusable AI guidance. The `lime/` directory is a normal Nuxt application.

For website work:

```bash
cd lime
pnpm install --frozen-lockfile
pnpm typecheck
pnpm generate
pnpm dev
```

For skill-repository validation:

```bash
python3 guidance/scripts/check_skill_repo.py
```

## 4. Make changes safely

- Inspect before editing.
- Do not invent APIs, credentials, policies, users, metrics, or deployment secrets.
- Ask for missing backend or authorization details before hybrid/backend work.
- Keep files separated by responsibility and preserve existing package boundaries.
- Add or update `DEPLOYMENT.md` when runtime, build, domain, adapter, or environment requirements change.
- Update `AI_CONTEXT.md` after architecture or command changes.
- Run relevant checks before committing and inspect the final diff for secrets and generated artifacts.

## 5. Commit and deploy

Use focused commits that explain why the change exists. The website deploys as static output from `lime/.output/public` through the GitHub Pages workflow at [`.github/workflows/lime-pages.yml`](./.github/workflows/lime-pages.yml). Cloudflare Pages is also documented as the primary static-hosting recommendation in [`DEPLOYMENT.md`](./DEPLOYMENT.md).

The current website does not require environment variables. If that changes, document variable names, purpose, public/private exposure, and environment scope—never commit secret values.
