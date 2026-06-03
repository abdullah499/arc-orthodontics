# -*- coding: utf-8 -*-
"""Static multi-page generator for Arc Orthodontics. Emits .html files to the site root."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://arc-orthodontics.netlify.app/"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,600;12..96,700;12..96,800&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">')

def head(title, desc, slug):
    canon = BASE + slug
    return ("<!DOCTYPE html><html lang=\"en\"><head>"
    "<meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
    "<title>" + title + "</title>"
    "<meta name=\"description\" content=\"" + desc + "\">"
    "<meta name=\"theme-color\" content=\"#0E3826\">"
    "<link rel=\"canonical\" href=\"" + canon + "\">"
    "<meta property=\"og:type\" content=\"website\"><meta property=\"og:site_name\" content=\"Arc Orthodontics\">"
    "<meta property=\"og:title\" content=\"" + title + "\">"
    "<meta property=\"og:description\" content=\"" + desc + "\">"
    "<meta property=\"og:url\" content=\"" + canon + "\">"
    "<meta property=\"og:image\" content=\"" + BASE + "assets/og-image.svg\">"
    "<meta name=\"twitter:card\" content=\"summary_large_image\">"
    "<meta name=\"twitter:title\" content=\"" + title + "\">"
    "<meta name=\"twitter:description\" content=\"" + desc + "\">"
    "<meta name=\"twitter:image\" content=\"" + BASE + "assets/og-image.svg\">"
    "<link rel=\"icon\" href=\"/favicon.svg\" type=\"image/svg+xml\">"
    + FONTS +
    "<link rel=\"stylesheet\" href=\"assets/styles.css\"></head><body>"
    "<a class=\"skip\" href=\"#main\">Skip to content</a>")

LOGO = ('<svg viewBox="0 0 100 100" fill="none" aria-hidden="true"><path d="M16 72 A46 46 0 0 1 84 34" '
        'stroke="#0C7E47" stroke-width="13" stroke-linecap="round"/><circle cx="84" cy="34" r="9" fill="#A7D930"/></svg>')

def header(active=""):
    def cls(name): return ' class="active"' if name==active else ''
    return ('<div class="topbar"><div class="wrap">'
    '<div class="t-hide">Austin, TX · Open Mon–Sat · Free parking</div>'
    '<div class="t-mid"><span class="star">★</span> 4.9 · 900 reviews</div>'
    '<a href="tel:+15125550148">(512) 555-0148</a></div></div>'
    '<header class="site"><div class="wrap">'
    '<a class="brand" href="index.html" aria-label="Arc Orthodontics home">' + LOGO + '<b>Arc</b></a>'
    '<nav class="nav" aria-label="Primary">'
    '<a href="index.html"' + cls("home") + '>Home</a>'
    '<a href="services.html"' + cls("services") + '>Services</a>'
    '<a href="plan.html"' + cls("plan") + '>Plan</a>'
    '<a href="stories.html"' + cls("stories") + '>Stories</a>'
    '<a href="insurance.html"' + cls("insurance") + '>Insurance</a>'
    '<a href="about.html"' + cls("about") + '>The Studio</a>'
    '<a href="journal.html"' + cls("journal") + '>Journal</a>'
    '<a href="contact.html"' + cls("contact") + '>Visit</a>'
    '</nav><div class="header-cta"><a href="contact.html" class="btn btn-primary">Book a visit</a>'
    '<button class="hamburger" id="openMenu" aria-label="Open menu" aria-expanded="false"><span></span></button>'
    '</div></div></header>'
    '<div class="drawer" id="drawer"><div class="drawer-bg" data-close></div>'
    '<div class="drawer-panel" role="dialog" aria-modal="true" aria-label="Menu">'
    '<div class="drawer-top"><a class="brand" href="index.html" data-close><b>Arc Orthodontics</b></a>'
    '<button class="drawer-close" data-close aria-label="Close menu">×</button></div>'
    '<a href="index.html" data-close>Home</a><a href="new-patients.html" data-close>New Patients</a>'
    '<a href="services.html" data-close>Services</a><a href="plan.html" data-close>Plan</a>'
    '<a href="journey.html" data-close>The Journey</a><a href="stories.html" data-close>Smile Stories</a>'
    '<a href="insurance.html" data-close>Insurance</a><a href="about.html" data-close>The Studio</a>'
    '<a href="journal.html" data-close>Journal</a><a href="contact.html" data-close>Contact</a>'
    '<div class="d-label">Tools</div>'
    '<a href="reviews.html" data-close>All Reviews</a><a href="finder.html" data-close>Treatment Finder</a>'
    '<a href="calculator.html" data-close>Cost Calculator</a><a href="compare.html" data-close>Compare</a>'
    '<a href="gallery.html" data-close>Before &amp; After</a>'
    '<a class="btn btn-lime" href="contact.html" data-close>Book a free smile scan</a>'
    '</div></div><main id="main">')

JSONLD = ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"MedicalBusiness",'
    '"name":"Arc Orthodontics","description":"Braces and Invisalign for teens and adults in Austin, TX.",'
    '"url":"https://arc-orthodontics.netlify.app/","telephone":"+1-512-555-0148","priceRange":"$$",'
    '"image":"https://arc-orthodontics.netlify.app/assets/og-image.svg",'
    '"address":{"@type":"PostalAddress","streetAddress":"240 Linden Way, Studio 3","addressLocality":"Austin","addressRegion":"TX","addressCountry":"US"},'
    '"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"18:00"},'
    '{"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"14:00"}],'
    '"aggregateRating":{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"900"}}</script>')

FOOTER = ('</main><footer class="site"><div class="wrap"><div class="foot-grid">'
    '<div><a class="brand" href="index.html" style="margin-bottom:10px"><svg viewBox="0 0 100 100" fill="none" aria-hidden="true" style="width:30px;height:30px"><path d="M16 72 A46 46 0 0 1 84 34" stroke="#0C7E47" stroke-width="13" stroke-linecap="round"/><circle cx="84" cy="34" r="9" fill="#A7D930"/></svg><b style="color:#fff">Arc</b></a>'
    '<p class="tagline">Made to move every smile forward. Braces &amp; Invisalign for teens and adults in Austin, TX.</p>'
    '<a href="contact.html" class="btn btn-lime">Book a free smile scan →</a></div>'
    '<div><h4>Treatments</h4><ul><li><a href="service-invisalign-adult.html">Invisalign — Adult</a></li><li><a href="service-invisalign-teen.html">Invisalign — Teen</a></li><li><a href="service-ceramic.html">Ceramic Braces</a></li><li><a href="service-metal.html">Metal Braces</a></li><li><a href="service-early.html">Early Treatment</a></li><li><a href="service-retainers.html">Retainers</a></li></ul></div>'
    '<div><h4>Explore</h4><ul><li><a href="new-patients.html">New Patients</a></li><li><a href="plan.html">Plan &amp; pricing</a></li><li><a href="journey.html">The Journey</a></li><li><a href="stories.html">Smile Stories</a></li><li><a href="journal.html">Journal</a></li><li><a href="about.html">The Studio</a></li></ul></div>'
    '<div><h4>Visit</h4><ul><li><a href="https://maps.google.com/?q=Austin,TX" target="_blank" rel="noopener">240 Linden Way, Studio 3</a></li><li><a href="tel:+15125550148">(512) 555-0148</a></li><li><a href="contact.html">Hours &amp; directions</a></li><li><a href="reviews.html">Reviews</a></li><li><a href="insurance.html">Insurance</a></li></ul></div>'
    '</div><div class="foot-bottom"><span>© <span id="yr">2026</span> Arc Orthodontics · Austin, TX</span><span>Demo site · Privacy · Terms</span></div>'
    '</div></footer>' + JSONLD + '<script src="assets/app.js" defer></script></body></html>')

from pages import PAGES

def build():
    for slug, (fname, active, title, desc, main) in PAGES.items():
        canon_slug = "" if fname == "index.html" else fname
        html = head(title, desc, canon_slug) + header(active) + main + FOOTER
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", fname, len(html), "bytes")

if __name__ == "__main__":
    build()
