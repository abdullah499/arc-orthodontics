# Arc Orthodontics — Demo Website

A fast, **fully responsive, multi-page** marketing site for a fictional orthodontics
practice (Arc Orthodontics, Austin TX). Clean static HTML/CSS/JS — no framework, no
build step needed to deploy. Works on any phone, tablet, or desktop.

**Live:** https://arc-orthodontics.netlify.app/

## Pages (21)

Home · New Patients · Services · Plan · The Journey · Smile Stories · Insurance ·
The Studio · Journal · Contact · Reviews · Treatment Finder · Cost Calculator ·
Compare · Before & After · and 6 treatment detail pages (Invisalign Adult/Teen,
Ceramic, Metal, Early Treatment, Retainers).

```
arc-orthodontics-site/
├── index.html ... + 20 more page .html files   ← the site (one file per page)
├── assets/
│   ├── styles.css      ← shared responsive stylesheet
│   ├── app.js          ← shared JS (menu, calculator, finder, sliders, filters)
│   ├── favicon.svg / logo-mark.svg / logo-lockup.svg / og-image.svg
├── build/              ← local generator (NOT deployed; ignored by git)
│   ├── generate.py     ← run this to regenerate the pages
│   ├── partials.py     ← reusable widgets
│   └── pages.py        ← the content of every page
├── netlify.toml · README.md · .gitignore · favicon.svg
```

## What makes this version solid

- **Multi-page + mobile-first** — every route is its own real HTML page, with a shared
  responsive header, hamburger menu, and footer. No horizontal scrolling on phones.
- **Crawlable & shareable** — all content + Open Graph / Twitter meta live in the static
  HTML, so Google indexes every page and WhatsApp/LinkedIn/iMessage show a preview card.
- **Instant load** — no client-side bundle unpacking, no in-browser transpiling.
- **Interactive, no framework** — cost calculator, treatment finder, before/after
  sliders, filter chips, and FAQ accordions in plain JavaScript.
- `MedicalBusiness` structured data on every page.

## Editing the site

Pages are generated from `build/`. To change content, edit `build/pages.py` (text),
`build/partials.py` (shared widgets), or `assets/styles.css` (design), then run:

```bash
cd build
python generate.py     # rewrites all .html files in the project root
```

Static one-off tweaks can also be made directly in the `.html` files.

> Forms are demo-only (they show a confirmation but don't send). Wire them to Netlify
> Forms or Formspree before going live. The before/after images are stylized
> placeholders — swap in real, consented patient photos for a real client.

## Deploy

Pushing to the `main` branch auto-deploys to Netlify. Build command: empty.
Publish directory: `.`

**Arc Orthodontics** · Braces & Invisalign in Austin, TX
Brand colors — Forest `#0E3826` · Emerald `#0C7E47` · Lime `#A7D930` · Linen `#F6F7F2`
