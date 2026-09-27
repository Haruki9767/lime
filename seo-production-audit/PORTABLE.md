# Portable Integration Guide

This package is plain Markdown plus one Python standard-library script. It does not require Manus, a specific model provider, an MCP server, a framework, or a proprietary API.

## Option 1: Add as project instructions

Place this directory in the project’s instructions or skills directory, then tell the assistant:

> Read `seo-production-audit/SKILL.md` and apply it to this project. Load only the references needed for the current task. Use the report template for the final audit and mark unavailable checks as `Not tested`.

Common locations include `.ai/skills/`, `.agents/skills/`, `.claude/skills/`, `.cursor/rules/`, `.github/`, or a project-specific `docs/` directory. Follow the host assistant’s documented instruction-file conventions.

## Option 2: Paste as a system or project prompt

Use this prompt with any assistant that can read local files:

```text
You are conducting a production SEO, accessibility, and AI-discovery audit. Read seo-production-audit/SKILL.md first. Inspect the project before proposing changes. Load references/advanced-technical-seo.md for deep technical audits, references/ai-discovery.md for AEO/GEO/LLMO/GSO/AI SEO work, and references/structured-data-and-entities.md for schema or entity work. Use templates/seo-audit-report.md for the report and templates/ai-discovery-test-matrix.md for repeatable generative-search observations. Never invent facts, claims, reviews, authors, prices, locations, citations, or schema values. Distinguish public indexable routes from private routes. Treat robots.txt as a crawl preference, not access control. Report evidence, limitations, and unperformed checks explicitly. Do not promise rankings or citations.
```

## Option 3: Use manually

Ask the assistant to read `SKILL.md`, answer the intake questions, inspect the repository and rendered HTML, then produce the report. References are ordinary Markdown and can be attached or pasted into assistants that cannot browse local files.

## Tool mapping

| Need | Any equivalent tool is acceptable |
|---|---|
| Read files | File browser, repository search, shell, IDE, or model attachments |
| Inspect routes | Framework inspection, static search, crawler, browser, or HTTP client |
| Render pages | Browser automation, headless browser, devtools, or framework build output |
| Check live HTTP | `curl`, HTTP client, browser, or crawler |
| Check accessibility | Accessibility engine, browser audit, screen reader, keyboard/manual review |
| Validate schema | Schema validator, JSON parser, search-engine testing tool, or manual review |
| Measure search | Search Console, analytics, server logs, rank/crawl provider, or documented sample |

If a tool is unavailable, downgrade the result to `Not tested` and explain the limitation. Never substitute an assumed result.

## Script requirements

The included `scripts/check_seo_html.py` uses only Python 3. It checks a saved rendered HTML file for a title, description, canonical link, Open Graph title and description, exactly one `h1`, and `alt` attributes on images:

```bash
python seo-production-audit/scripts/check_seo_html.py path/to/rendered-page.html
```

It is a smoke test, not a crawler, accessibility conformance test, structured-data validator, or live search test.

## Output contract

A compatible assistant should return:

1. Scope, assumptions, and route classification.
2. Evidence-based findings with file, route, or test references.
3. Changes made, if implementation was requested.
4. SEO, AI-discovery, and accessibility verification tables.
5. Prioritized backlog with impact, effort, risk, and measurement.
6. Remaining issues and limitations, including every unavailable or unperformed check.
