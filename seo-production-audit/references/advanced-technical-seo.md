# Advanced Technical SEO Reference

Use this reference when a task requires more than page metadata and basic sitemap checks.

## Rendering and crawl control

- Compare source HTML, rendered DOM, response headers, and browser behavior. Critical titles, canonicals, links, structured data, and content should not depend on a fragile interaction.
- Inventory status codes, redirect chains, soft 404s, canonical conflicts, blocked resources, hydration errors, orphan URLs, and accidental noindex directives.
- Model URL spaces created by facets, sort orders, filters, sessions, calendars, internal search, and tracking parameters. Set an explicit policy for each family.
- Use `robots.txt` to manage crawl preferences only. Use authentication and authorization to protect private data.
- Use log analysis at scale: compare bot requests with sitemap URLs, canonical URLs, indexable URLs, response classes, latency, and stale or wasted crawl paths.

## Architecture and migrations

- Prefer one stable canonical URL for each distinct intent.
- Use contextual internal links, breadcrumbs, hubs, and descriptive anchors to expose important pages.
- For migrations, inventory old-to-new URLs, preserve intent, test redirect chains, update canonicals and internal links, retain assets, and monitor 404s and indexing after launch.
- Define behavior for deleted, merged, expired, paginated, and localized content before implementation.

## Performance and resilience

Measure real-user and lab evidence separately. Check server response time, caching, compression, image dimensions and formats, font loading, JavaScript cost, layout stability, interaction latency, and failure states. Do not improve a metric by removing meaningful content or accessible functionality.

## International and local systems

Validate locale routing, translated visible content, self-referencing and reciprocal `hreflang`, locale-appropriate canonicals, fallback behavior, and language declarations. For local SEO, reconcile genuine business identity, address or service area, phone, hours, location content, and profile links. Never create doorway location pages or fictional locations.

## Launch test set

- Direct navigation and refresh for every public route.
- 404/410 behavior and redirect correctness.
- HTTPS, preferred host, trailing-slash and case policy.
- Production robots and sitemap contents.
- Rendered title, description, canonical, social metadata, headings, links, and schema.
- No staging URLs, credentials, secrets, private user data, or debug payloads in output.
- Representative mobile, keyboard, zoom, slow-network, and reduced-motion checks.
