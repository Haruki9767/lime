# Production SEO Audit Skill

A Manus skill for production SEO, technical search visibility, accessibility, entity optimization, and AI-mediated discovery.

## What it covers

- Technical SEO: crawlability, rendering, indexation, URLs, redirects, sitemaps, robots, performance, internationalization, and structured data.
- Content and entity SEO: search intent, topical coverage, internal linking, authorship, trust, evidence, and content governance.
- AEO: answer-oriented information architecture and direct, verifiable responses.
- GEO, LLMO, and GSO: making public information clear, retrievable, attributable, and useful in generative search and language-model experiences.
- AI SEO governance: provenance, human review, accessibility, privacy, hallucination controls, and anti-spam safeguards.
- Reporting: prioritized backlogs, verification matrices, measurement baselines, and explicit limitations.

## Package layout

```text
seo-production-audit/
├── SKILL.md
├── README.md
├── references/
│   ├── advanced-technical-seo.md
│   ├── ai-discovery.md
│   └── structured-data-and-entities.md
├── scripts/
│   └── check_seo_html.py
└── templates/
    ├── ai-discovery-test-matrix.md
    └── seo-audit-report.md
```

`SKILL.md` contains the core workflow. Load a reference only when the task needs that depth. Use templates for consistent deliverables and run the HTML checker against representative rendered pages.

## Usage principles

1. Discover the framework, routes, domain, audience, goals, and evidence before changing page-specific content.
2. Build technical and content foundations before adding AI-discovery recommendations.
3. Never invent claims, reviews, authors, prices, locations, citations, or structured-data values.
4. Treat `robots.txt` as a crawl preference, not access control.
5. Never promise rankings, traffic, featured snippets, or generative citations.
6. Report unperformed checks as `Not tested`, not as passing.

## Local validation

From the repository root:

```bash
python /home/ubuntu/skills/skill-creator/scripts/quick_validate.py seo-production-audit
python seo-production-audit/scripts/check_seo_html.py path/to/rendered-page.html
```

The checker is a focused static smoke test, not a replacement for a browser crawl, accessibility audit, Search Console data, server logs, or live-engine testing.
