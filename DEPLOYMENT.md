# Deployment guide

This repository now contains a Nuxt 4 public site for `https://lime.isroot.in`.

## Recommended platform: Cloudflare Pages

**Cloudflare Pages** is the best fit for this site because it supports Nuxt’s static output, global edge delivery, preview deployments from GitHub, custom domains, and HTTPS without adding a server or database. The site is frontend-only and can be deployed as static files.

### Project configuration

Create a Pages project connected to `Haruki9767/skills` with:

| Setting | Value |
|---|---|
| Framework preset | Nuxt.js (or None if the preset is unavailable) |
| Production branch | `main` |
| Build command | `pnpm generate` |
| Build output directory | `.output/public` |
| Node.js version | `22` |
| Package manager | `pnpm` |
| Install command | `pnpm install --frozen-lockfile` |

Commit the generated `pnpm-lock.yaml` and keep it as the only lockfile authority.

## Environment variables

This static site currently requires **no environment variables**. Do not add an `.env` file or configure placeholder secrets in the hosting dashboard.

If a future feature adds server functionality, document each variable here with its purpose, whether it is public (`NUXT_PUBLIC_*`) or private, and the environments where it must exist. Never commit secret values.

## Domain and DNS

1. Add `lime.isroot.in` as a custom domain in Cloudflare Pages.
2. If DNS is managed by Cloudflare, accept the suggested CNAME record. Otherwise create the provider’s requested CNAME record at your DNS host.
3. Set `https://lime.isroot.in` as the canonical production URL.
4. Confirm that `https://lime.isroot.in/robots.txt` references `https://lime.isroot.in/sitemap.xml`.

## Preview and production

- Pull requests should deploy to a preview URL and must not be added to the canonical sitemap.
- Only `main` is production and should use the `lime.isroot.in` custom domain.
- The site has no private routes, API routes, cookies, analytics, or user-submitted data at this time.

## Post-deploy verification

```bash
curl -I https://lime.isroot.in/
curl -I https://lime.isroot.in/robots.txt
curl -I https://lime.isroot.in/sitemap.xml
curl -I https://lime.isroot.in/not-a-real-route
```

Expected results: `200` for the home page, `robots.txt`, and `sitemap.xml`; a true `404` for the unknown route. Then inspect the page source for the canonical URL, title, description, and Open Graph tags.

## Alternatives

- **Vercel:** use `pnpm generate` with output directory `.output/public`, or use Nuxt’s Vercel preset if server rendering is introduced later.
- **Netlify:** use `pnpm generate` with publish directory `.output/public`.

For the current static site, do not add an adapter or server preset solely for deployment.
