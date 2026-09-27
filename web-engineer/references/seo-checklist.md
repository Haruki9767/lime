# SEO and accessibility checklist

Use this reference after discovery. Mark each item pass, fail, not applicable, or not tested, with file/URL evidence.

## Metadata

- Unique title per indexable page; visible heading and title agree.
- Human-written description matches visible content; no keyword stuffing.
- HTTPS canonical uses the preferred origin and normalized trailing-slash policy.
- `og:title`, `og:description`, `og:type`, `og:url`, and a public `og:image` are accurate.
- Twitter/X card metadata is present and accurate.
- Structured data describes only visible, verifiable facts.
- Private, account, admin, API, search, duplicate, and unknown routes are not indexable.

## Crawl and routing

- Sitemap contains only canonical public URLs, no duplicates or staging domains.
- Robots file names the exact sitemap and does not act as access control.
- Direct navigation and refresh work for every public route.
- Unknown paths produce a real 404 where the host supports it; otherwise record soft-404 behavior.
- HTTP redirects converge on HTTPS and the preferred host.
- No stale asset, test URL, or local development origin remains in production output.

## Content and accessibility signals

- One meaningful `h1` per public page with logical heading hierarchy.
- Meaningful images have concise alt text; decorative images use empty alt text.
- Images reserve dimensions or aspect ratio to reduce layout shift.
- Form controls have visible labels, correct types, autocomplete where useful, and associated errors.
- Native links/buttons are used for interactions; custom controls have keyboard and screen-reader semantics.
- Focus is visible, tab order is logical, dialogs have names and Escape behavior, and status/error messages are announced.
- Contrast, zoom, mobile layout, reduced motion, and touch targets are tested separately and never claimed without evidence.
