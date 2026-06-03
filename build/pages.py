# -*- coding: utf-8 -*-
"""Page bodies (the <main> content) for every route, keyed by slug."""
from partials import page_hero, FINAL, FINDER, CALC, review, ba_card, step, service_detail

# ---------- shared chunks ----------
LOCATION = ('<section class="sec"><div class="wrap"><div class="loc-grid">'
 '<div class="card-b"><span class="eyebrow">Visit us</span>'
 '<h2 style="font-size:clamp(1.6rem,3.5vw,2.3rem);margin:10px 0 6px">Easy to reach, easy to park.</h2>'
 '<ul class="hours"><li><b>Monday – Friday</b><span>8:00a – 6:00p</span></li>'
 '<li><b>Saturday</b><span>9:00a – 2:00p</span></li><li class="closed"><b>Sunday</b><span>Closed</span></li></ul>'
 '<p style="font-weight:600">240 Linden Way · Studio 3 · Austin, TX</p>'
 '<p class="muted" style="margin-bottom:18px">Free parking · Wheelchair accessible</p>'
 '<div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary" href="https://maps.google.com/?q=Austin,TX" target="_blank" rel="noopener">Get directions</a>'
 '<a class="btn btn-ghost" href="tel:+15125550148">Call (512) 555-0148</a></div></div>'
 '<div class="map" aria-label="Map of the Arc Orthodontics studio"><div class="grid-lines"></div>'
 '<div class="pin"><div class="dot"></div><b>Arc Orthodontics</b></div></div></div></div></section>')

SVC_CARDS = ('<div class="svc-grid">'
 '<a class="svc" href="service-invisalign-adult.html"><div class="num">01</div><span class="arrow">→</span><h3>Invisalign® — Adult</h3><div class="meta">6–18 months</div><div class="desc">Clear aligners, planned in 3D. Straighten discreetly while you work and live.</div><div class="price">from $4,800</div></a>'
 '<a class="svc" href="service-invisalign-teen.html"><div class="num">02</div><span class="arrow">→</span><h3>Invisalign® — Teen</h3><div class="meta">12–18 months</div><div class="desc">Built for teen life, with wear indicators and a progress app they actually use.</div><div class="price">from $4,500</div></a>'
 '<a class="svc" href="service-ceramic.html"><div class="num">03</div><span class="arrow">→</span><h3>Clear Ceramic Braces</h3><div class="meta">12–24 months</div><div class="desc">Tooth-coloured brackets that blend in while they do the heavy lifting.</div><div class="price">from $4,500</div></a>'
 '<a class="svc" href="service-metal.html"><div class="num">04</div><span class="arrow">→</span><h3>Modern Metal Braces</h3><div class="meta">12–24 months</div><div class="desc">The most efficient, budget-friendly route for complex cases.</div><div class="price">from $3,800</div></a>'
 '<a class="svc" href="service-early.html"><div class="num">05</div><span class="arrow">→</span><h3>Early Treatment (Phase 1)</h3><div class="meta">Ages 7–10</div><div class="desc">Gentle guidance at the right moment, often shortening later treatment.</div><div class="price">from $2,500</div></a>'
 '<a class="svc" href="service-retainers.html"><div class="num">06</div><span class="arrow">→</span><h3>Retainers &amp; Retention</h3><div class="meta">Per arch</div><div class="desc">Custom retainers to protect your result for life.</div><div class="price">from $250</div></a>'
 '</div>')

REVIEWS = [
 (5,"March 2026","“Eleven months and I finally stopped hiding my smile in photos. The team made every check-in feel like a win.”","Priya N.","Invisalign","invisalign"),
 (5,"February 2026","“They actually made my 14-year-old excited about her braces. The app turned it into a game she wanted to win.”","The Carters","Teen","teen"),
 (5,"February 2026","“Dr. Park is exact in the best way, predicted my finish month and we landed on it. Quiet, professional, kind.”","Maya T.","Braces","braces"),
 (5,"January 2026","“Discreet and easy to live with. They filed all my insurance and the monthly plan made it genuinely painless.”","Daniel R.","Invisalign","invisalign"),
 (5,"January 2026","“My son needed early treatment and they only acted when the timing was right. No upselling, just honest advice.”","Rebecca M.","Early","early"),
 (5,"December 2025","“The 3D preview sold me. Seeing the result before starting made the whole decision easy.”","Tom H.","Invisalign","invisalign"),
 (5,"December 2025","“Front gap closed in seven months. Friendly front desk, never felt rushed, parking is genuinely free.”","Aisha K.","Invisalign","invisalign"),
 (5,"November 2025","“Ceramic braces you can barely see. My daughter is thrilled and so are we.”","The Nguyens","Teen","teen"),
 (4,"November 2025","“Knocked off a star only because they are very booked, worth the wait though. Excellent care.”","Marcus L.","Braces","braces"),
 (5,"October 2025","“The Smile Club made it affordable without insurance. Clear pricing, zero surprises.”","Sofia D.","Invisalign","invisalign"),
 (5,"October 2025","“Professional, warm, and on time every visit. The progress app kept my teen motivated all year.”","Grace P.","Teen","teen"),
 (5,"September 2025","“Adult relapse from years ago, redone in nine months. I wish I had come here first.”","Hannah W.","Invisalign","invisalign"),
]

CARRIERS = ['Aetna','Blue Cross Blue Shield','Cigna','Delta Dental','Guardian','Humana','MetLife','UnitedHealthcare','Ameritas','Principal','GEHA','+ many more']

# ---------- HOME ----------
HOME = ('<section class="hero"><div class="wrap"><div class="hero-grid"><div>'
 '<span class="tag">Braces &amp; Invisalign · Teens &amp; Adults</span>'
 '<h1>A confident smile, <span class="accent">already in motion.</span></h1>'
 '<p class="lead">See your future smile before day one. We map your whole treatment with a digital scan, show you the result up front, and make the journey there genuinely exciting.</p>'
 '<div class="hero-cta"><a href="contact.html" class="btn btn-primary">Book a free smile scan</a>'
 '<a href="plan.html" class="btn btn-ghost">Plan your treatment →</a></div></div>'
 '<div class="hero-card"><div class="hc-label">Your future smile · 3D preview</div>'
 '<div class="smile"><svg viewBox="0 0 200 120" aria-hidden="true"><path d="M30 45 Q100 120 170 45" fill="none" stroke="#A7D930" stroke-width="4" opacity=".5"/>'
 '<g fill="#fff"><rect x="62" y="50" width="15" height="22" rx="4"/><rect x="80" y="52" width="15" height="24" rx="4"/><rect x="98" y="52" width="15" height="24" rx="4"/><rect x="116" y="50" width="15" height="22" rx="4"/></g></svg></div>'
 '<div class="hc-label" style="color:#bfe0cd">Free · No obligation</div>'
 '<p style="margin-top:6px;color:#cfe6d8;font-size:.95rem">Thirty unhurried minutes. Leave with a 3D preview, an exact price, and a 0%-interest plan.</p></div></div>'
 '<div class="stats"><div class="stat"><b>12,000+</b><span>Smiles moved</span></div>'
 '<div class="stat"><b>4.9★</b><span>On 900 reviews</span></div><div class="stat"><b>$0</b><span>Down · 0% plans</span></div></div></div></section>'
 '<section class="sec bg-forest"><div class="wrap"><div class="grid-2 align-center"><div>'
 '<span class="eyebrow" style="color:var(--lime)">Why Arc</span>'
 '<h2 style="font-size:clamp(1.8rem,4vw,2.8rem);max-width:18ch;margin-top:12px">Straight teeth are the easy part.</h2>'
 '<p style="font-size:1.1rem;margin-top:18px">What we are really building is the confidence to stop hiding your smile. Specialist-led orthodontics for growing kids, busy teens, and adults who never quite got around to it.</p>'
 '<a href="about.html" class="btn btn-lime" style="margin-top:24px">Meet the studio →</a></div>'
 '<ul class="ticks" style="gap:14px"><li>A two-minute digital scan replaces uncomfortable moulds.</li>'
 '<li>Simulations show you the result before you ever commit.</li>'
 '<li>$0 down, 0% interest, and we file your insurance for you.</li>'
 '<li>Specialist orthodontists, not a general dental chain.</li></ul></div></div></section>'
 '<section class="sec"><div class="wrap"><div class="sec-head"><span class="eyebrow">Treatments</span>'
 '<h2>Every smile, a path forward.</h2><p>Specialist treatment for growing smiles, matched to your life, your timeline, and your budget.</p></div>'
 + SVC_CARDS + '<div style="margin-top:28px"><a href="services.html" class="btn btn-ghost">Explore all treatments →</a></div></div></section>'
 '<section class="sec bg-linen"><div class="wrap"><div class="sec-head"><span class="eyebrow">Real results</span>'
 '<h2>Drag to watch the change.</h2><p>Real Arc patients, photographed in the same light. Slide the handle to see where momentum takes a smile.</p></div>'
 '<div class="ba-cases">' + ba_card("Case 042 · Invisalign, both arches","Adult · 11 months") + ba_card("Case 118 · Ceramic braces","Teen · 16 months") + '</div>'
 '<div style="margin-top:28px"><a href="gallery.html" class="btn btn-ghost">See the full gallery →</a></div></div></section>'
 '<section class="sec"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Plan your treatment</span>'
 '<h2>Find it. Price it. Book it.</h2><p>Three quick tools to narrow your options and see an honest price, with no phone call and no email gate.</p></div>'
 '<div class="grid-3">'
 '<a class="card-b" href="finder.html" style="text-align:center"><h3 style="font-size:1.25rem">Treatment Finder</h3><p class="muted" style="margin-top:6px">Answer four questions, get your likely fit.</p></a>'
 '<a class="card-b" href="calculator.html" style="text-align:center"><h3 style="font-size:1.25rem">Cost Calculator</h3><p class="muted" style="margin-top:6px">See a real monthly plan after insurance.</p></a>'
 '<a class="card-b" href="compare.html" style="text-align:center"><h3 style="font-size:1.25rem">Compare Treatments</h3><p class="muted" style="margin-top:6px">All six options, side by side.</p></a></div></div></section>'
 '<section class="sec bg-linen"><div class="wrap"><div class="sec-head"><span class="eyebrow">In writing</span>'
 '<h2>Nine hundred recommendations.</h2><p>Verified on Google. Real Arc patients, in their own words.</p></div>'
 '<div class="rev-grid">' + ''.join(review(*r) for r in REVIEWS[:4]) + '</div>'
 '<div style="margin-top:28px"><a href="reviews.html" class="btn btn-ghost">Read all 900 reviews →</a></div></div></section>'
 + LOCATION + FINAL)

# ---------- SERVICES ----------
SERVICES = (page_hero('<a href="services.html">Treatments</a>','Every option, one honest menu.',
  'Six specialist treatments for teens, adults, and growing kids. Clear pricing, clear timelines, and a free scan to find the right one for you.')
 + '<section class="sec"><div class="wrap">' + SVC_CARDS + '</div></section>'
 + '<section class="sec bg-linen"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Not sure which?</span>'
 '<h2>Let the tools point the way.</h2><p>No phone call, no email gate. Narrow it down in a couple of minutes.</p></div>'
 '<div class="grid-3"><a class="card-b" href="finder.html" style="text-align:center"><h3 style="font-size:1.25rem">Treatment Finder</h3><p class="muted" style="margin-top:6px">Four questions to your likely fit.</p></a>'
 '<a class="card-b" href="calculator.html" style="text-align:center"><h3 style="font-size:1.25rem">Cost Calculator</h3><p class="muted" style="margin-top:6px">A real monthly plan after insurance.</p></a>'
 '<a class="card-b" href="compare.html" style="text-align:center"><h3 style="font-size:1.25rem">Compare</h3><p class="muted" style="margin-top:6px">Every treatment, side by side.</p></a></div></div></section>' + FINAL)

# ---------- NEW PATIENTS ----------
NEWPAT = (page_hero('New Patients','Your first visit, made simple.',
  'Welcome to Arc. Here is exactly what happens at your free smile scan: no paperwork marathon, no pressure, no surprises.')
 + '<section class="sec"><div class="wrap"><div class="sec-head"><span class="eyebrow">What to expect</span><h2>Thirty easy minutes.</h2></div>'
 '<div class="steps">'
 + step(1,"On arrival","Warm welcome","A friendly hello, a quick chat about what you would like to change, and a tour if you want one.")
 + step(2,"Two minutes","Digital scan","A comfortable two-minute scan, no goopy moulds, builds your 3D smile on screen.")
 + step(3,"The fun part","See your future smile","We show you a preview of the result and talk through which treatments fit.")
 + step(4,"To take home","Your plan and price","A clear plan with timelines, an honest price, and a monthly option, with no pressure.")
 + '</div></div></section>'
 '<section class="sec bg-linen"><div class="wrap"><div class="grid-2 align-center"><div>'
 '<span class="eyebrow">Paperless intake</span><h2 style="font-size:clamp(1.6rem,3.5vw,2.3rem);margin:12px 0 14px">Fill it in before you arrive.</h2>'
 '<p class="muted">Our intake is fully paperless and HIPAA secure. Complete it online in about five minutes and save that time in the chair, or do it with a coffee when you get here.</p>'
 '<div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:22px"><a href="contact.html" class="btn btn-primary">Start my forms online →</a><a href="contact.html" class="btn btn-ghost">Book a free smile scan</a></div></div>'
 '<div class="card-b"><ul class="ticks" style="gap:14px"><li>Contact &amp; medical history · about 3 minutes</li><li>Insurance details · we verify your benefits</li>'
 '<li>Consent forms · signed securely online</li><li>Nothing to print, nothing to remember</li></ul></div></div></div></section>' + FINAL)

# ---------- ABOUT ----------
TEAM = ('<div class="team">'
 '<div class="member"><div class="ph"><div class="av">DP</div></div><div class="mb"><div class="role">Orthodontist</div><h3>Dr. Daniel Park</h3><p>Specialist in complex bite correction and early treatment. Fourteen years in practice, and the calm voice every nervous teen and parent hopes to meet.</p></div></div>'
 '<div class="member"><div class="ph"><div class="av">SR</div></div><div class="mb"><div class="role">Treatment Coordinator</div><h3>Sofia Reyes</h3><p>Your guide from first scan to final reveal. Sofia turns insurance, scheduling, and payment plans into something genuinely simple.</p></div></div>'
 '<div class="member"><div class="ph"><div class="av">JB</div></div><div class="mb"><div class="role">Lead Clinical Technician</div><h3>Jordan Blake</h3><p>Runs our digital scanning and smile simulations. If you have seen your future smile on screen, Jordan made it appear.</p></div></div></div>')
FIGURES = ('<div class="figures"><div class="figure"><b>12,000+</b><span>Smiles moved</span></div>'
 '<div class="figure"><b>4.9★</b><span>900 reviews</span></div><div class="figure"><b>98%</b><span>Finish on/ahead of plan</span></div>'
 '<div class="figure"><b>10 min</b><span>Avg wait time</span></div><div class="figure"><b>$0</b><span>Down · 0% plans</span></div>'
 '<div class="figure"><b>2</b><span>Board-certified orthodontists</span></div></div>')
ABOUT = (page_hero('The Studio','Tech-forward, human-first.',
  'A specialist-led team who treat the nervous first visit as seriously as the final reveal. Here is who you will meet, and the numbers behind the smiles.')
 + '<section class="sec"><div class="wrap"><div class="sec-head"><span class="eyebrow">The team</span><h2>The people behind your smile.</h2></div>'
 + TEAM + FIGURES + '</div></section>'
 '<section class="sec bg-forest"><div class="wrap"><div class="grid-2 align-center"><div>'
 '<span class="eyebrow" style="color:var(--lime)">Why Arc</span><h2 style="margin-top:12px">A confident smile should feel as good as the result.</h2></div>'
 '<ul class="ticks" style="gap:14px"><li>Digital scanning replaces uncomfortable moulds in two minutes.</li>'
 '<li>You see your projected smile before you ever commit.</li><li>Honest, no-pressure plans with transparent pricing.</li>'
 '<li>Specialist orthodontists for every age, in one calm studio.</li></ul></div></div></section>' + FINAL)

# ---------- CONTACT ----------
CONTACT = (page_hero('Contact','Book your free smile scan.',
  'Thirty unhurried minutes. Leave with a 3D preview of your future smile, an exact price, and a 0%-interest plan, then decide on your own time.', ctas=False)
 + '<section class="sec"><div class="wrap"><div class="grid-2 align-start"><div>'
 '<span class="eyebrow">Free · No obligation</span><h2 style="font-size:clamp(1.7rem,3.5vw,2.4rem);margin:12px 0 14px">Reserve your scan.</h2>'
 '<ul class="ticks" style="gap:12px"><li>A real, costed plan the same day</li><li>We file your insurance for you</li><li>Zero pressure to start</li></ul>'
 '<p class="muted" style="margin-top:24px;font-weight:600">240 Linden Way · Studio 3 · Austin, TX</p>'
 '<p class="muted">Mon–Fri 8:00a–6:00p · Sat 9:00a–2:00p</p><p class="muted"><a href="tel:+15125550148" style="color:var(--emerald);font-weight:600">(512) 555-0148</a></p></div>'
 '<form class="card-b" data-demo novalidate>'
 '<div class="row-2"><div class="field"><label for="fn">First name</label><input id="fn" name="fn" required autocomplete="given-name"></div>'
 '<div class="field"><label for="mob">Mobile</label><input id="mob" name="mob" type="tel" autocomplete="tel"></div></div>'
 '<div class="field"><label for="int">I am interested in</label><select id="int"><option>Not sure yet — help me decide</option>'
 '<option>Invisalign (adult)</option><option>Invisalign (teen)</option><option>Braces</option><option>Early treatment (child)</option><option>Retainers</option></select></div>'
 '<div class="field"><label for="time">Best time</label><select id="time"><option>Weekday morning</option><option>Weekday afternoon</option><option>Evening</option><option>Saturday</option></select></div>'
 '<button type="submit" class="btn btn-primary">Reserve my free scan →</button>'
 '<p class="form-note">Your details stay private. Never shared, never spammed.</p>'
 '<div class="form-ok">Thanks! This is a demo form. On the live site this books your scan and texts a confirmation.</div></form></div></div></section>'
 + LOCATION)

# ---------- PLAN ----------
PLAN = (page_hero('Plan','Find it. Price it. Book it.',
  'Two short steps, one page. First we narrow the field to the one or two treatments that fit your goals, then we give you an honest estimate with $0-down monthly plans. No phone call, no email gate.')
 + '<section class="sec"><div class="wrap"><div class="tools-grid">' + FINDER + CALC + '</div></div></section>'
 '<section class="sec bg-linen"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Still deciding?</span>'
 '<h2>Put them side by side.</h2><p>Visibility, time, cost, and daily care for all six treatments, in one plain table.</p></div>'
 '<div class="center"><a href="compare.html" class="btn btn-primary">Compare all treatments →</a></div></div></section>' + FINAL)

# ---------- JOURNEY ----------
JOURNEY = (page_hero('The Journey','Every step, mapped out.',
  'From your first free scan to the retainer that protects it for life, here is exactly what the road to your confident smile looks like.')
 + '<section class="sec"><div class="wrap"><div class="sec-head"><span class="eyebrow">Step by step</span>'
 '<h2>Six steps, all momentum.</h2><p>A typical Invisalign or braces journey, start to finish. Your exact plan is mapped at your free scan.</p></div><div class="steps">'
 + step(1,"Day one · 30 min","Free smile scan","A two-minute digital scan replaces messy moulds and builds your 3D plan. You see your projected smile on screen the same day.")
 + step(2,"Within ~1 week","Your plan, in 3D","We refine every move and show you the finish line, the timeline, and the all-in price before anything begins.")
 + step(3,"Start day","First aligners or braces","Discreet attachments or brackets go on. You leave with your first trays and the progress app, or your first adjustment booked.")
 + step(4,"Every 1–2 weeks","Quiet progress","Fresh aligners or short adjustment visits keep you ahead of schedule. Small moves you barely notice.")
 + step(5,"Final weeks","Refinement","A short polishing phase fine-tunes the details so the finish matches the plan exactly.")
 + step(6,"For life","Retain and protect","Braces off, smile on, and a custom retainer to keep it that way.")
 + '</div></div></section>'
 '<section class="sec bg-linen"><div class="wrap"><div class="sec-head"><span class="eyebrow">Real journeys</span><h2>See it on a real smile.</h2></div>'
 '<div class="ba-cases">' + ba_card("Priya · Invisalign Adult","11 months") + ba_card("Maya · Ceramic braces","16 months") + '</div>'
 '<div style="margin-top:28px"><a href="gallery.html" class="btn btn-ghost">See the full gallery →</a></div></div></section>' + FINAL)

# ---------- STORIES ----------
STORIES = (page_hero('Smile Stories','Real smiles, real momentum.',
  'Nine hundred verified recommendations, and the before-and-afters behind them. Slide the handle, read the words, picture your own.')
 + '<section class="sec"><div class="wrap"><div class="sec-head"><span class="eyebrow">Real results</span><h2>Drag to see it.</h2></div>'
 '<div class="ba-cases">' + ba_card("Crowding, quietly fixed","Invisalign Adult · 11 months") + ba_card("A confident teen smile","Ceramic braces · 16 months") + '</div></div></section>'
 '<section class="sec bg-linen"><div class="wrap"><div class="sec-head"><span class="eyebrow">In writing</span>'
 '<h2>Nine hundred recommendations.</h2><p>Verified on Google. Filter by treatment to read what your case sounded like.</p></div>'
 '<div class="rev-grid">' + ''.join(review(*r) for r in REVIEWS[:8]) + '</div>'
 '<div style="margin-top:28px"><a href="reviews.html" class="btn btn-ghost">Read all reviews →</a></div></div></section>' + FINAL)

# ---------- INSURANCE ----------
INSURANCE = (page_hero('Insurance','Honest pricing, made simple.',
  'Start treatment without paying anything up front, and let us handle the paperwork. Here is exactly how payment, insurance, and our membership work.')
 + '<section class="sec"><div class="wrap"><div class="perks">'
 '<div class="perk"><b>$0</b><span>Down</span><small>Start treatment without paying anything up front.</small></div>'
 '<div class="perk"><b>0%</b><span>Interest</span><small>Spread the cost over 12–24 months, interest-free.</small></div>'
 '<div class="perk"><b>5%</b><span>Off in full</span><small>Prefer to pay up front? Save 5% on the total.</small></div>'
 '<div class="perk"><b>✓</b><span>We file for you</span><small>Every insurance claim handled on your behalf.</small></div></div>'
 '<div class="ins-2"><div class="carriers"><span class="eyebrow">In-network</span>'
 '<h3 style="font-size:1.5rem;margin:10px 0 6px">The carriers we work with.</h3>'
 '<p class="muted" style="font-size:.95rem">In-network with most major plans, and if yours is not listed, we will still file as an out-of-network provider.</p>'
 '<div class="carrier-list">' + ''.join('<span>'+c+'</span>' for c in CARRIERS) + '</div></div>'
 '<div class="club"><span class="eyebrow" style="color:var(--lime)">No insurance? No problem.</span>'
 '<h3 style="font-size:1.5rem;margin:10px 0 0">The Arc Smile Club.</h3><div class="price">$29<span style="font-size:1rem;color:#bfe0cd">/mo</span></div>'
 '<ul><li>Free smile scan &amp; records visit</li><li>10% off any treatment</li><li>Priority scheduling</li><li>$0-down, 0% monthly plans</li></ul>'
 '<a href="contact.html" class="btn btn-lime">Join the Smile Club →</a></div></div>'
 '<div style="margin-top:34px" class="center"><a href="calculator.html" class="btn btn-primary">Estimate my monthly plan →</a></div></div></section>'
 '<section class="sec bg-linen"><div class="wrap"><div class="sec-head center"><span class="eyebrow">Good questions</span><h2>Payment, answered.</h2></div>'
 '<div class="faq"><details open><summary>How do the $0-down plans work? <span class="pl">+</span></summary><div class="ans">You start with nothing up front and spread the balance over 12 to 24 months at 0% interest. We set the monthly figure with you at your free scan.</div></details>'
 '<details><summary>What if I do not have insurance? <span class="pl">+</span></summary><div class="ans">The Arc Smile Club is a simple in-house membership at $29/mo with your scan included, 10% off any treatment, and locked-in 0% plans. No claims, no deductibles, no waiting periods.</div></details>'
 '<details><summary>Do you really file the claim for me? <span class="pl">+</span></summary><div class="ans">Yes. We verify your benefits before you start and file every claim on your behalf, so you are not chasing paperwork.</div></details></div></div></section>' + FINAL)

# ---------- JOURNAL ----------
JOURNAL = (page_hero('Journal','Smart reading, before you start.',
  'Honest, jargon-free guides to straightening your smile, for parents, teens, and grown-ups weighing their options.', ctas=False)
 + '<section class="sec"><div class="wrap"><div data-filter-group class="chips">'
 '<button class="chip active" data-f="all">All</button><button class="chip" data-f="invisalign">Invisalign</button>'
 '<button class="chip" data-f="teen">Teens</button><button class="chip" data-f="adult">Adults</button>'
 '<button class="chip" data-f="kids">Kids</button><button class="chip" data-f="cost">Cost</button></div>'
 '<div class="blog-grid">'
 '<article class="post feat" data-cat="invisalign adult"><div class="thumb"><span class="cat">Invisalign</span></div><div class="pb"><div class="meta">April 2026 · 6 min read</div><h3>Invisalign vs braces: which actually fits your life?</h3><p>A no-spin guide to choosing between clear aligners and braces by lifestyle, budget, and how complex your case really is.</p><span class="more">Read article →</span></div></article>'
 '<article class="post" data-cat="teen"><div class="thumb t2"><span class="cat">Teens</span></div><div class="pb"><div class="meta">March 2026 · 4 min</div><h3>How to keep a teen motivated through treatment.</h3><p>Wear indicators, the progress app, and the small rituals that turn 22 hours a day into a streak they want to keep.</p><span class="more">Read article →</span></div></article>'
 '<article class="post" data-cat="adult"><div class="thumb t3"><span class="cat">Adults</span></div><div class="pb"><div class="meta">March 2026 · 5 min</div><h3>Is 35 too old for braces? (Short answer: no.)</h3><p>Why more adults than ever are straightening their teeth, and how discreet modern options really are.</p><span class="more">Read article →</span></div></article>'
 '<article class="post" data-cat="cost"><div class="thumb t2"><span class="cat">Cost</span></div><div class="pb"><div class="meta">February 2026 · 7 min</div><h3>What orthodontics really costs in 2026.</h3><p>A transparent breakdown of treatment prices, what insurance typically covers, and how $0-down plans work.</p><span class="more">Read article →</span></div></article>'
 '<article class="post" data-cat="kids"><div class="thumb"><span class="cat">Kids</span></div><div class="pb"><div class="meta">February 2026 · 4 min</div><h3>When should my child first see an orthodontist?</h3><p>The age-7 rule, what early treatment can prevent, and why watching is often the right call.</p><span class="more">Read article →</span></div></article>'
 '<article class="post" data-cat="invisalign adult"><div class="thumb t3"><span class="cat">Tech</span></div><div class="pb"><div class="meta">January 2026 · 5 min</div><h3>How a 3D smile preview is made.</h3><p>From a two-minute scan to the simulation that shows your result before you commit to a thing.</p><span class="more">Read article →</span></div></article>'
 '</div></div></section>' + FINAL)

# ---------- REVIEWS ----------
REVIEWSP = (page_hero('Reviews','Nine hundred recommendations.',
  'Verified on Google, in patients’ own words. Filter by treatment to read what your case sounded like.', ctas=False)
 + '<section class="sec"><div class="wrap">'
 '<div class="card-b" style="display:flex;gap:24px;align-items:center;flex-wrap:wrap;margin-bottom:34px">'
 '<div style="text-align:center"><div style="font-family:var(--display);font-weight:800;font-size:3rem;color:var(--forest);line-height:1">4.9</div><div class="stars" style="color:var(--lime);font-size:1.1rem">★★★★★</div></div>'
 '<div><b style="font-family:var(--display);font-size:1.2rem;color:var(--forest)">900 verified reviews</b><p class="muted">Across Google, with a 98% five-star rate. Below is a representative sample.</p></div></div>'
 '<div data-filter-group class="chips"><button class="chip active" data-f="all">All</button>'
 '<button class="chip" data-f="invisalign">Invisalign</button><button class="chip" data-f="teen">Teen</button>'
 '<button class="chip" data-f="braces">Braces</button><button class="chip" data-f="early">Early</button></div>'
 '<div class="rev-grid">' + ''.join(review(*r) for r in REVIEWS) + '</div></div></section>' + FINAL)

# ---------- FINDER PAGE ----------
FINDERP = (page_hero('Treatment Finder','Find your fit in four questions.',
  'No phone call, no email gate. Answer a few quick questions and we will point you to the one or two treatments that suit your life, never just the priciest.', ctas=False)
 + '<section class="sec"><div class="wrap" style="max-width:640px">' + FINDER + '</div></section>'
 '<section class="sec bg-linen"><div class="wrap center"><div class="sec-head center" style="margin-bottom:24px"><h2 style="font-size:clamp(1.6rem,3.5vw,2.2rem)">Want the numbers too?</h2><p>See a real monthly plan after insurance.</p></div>'
 '<a href="calculator.html" class="btn btn-primary">Open the cost calculator →</a></div></section>')

# ---------- CALCULATOR PAGE ----------
CALCP = (page_hero('Cost Calculator','Estimate the cost, honestly.',
  'Pick a treatment, set a payment term, and apply your insurance benefit to see a realistic monthly figure, before you ever call.', ctas=False)
 + '<section class="sec"><div class="wrap" style="max-width:640px">' + CALC + '</div></section>'
 '<section class="sec bg-linen"><div class="wrap center"><div class="sec-head center" style="margin-bottom:24px"><h2 style="font-size:clamp(1.6rem,3.5vw,2.2rem)">Not sure which treatment?</h2><p>Answer four quick questions to find your fit.</p></div>'
 '<a href="finder.html" class="btn btn-primary">Open the treatment finder →</a></div></section>')

# ---------- COMPARE ----------
def _ctd(*cells): return ''.join('<td>'+c+'</td>' for c in cells)
COMPARE = (page_hero('Compare','Every option, side by side.',
  'All six treatments laid out plainly: visibility, time, cost, daily care, and what each one is genuinely best for. No jargon, no sales spin.', ctas=False)
 + '<section class="sec"><div class="wrap"><div class="table-scroll"><table class="compare"><thead><tr>'
 '<th>Treatment</th><th>Best for</th><th>Visibility</th><th>Typical time</th><th>Removable?</th><th>From</th></tr></thead><tbody>'
 '<tr><th>Invisalign Adult</th>' + _ctd('Discreet adult cases','Nearly invisible','6–18 months','Yes','<span class="price-cell">$4,800</span>') + '</tr>'
 '<tr><th>Invisalign Teen</th>' + _ctd('Busy teen lives','Nearly invisible','12–18 months','Yes','<span class="price-cell">$4,500</span>') + '</tr>'
 '<tr><th>Ceramic Braces</th>' + _ctd('Complex, kept low-key','Subtle (clear)','12–24 months','No (fixed)','<span class="price-cell">$4,500</span>') + '</tr>'
 '<tr><th>Metal Braces</th>' + _ctd('Budget &amp; complex cases','Visible','12–24 months','No (fixed)','<span class="price-cell">$3,800</span>') + '</tr>'
 '<tr><th>Early · Phase 1</th>' + _ctd('Guiding ages 7–10','Varies','Phase 1 + monitor','Varies','<span class="price-cell">$2,500</span>') + '</tr>'
 '<tr><th>Retainers</th>' + _ctd('Holding your result','Clear or hidden','Nightly, for life','Clear: yes','<span class="price-cell">$250</span>') + '</tr>'
 '</tbody></table></div>'
 '<p class="muted" style="margin-top:14px;font-size:.9rem">Scroll the table sideways on a phone. Prices are starting points, confirmed at your free scan.</p>'
 '<div style="margin-top:24px;display:flex;gap:10px;flex-wrap:wrap"><a href="finder.html" class="btn btn-primary">Help me choose →</a><a href="calculator.html" class="btn btn-ghost">Estimate the cost</a></div></div></section>' + FINAL)

# ---------- GALLERY ----------
GALLERY = (page_hero('Before &amp; After','Real smiles, no retouching.',
  'Every case is photographed in the same light, in our chair. Drag each slider to watch the change a little momentum makes.', ctas=False)
 + '<section class="sec"><div class="wrap"><div data-filter-group class="chips">'
 '<button class="chip active" data-f="all">All</button><button class="chip" data-f="invisalign">Invisalign</button>'
 '<button class="chip" data-f="braces">Braces</button><button class="chip" data-f="early">Early</button></div>'
 '<div class="ba-cases" style="grid-template-columns:repeat(3,1fr)">'
 + ba_card("Crowding, quietly fixed","Invisalign Adult · 11 months · age 28","invisalign")
 + ba_card("Closing the front gap","Invisalign Adult · 7 months · age 34","invisalign")
 + ba_card("A confident teen smile","Ceramic braces · 16 months · age 14","braces")
 + ba_card("Deep bite corrected","Metal braces · 19 months · age 15","braces")
 + ba_card("Crossbite, guided early","Phase 1 expander · age 8","early")
 + ba_card("Adult relapse, redone","Invisalign Adult · 9 months · age 41","invisalign")
 + '</div></div></section>' + FINAL)

# ---------- SERVICE DETAIL PAGES ----------
J_ADULT = [("Day one","Free smile scan","A two-minute digital scan, no goopy moulds. You see your projected result the same day."),
 ("Within ~1 week","Your plan, in 3D","We refine every move by hand. You approve the finish line before we begin."),
 ("Start day","First aligners","Discreet tooth-coloured attachments go on; you leave with your first trays and a progress app."),
 ("Every 1–2 wks","Quiet progress","Fresh aligners every 1 to 2 weeks. Quick check-ins keep you ahead of schedule."),
 ("Final weeks","Reveal and retain","A short refinement, then a custom retainer to protect your new smile.")]
J_TEEN = [("Day one","Free smile scan","A comfortable digital scan builds the 3D plan and shows the projected result on screen."),
 ("Within ~1 week","Your plan, in 3D","We map every move and set the finish line, with a progress app built for teens."),
 ("Start day","First aligners","Clear aligners with discreet attachments and built-in wear indicators go on."),
 ("Every 1–2 wks","Streak it up","Fresh trays on a schedule, with app reminders that keep wear-time on track."),
 ("Final weeks","Reveal and retain","A short refinement, then a retainer to hold the result for life.")]
J_CERAMIC = [("Day one","Free smile scan","Digital scan and photos map your bite and the exact moves your smile needs."),
 ("A clear plan","Costed up front","We show you the path, the timeline, and the all-in price before anything goes on."),
 ("Fitting day","Brackets on","Clear ceramic brackets and tooth-coloured wires go on gently, usually about an hour."),
 ("Every few wks","Adjustments","Short visits guide progress; keep them invisible or pick tie colours."),
 ("Final weeks","Reveal and retain","Braces off, smile on, and a custom retainer to keep it that way.")]
J_METAL = [("Day one","Free smile scan","Digital scan and photos map the bite and the full treatment plan."),
 ("A clear plan","Costed up front","The path, the timeline, and the all-in price, agreed before we start."),
 ("Fitting day","Brackets on","Modern low-profile metal brackets go on gently, usually about an hour."),
 ("Every few wks","Adjustments","Short, efficient visits move teeth quickly and predictably."),
 ("Final weeks","Reveal and retain","Braces off and a custom retainer to protect the result.")]
J_EARLY = [("Day one","Free growth check","A relaxed first visit and digital scan to see how the jaw and adult teeth are developing."),
 ("Watch or act","Honest timing","Often the answer is simply to monitor, free of charge. We treat only when timing truly helps."),
 ("Phase 1","Gentle guidance","A short course of an expander or partial braces creates space and guides growth."),
 ("Rest","Monitor","A break while the remaining adult teeth arrive, with free check-ups along the way."),
 ("Later","Phase 2 if needed","Any later treatment is usually shorter and simpler thanks to the early groundwork.")]
J_RET = [("After treatment","Custom scan","We scan your finished smile and make retainers fitted to the millimetre."),
 ("Choose","Clear or bonded","A removable clear retainer, a discreet bonded wire, or both, to suit your life."),
 ("Nightly","Simple routine","Most patients wear a clear retainer at night. Rinse, wear, store, repeat."),
 ("Check-ins","Quick reviews","Occasional reviews make sure everything is holding beautifully."),
 ("For life","Protect it","Replace or refresh anytime. Your result is worth keeping.")]

SVC_ADULT = service_detail("01","Clear Aligners","Invisalign for adults",
 "Clear aligners, planned in 3D and fitted to the millimetre. Straighten discreetly while you work, present, and live your life. Most adult cases finish in well under a year, and nobody has to know unless you tell them.",
 "from $4,800","or ~$140/mo · 6–18 months",("22 hrs","wear per day"),("~6 wk","between check-ins"),
 J_ADULT,"Small, weekly moves you barely notice, until the day you catch your new smile in a window and stop.")
SVC_TEEN = service_detail("02","Clear Aligners","Invisalign for teens",
 "Clear aligners built for teen life. Discreet, removable for sport and big days, with wear indicators and a progress app that turns 22 hours a day into a streak they want to keep.",
 "from $4,500","or ~$130/mo · 12–18 months",("Wear","indicators"),("App","progress tracking"),
 J_TEEN,"Made for real teenage schedules, with just enough gamification to keep momentum going.")
SVC_CERAMIC = service_detail("03","Braces","Clear ceramic braces",
 "Tooth-coloured brackets that quietly blend in while they do the heavy lifting. All the predictable power of braces for complex cases, far harder for anyone to spot across a meeting room.",
 "from $4,500","or ~$135/mo · 12–24 months",("Tooth","coloured"),("Fixed","no compliance"),
 J_CERAMIC,"Fixed to your teeth and always working, ideal when a case needs more control than aligners can give, without the metal look.")
SVC_METAL = service_detail("04","Braces","Modern metal braces",
 "The most efficient, most affordable route to a great result. Low-profile modern brackets move teeth quickly and predictably, and handle the most complex cases with ease.",
 "from $3,800","or ~$110/mo · 12–24 months",("Strong","most efficient"),("Fixed","no compliance"),
 J_METAL,"Proven, powerful, and budget-friendly, the workhorse that gets complex smiles where they need to go.")
SVC_EARLY = service_detail("05","Growing Smiles","Early treatment (Phase 1)",
 "For children roughly 7 to 10, a little guidance at the right moment can make all the difference. We gently steer growing jaws and incoming teeth, often making any later treatment shorter, simpler, and less expensive.",
 "from $2,500","Phase 1 · Ages 7–10",("Shorter","phase 2 later"),("Free","growth check-ups"),
 J_EARLY,"The goal is not a perfect smile today, it is creating room and balance now so the permanent smile has the easiest possible path.")
SVC_RET = service_detail("06","Retention","Retainers and retention",
 "The result is worth protecting. Custom retainers, clear or bonded, keep your smile exactly where we finished it, for life. New patients and past-treatment touch-ups both welcome.",
 "from $250","per arch",("Nightly","wear for life"),("Clear","or bonded"),
 J_RET,"Straightening is only half the job. Retention is how a great result stays a great result.")

# ---------- registry ----------
PAGES = {
 "home": ("index.html","", "Arc Orthodontics — Braces &amp; Invisalign in Austin, TX",
   "Arc Orthodontics in Austin, TX. Braces and Invisalign for teens and adults. See your future smile with a free 3D smile scan, get an honest price, and start with $0 down on 0% plans.", HOME),
 "services": ("services.html","services","Treatments — Arc Orthodontics",
   "Six specialist orthodontic treatments in Austin: Invisalign for adults and teens, ceramic and metal braces, early treatment, and retainers. Clear pricing from $250.", SERVICES),
 "new-patients": ("new-patients.html","","New Patients — Arc Orthodontics",
   "Your first visit at Arc Orthodontics: a free 30-minute smile scan, a 3D preview of your future smile, paperless intake, and an honest plan with pricing. No pressure.", NEWPAT),
 "about": ("about.html","about","The Studio — Arc Orthodontics",
   "Meet the Arc Orthodontics team in Austin, TX. Specialist-led, tech-forward, human-first orthodontics with 12,000+ smiles moved and a 4.9-star rating across 900 reviews.", ABOUT),
 "contact": ("contact.html","contact","Book a Visit — Arc Orthodontics",
   "Book your free smile scan at Arc Orthodontics, Austin TX. 240 Linden Way, Studio 3. Open Mon–Sat with free parking. Call (512) 555-0148 or reserve online.", CONTACT),
 "plan": ("plan.html","plan","Plan Your Treatment — Arc Orthodontics",
   "Find the right treatment and price it in two steps. A four-question treatment finder and a live cost calculator with $0-down, 0% monthly plans. No phone call required.", PLAN),
 "journey": ("journey.html","","The Journey — Arc Orthodontics",
   "From your first free scan to a retainer for life, see every step of orthodontic treatment at Arc Orthodontics in Austin, mapped out clearly.", JOURNEY),
 "stories": ("stories.html","stories","Smile Stories — Arc Orthodontics",
   "Real before-and-afters and 900 verified reviews from Arc Orthodontics patients in Austin, TX. Drag the sliders and read the words behind the smiles.", STORIES),
 "insurance": ("insurance.html","insurance","Insurance &amp; Payment — Arc Orthodontics",
   "$0 down, 0% interest plans, and we file your insurance for you. In-network with most major carriers, plus the $29/mo Arc Smile Club for patients without coverage.", INSURANCE),
 "journal": ("journal.html","journal","Journal — Arc Orthodontics",
   "Honest, jargon-free guides to braces and Invisalign for parents, teens, and adults: choosing a treatment, what it costs, and staying motivated.", JOURNAL),
 "reviews": ("reviews.html","","Reviews — Arc Orthodontics",
   "900 verified Google reviews of Arc Orthodontics in Austin, TX, with a 4.9-star average. Filter by treatment and read patients in their own words.", REVIEWSP),
 "finder": ("finder.html","","Treatment Finder — Arc Orthodontics",
   "Answer four quick questions and we will point you to the one or two orthodontic treatments that fit your life. No phone call, no email gate.", FINDERP),
 "calculator": ("calculator.html","","Cost Calculator — Arc Orthodontics",
   "Estimate your orthodontic treatment cost in Austin. Pick a treatment, set a term, apply your insurance benefit, and see a real $0-down monthly plan.", CALCP),
 "compare": ("compare.html","","Compare Treatments — Arc Orthodontics",
   "Compare Invisalign, ceramic and metal braces, early treatment, and retainers side by side: visibility, time, cost, and daily care. No jargon.", COMPARE),
 "gallery": ("gallery.html","","Before &amp; After — Arc Orthodontics",
   "Real, unretouched before-and-after smiles from Arc Orthodontics patients in Austin. Drag each slider to watch the change.", GALLERY),
 "s-adult": ("service-invisalign-adult.html","","Invisalign for Adults — Arc Orthodontics",
   "Invisalign for adults in Austin from $4,800 (about $140/mo). Clear, removable aligners planned in 3D. Most cases finish in under a year. Free smile scan.", SVC_ADULT),
 "s-teen": ("service-invisalign-teen.html","","Invisalign for Teens — Arc Orthodontics",
   "Invisalign for teens in Austin from $4,500 (about $130/mo). Discreet aligners with wear indicators and a progress app. Book a free smile scan.", SVC_TEEN),
 "s-ceramic": ("service-ceramic.html","","Clear Ceramic Braces — Arc Orthodontics",
   "Clear ceramic braces in Austin from $4,500 (about $135/mo). Tooth-coloured brackets with the full power of braces for complex cases. Free smile scan.", SVC_CERAMIC),
 "s-metal": ("service-metal.html","","Modern Metal Braces — Arc Orthodontics",
   "Modern metal braces in Austin from $3,800 (about $110/mo). The most efficient, budget-friendly route for complex cases. Book a free smile scan.", SVC_METAL),
 "s-early": ("service-early.html","","Early Treatment (Phase 1) — Arc Orthodontics",
   "Early orthodontic treatment for children ages 7–10 in Austin from $2,500. Gentle Phase 1 guidance with free growth check-ups. Book a free growth check.", SVC_EARLY),
 "s-ret": ("service-retainers.html","","Retainers &amp; Retention — Arc Orthodontics",
   "Custom retainers in Austin from $250 per arch, clear or bonded. Protect your orthodontic result for life. New patients and touch-ups welcome.", SVC_RET),
}
