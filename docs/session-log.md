# Session log

## 10 Oct 2026 — Session 1 foundation

Static HTML, CSS, and JS for the six pages, shared header and footer, design tokens, and a GitHub Actions workflow that deploys `site/` with `actions/upload-pages-artifact` and `actions/deploy-pages`. No custom domain and no CNAME. Slider behaviour, mobile-menu polish, and the full responsive pass are left as TODOs in `site/css/site.css` and `site/js/site.js`.

Agreed defaults used here: a 3-slide hero with no autoplay (markup only), the live-site DELTA logo, contact via WhatsApp with a mailto fallback, and Hall of Fame cards with no student names or photos.

Notes for Cody:

- Slide 2 and slide 3 sublines are draft copy so the skeleton has text. Confirm them against the Figma master slides.
- The live daycare timetable writes "11.45pm" in the morning session. This site uses 11.45 am, because that block sits before 12:00 pm.
- Centre hours on every page are Mon–Fri 8:00 am – 6:00 pm, as in the design. The daycare timetable still runs 7:00 am – 7:00 pm, as on the current site. Both are shown, with one sentence on the daycare page.
- Vision text keeps "pursuit forwards". Flagged, not changed.
- "35 years" and "since 1988" both remain, as on the current site.
- Public speaking has no trainer section, no Mandarin, and no "Coming Soon". The fifth live-site FAQ (parent progress updates) is not on the page; the design uses four FAQ cards. The six "what students gain" cards are shortened from the current site. "Networking" is written as "A wider circle" so the page does not describe primary pupils as building a professional network.
- Nav stacks below 1100px. The spec's 768–900px tablet switch does not fit this logo beside six links, so that breakpoint is part of the later responsive pass.
- Social URLs are the ones in the design notes and are marked pending. TikTok and Xiaohongshu are filler addresses.

— Sage
