# Deployment guide

This repository now contains a Nuxt 4 public site in the `lime/` directory for `https://lime.isroot.in`.

## Recommended platform: Cloudflare Pages

**Cloudflare Pages** is the best fit for this site because it supports Nuxt’s static output, global edge delivery, preview deployments from GitHub, custom domains, and HTTPS without adding a server or database. The site is frontend-only and can be deployed as static files.

### Project configuration

Create a Pages project connected to `Haruki9767/skills` with:

| Setting | Value |
|---|---|
| Framework preset | Nuxt.js (or None if the preset is unavailable) |
| Production branch | `main` |
| Root / working directory | `lime` |
| Build command | `pnpm generate` |
| Build output directory | `.output/public` |
| Node.js version | `22` |
| Package manager | `pnpm` |
| Install command | `pnpm install --frozen-lockfile` |

The web project’s package manifest and lockfile are `lime/package.json` and `lime/pnpm-lock.yaml`. Keep that lockfile as the only lockfile authority for the web project.

## GitHub Pages

GitHub Pages deployment is automated by [`.github/workflows/lime-pages.yml`](./.github/workflows/lime-pages.yml). It runs when files in `lime/` change on `main`, installs dependencies from the `lime/` working directory, typechecks, generates `.output/public`, uploads the Pages artifact, and deploys it.

In the repository’s **Settings → Pages → Build and deployment**, select **GitHub Actions** as the source. The workflow uses the `github-pages` environment and requires the standard Pages write and OIDC permissions already declared in the workflow.

GitHub Pages is a suitable static host for this site. Cloudflare Pages remains the primary recommendation for custom-domain edge delivery and preview deployments; use one production host at a time to avoid conflicting DNS and canonical URL behavior.

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

For the current static site, do not add an adapter or server preset solely for deployment. If the GitHub Pages project uses a repository subpath instead of the custom domain, add a Nuxt `app.baseURL` configuration for that path before deploying; `lime.isroot.in` uses the root path and does not need one.
