# Session log

## 10 Oct 2026 — Session 1 foundation

Static HTML, CSS, and JS for the six pages, shared header and footer, design tokens, and a GitHub Actions workflow that deploys `site/` with `actions/upload-pages-artifact` and `actions/deploy-pages`. No custom domain and no CNAME. Slider behaviour, mobile-menu polish, and the full responsive pass are left as TODOs in `site/css/site.css` and `site/js/site.js`.

Agreed defaults used here: a 3-slide hero with no autoplay (markup only), the live-site DELTA logo, contact via WhatsApp with a mailto fallback, and Hall of Fame cards with no student names or photos.

Notes for Cody:

- Slide 2 and slide 3 sublines carry a visible DRAFT marker. The copy stays until it is checked against the Figma master slides.
- The live daycare timetable writes "11.45pm" in the morning session. This site uses 11.45 am, because that block sits before 12:00 pm.
- Centre hours on every page are Mon–Fri 8:00 am – 6:00 pm, as in the design. The daycare timetable still runs 7:00 am – 7:00 pm, as on the current site. Both are shown, with one sentence on the daycare page.
- Vision text keeps "pursuit forwards". Flagged, not changed.
- "35 years" and "since 1988" both remain, as on the current site.
- Public speaking has no trainer section, no Mandarin, and no "Coming Soon". The fifth live-site FAQ (parent progress updates) is not on the page; the design uses four FAQ cards. The six "what students gain" cards are shortened from the current site. "Networking" is written as "A wider circle" so the page does not describe primary pupils as building a professional network.
- Nav stacks below 1100px. The spec's 768–900px tablet switch does not fit this logo beside six links, so that breakpoint is part of the later responsive pass.
- Social URLs are the ones in the design notes and are marked pending. TikTok and Xiaohongshu are filler addresses.

— Sage

## 10 Oct 2026 — Session 2 interactions

Home hero cycles three existing slides by hand: previous, next, and dots, plus Left and Right keys. Nothing autoplays. The change takes 450ms, and it is instant when `prefers-reduced-motion` is set. Below 1100px the arrows are hidden, a swipe of about 40px changes the slide without taking over vertical scroll, dots sit under the photo, and a chip reads N / 3.

The mobile menu traps Tab, marks the header, main, and footer inert, closes on Escape, and puts focus back on the menu button. Opening and closing fade. Scroll position is restored when the menu closes.

Tablet widths from 768px use two-column splits, schedules, and contact cards, and a roomier type scale. Six links do not fit beside this logo in the 768–900px band, so the menu button stays until 1000px. Horizontal nav starts there, before the rest of the desktop layout at 1100px.

Placeholders are unchanged. No custom domain.

— Sage

## 11 Oct 2026 — Timetable amendments

Primary Daycare now publishes the morning session as 7.30am – 11.15am for Year 1–3 and the afternoon session as 2.00pm – 3.45pm for Year 4–6. Who & when reads Monday – Friday. The overview line is “Daycare, homework guidance, tuition and ECA programme.” Art & craft, meals, and transport wording are gone from that page, including the Transportation and Wholesome food cards. The four remaining feature cards sit two by two on desktop and mobile.

Public Speaking is Saturday only. The Sunday schedule card is removed.

Header bar hours are unchanged. The desktop timetable stays side by side; stacking Morning and Afternoon full width with a 24px gap is on hold pending Bryan.

— Sage (Second)

## 11 Oct 2026 — Desktop timetable released

The hold is released. On desktop the Primary Daycare timetable row is 1120px wide with a 24px gap: Morning is 784×123 and Afternoon is 312×123. Each period is a chip with the time in red above the activity, sized to the text and spaced across the card. The programme band is 550px tall. Below 1100px the two cards stack so the chips stay on one line. The 390px frame still uses the tables.

— Sage (Second)

## 11 Oct 2026 — Sections removed

Primary Tuition, the Public Speaking FAQ, Explore more, and the contact registration form are gone. The daycare timetable still mentions tuition as part of the day. The gallery before the public-speaking call to action keeps the orange wave class that sat on Explore more. WhatsApp, phone, and email stay on Contact. No nav item pointed at the removed sections.

— Sage (Second)

## 11 Oct 2026 — Wavy dividers

Band colours use background-color, so the wave image stays. Desktop bands use the traced 58px divider and mobile uses the 20px vector. Page heroes use the same pair. Nunito 600 is on the Google Fonts link.

— Sage (Second)

## 11 Oct 2026 — Hall of Fame mobile

The all-stars grid no longer forces two 204px cards onto a 390px screen. Cards can shrink, and the mobile gap is 12px so two columns fit inside the 342px content width.

— Sage (Second)

## 11 Oct 2026 — Subpage value tiles

About Us values are white tiles: 2px #FFDD98 border, 12px radius, Nunito 600. Mobile is 15px type in a 165×82 two-column grid. Desktop is 18px type, seven across, 150×132.

The same tile treatment now covers Primary Daycare “What sets us apart” (2px border, 20px padding, two columns) and Public Speaking “What students gain” (1.5px border, 22px padding, two columns below 1100px and three on desktop). Titles are Nunito 700 at 18px and the body is 15px #595966.

— Sage (Second)

## 11 Oct 2026 — Figma photos

Programme photos replace the dashed placeholders: hero crops, Our Story, the What We Do collage, the home gallery, the lounge on Home, About, daycare, public speaking, and the Hall of Fame cohort. The collage and lounge keep the rounded frame that is already in the PNG. Hero slides stay at the native crop size. The contact map is still a placeholder, and Primary Tuition, FAQ, Explore more, and the contact form have no photos.

— Sage (Second)

## 11 Oct 2026 — Subpage hero type

Subpage heroes use the Figma type: on a 390px screen the eyebrow is 12px, the heading is 36px (40px on Contact), and the line under it is 15px regular. At 1440 the eyebrow is 14px, the heading is 56px, and the line is 18px regular. The Hall of Fame description no longer says the page is still a placeholder. Each portrait alt is “Portrait of” plus the name already printed on that card.

— Sage (Second)

## 11 Oct 2026 — Home testimonials

The Home parent band is orange, with three cards and a highlighted middle card. The quotes and names are the Figma copy: Emily Song, Joelyn Chong, and Amanda Wyt. The circles use the exported avatars, at 80px on a wide screen and 48px on a phone. The 1440×134 flourish sits on the top and bottom of that band on a wide screen. A phone keeps the plain 20px wave.

— Sage (Second)

## 11 Oct 2026 — CTA and footer

Subpage pages end on a yellow visit band. Enquire stays accent, and WhatsApp Us is navy. Home ends on the yellow Join Us band, with the lounge photo, and has no visit band. The footer bar is #384C86 on Home and #20409A on the other pages. On a 390px Home screen the footer also shows hours, the WhatsApp number, and the social circles.

— Sage (Second)

## 11 Oct 2026 — Home hero

The Home hero type follows the 390 and 1440 frames: a white eyebrow pill and a 32px heading on a phone, and a 16px eyebrow, 52px heading, and bold 20px line on a wide screen. The trust row is white, with 16px bold type. The three offers sit in a plain row, without the cream cards. Each offer uses its exported icon at 64px on a phone and 88px on a wide screen.

— Sage (Second)

## 11 Oct 2026 — Page heights

On a wide screen, subpage sections use 48px of padding instead of 64px. Home stays on 64px. The content width stays 1120px, and the wave still sits inside the section padding.

— Sage (Second)

## 11 Oct 2026 — About and Contact

On a wide screen the About story photos sit on the left. The story wrapper uses the same indent as the other sections. The vision card is cream and the mission card is navy. “Our Vision” and “Our Mission” are visible 24px headings: the vision title is accent orange, and the mission title is white. Contact reach cards are cream with a 12px radius and a 1px border. The map placeholder is a Google Maps embed of the Bandar Botanik address, 280px tall on a phone and 240px tall on a wide screen. Each value tile has its exported icon on a #FFDD98 circle, 24px on a wide screen and 16.8px on a phone.

— Sage (Second)

## 12 Oct 2026 — Daycare fact tiles

Primary Daycare programme facts are four white tiles (radius 12, no border), including Subjects. The timetable is chip rows at every width: time above the activity on a wide screen, time on the left on a phone. The tables are gone. “What sets MyDelta Daycare apart?” sits on white, and those titles no longer break mid-word at 390px. “Life at MyDelta” drops the extra line. The orange wave above the visit band is unchanged in this batch.

— Sage (Second)

## 12 Oct 2026 — Speaking tiles and cards

Public Speaking opens with the photo on the left and three outline tiles. The yellow band is three fact tiles plus a Saturday schedule card, not a table. Student voices are outlined cards with orange names. Good to know is four static tiles. The student quotes are unchanged.

— Sage (Second)

## 12 Oct 2026 — About story, history, and values

About uses the heading “Our Story”, one paragraph, and three highlight cards. History is three paragraphs, with one photo on a phone. Mission and Vision sit in two cards. Our Values is its own heading above the fourteen tiles, which use a 1px stone border and 12px bold labels. The published Vision sentence is unchanged.

— Sage (Second)

## 12 Oct 2026 — Home welcome band

“Welcome to MyDelta” is 36px accent orange on a wide screen and 28px on a phone. The line under it is bold navy. On a phone the band is centred. The ribbon, basket, and bird artwork is not in the repo, so the yellow “35 years” circle stays until those files exist.

— Sage (Second)

## 12 Oct 2026 — Waves and the visit button

About, Daycare, Speaking, and Hall of Fame no longer paint an orange wave into the yellow visit band. The wave into a subpage footer is #20409A. Home keeps the #384C86 wave. The visit band’s WhatsApp button has no icon, stays on one line, and is 240px wide on a wide screen.

— Sage (Second)

## 12 Oct 2026 — Hall of Fame headings

The hero line, “Top of the class”, and “More of our stars” replace the internal standout notes. Card text is centred, photos are square, and the last row is centred. Section headings stay left aligned. The “More of our stars” band is white.

— Sage (Second)

## 12 Oct 2026 — Visible notes

The daycare hero no longer says that pricing is absent. The Home slides no longer show a DRAFT marker. The mobile menu no longer says the social links are placeholders. The logo alt text on every page is “MyDelta Academy”. The Xiaohongshu address is unchanged.

— Sage (Second)

## 12 Oct 2026 — Contact map

The contact map uses the live site’s Google Maps place for 20, Jalan Mahogani 1, Bandar Botanik. The iframe is lazy, sends no referrer, and is sandboxed to the permissions Maps needs. A page policy allows frames only from Google Maps. Join Us copy is unchanged.

— Sage (Second)
