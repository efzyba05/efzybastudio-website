from shared import page

# ============================ PORTFOLIO ============================
projects = [
 ("case-fundjoy.html","project-fundjoy.jpg","Web Design · Non-profit","FundJoy — Empowering Fundraising & Public Speaking","A vibrant platform that helps organisations raise funds and amplify voices on stage.","reveal-l"),
 ("case-hebe.html","project-hebe.jpg","Web Design · CleanTech","Hebe Network — Transforming Renewable Energy Storage","A credibility-building site for the future of clean energy storage.","reveal-r"),
 ("case-brightsites.html","project-brightsites.jpg","Web Design · Framer","BrightSites — Website Made in Framer","A bold, conversion-led agency site built entirely in Framer.","reveal-l"),
 ("case-designcube.html","project-designcube.jpg","Web Design · Framer","DesignCube — Framer Website","A playful 3D-flavoured studio site with motion at its core.","reveal-r"),
 ("case-healthwell.html","project-healthwell.jpg","Web Design · Health","HealthWell — Website in Framer","A calm, trustworthy wellness platform with seamless appointment flows.","reveal-l"),
 ("case-thelist.html","project-thelist.jpg","Web Design · Directory","Thelist — Framer Website","An elegant, minimal curation platform with editorial polish.","reveal-r"),
]

cards = ""
for href,img,cat,title,desc,rev in projects:
    cards += f"""
      <a class="work-card {rev}" href="{href}">
        <div class="thumb"><img src="assets/img/{img}" alt="{title}" loading="lazy"></div>
        <div class="meta"><div><span class="cat">{cat}</span><h3>{title}</h3><p style="color:var(--muted);font-size:.88rem;margin-top:6px">{desc}</p></div><span class="go">→</span></div>
      </a>"""

portfolio_body = f"""
<main>
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; <b>Portfolio</b></p>
    <h1>Work that <span class="grad">works</span></h1>
    <p>Case studies and launches across non-profit, clean energy, health, SaaS and creative industries.</p>
  </div>
</section>

<section style="padding-top:20px">
  <div class="container">
    <div class="work-grid">{cards}
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="cta-band reveal-zoom">
      <span class="eyebrow">Your project next?</span>
      <h2>Let's add your brand to this list</h2>
      <p>Every project starts with a conversation. Tell us your vision and we'll show you what's possible.</p>
      <a href="contact.html" class="btn btn-primary">Start a Project <span class="arr">→</span></a>
    </div>
  </div>
</section>
</main>
"""

open("../portfolio.html","w").write(page("portfolio",
  "Portfolio & Case Studies — Efzyba Studio",
  "Explore Efzyba Studio's portfolio: FundJoy, Hebe Network, BrightSites, DesignCube, HealthWell and Thelist — web design case studies across non-profit, energy, health and SaaS.",
  "web design portfolio, Framer case study, agency case studies, website examples, Efzyba Studio work",
  portfolio_body))
print("portfolio.html written")

# ============================ CASE STUDY TEMPLATE ============================
def case_study(fname, title, cat, intro, img, stats, challenge, solution, results, client, year, platform, services_list, next_href, next_title):
    stats_html = "".join(f'<div class="cs-stat reveal d{i+1}"><b>{v}</b><span>{k}</span></div>' for i,(k,v) in enumerate(stats))
    services_html = "<br>".join(services_list)
    body = f"""
<main>
<section class="cs-hero">
  <div class="container">
    <p class="crumbs reveal"><a href="index.html">Home</a> &nbsp;/&nbsp; <a href="portfolio.html">Portfolio</a> &nbsp;/&nbsp; <b>{title.split('—')[0].strip()}</b></p>
    <span class="cat" style="display:block;margin-top:26px" >{cat}</span>
    <h1>{title}</h1>
    <p style="color:var(--muted);max-width:640px;font-size:1.1rem">{intro}</p>
    <div class="cs-stats">{stats_html}</div>
    <div class="article-cover reveal-zoom" style="margin-top:10px"><img src="assets/img/{img}" alt="{title} website design by Efzyba Studio"></div>
    <div class="cs-body">
      <div class="reveal">
        <h2>The Challenge</h2>
        <p>{challenge}</p>
        <h2>Our Solution</h2>
        <p>{solution}</p>
        <h2>The Results</h2>
        <p>{results}</p>
      </div>
      <aside class="cs-side reveal-r">
        <div class="row"><h4>Client</h4><p>{client}</p></div>
        <div class="row"><h4>Year</h4><p>{year}</p></div>
        <div class="row"><h4>Platform</h4><p>{platform}</p></div>
        <div class="row"><h4>Services</h4><p>{services_html}</p></div>
        <a href="contact.html" class="btn btn-primary btn-sm" style="width:100%;justify-content:center;margin-top:6px">Start a Similar Project</a>
      </aside>
    </div>
  </div>
</section>

<section style="padding-top:30px">
  <div class="container">
    <div class="cta-band reveal-zoom">
      <span class="eyebrow">Keep exploring</span>
      <h2>Next case study</h2>
      <p>{next_title}</p>
      <a href="{next_href}" class="btn btn-primary">View Case Study <span class="arr">→</span></a>
    </div>
  </div>
</section>
</main>
"""
    open("../"+fname,"w").write(page("portfolio",
      f"{title} — Case Study | Efzyba Studio",
      intro, "case study, web design, " + cat, body))
    print(fname, "written")

case_study("case-fundjoy.html",
  "FundJoy — Empowering Fundraising & Public Speaking","Web Design · Non-profit",
  "FundJoy needed a digital home that could inspire donors and empower public speakers — we delivered a warm, conversion-led platform that does both.",
  "project-fundjoy.jpg",
  [("Increase in donations","+64%"),("Bounce rate drop","-38%"),("Pages designed","12"),("Launch time","3 wks")],
  "FundJoy's mission spans two worlds — fundraising and public speaking education — and their previous site told neither story well. Donation flows were buried, event information was scattered, and the brand's infectious energy was lost in a generic template. They needed a single experience that could move visitors to donate, register and speak.",
  "We started with audience research, mapping two distinct user journeys: donors seeking trust and impact, and aspiring speakers seeking opportunity. The new design leads with bold storytelling, real photography and progress-driven donation cards that make giving feel tangible. A restructured information architecture brings events, training and impact reports within two clicks of anywhere. Built responsively with SEO-ready structure and a CMS so the FundJoy team publishes updates themselves.",
  "Within three months of launch, online donations rose 64%, bounce rate dropped 38% and event registrations doubled. FundJoy's team now manages all content in-house, and the platform has become the centrepiece of their digital campaigns.",
  "FundJoy","2025","Framer + CMS",["Web Design","UX Research","SEO","CMS Integration"],
  "case-hebe.html","Hebe Network — Transforming Renewable Energy Storage")

case_study("case-hebe.html",
  "Hebe Network — Transforming Renewable Energy Storage","Web Design · CleanTech",
  "A credibility-first website for a renewable energy innovator — translating complex storage technology into a story investors and partners instantly understand.",
  "project-hebe.jpg",
  [("Qualified leads","+85%"),("Avg. session time","3.4 min"),("Pages designed","10"),("Launch time","4 wks")],
  "Hebe Network is pioneering renewable energy storage, but their technology story was complex and their old website read like a whitepaper. Investors, partners and journalists needed to grasp the value proposition in seconds — not paragraphs. The brand also needed visual gravity to stand alongside established energy players.",
  "We distilled the technology narrative into a clear three-act story: the problem with renewable intermittency, the Hebe storage solution, and the measurable impact. Custom data-styled visuals and dashboard-inspired UI elements communicate technical credibility without jargon. A dark, premium aesthetic with energetic accents positions Hebe as both serious and forward-looking. Structured data and technical SEO make the site discoverable for high-intent clean energy searches.",
  "Qualified partnership enquiries grew 85% quarter-over-quarter, average session time reached 3.4 minutes, and the site now anchors Hebe's investor communications. The team reports that meetings start further along — because prospects arrive already understanding the technology.",
  "Hebe Network","2025","Framer",["Web Design","Brand Identity","Technical SEO","Copywriting"],
  "case-brightsites.html","BrightSites — Website Made in Framer")

case_study("case-brightsites.html",
  "BrightSites — Website Made in Framer","Web Design · Framer",
  "A bold, high-energy agency website built end-to-end in Framer — proving that no-code can look anything but generic.",
  "project-brightsites.jpg",
  [("Build time","10 days"),("PageSpeed score","97"),("Conversion lift","+41%"),("Pages","8")],
  "BrightSites wanted an agency website that practised what it preached: fast, bold and impossible to ignore. The catch — they needed it live in under two weeks to support a launch campaign, with zero compromise on motion design or performance.",
  "Framer was the obvious weapon. We designed directly in the canvas, building a vivid identity around bold typography, geometric shapes and confident colour. Scroll-triggered animations and micro-interactions give the site energy without hurting performance — it ships with a 97 PageSpeed score. The portfolio grid, testimonials and pricing all run on Framer CMS for instant updates.",
  "Delivered in ten days, the site lifted demo-call conversions by 41% in the first month. BrightSites now uses it as their primary sales asset, and the build became a reference example of what fast, no-code-first delivery can achieve.",
  "BrightSites","2024","Framer",["Web Design","Motion Design","CMS","Performance"],
  "case-designcube.html","DesignCube — Framer Website")

case_study("case-designcube.html",
  "DesignCube — Framer Website","Web Design · Framer",
  "A playful, 3D-flavoured website for a creative studio — where motion design carries the brand personality.",
  "project-designcube.jpg",
  [("Engagement rate","+58%"),("Demo requests","2.3×"),("Pages","7"),("Launch time","2 wks")],
  "DesignCube's brand is built on dimensionality and play, but their previous site was flat in every sense. They needed a digital experience that felt like stepping inside their creative process — interactive, layered and fun — while remaining fast and easy to navigate.",
  "We built a motion-first experience in Framer: a 3D cube hero that responds to the cursor, layered parallax sections, and service cards that tilt and glow on hover. A purple-to-blue gradient world gives the brand a distinctive signature, while careful information hierarchy keeps the playfulness from ever getting in the way of the message.",
  "Engagement rate rose 58% and demo requests grew 2.3× within two months. The site has been shared widely in design communities, generating inbound leads on its own — exactly the kind of self-marketing asset a creative studio needs.",
  "DesignCube","2024","Framer",["Web Design","3D & Motion","UI Design","Prototyping"],
  "case-healthwell.html","HealthWell — Website in Framer")

case_study("case-healthwell.html",
  "HealthWell — Website in Framer","Web Design · Health",
  "A calm, trustworthy wellness platform that makes booking care feel as good as receiving it.",
  "project-healthwell.jpg",
  [("Online bookings","+72%"),("Mobile traffic","68%"),("Pages","9"),("Launch time","3 wks")],
  "HealthWell's patients are often stressed when they arrive online — the last thing they need is a confusing website. The old site had buried booking flows, inconsistent information and no mobile optimisation, despite most patients browsing on phones.",
  "We designed for calm: a soft, breathable palette, generous whitespace, friendly photography and rounded, reassuring UI. The appointment booking widget sits one tap away from every page. Service pages answer the questions patients actually ask, structured for both readability and health-related search queries. The fully responsive build prioritises the 68% of visitors on mobile.",
  "Online bookings rose 72% in the first quarter, call-centre volume dropped as patients self-served, and patient feedback specifically praised how easy the new site is to use. HealthWell now treats the website as a core part of the care experience.",
  "HealthWell","2024","Framer",["Web Design","UX Design","Accessibility","SEO"],
  "case-thelist.html","Thelist — Framer Website")

case_study("case-thelist.html",
  "Thelist — Framer Website","Web Design · Directory",
  "An elegant, minimal curation platform with editorial polish — designed to make every listing feel hand-picked.",
  "project-thelist.jpg",
  [("Time on site","+47%"),("Listings indexed","500+"),("Pages","6 + CMS"),("Launch time","2 wks")],
  "Thelist curates the best of its niche, but its previous design made premium listings look like classified ads. The platform needed editorial sophistication — a design language that signals taste — plus a scalable CMS structure to handle hundreds of listings without manual page-building.",
  "We drew from editorial design: an elegant serif voice, a disciplined black-and-cream palette, and listing cards with generous imagery and typographic hierarchy. Under the hood, a Framer CMS architecture powers categories, tags and detail pages automatically — add a listing, and the site does the rest. Structured data markup helps each listing earn rich results in search.",
  "Average time on site rose 47%, over 500 listings were indexed by Google within weeks, and partners began requesting placement specifically because of how premium the platform looks. Thelist now scales content without touching design.",
  "Thelist","2024","Framer + CMS",["Web Design","CMS Architecture","Editorial Design","SEO"],
  "case-fundjoy.html","FundJoy — Empowering Fundraising & Public Speaking")
