#!/usr/bin/env python3
"""Assemble the static pages from shared partials.

Edit files in src/, then run this script and commit site/*.html with the
sources. GitHub Pages publishes site/ as-is and does not run this script.

— Sage
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTIALS = ROOT / "src" / "partials"
PAGES = ROOT / "src" / "pages"
ICONS = ROOT / "src" / "icons"
OUT = ROOT / "site"

WHATSAPP = "https://wa.me/60126726140?text=Hi%20MyDelta%2C%20I%27d%20like%20to%20enquire"

SOCIAL = (
    ("Facebook", "https://facebook.com/profile.php?id=100091626355787", "facebook"),
    ("Instagram", "https://www.instagram.com/mydeltaedu", "instagram"),
    ("TikTok", "https://www.tiktok.com/@mydeltaedu", "tiktok"),
    ("Xiaohongshu", "https://www.xiaohongshu.com/explore", "xiaohongshu"),
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
        "Weekend public speaking for Year 1 to Year 6, in Bahasa Melayu and English.",
    ),
    (
        "hall-of-fame.html",
        "hof",
        "Hall of Fame",
        "Hall of Fame placeholders. No student names, photos, or results yet.",
    ),
    (
        "contact.html",
        "contact",
        "Contact",
        "WhatsApp, phone, email, and the address for MyDelta in Bandar Botanik, Klang.",
    ),
)


def icon_svg(name):
    raw = (ICONS / f"{name}.svg").read_text(encoding="utf-8")
    match = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S)
    if not match:
        sys.exit(f"Could not read icon {name}")
    inner = re.sub(r"<title>.*?</title>", "", match.group(1))
    return (
        '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
        + inner
        + "</svg>"
    )


def social_list(variant):
    items = []
    for label, url, name in SOCIAL:
        items.append(
            '<li><a class="social-link" href="{url}" data-placeholder="social-pending" '
            'target="_blank" rel="noopener noreferrer">'
            '<span class="visually-hidden">{label} (placeholder URL, pending confirmation)</span>'
            "{icon}</a></li>".format(url=url, label=label, icon=icon_svg(name))
        )
    return '<ul class="social-list social-list--{variant}">{items}</ul>'.format(
        variant=variant, items="".join(items)
    )


def fill(text, tokens):
    for key, value in tokens.items():
        text = text.replace(key, value)
    return text


def main():
    head = (PARTIALS / "head.html").read_text(encoding="utf-8")
    header = (PARTIALS / "header.html").read_text(encoding="utf-8")
    footer = (PARTIALS / "footer.html").read_text(encoding="utf-8")
    cta = (PARTIALS / "cta.html").read_text(encoding="utf-8")
    shared = {
        "{{WHATSAPP}}": WHATSAPP,
        "{{ICON:whatsapp}}": icon_svg("whatsapp"),
        "{{SOCIAL_INLINE}}": social_list("inline"),
        "{{SOCIAL_CIRCLES}}": social_list("circles"),
    }
    banner = (
        "<!-- Assembled from src/ by scripts/assemble_pages.py. "
        "Edit the sources, then re-run the script. — Sage -->\n"
    )

    for filename, nav, title, description in PAGES_META:
        body = (PAGES / filename).read_text(encoding="utf-8")
        body = body.replace("{{CTA}}", cta)
        tokens = dict(shared)
        tokens["{{TITLE}}"] = title
        tokens["{{DESCRIPTION}}"] = description
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
            "<body>\n"
            + header
            + '<main id="main">\n'
            + body
            + "</main>\n"
            + footer
            + '<script src="js/site.js"></script>\n'
            "</body>\n"
            "</html>\n"
        )
        document = banner + fill(document, tokens)
        if "{{" in document:
            sys.exit(f"Unreplaced token left in {filename}")
        (OUT / filename).write_text(document, encoding="utf-8")
        print(f"wrote site/{filename}")


if __name__ == "__main__":
    main()
