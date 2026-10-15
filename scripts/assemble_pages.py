#!/usr/bin/env python3
"""Assemble the static pages from shared partials.

Edit files in src/, then run this script and commit site/*.html with the
sources. GitHub Pages publishes site/ as-is and does not run this script.

— Sage
"""

import argparse
import os
import hashlib
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTIALS = ROOT / "src" / "partials"
PAGES = ROOT / "src" / "pages"
ICONS = ROOT / "src" / "icons"
OUT = ROOT / "site"

WHATSAPP = "https://wa.me/60126726140?text=Hi%20MyDelta%2C%20I%27d%20like%20to%20enquire"

SOCIAL = (
    ("Facebook", "https://facebook.com/profile.php?id=100091626355787", "facebook", True),
    ("Instagram", "https://www.instagram.com/mydeltaedu", "instagram", True),
    ("Xiaohongshu", "https://xhslink.cn/m/9gdk3OmwT5C", "xiaohongshu", False),
)

NAV_KEYS = ("home", "about", "daycare", "speaking", "hof", "contact")

PAGES_META = (
    (
        "index.html",
        "home",
        "Primary Daycare & Tuition in Klang",
        "MyDelta in Bandar Botanik, Klang: primary daycare, tuition, and public speaking.",
    ),
    (
        "about.html",
        "about",
        "About Us",
        "Our story, history, mission, vision, and values at MyDelta in Klang.",
    ),
    (
        "primary-daycare.html",
        "daycare",
        "Primary Daycare",
        "Primary daycare and tuition in Bandar Botanik for Year 1 to Year 6.",
    ),
    (
        "public-speaking.html",
        "speaking",
        "Public Speaking",
        "Saturday public speaking for Year 1 to Year 6.",
    ),
    (
        "hall-of-fame.html",
        "hof",
        "Hall of Fame",
        "The Hall of Fame for students from MyDelta in Bandar Botanik, Klang.",
    ),
    (
        "contact.html",
        "contact",
        "Contact",
        "WhatsApp, phone, email, and the address for MyDelta in Bandar Botanik, Klang.",
    ),
)

# Source page -> clean URL path (relative to the base path). Pages are written
# as <path>/index.html so /about works on any static host.
PAGE_PATHS = {
    "index.html": "",
    "about.html": "about",
    "primary-daycare.html": "primary-daycare",
    "public-speaking.html": "public-speaking",
    "hall-of-fame.html": "hall-of-fame",
    "contact.html": "contact",
}

NOT_FOUND = (
    "404.html",
    "",
    "Page not found",
    "The page you were looking for is not on the MyDelta website.",
)

DEFAULT_SITE_URL = "https://mydeltaedu.my"


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base-path",
        default=os.environ.get("BASE_PATH", "/"),
        help="URL path the site is served from, e.g. / or /mydelta-website/",
    )
    parser.add_argument(
        "--site-url",
        default=os.environ.get("SITE_URL", DEFAULT_SITE_URL),
        help="Origin used for canonical URLs and the sitemap",
    )
    parser.add_argument(
        "--noindex",
        action="store_true",
        default=os.environ.get("NOINDEX", "") not in ("", "0", "false"),
        help="Staging/preview build: robots noindex and Disallow all",
    )
    args = parser.parse_args()
    base = "/" + args.base_path.strip("/")
    args.base_path = base if base == "/" else base + "/"
    args.site_url = args.site_url.rstrip("/")
    return args


def page_url(base, path):
    return base + path if path else base


def rewrite_links(document, base):
    """Make page links clean and asset paths root-absolute under base."""

    def page_link(match):
        name, frag = match.group(1) + ".html", match.group(2) or ""
        if name not in PAGE_PATHS:
            sys.exit(f"Link to unknown page {name}")
        return 'href="' + page_url(base, PAGE_PATHS[name]) + frag + '"'

    document = re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', page_link, document)
    document = re.sub(r'(=")(assets|css|js)/', lambda m: m.group(1) + base + m.group(2) + "/", document)
    document = re.sub(r'(,\s*)(assets)/', lambda m: m.group(1) + base + m.group(2) + "/", document)
    return document


ICON_SIZES = {
    "facebook": (18, 18),
    "instagram": (18, 18),
    "xiaohongshu": (26, 9.289),  # 24:8.574 viewBox ratio
    "whatsapp": (22, 22),
}


def icon_svg(name):
    raw = (ICONS / f"{name}.svg").read_text(encoding="utf-8")
    match = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S)
    if not match:
        sys.exit(f"Could not read icon {name}")
    inner = re.sub(r"<title>.*?</title>", "", match.group(1))
    # Xiaohongshu's official mark is a wide wordmark. A square viewBox
    # letterboxes it, so use the tight bounds of that path.
    view_box = "0 7.714 24 8.574" if name == "xiaohongshu" else "0 0 24 24"
    # Fallback size so the icon stays small if the stylesheet fails or is stale.
    w, h = ICON_SIZES.get(name, (20, 20))
    return (
        f'<svg class="icon icon--{name}" width="{w}" height="{h}" viewBox="{view_box}" aria-hidden="true" focusable="false">'
        + inner
        + "</svg>"
    )


def social_list(variant):
    items = []
    for label, url, name, pending in SOCIAL:
        placeholder = ' data-placeholder="social-pending"' if pending else ""
        extra = " social-link--xiaohongshu" if name == "xiaohongshu" else ""
        items.append(
            '<li><a class="social-link{extra}" href="{url}"{placeholder} '
            'target="_blank" rel="noopener noreferrer">'
            '<span class="visually-hidden">{label}</span>'
            "{icon}</a></li>".format(
                url=url,
                extra=extra,
                placeholder=placeholder,
                label=label,
                icon=icon_svg(name),
            )
        )
    return '<ul class="social-list social-list--{variant}" style="list-style: none; padding-left: 0;">{items}</ul>'.format(
        variant=variant, items="".join(items)
    )


def fill(text, tokens):
    for key, value in tokens.items():
        text = text.replace(key, value)
    return text


HASHED_ASSETS = ("css/tokens.css", "css/site.css", "js/site.js")


def write_hashed_assets():
    """Copy each css/js file to name.<hash>.ext and return {plain: hashed}."""
    mapping = {}
    for rel in HASHED_ASSETS:
        src = OUT / rel
        stem, ext = src.stem, src.suffix
        for old in src.parent.glob(f"{stem}.*{ext}"):
            if re.fullmatch(rf"{re.escape(stem)}\.[0-9a-f]{{10}}{re.escape(ext)}", old.name):
                old.unlink()
        digest = hashlib.sha256(src.read_bytes()).hexdigest()[:10]
        hashed = src.with_name(f"{stem}.{digest}{ext}")
        shutil.copyfile(src, hashed)
        mapping[rel] = str(hashed.relative_to(OUT))
    return mapping


def bust_assets(document, mapping):
    """Point every css/js reference at its hashed filename."""
    for plain, hashed in mapping.items():
        document = re.sub(r'((?:href|src)="[^"]*?)' + re.escape(plain) + '"', lambda m: m.group(1) + hashed + '"', document)
    return document


def check_svgs(document, name):
    """Every inline SVG needs width/height so it cannot blow up without CSS."""
    for tag in re.findall(r"<svg\b[^>]*>", document):
        if not (re.search(r'\swidth="', tag) and re.search(r'\sheight="', tag)):
            sys.exit(f"Inline SVG without width/height in {name}: {tag[:80]}")


def main():
    args = parse_args()
    hashed_assets = write_hashed_assets()
    base = args.base_path
    head = (PARTIALS / "head.html").read_text(encoding="utf-8")
    header = (PARTIALS / "header.html").read_text(encoding="utf-8")
    footer = (PARTIALS / "footer.html").read_text(encoding="utf-8")
    cta = (PARTIALS / "cta.html").read_text(encoding="utf-8")
    shared = {
        "{{WHATSAPP}}": WHATSAPP,
        "{{ICON:whatsapp}}": icon_svg("whatsapp"),
        "{{SOCIAL_INLINE}}": social_list("inline"),
        "{{SOCIAL_CIRCLES}}": social_list("circles"),
        "{{ROBOTS}}": (
            '<meta name="robots" content="noindex, nofollow">\n' if args.noindex else ""
        ),
    }
    banner = (
        "<!-- Assembled from src/ by scripts/assemble_pages.py. "
        "Edit the sources, then re-run the script. — Sage -->\n"
    )

    # Remove pages from earlier runs (flat *.html and page folders).
    for old in OUT.glob("*.html"):
        old.unlink()
    for path in PAGE_PATHS.values():
        if path and (OUT / path).is_dir():
            shutil.rmtree(OUT / path)

    for filename, nav, title, description in PAGES_META + (NOT_FOUND,):
        body = (PAGES / filename).read_text(encoding="utf-8")
        body = body.replace("{{CTA}}", cta)
        tokens = dict(shared)
        tokens["{{TITLE}}"] = title
        tokens["{{DESCRIPTION}}"] = description
        if filename == NOT_FOUND[0]:
            tokens["{{CANONICAL}}"] = ""
            if not args.noindex:
                tokens["{{ROBOTS}}"] = '<meta name="robots" content="noindex">\n'
        else:
            url = args.site_url + page_url("/", PAGE_PATHS[filename])
            tokens["{{CANONICAL}}"] = (
                '<link rel="canonical" href="' + url + '">\n'
                '<meta property="og:url" content="' + url + '">\n'
                '<meta property="og:title" content="' + title + ' · MyDelta">\n'
                '<meta property="og:description" content="' + description + '">\n'
                '<meta property="og:type" content="website">\n'
            )
        for key in NAV_KEYS:
            current = key == nav
            tokens["{{CLASS:" + key + "}}"] = " is-current" if current else ""
            tokens["{{CURRENT:" + key + "}}"] = ' aria-current="page"' if current else ""
        document = (
            "<!DOCTYPE html>\n"
            '<html lang="en">\n'
            "<head>\n"
            + head
            + "</head>\n"
            '<body class="page-' + (nav or "404") + '">\n'
            + header
            + '<main id="main">\n'
            + body
            + "</main>\n"
            + footer
            + '<script src="js/site.js"></script>\n'
            "</body>\n"
            "</html>\n"
        )
        document = banner + bust_assets(rewrite_links(fill(document, tokens), base), hashed_assets)
        check_svgs(document, filename)
        if "{{" in document:
            sys.exit(f"Unreplaced token left in {filename}")
        if filename == NOT_FOUND[0]:
            target = OUT / "404.html"
        else:
            folder = OUT / PAGE_PATHS[filename]
            folder.mkdir(parents=True, exist_ok=True)
            target = folder / "index.html"
        target.write_text(document, encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")

    urls = "".join(
        "  <url><loc>" + args.site_url + page_url("/", PAGE_PATHS[f]) + "</loc></url>\n"
        for f, *_ in PAGES_META
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + urls
        + "</urlset>\n",
        encoding="utf-8",
    )
    if args.noindex:
        robots = "User-agent: *\nDisallow: /\n"
    else:
        robots = "User-agent: *\nAllow: /\n\nSitemap: " + args.site_url + "/sitemap.xml\n"
    (OUT / "robots.txt").write_text(robots, encoding="utf-8")
    print("wrote site/sitemap.xml and site/robots.txt")


if __name__ == "__main__":
    main()
