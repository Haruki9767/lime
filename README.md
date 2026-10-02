# Lime Skills

Reusable, platform-neutral Lime Skills for AI-assisted web work. Each skill is a self-contained package that can be adapted to an assistant’s project instructions, system prompt, or local skill directory.

## Included skills

- [`guidance`](./guidance/) — project coordination, skill routing, frontend/backend classification, architecture and API logic checks, maintainable file boundaries, skeleton-first delivery, migration documentation, AI handoffs, deployment guidance, and layered anti-bot protection.
- [`web-engineer`](./web-engineer/) — design-preserving web engineering with framework/font/design preference intake, researched best practices, pnpm-first CI, accessibility and SEO, security and business-logic checks, and privacy/cookie/terms readiness.
- [`web-design`](./web-design/) — distinctive web creation and review with AI-slop detection, approved visual direction, React/Vue selection, custom 404/error handling, motion/accessibility safeguards, and post-build SEO and engineering handoffs.
- [`seo-production-audit`](./seo-production-audit/) — production SEO, technical search, accessibility, structured data, GEO, AEO, LLMO, GSO, and AI SEO audits and implementations. See its [`PORTABLE.md`](./seo-production-audit/PORTABLE.md) for cross-assistant integration.

The shared [`final questions protocol`](./guidance/references/final-questions.md) keeps clarification prompts scope-specific: assistants inspect first, ask only about areas the task actually touches, finish and verify safe work, then group any remaining questions at the end.

## Install a skill

Download [`skillmd.zip`](./skillmd.zip), extract it, and copy the complete directory for each skill you want into the assistant’s local skill directory. Keep each directory intact: `SKILL.md` is the entrypoint, while its `references/`, `scripts/`, and `templates/` provide optional supporting material. Do not flatten the files.

The ZIP contains the four skill packages, not the Nuxt showcase website. To regenerate it after editing a skill, run:

```bash
python3 guidance/scripts/build_skill_archive.py
```

The repository validator checks that the committed ZIP exactly matches the current package files.

## Releases

Push a version tag such as `v1.0.0` to run [the release workflow](./.github/workflows/release.yml). It validates the skill packages and tests, verifies that `skillmd.zip` matches the tagged sources, then creates a GitHub Release with generated notes and the ZIP attached. Ordinary pushes to `main` do not create a release.

## AI setup in this repository

Use the root [`SKILL.md`](./SKILL.md) to route work to focused skills and [`Profile`](./Profile) for repository boundaries and AI working rules. [`tooling.md`](./tooling.md) lists expected runtime and package-manager versions. The [`lime/`](./lime/) directory is the separate Nuxt/Vue showcase site; it is not a skill package.

## License

MIT — see [`LICENSE`](./LICENSE).
