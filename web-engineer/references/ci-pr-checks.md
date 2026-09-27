# CI and Pull-Request Checks

## Table of contents

1. [Package-manager policy](#package-manager-policy)
2. [Required pull-request gates](#required-pull-request-gates)
3. [GitHub workflow pattern](#github-workflow-pattern)
4. [Safe artifacts and secrets](#safe-artifacts-and-secrets)

## Package-manager policy

Prefer pnpm for JavaScript/TypeScript repositories. Follow the exact `packageManager` or `devEngines.packageManager` declaration in `package.json`, commit `pnpm-lock.yaml`, and use `pnpm install --frozen-lockfile` in CI. This makes manifest/lockfile drift fail instead of silently rewriting dependencies.

Treat one lockfile as authoritative. If npm, pnpm, yarn, or bun lockfiles coexist, inspect them and ask the user when they disagree. Remove or regenerate stale competing lockfiles only with authorization. Never choose a package manager merely because an old lockfile happens to be present.

Cache pnpm’s store only when useful and key it with `pnpm-lock.yaml` plus relevant OS/runtime dimensions. Treat store and metadata caches as trusted data; do not let untrusted pull requests write caches later restored by trusted jobs. Keep the pnpm version compatible with the lockfile writer.

## Required pull-request gates

A quality workflow should run on pull requests and pushes to the default branch. It should use read-only repository permissions and run available checks rather than inventing scripts. Preferred order: dependency installation, diff validation, protected-scope validation, typecheck/lint, tests, production build, SEO/accessibility checks, dependency/security audit, secret scan, scanner, and final artifact validation.

At minimum, check that the diff has no whitespace errors, no committed credential patterns, no stale canonical hostname, and no accidental changes to protected design/backend/auth/database/deployment files outside declared scope. For frontend repositories, validate build output and static 404, robots, sitemap, and canonical metadata when applicable.

## GitHub workflow pattern

Adapt this pattern to the repository; do not copy commands that do not exist:

```yaml
name: Web quality
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with:
          version: <follow packageManager declaration>
      - uses: actions/setup-node@v4
        with:
          node-version: <project version>
          cache: pnpm
      - run: pnpm install --frozen-lockfile
      - run: git diff --check
      - run: pnpm run check --if-present
      - run: pnpm test --if-present
      - run: pnpm run build --if-present
      - run: pnpm run seo:check --if-present
      - run: pnpm audit --audit-level=high
      - run: python3 /path/to/scan_web_quality.py --root . --origin "$SITE_ORIGIN" --fail-on high
```

Prefer current official pnpm setup guidance and pin/review third-party actions according to the repository’s policy. If the project explicitly uses another manager, document the exception rather than silently rewriting its lockfiles.

## Safe artifacts and secrets

Never print environment variables, tokens, cookies, deployment credentials, or full audit payloads containing secrets. Upload only redacted diagnostics when necessary. Do not use pull-request code to access production secrets. For forked pull requests, avoid privileged secrets and external write operations. Keep workflow permissions least-privilege and treat dependency caches as trusted inputs.
