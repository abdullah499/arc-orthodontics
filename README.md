# Arc Orthodontics — Demo Website

A fast, **fully responsive** marketing site for a fictional orthodontics practice
(Arc Orthodontics, Austin TX). Built as clean static HTML/CSS/JS — no build step,
no framework, no dependencies. Works on any phone, tablet, or desktop.

```
arc-orthodontics-site/
├── index.html        ← the whole site (semantic HTML + inline CSS + vanilla JS)
├── favicon.svg
├── netlify.toml      ← Netlify config (publish dir + headers)
├── .gitignore
├── README.md
└── assets/
    ├── favicon.svg
    ├── logo-mark.svg
    ├── logo-lockup.svg
    └── og-image.svg  ← social share preview (1200×630)
```

## What makes this version solid

- **Mobile-first responsive** — proper breakpoints, a hamburger menu, fluid type,
  and grids that collapse to one column. No horizontal scrolling on phones.
- **Crawlable & shareable** — all content and Open Graph / Twitter meta are in the
  static HTML, so Google indexes it and WhatsApp/LinkedIn/iMessage show a real
  link-preview card.
- **Instant load** — no client-side bundle unpacking, no in-browser transpiling.
- **Interactive, no framework** — working cost calculator, treatment finder,
  before/after sliders, and FAQ accordion in plain JavaScript.
- `MedicalBusiness` structured data for rich search results.

> Forms are demo-only (they show a confirmation but don't send anywhere). Wire them
> to Netlify Forms, Formspree, or your booking tool before going live.

---

## 1 · Push to GitHub

```bash
cd arc-orthodontics-site
git init
git add .
git commit -m "Arc Orthodontics demo site"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/arc-orthodontics.git
git push -u origin main
```

## 2 · Deploy on Netlify

1. Netlify → **Add new site → Import an existing project → GitHub** → pick the repo.
2. Build settings: **Build command** empty, **Publish directory** `.` (already set in `netlify.toml`).
3. **Deploy.** You'll get a live `https://<name>.netlify.app` URL in seconds.

Every future `git push` to `main` auto-deploys.

**Fast path (no GitHub):** drag this folder onto <https://app.netlify.com/drop>.

---

## 3 · Before showing a real client

- Replace the placeholder phone `(512) 555-0148`, address, and the `arcortho.com`
  URLs in the `<head>` (`canonical`, `og:url`, `og:image`) with the real ones.
- Swap the before/after illustrations for real (consented) patient photos.
- Connect the booking form to a real endpoint.

**Arc Orthodontics** · Braces & Invisalign in Austin, TX
Brand colors — Forest `#0E3826` · Emerald `#0C7E47` · Lime `#A7D930` · Linen `#F6F7F2`
