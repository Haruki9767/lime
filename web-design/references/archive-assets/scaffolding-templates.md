# Scaffolding Templates

Copy-paste starting points. Fill in the placeholders for the actual project.

## public/sitemap.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://YOUR-DOMAIN.com/</loc>
    <lastmod>YYYY-MM-DD</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://YOUR-DOMAIN.com/about</loc>
    <lastmod>YYYY-MM-DD</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <!-- Add one <url> block per real route. Do not include /404 or API routes. -->
</urlset>
```

For larger sites, prefer generating this dynamically via Next.js's `app/sitemap.ts`:

```ts
import type { MetadataRoute } from 'next'

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    { url: 'https://YOUR-DOMAIN.com/', lastModified: new Date(), changeFrequency: 'weekly', priority: 1 },
    { url: 'https://YOUR-DOMAIN.com/about', lastModified: new Date(), changeFrequency: 'monthly', priority: 0.7 },
  ]
}
```

## public/robots.txt

```
User-agent: *
Allow: /

Sitemap: https://YOUR-DOMAIN.com/sitemap.xml
```

If there are routes to keep out of search (e.g. `/admin`, `/api`), add explicit `Disallow` lines above the sitemap reference.

## public/llms.txt

Follows the emerging llms.txt convention: a short, plain-markdown briefing for LLM agents/crawlers about what the site is and where things live.

```markdown
# SITE NAME

> One-sentence description of what this site/product is and who it's for.

## Pages

- [Home](https://YOUR-DOMAIN.com/): what the homepage covers
- [About](https://YOUR-DOMAIN.com/about): what this page covers
- [Contact](https://YOUR-DOMAIN.com/contact): what this page covers

## Notes

Any other context an AI agent would need — key products/services, tone, or facts worth surfacing accurately (avoid marketing fluff here; be factual and concise).
```

Keep it factual and short — this file exists to help AI systems accurately represent the site, not to market to humans.

## app/not-found.tsx (Next.js App Router)

Must reuse the site's visual identity — same hero treatment, not a bare framework default. Example skeleton (adapt background image, copy, and colors to the project):

```tsx
import Link from 'next/link'
import Image from 'next/image'

export default function NotFound() {
  return (
    <main className="relative min-h-screen overflow-hidden rounded-3xl">
      <Image
        src="/images/hero-background.jpg" // reuse or pick a moodier still from the same shoot
        alt=""
        fill
        priority
        className="object-cover"
      />
      {/* Solid dark scrim — NOT a gradient */}
      <div className="absolute inset-0 bg-black/50" />

      <div className="relative z-10 flex min-h-screen flex-col justify-end p-10 md:p-16">
        <h1 className="text-6xl md:text-8xl font-extrabold tracking-tight text-white">
          404
        </h1>
        <p className="mt-2 text-lg text-white/80">
          This page wandered off the map.
        </p>
        <Link
          href="/"
          className="mt-8 inline-block w-fit rounded-md bg-white px-6 py-3 text-sm font-semibold text-black"
        >
          Back to home
        </Link>
      </div>
    </main>
  )
}
```
