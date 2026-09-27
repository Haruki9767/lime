# Lime Skills Deployment

## Recommended platform

**GitHub Pages via the repository’s GitHub Actions workflow** is the recommended production target. The repository already uses the Pages artifact/deploy actions and identifies the custom domain `lime.isroot.in`. The Nuxt project generates a static site, so no long-running Node server or application secrets are required.

## Runtime and build

- Node.js: 22
- pnpm: 11 (the workflow installs pnpm 11)
- Install: `pnpm install --frozen-lockfile`
- Local development: `pnpm dev --host 0.0.0.0`
- Static production build: `pnpm generate`
- Artifact directory: `lime/.output/public` in CI; `.output/public` from this project directory locally
- No environment variables are required. The canonical site URL is public configuration in `nuxt.config.mjs` (`https://lime.isroot.in`). Do not put credentials there.

`pnpm generate` runs Nuxt prerendering and then `scripts/finalize-static.mjs`. The finalizer uses prerendered Vue `/404` markup to create a script-free root `404.html` and removes Nuxt’s unused `200.html` shell. Keep the root `404.html` in the Pages artifact.

## GitHub Actions behavior

`.github/workflows/lime-pages.yml`:

- Pull requests targeting `main` that touch `lime/**` or the workflow install the frozen lockfile, generate the static site, and upload a build artifact; the deploy job is skipped for pull requests.
- A push to `main` or a manual workflow dispatch builds and deploys through the `github-pages` environment.
- The build job has `contents: read`; only the deploy job receives `pages: write` and `id-token: write`.

In repository **Settings → Pages → Build and deployment**, choose **GitHub Actions**. Configure the custom domain as `lime.isroot.in` if it is not already set.

## Domain and DNS

The site source declares `lime.isroot.in` in `public/CNAME`. For this subdomain, configure a DNS `CNAME` record with host/name `lime` pointing to `Haruki9767.github.io` (not to a repository path). Set the same custom domain in repository Pages settings. Do not use wildcard DNS. Enable **Enforce HTTPS** after GitHub reports that it is available and confirm the certificate is issued.

GitHub notes that custom-workflow publishing does not require a `CNAME` file; the Pages repository setting is authoritative for the custom domain. The project keeps its existing public CNAME asset as source documentation.

## Preview and production differences

A pull-request artifact is a local build validation, not a production deployment. For local static preview after `pnpm generate`, run:

```sh
python3 -m http.server 4176 --bind 127.0.0.1 --directory .output/public
```

This simple server does not reproduce GitHub Pages’ custom 404 behavior; inspect the built `404.html` separately. Production uses the `github-pages` environment, the configured domain, and GitHub-managed HTTPS. `pnpm preview` is Nuxt’s build-server preview and is not the static-artifact preview command.

## Post-deploy verification

After the Pages workflow succeeds, run:

```sh
curl -fsSI https://lime.isroot.in/
curl -fsSI https://lime.isroot.in/guidance/
curl -fsS https://lime.isroot.in/seo-production-audit/ | grep -E 'canonical|og:url|<title>'
curl -sS -o /tmp/lime-404.html -w '%{http_code}\n' https://lime.isroot.in/route-that-does-not-exist
 grep -q 'That page went' /tmp/lime-404.html
```

The unknown route should return HTTP `404` and the custom error text. Also verify the HTTPS lock/certificate, the public sitemap at `https://lime.isroot.in/sitemap.xml`, and `robots.txt`.

## Rollback

If a deployment regresses, revert the release commit on `main` and let the same workflow redeploy the prior static source. There is no database or backend state to restore. For domain/certificate failures, correct the Pages custom-domain setting or DNS CNAME and re-check DNS propagation; do not change the app’s canonical URL unless the production domain actually changes.

## Sources

- [GitHub Pages custom workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [GitHub Pages custom 404](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-custom-404-page-for-your-github-pages-site)
- [GitHub Pages custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
