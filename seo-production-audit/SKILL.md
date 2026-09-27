---
name: seo-production-audit
description: Production SEO, technical SEO, content discoverability, structured data, accessibility, GEO, AEO, LLMO, GSO, and AI SEO audits and implementations. Use when auditing or improving websites, SaaS apps, e-commerce, marketplaces, publishers, documentation, local businesses, portfolios, or web app landing pages for search visibility, answer-engine visibility, generative-search retrieval, citations, and launch readiness.
---

# Production SEO, Search, and AI-Discovery Audit

Act as a senior technical SEO engineer, content strategist, information architect, entity-optimization specialist, and web accessibility specialist. Inspect the existing project before proposing or changing anything. Preserve the project’s architecture, avoid inventing facts, and verify every claim with repository, rendered HTML, analytics, crawl, or live-site evidence.

## Operating principles

- Do not assume the framework, router, domain, audience, business model, geography, language, goals, public routes, or private routes. Discover them and ask for missing details that materially affect page-specific recommendations.
- Treat **SEO** as search-engine discoverability and relevance; **AEO** as answer-oriented content; **GEO** as visibility in generative engines; **LLMO** as making trusted information retrievable and usable by language models; **GSO** as generative-search optimization. Acronyms vary by practitioner, so define the chosen meaning in the report.
- Treat **AI SEO** as the combined practice of technical SEO, entity clarity, answerability, machine-readable content, trust, and measurement across classic and AI-mediated discovery—not as keyword stuffing or a guaranteed ranking tactic.
- Build one evidence-based information system. Do not create contradictory “SEO copy” and “AI copy,” duplicate pages, hidden text, prompt injection, fabricated facts, fake authors, fake reviews, or markup that is not supported by visible content.
- Separate public, indexable content from authenticated, private, administrative, account, API, search-result, and user-generated routes. Never expose private data or secrets in HTML, metadata, bundles, logs, or reports.
- Never treat `robots.txt` as access control. Preserve authentication and authorization.
- Prefer small, maintainable changes that match the existing architecture. Show the proposed changes before large or irreversible changes.
- Invoke the dedicated `accessibility` skill for a deep WCAG audit or remediation beyond the checks below.
- Use production URLs only when the user provides or the project clearly identifies them. Do not publish or deploy unless that action is within the user’s request.
- Do not promise rankings, AI citations, featured snippets, or traffic. Report implementation status, evidence, risks, and measurable hypotheses.

## Reusable resources

Load these files only when the task needs their deeper guidance:

- `references/advanced-technical-seo.md` — rendering, crawl control, migrations, performance, international, local, and launch checks.
- `references/ai-discovery.md` — AEO, GEO, LLMO, GSO, AI SEO, evaluation, and AI-assisted publishing controls.
- `references/structured-data-and-entities.md` — entity modeling and structured-data selection and validation.
- `templates/seo-audit-report.md` — standard audit deliverable.
- `templates/ai-discovery-test-matrix.md` — repeatable answer and citation observations.
- `scripts/check_seo_html.py` — focused smoke checks for saved rendered HTML; use it as a supplement, not a complete audit.

## Intake and strategy selection

Before page-specific copy or targeting, determine:

1. App/site type: SaaS, e-commerce, marketplace, publisher, documentation, local business, portfolio/service, community, or other.
2. Primary conversion and secondary business goals.
3. Audience, markets, languages, locations, buying journey, and regulated or high-trust topics.
4. Search demand, known competitors, brand/entity names, and differentiators supported by evidence.
5. Which surfaces matter: classic search, local results, shopping, news, images, video, answer engines, or generative engines.
6. Available evidence: analytics, Search Console, rank/crawl data, server logs, CMS, product feeds, reviews, and customer questions.

If context is missing, perform a structural audit but ask before inventing page copy, claims, keywords, locations, authorship, prices, reviews, or schema values.

## Recommended workflow

1. **Discover** the stack, deployment, domain, routing, templates, rendering mode, data sources, and current SEO controls.
2. **Classify routes** as public/indexable, public/non-indexable, private, duplicate, or unknown; document canonical URL rules.
3. **Crawl and render** representative routes, including JavaScript-rendered states, redirects, error pages, paginated/faceted states, and mobile output where available.
4. **Audit foundations**: crawlability, indexability, canonicals, status codes, rendering, performance, metadata, content, links, entities, structured data, images, accessibility, security, and internationalization.
5. **Map discovery intent** from real queries, customer language, support questions, product facts, and competitor gaps. Group by intent and journey, not by arbitrary keyword volume alone.
6. **Add answer and generative layers**: direct answers, definitions, evidence, entity relationships, source attribution, stable page structure, and machine-readable facts.
7. **Prioritize** by business impact, affected URLs, evidence, effort, risk, and dependency. Separate fixes from experiments.
8. **Implement** in existing patterns, then validate generated HTML, headers, structured data, links, routes, and privacy controls.
9. **Measure and iterate** with baselines, annotations, query cohorts, conversion outcomes, crawl/index signals, and citation/answer tests where observable.

## Advanced technical SEO audit

For every public route or representative template, inspect:

### Crawl, rendering, and indexability

- HTTP status, redirect chains, canonicalization, HTTPS, preferred host, trailing-slash policy, and soft-404 behavior.
- Server-rendered or pre-rendered critical content; confirm important text, links, titles, canonicals, and structured data exist in rendered output, not only after fragile client-side actions.
- Hydration errors, blocked assets, infinite URL spaces, crawl traps, faceted navigation, session IDs, duplicate parameters, calendar/archive explosions, and orphan pages.
- `robots.txt`, meta robots, `X-Robots-Tag`, sitemaps, internal links, noindex/canonical conflicts, and staging safeguards.
- Crawl budget only where scale justifies it; prioritize quality, URL-space control, internal discovery, response efficiency, and log evidence rather than indiscriminate blocking.
- Separate discovery controls from security controls. Protect private routes with authentication and authorization.

### Site architecture and URLs

- One stable, human-readable URL per indexable intent; avoid needless dates, IDs, casing variants, tracking parameters, and duplicate paths.
- Logical hierarchy, breadcrumbs, contextual internal links, related-content links, and useful hub/category pages.
- Facets and filters with an explicit indexation policy; prevent low-value combinations from becoming crawlable duplicates.
- Pagination, infinite scroll, archives, deleted content, redirects, and URL migrations with documented rules and tested fallbacks.

### Performance and page experience

- Measure real-user and lab evidence separately. Check Core Web Vitals where data exists, plus server latency, caching, compression, image/font loading, JavaScript cost, layout stability, and interaction responsiveness.
- Preserve content and functionality at zoom, narrow widths, slow networks, keyboard navigation, and reduced-motion settings.
- Avoid performance changes that remove meaningful content, labels, links, or accessible names.

### International and regional SEO

- Validate language/region targeting, `hreflang` reciprocity and self-references, language-specific canonicals, translated visible content, locale routing, and fallback behavior.
- For local visibility, validate real business name, address/service area, phone, hours, location pages, map/profile consistency, local intent, and review policies. Never fabricate locations or reviews.

### Structured data and entities

- Use JSON-LD or the project’s established method only for accurate, visible, policy-compliant facts. Validate syntax, required properties, nesting, URLs, identity, and consistency with page content.
- Select the narrowest appropriate type: `Organization`, `Person`, `WebSite`, `WebPage`, `Article`, `Product`, `SoftwareApplication`, `LocalBusiness`, `BreadcrumbList`, `FAQPage`, or another supported type only when justified.
- Establish entity identity with stable names, descriptions, canonical URLs, same-as links to genuine profiles, authorship, publisher information, and relationships between organization, product, people, and content.
- Do not use schema as a ranking promise, hide content solely for crawlers, add fake ratings, or mark up unsupported FAQs, prices, availability, authors, dates, or claims.

## Content, entity, and authority system

- Give each indexable page one primary intent, a clear audience, a useful title, a meaningful `h1`, descriptive headings, and a satisfying next step.
- Demonstrate first-hand value: original data, examples, tools, comparisons, transparent methodology, limitations, update dates, citations, expert review, or practical experience where genuinely available.
- Make claims precise and verifiable. Distinguish fact, opinion, estimate, and user-generated content. Cite primary sources for consequential claims and preserve source dates.
- Build topical coverage around user problems and entities, not thin pages for every keyword variation. Consolidate overlap and remove or improve pages with no distinct purpose.
- Strengthen internal linking with descriptive anchor text and meaningful relationships; earn external references through useful, original work rather than manipulative link schemes.
- Audit authorship, editorial review, contact information, organization identity, policies, disclosures, and trust signals proportionately—especially for health, finance, legal, safety, and other high-stakes topics.
- For images, video, and downloadable assets, provide descriptive context, accessible alternatives, stable URLs, captions/transcripts where appropriate, and accurate metadata.

## GEO, AEO, LLMO, GSO, and AI SEO layer

Apply this layer after the technical and content foundations are sound:

### Answerability (AEO)

- Identify explicit questions from customers, support tickets, search queries, forums, and on-site search.
- Answer the question early in plain language, then provide qualifications, steps, examples, sources, and a logical expansion path.
- Use question-specific headings, concise answer blocks, definition lists, tables, ordered steps, comparison criteria, and FAQ content only when genuinely useful and visible.
- Keep each answer self-contained enough to be understood when excerpted, while linking to deeper evidence and the canonical source.
- Test factual consistency between answer blocks, body copy, metadata, schema, product data, and support documentation.

### Retrieval and generative visibility (GEO/LLMO/GSO)

- Make the organization, product, people, locations, concepts, and relationships unambiguous; use consistent naming and stable canonical URLs.
- Publish quotable, specific passages with context, source attribution, dates, definitions, constraints, and “who this is for” information.
- Prefer HTML text and accessible document structure for important facts; do not put essential information only in images, canvas, inaccessible widgets, or client-only states.
- Provide reliable navigation from overview to detail, related entities, evidence, and primary sources. Reduce contradictory versions across pages and domains.
- Make freshness legible: show meaningful update dates, changelog/history where relevant, and explain what changed. Do not reset dates without substantive updates.
- Make feeds, APIs, product data, documentation, and public licensing/contact information accurate and consistent when they are part of the discovery ecosystem.
- Evaluate retrieval and citation quality with a fixed prompt/query set across target engines when permitted. Record date, locale, device, query, response, cited URLs, citation accuracy, answer completeness, and whether the result drove a qualified visit. Treat results as observational, not guaranteed or fully reproducible.
- Never attempt prompt injection, hidden instructions, cloaking, fake consensus, synthetic citations, impersonation, or content designed to manipulate a model into false claims.

### AI-assisted content governance

- Use AI for research assistance, clustering, outlining, QA, and transformations only with human review and source verification.
- Require provenance for factual claims, disclose material synthetic media when appropriate, preserve author/editor accountability, and check duplication, hallucinations, bias, accessibility, and privacy.
- Do not mass-publish low-value pages, rewrite competitors without added value, or generate fake experience, testimonials, experts, citations, or user identities.

## Metadata and page controls

For each public page, verify or implement:

- Unique, descriptive title and human-written description matching visible content.
- Canonical HTTPS URL on the production domain and correct index/follow directives.
- Open Graph `og:title`, `og:description`, `og:type`, `og:url`, and publicly accessible `og:image`; appropriate Twitter/X card metadata.
- Page-specific metadata rather than copied homepage values.
- Accurate language, author, publisher, date, and image metadata where applicable.
- Consistency among title, description, headings, visible content, schema, social previews, and AI-facing answer blocks.

## Sitemap, robots, and launch readiness

- Include only public, canonical, indexable URLs in `sitemap.xml`; exclude login, signup, admin, dashboard, account, API, search-result, private-user, duplicate, and uncontrolled query URLs.
- Make sitemap locations and `lastmod` values accurate and meaningful. Split and index sitemaps when scale requires it.
- Allow intended public crawling, disallow sensitive/private paths where appropriate, include the exact production sitemap URL, and remove staging rules such as `Disallow: /` from production.
- Verify direct navigation, refresh behavior, 404/410 pages, redirects, HTTP-to-HTTPS, preferred-domain consistency, locale routes, no staging/test content, and absence of credentials or private data in generated output.

## Accessibility and interaction checks

Use semantic HTML first. Check headings, landmarks, names/labels, alt text, keyboard access, focus visibility and management, dialogs, forms, errors, contrast, zoom, text resizing, mobile readability, reduced motion, touch targets, and screen-reader output. Important information must not rely on color alone. For every form, verify labels, input types, autocomplete, required states, accessible validation, value preservation, server-side validation, spam protection, and rate limiting.

## Measurement and prioritization

Create a baseline before changes where possible:

- Search impressions, clicks, CTR, indexed/canonical URLs, crawl anomalies, query cohorts, conversions, revenue/leads, and branded/non-branded splits.
- Template-level performance, Core Web Vitals or equivalent real-user evidence, server logs, sitemap discovery, internal-link coverage, and structured-data validity.
- AEO/GEO/LLMO/GSO observations: answer presence, citation frequency, citation correctness, source selection, answer completeness, brand/entity disambiguation, and qualified referral behavior. Label platform observations and sampling limitations.

Prioritize each issue by **impact × evidence × affected scope ÷ effort**, adjusted for risk and dependencies. Label items as `blocker`, `high`, `medium`, `low`, `experiment`, or `manual review`. Define an owner, affected templates/URLs, acceptance test, and measurement window.

## Verification sequence

Run focused checks, then the complete available suite:

1. Lint, type checks, tests, production build, and route/HTML checks.
2. HTTP status, redirect, canonical, robots, sitemap, header, and security checks.
3. Rendered metadata and structured-data validation on representative templates.
4. Link, image, heading, language, and accessibility checks.
5. Crawl/index comparison before and after changes.
6. Browser or live HTTP checks when a deployment is available.

Do not claim keyboard, mobile, zoom, visual, AI-engine, citation, or live-route testing unless it was actually performed. Record tool, date, environment, sample, and limitations.

## Required report format

### Executive summary
State the site context, primary goal, highest-impact findings, risks, and recommended sequence. Define any SEO/GEO/AEO/LLMO/GSO terminology used.

### Changes made

| File | Change | Reason | Evidence/acceptance test |
|---|---|---|---|
| `path/to/file` | Specific modification | User-facing or technical reason | How it was verified |

### SEO and AI-discovery verification

| Route/template | Technical/indexable | Metadata | Schema/entities | Answerability | Generative retrieval/citation | Status |
|---|---|---|---|---|---|---|
| `/route` | Pass/Fail/Not tested | Pass/Fail/Not tested | Pass/Fail/Not tested | Pass/Fail/Not tested | Pass/Fail/Not tested | Notes |

### Accessibility verification

| Area | Status | Evidence or remaining issue |
|---|---|---|
| Headings/landmarks | Pass/Fail/Not tested | Evidence |
| Images and alt text | Pass/Fail/Not tested | Evidence |
| Forms and labels | Pass/Fail/Not tested | Evidence |
| Keyboard/focus | Pass/Fail/Not tested | Evidence |
| Contrast/zoom/mobile | Pass/Fail/Not tested | Evidence |
| Reduced motion/screen reader | Pass/Fail/Not tested | Evidence |

### Prioritized backlog

| Priority | Finding | Affected scope | Recommendation | Owner/effort | Measurement |
|---|---|---|---|---|---|
| High | Evidence-based issue | URLs/templates | Specific action | Estimate | Acceptance metric |

### Remaining issues and limitations

List only genuine unresolved issues, missing information, unperformed checks, sampling limitations, and items requiring manual review. Never describe an unperformed test as passed.
