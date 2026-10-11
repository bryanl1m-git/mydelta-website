# Asset export manifest - MyDelta website (Figma file Fb9MOeeXZ0RAoFoFYoz1XU)
Exported Mon 12 Oct 2026 (MYT) via Figma connector (download_assets for original image fills; read-only use_figma exportAsync SVG_STRING for vector icons). Figma was NOT modified. Frames: Home D 191:1364 / M 191:1459, About D 191:1798 / M 191:1955.

Counts: 3 testimonial avatars (same 3 images on desktop and mobile; x2 formats = 6 files), 2 quote-icon PNGs, 2 flourish PNGs (+2 upscaled @2x), 3 offer icons, 14 About value icons. Total 29 asset files + this MANIFEST.md (~210 KB).

## 1) Home - "What parents say" avatars (folder home-testimonials/)
Source = original image fill in Figma, **80x80 px only** (that is the highest resolution Figma stores; same image hash used by desktop and mobile; displayed 80px desktop, 48px mobile -> 80px source is 1.67x mobile, 1.0x desktop; NOT 2x on desktop - cannot be improved without new photos from the client).
**Circle crop IS baked into the Figma source PNG** (transparent corners, alpha circle). Figma also clips them with an ELLIPSE node. So: use the .png (transparent corners) as-is, no border-radius needed (adding `border-radius:50%` is harmless). The .jpg is the same image flattened on WHITE (JPEG has no alpha; corners are white, circle still baked) - only use it where the background is white (mobile card); on the desktop orange band use the .png.
| File | Person (card) | Figma node D | Figma node M | Display D / M | Notes |
|---|---|---|---|---|---|
| home-testimonial-avatar-1-emily-song.png / .jpg | Emily Song (white card 1) | I191:1430;12:55 (in 191:1430) | I191:1500;21:174 (in 191:1500) | 80x80 / 48x48 | image hash 048d89f1; woman portrait |
| home-testimonial-avatar-2-joelyn-chong.png / .jpg | Joelyn Chong (yellow #F7B815 card 2) | I191:1431;12:62 (in 191:1431) | I191:1501;21:181 (in 191:1501) | 80x80 / 48x48 | hash d80cf7d6; image is a Chinese lucky-bag/ornament graphic, not a person |
| home-testimonial-avatar-3-amanda-wyt.png / .jpg | Amanda Wyt (white card 3) | I191:1432;12:62 (in 191:1432) | I191:1502;21:174 (in 191:1502) | 80x80 / 48x48 | hash d803be6a; image is a sunset landscape, not a person |
Also exported (same section): home-testimonial-quote-icon-white-card.png (34x27, hash 121c4250; cards 1 & 3; desktop node I191:1430;12:52, mobile 30x24 display I191:1500;21:171) and home-testimonial-quote-icon-yellow-card.png (34x27, hash 41289bd8; card 2; I191:1431;12:59 / I191:1501;21:178). Raster, transparent, pale tint (rendered ~light grey/white-ish at low opacity in Figma) - not vector in Figma.

## 2) Home - testimonial flourish (orange brush / curved decoration)
It is NOT vector in Figma: it is two full-width RASTER wave images with white fill + dark brush-stroke flourishes, transparent so the band colour #F05D23 shows through. Native source 1440x134 (1x only - no higher-res exists). Desktop only (mobile 191:1494/1504 uses the plain 390x20 vector wave, no flourish; see svg/CLEAN-mobile-wave-1494 / 1504).
| File | Figma node | Display size | Notes |
|---|---|---|---|
| home-testimonial-flourish-wave-top-1440x134.png | 191:1424 "Wave (top)" (in Testimonials 191:1423, y=0) | 1440x134 | native source, RGBA; white mask w/ brush strokes; place at top of #F05D23 band |
| home-testimonial-flourish-wave-bottom-1440x134.png | 191:1425 "Wave (bottom)" (y=637) | 1440x134 | native source, RGBA; place at bottom of band |
| ...-top@2x-upscaled-2880x268.png, ...-bottom@2x-upscaled-2880x268.png | same | 1440x134 | LANCZOS upscale of the 1x source for retina convenience - NOT true 2x detail; fine for srcset, or ask designer for a vector |
Colours: mask white #FFFFFF, band behind #F05D23 (stroke marks are darker shades inside the PNG). Previously exported copies also exist in ../svg/desktop-wave-1424/1425 (byte-identical).
Note: a second raw image (505x47) is attached to each wave node in Figma's asset list; it is a low-res duplicate and was not used.

## 3) Home - offer-row icons (folder home-offer-icons/) = Home "Features" row (Primary Daycare / Public Speaking / ECA Programs)
RASTER in Figma (illustrated icon tiles with rounded background baked in, transparent corners), NOT vector, so PNG. Source is 99x99 px; displayed 88x88 desktop, 64x64 mobile (so ~1.1x desktop; no true 2x exists). Same image on desktop and mobile.
| File | Label | Figma node D (Features 191:1388) | Figma node M (Features 191:1463) | Display D / M | Colours / notes |
|---|---|---|---|---|---|
| home-offer-icon-primary-daycare.png | Primary Daycare | I191:1389;12:46 | I191:1464;21:165 | 88 / 64 | school-bus illustration on tan rounded tile; hash 7b66da05; rounded-tile shape baked |
| home-offer-icon-public-speaking.png | Public Speaking | I191:1390;12:46 | I191:1465;21:165 | 88 / 64 | child-at-desk illustration on cream/yellow rounded tile; hash 7f768532 |
| home-offer-icon-eca-programs.png | ECA Programs | I191:1391;12:46 | I191:1466;21:165 | 88 / 64 | badminton-player illustration on pink rounded tile; hash bf20229e |
Colours are illustration colours (multi-colour raster), no single hex. Tile radius is baked into the PNG.

## 4) About - 14 value-tile icons (folder about-values/), SVG, vector in Figma
Desktop tiles: Values Row 1/2 in 191:1861 (150x132 tile, white, 1px border #F0E6D2, icon circle 40px #FFDD98, icon 24x24, label Nunito Bold 12 #20409A). Mobile tiles: 191:2011.. (VR0-VR12, 163x82 tile, icon circle 28px #FFDD98, icon scaled to 16.8x16.8). The mobile icons are the SAME vectors scaled 0.7 - one SVG (viewBox 0 0 24 24) serves both; size via CSS (24px desktop, ~17px mobile).
Icon colour: #FA5C3B only (accent orange). The 24x24 icon frame has a hidden white fill (not exported); the yellow circle (#FFDD98, radius 20 / full circle) is a separate wrapper, NOT included in the SVGs - build in CSS. Strokes (2px, round caps) for stroke icons; fills for solid icons. Cleaned one export artefact: removed a zero-area `fill="black"` path from #07 (Critical Thinking).
No crop/radius baked (icons only).
| # | File | Tile label | Figma icon layer name | Tile node D | Tile node M | Icon node D | Icon node M | Colour |
|---|---|---|---|---|---|---|---|---|
| 01 | about-values/about-value-01-nurturing-joy.svg | Nurturing Joy | icon/heart | 191:1865 | 191:2012 | 191:1867 | 191:2014 | #FA5C3B |
| 02 | about-values/about-value-02-selflessness.svg | Selflessness | icon/hands | 191:1870 | 191:2017 | 191:1872 | 191:2019 | #FA5C3B |
| 03 | about-values/about-value-03-safety.svg | Safety | icon/shield | 191:1875 | 191:2023 | 191:1877 | 191:2025 | #FA5C3B |
| 04 | about-values/about-value-04-innovative.svg | Innovative | icon/bulb | 191:1880 | 191:2028 | 191:1882 | 191:2030 | #FA5C3B |
| 05 | about-values/about-value-05-compassion.svg | Compassion | icon/heart | 191:1885 | 191:2034 | 191:1887 | 191:2036 | #FA5C3B |
| 06 | about-values/about-value-06-respect.svg | Respect | icon/star | 191:1890 | 191:2039 | 191:1892 | 191:2041 | #FA5C3B |
| 07 | about-values/about-value-07-critical-thinking.svg | Critical Thinking | icon/brain | 191:1895 | 191:2045 | 191:1897 | 191:2047 | #FA5C3B |
| 08 | about-values/about-value-08-continuous-improvement.svg | Continuous Improvement | icon/trend | 191:1902 | 191:2051 | 191:1904 | 191:2053 | #FA5C3B |
| 09 | about-values/about-value-09-integrity.svg | Integrity | icon/check | 191:1908 | 191:2058 | 191:1910 | 191:2060 | #FA5C3B |
| 10 | about-values/about-value-10-teamwork.svg | Teamwork | icon/people | 191:1914 | 191:2064 | 191:1916 | 191:2066 | #FA5C3B |
| 11 | about-values/about-value-11-leadership.svg | Leadership | icon/flag | 191:1921 | 191:2072 | 191:1923 | 191:2074 | #FA5C3B |
| 12 | about-values/about-value-12-empathy.svg | Empathy | icon/heart | 191:1927 | 191:2078 | 191:1929 | 191:2080 | #FA5C3B |
| 13 | about-values/about-value-13-excellence.svg | Excellence | icon/star | 191:1932 | 191:2084 | 191:1934 | 191:2086 | #FA5C3B |
| 14 | about-values/about-value-14-student-centric.svg | Student-centric | icon/child | 191:1937 | 191:2089 | 191:1939 | 191:2091 | #FA5C3B |

Count confirmed: 14 tiles (7 + 7 desktop; 7 rows of 2 on mobile) = 14 icons. Ambiguities: icons are reused in Figma - heart (#01, #05, #12 identical), star (#06, #13 identical); layer "icon/brain" (#07 Critical Thinking) actually draws a circle with a plus (a placeholder-looking glyph), "icon/hands" (#02) etc. are simple line glyphs - exported exactly as designed. The developer can dedupe heart/star into one file each if desired.
