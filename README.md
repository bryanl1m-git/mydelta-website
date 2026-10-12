# MyDelta website

Static marketing site for MyDelta Academy in Bandar Botanik, Klang. Six pages, plain HTML, CSS, and JS. GitHub Pages deploys from Actions when `main` changes. This repo does not set a custom domain.

## Pages

Clean URLs: each page is written as `<path>/index.html`, and links are root-absolute (`/about`, not `about.html`).

- `site/index.html` — Home, `/` (manual 3-slide hero, no autoplay)
- `site/about/index.html` — About Us, `/about`
- `site/primary-daycare/index.html` — Primary Daycare, `/primary-daycare`
- `site/public-speaking/index.html` — Public Speaking, `/public-speaking`
- `site/hall-of-fame/index.html` — Hall of Fame placeholders, `/hall-of-fame`
- `site/contact/index.html` — Contact, WhatsApp / email fallback, `/contact`
- `site/404.html`, `site/sitemap.xml`, `site/robots.txt` — generated too

## Build options

`scripts/assemble_pages.py` takes:

- `--base-path` (or `BASE_PATH`), default `/`. The Pages workflow builds with `/mydelta-website/` so the project-URL preview keeps working.
- `--site-url` (or `SITE_URL`), default `https://mydeltaedu.my`, used for canonical, og:url and the sitemap.
- `--noindex` (or `NOINDEX=1`) for staging and previews: adds `<meta name="robots" content="noindex, nofollow">` and a `Disallow: /` robots.txt.

Commit `site/` built with the defaults (production, base `/`). The PR check fails otherwise.

## Preview

From the repo root, after assembling:

```bash
python3 scripts/assemble_pages.py
python3 -m http.server 8765 --directory site
```

Then open `http://127.0.0.1:8765/`. `python3 -m http.server` serves `/about/` but not `/about` without the slash; that is a preview-server limit, Firebase and GitHub Pages handle both.

Shared header and footer live in `src/partials/`. Page sections live in `src/pages/`. Edit those, run the script, and commit both the sources and `site/*.html`. The Pages workflow uploads `site/` and does not run the script. Pull requests run the script and fail if the committed HTML does not match.

## Session 1

Done: tokens, shared chrome, page skeletons, contact fallback, Pages workflow.

## Session 2

Done: manual hero slider (previous, next, dots, keyboard, swipe, no autoplay), mobile menu focus trap and animation, and a tablet layout. The menu button stays through 999px, including the 768–900px band, because the six links do not fit beside the logo there. Horizontal nav starts at 1000px.

Still open, in the CSS header:

- Per-section wave heights
- Column alignment and equal photo heights

Placeholder photos, reviews, Hall of Fame cards, and social URLs are listed in `docs/placeholders.md`. The session log is `docs/session-log.md`.

## Deploy

`.github/workflows/pages.yml` checks out the repo, uploads `site/` with `actions/upload-pages-artifact`, and deploys with `actions/deploy-pages`. It runs on a push to `main`, or by hand. There is no `CNAME` file. `.github/workflows/pr-check.yml` runs on pull requests: it assembles the pages and checks that `site/*.html` matches the sources.

## Sign-off

Commit author is the person and team, for example `Sage (Second)`. Commit messages start with the name, for example `[Sage] add the page skeletons`. Branches are named after the person. Log entries end with the author's name.
