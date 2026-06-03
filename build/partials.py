# -*- coding: utf-8 -*-
"""Reusable HTML widgets for page bodies."""

def page_hero(crumb, h1, lead, ctas=True):
    c = ('<div class="hero-cta"><a href="contact.html" class="btn btn-primary">Book a free smile scan</a>'
         '<a href="plan.html" class="btn btn-ghost">Plan your treatment →</a></div>') if ctas else ''
    return ('<section class="page-hero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / ' + crumb + '</div>'
            '<h1>' + h1 + '</h1><p class="lead">' + lead + '</p>' + c + '</div></section>')

FINAL = ('<section class="sec final"><div class="wrap"><h2>Your free scan is 30 minutes away.</h2>'
    '<p>A digital scan, a look at your future smile, and a clear plan with pricing, free, with zero pressure to commit.</p>'
    '<div class="cta-row"><a href="contact.html" class="btn btn-lime">Book a free smile scan</a>'
    '<a href="new-patients.html" class="btn btn-light">What to expect →</a></div></div></section>')

FINDER = ('<div class="tool finder"><h3>Find your fit</h3><p class="t-sub">Four quick questions.</p>'
 '<div class="progress"><i></i></div><div class="f-steps">'
 '<div class="f-step" data-step="0"><p class="q-title">Who is this for?</p>'
 '<button class="q-opt" data-next><b>Me, an adult<span>A grown-up, discreet fix.</span></b><span class="chev">→</span></button>'
 '<button class="q-opt" data-next><b>My teenager<span>Ages 11–17.</span></b><span class="chev">→</span></button>'
 '<button class="q-opt" data-next><b>My young child<span>Ages 7–10.</span></b><span class="chev">→</span></button></div>'
 '<div class="f-step" data-step="1" hidden><p class="q-title">What matters most?</p>'
 '<button class="q-opt" data-next><b>Barely visible<span>Discretion is the priority.</span></b><span class="chev">→</span></button>'
 '<button class="q-opt" data-next><b>Fastest result<span>Speed over everything.</span></b><span class="chev">→</span></button>'
 '<button class="q-opt" data-next><b>Lowest cost<span>Budget-friendly and proven.</span></b><span class="chev">→</span></button></div>'
 '<div class="f-step" data-step="2" hidden><p class="q-title">How is the crowding?</p>'
 '<button class="q-opt" data-next><b>Mild<span>A little uneven.</span></b><span class="chev">→</span></button>'
 '<button class="q-opt" data-next><b>Moderate<span>Noticeable spacing or crowding.</span></b><span class="chev">→</span></button>'
 '<button class="q-opt" data-next><b>Not sure<span>Let the specialist assess.</span></b><span class="chev">→</span></button></div>'
 '<div class="f-step" data-step="3" hidden><p class="q-title">Ready to start?</p>'
 '<button class="q-opt" data-next><b>Within a month<span>Let us get moving.</span></b><span class="chev">→</span></button>'
 '<button class="q-opt" data-next><b>Just exploring<span>Gathering information.</span></b><span class="chev">→</span></button></div>'
 '</div><div class="finder-result"><span class="eyebrow">Your likely fit</span>'
 '<div class="pill f-pill">Invisalign — Adult</div><p class="muted f-why">Discreet, removable, and ideal for most adult cases.</p>'
 '<div style="display:flex;gap:10px;justify-content:center;margin-top:16px;flex-wrap:wrap">'
 '<a href="service-invisalign-adult.html" class="btn btn-primary f-link">See this treatment</a>'
 '<button class="btn btn-ghost f-restart">Start over</button></div></div></div>')

CALC = ('<div class="tool calc"><h3>Estimate the cost</h3><p class="t-sub">A real range, before you ever call.</p>'
 '<label class="cl" for="cTreat">Choose treatment</label>'
 '<select id="cTreat"><option value="4800">Invisalign — Adult · from $4,800</option>'
 '<option value="4500">Invisalign — Teen · from $4,500</option>'
 '<option value="4500">Clear Ceramic Braces · from $4,500</option>'
 '<option value="3800">Modern Metal Braces · from $3,800</option>'
 '<option value="2500">Early Treatment (Phase 1) · from $2,500</option></select>'
 '<label class="cl" for="cTerm">Payment term · <span class="term-val" id="cTermV">18 months</span></label>'
 '<input type="range" id="cTerm" min="12" max="24" step="3" value="18">'
 '<label class="cl" for="cIns">Insurance ortho benefit</label>'
 '<select id="cIns"><option value="0">None / not sure</option><option value="1000">$1,000</option>'
 '<option value="1500" selected>$1,500</option><option value="2000">$2,000</option><option value="2500">$2,500</option></select>'
 '<div class="calc-out"><div class="big">$<span id="cMonthly">181</span><span>/mo · 0% interest</span></div>'
 '<small id="cSummary">$3,300 after insurance, over 18 months · $0 down</small></div>'
 '<div style="margin-top:14px"><div class="calc-rows"><span>Treatment</span><b id="cBase">$4,800</b></div>'
 '<div class="calc-rows"><span>Less insurance benefit</span><b id="cBen">– $1,500</b></div>'
 '<div class="calc-rows"><span>Your estimate</span><b id="cNet">$3,300</b></div></div>'
 '<p class="form-note" style="margin-top:14px">Estimate only. Your exact price is confirmed at your free scan.</p></div>')

def review(stars, date, text, who, tag, cat):
    return ('<article class="rev" data-cat="' + cat + '"><div class="stars">' + ('★'*stars) + '</div>'
            '<div class="date">' + date + '</div><p>' + text + '</p>'
            '<div class="who">' + who + '<small>' + tag + '</small></div></article>')

def ba_card(title, sub, cat="all"):
    return ('<div class="ba-card" data-cat="' + cat + '"><div class="ba-img" data-ba>'
            '<div class="ba-pane ba-before"><div class="teeth"><i></i><i></i><i></i><i></i><i></i><i></i></div></div>'
            '<div class="ba-pane ba-after"><div class="teeth"><i></i><i></i><i></i><i></i><i></i><i></i></div></div>'
            '<span class="ba-label bl">Before</span><span class="ba-label al">After</span><div class="ba-handle"></div></div>'
            '<div class="ba-cap"><b>' + title + '</b><span>' + sub + '</span></div></div>')

def step(n, when, h3, p):
    return ('<div class="step"><div class="n">' + str(n) + '</div><div><div class="when">' + when + '</div>'
            '<h3>' + h3 + '</h3><p>' + p + '</p></div></div>')

def service_detail(num, kind, name, blurb, price, mo, spec2, spec3, journey, best_for):
    """Builds a service detail page body."""
    spec = ('<div class="svc-spec"><div><b>' + price + '</b><span>typical case</span></div>'
            '<div><b>' + spec2[0] + '</b><span>' + spec2[1] + '</span></div>'
            '<div><b>' + spec3[0] + '</b><span>' + spec3[1] + '</span></div></div>')
    steps = ''.join(step(i+1, w, h, p) for i,(w,h,p) in enumerate(journey))
    return ('<section class="page-hero"><div class="wrap"><div class="crumb"><a href="index.html">Home</a> / '
        '<a href="services.html">Treatments</a> / ' + name + '</div>'
        '<div class="svc-hero"><div><span class="eyebrow">' + num + ' · ' + kind + '</span>'
        '<h1>' + name + '.</h1><p class="lead">' + blurb + '</p>' + spec + '</div>'
        '<div class="price-badge"><div class="p">' + price + '</div><div class="sub">' + mo + '</div>'
        '<a href="contact.html" class="btn btn-lime" style="width:100%;justify-content:center">Book a free smile scan</a>'
        '<a href="calculator.html" class="btn" style="width:100%;justify-content:center;margin-top:10px;background:rgba(255,255,255,.1);color:#fff">Estimate my plan</a></div>'
        '</div></div></section>'
        '<section class="sec"><div class="wrap"><div class="sec-head"><span class="eyebrow">The journey</span>'
        '<h2>Five steps, all momentum.</h2><p>' + best_for + '</p></div><div class="steps">' + steps + '</div>'
        '<div style="margin-top:28px"><a href="compare.html" class="btn btn-ghost">Compare all treatments →</a></div>'
        '</div></section>')
