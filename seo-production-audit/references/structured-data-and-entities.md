# Structured Data and Entity Reference

Use this reference when selecting schema, modeling entities, or auditing consistency across pages.

## Entity model

Document stable canonical identities for the organization, people, products, services, locations, publishers, authors, and content. Record preferred names, aliases, relationships, canonical URLs, genuine profile links, and source evidence. Resolve ambiguous names instead of relying on keyword repetition.

## Schema workflow

1. Identify visible facts and the page’s primary purpose.
2. Select the narrowest appropriate type supported by the project and the search feature being targeted.
3. Add only properties supported by visible content or authoritative project data.
4. Keep URLs, names, dates, authors, publishers, prices, availability, ratings, and images consistent with the page.
5. Validate JSON-LD syntax, nesting, required properties, URL reachability, and representative rendered output.
6. Recheck after template, CMS, locale, or product-feed changes.

Common legitimate types include `Organization`, `Person`, `WebSite`, `WebPage`, `Article`, `Product`, `SoftwareApplication`, `LocalBusiness`, and `BreadcrumbList`. Use `FAQPage`, reviews, ratings, offers, and other specialized types only when the content genuinely meets the applicable requirements and is visible.

## Failure modes

- Marking up hidden, contradictory, or fictional content.
- Copying homepage schema onto every route.
- Publishing fake ratings, reviews, authors, prices, availability, or dates.
- Using schema as a ranking promise.
- Treating `sameAs` as a place to list unrelated or unverified profiles.
- Emitting duplicate or conflicting JSON-LD from multiple components.
