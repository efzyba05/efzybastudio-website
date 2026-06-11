from shared import page

body = """
<main>
<!-- ================= HERO ================= -->
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="eyebrow">Web Design &amp; Digital Marketing · Nigeria → Worldwide</span>
      <h1>We design <span class="grad">digital experiences</span> that feel like the <span class="outline">future</span></h1>
      <p class="lead">Efzyba Studio is a full-stack creative agency — websites, e-commerce, UI/UX, data analytics and growth marketing — built to turn your boldest ideas into measurable results.</p>
      <div class="hero-actions">
        <a href="contact.html" class="btn btn-primary">Start a Project <span class="arr">→</span></a>
        <a href="portfolio.html" class="btn btn-ghost">View Our Work</a>
      </div>
      <div class="hero-stats">
        <div class="hstat"><span class="num" data-count="80" data-suffix="+">0</span><span class="lbl">Happy Clients</span></div>
        <div class="hstat"><span class="num" data-count="120" data-suffix="+">0</span><span class="lbl">Projects Shipped</span></div>
        <div class="hstat"><span class="num" data-count="6" data-suffix="+">0</span><span class="lbl">Years Experience</span></div>
      </div>
    </div>
    <div class="hero-visual">
      <canvas id="torusCanvas" aria-hidden="true"></canvas>
      <div class="hero-logo-3d"><img src="assets/img/icon.png" alt="Efzyba Studio emblem"></div>
      <div class="float-chip fc-1"><span class="ic">🚀</span> Web Design</div>
      <div class="float-chip fc-2"><span class="ic">📊</span> Data Analytics</div>
      <div class="float-chip fc-3"><span class="ic">🎨</span> UI/UX Design</div>
      <div class="float-chip fc-4"><span class="ic">📈</span> SEO &amp; Marketing</div>
      <div class="shape3d cube3d sh-1"><i></i><i></i><i></i><i></i><i></i><i></i></div>
      <div class="shape3d cube3d sh-2"><i></i><i></i><i></i><i></i><i></i><i></i></div>
    </div>
  </div>
  <div class="scroll-hint"><div class="mouse"><i></i></div>scroll</div>
</section>

<!-- ================= MARQUEE ================= -->
<div class="marquee" aria-hidden="true">
  <div class="marquee-track">
    <span>Web Design <em>E-commerce</em> UI/UX <em>SEO</em> Branding <em>Data Analytics</em> Framer <em>WordPress</em> Webflow <em>Shopify</em></span>
    <span>Web Design <em>E-commerce</em> UI/UX <em>SEO</em> Branding <em>Data Analytics</em> Framer <em>WordPress</em> Webflow <em>Shopify</em></span>
  </div>
</div>

<!-- ================= SERVICES PREVIEW ================= -->
<section id="services">
  <div class="container">
    <div class="sec-head split reveal">
      <div>
        <span class="eyebrow">What We Do</span>
        <h2>Services engineered for <span class="grad">growth</span></h2>
        <p>From first wireframe to launch day and beyond — one studio, every digital capability you need.</p>
      </div>
      <a href="services.html" class="btn btn-ghost">All Services <span class="arr">→</span></a>
    </div>
    <div class="cards-grid">
      <article class="card tilt reveal d1">
        <div class="icon">🖥️</div>
        <h3>Website Design &amp; Development</h3>
        <p>Beautiful, conversion-focused websites built with deep UX research, intuitive navigation and modern front-end technology that guides visitors to action.</p>
        <div class="tags"><span class="tag">Framer</span><span class="tag">WordPress</span><span class="tag">Webflow</span></div>
        <a class="card-link" href="services.html">Learn more <span class="arr">→</span></a>
      </article>
      <article class="card tilt reveal d2">
        <div class="icon">🛒</div>
        <h3>E-commerce Websites</h3>
        <p>Seamless online stores that showcase your products beautifully, with intuitive browsing, secure payments and streamlined checkouts that maximise sales.</p>
        <div class="tags"><span class="tag">Shopify</span><span class="tag">WooCommerce</span></div>
        <a class="card-link" href="services.html">Learn more <span class="arr">→</span></a>
      </article>
      <article class="card tilt reveal d3">
        <div class="icon">🎯</div>
        <h3>Landing Pages</h3>
        <p>High-impact pages laser-focused on one goal: converting. Compelling headlines, captivating visuals and optimised CTAs that turn visitors into customers.</p>
        <div class="tags"><span class="tag">CRO</span><span class="tag">A/B Testing</span></div>
        <a class="card-link" href="services.html">Learn more <span class="arr">→</span></a>
      </article>
      <article class="card tilt reveal d1">
        <div class="icon">🧪</div>
        <h3>UI/UX &amp; Prototyping</h3>
        <p>Interactive prototypes that let you experience user flows before a line of code is written — plus research and usability testing that puts users first.</p>
        <div class="tags"><span class="tag">Figma</span><span class="tag">Framer</span></div>
        <a class="card-link" href="services.html">Learn more <span class="arr">→</span></a>
      </article>
      <article class="card tilt reveal d2">
        <div class="icon">📈</div>
        <h3>SEO &amp; Digital Marketing</h3>
        <p>Get found by the right audience. On-page SEO, SEM, email marketing and social strategies that drive measurable, compounding organic growth.</p>
        <div class="tags"><span class="tag">SEO</span><span class="tag">Email</span><span class="tag">SEM</span></div>
        <a class="card-link" href="services.html">Learn more <span class="arr">→</span></a>
      </article>
      <article class="card tilt reveal d3">
        <div class="icon">📊</div>
        <h3>Data Analytics</h3>
        <p>Turn raw numbers into decisions. Dashboards, reporting and insight that reveal what your customers want and where your next opportunity lives.</p>
        <div class="tags"><span class="tag">Analytics</span><span class="tag">Dashboards</span></div>
        <a class="card-link" href="services.html">Learn more <span class="arr">→</span></a>
      </article>
    </div>
  </div>
</section>

<!-- ================= PORTFOLIO PREVIEW ================= -->
<section id="work" style="background:linear-gradient(180deg,transparent,rgba(23,16,8,.5),transparent)">
  <div class="container">
    <div class="sec-head split reveal">
      <div>
        <span class="eyebrow">Selected Work</span>
        <h2>Projects we're <span class="grad">proud of</span></h2>
        <p>A snapshot of recent launches across web design, SaaS, energy, health and non-profit.</p>
      </div>
      <a href="portfolio.html" class="btn btn-ghost">Full Portfolio <span class="arr">→</span></a>
    </div>
    <div class="work-grid">
      <a class="work-card reveal-l" href="case-fundjoy.html">
        <div class="thumb"><img src="assets/img/project-fundjoy.jpg" alt="FundJoy fundraising platform website" loading="lazy"></div>
        <div class="meta"><div><span class="cat">Web Design · Non-profit</span><h3>FundJoy — Fundraising &amp; Public Speaking</h3></div><span class="go">→</span></div>
      </a>
      <a class="work-card reveal-r" href="case-hebe.html">
        <div class="thumb"><img src="assets/img/project-hebe.jpg" alt="Hebe Network renewable energy website" loading="lazy"></div>
        <div class="meta"><div><span class="cat">Web Design · CleanTech</span><h3>Hebe Network — Renewable Energy Storage</h3></div><span class="go">→</span></div>
      </a>
      <a class="work-card reveal-l" href="portfolio.html">
        <div class="thumb"><img src="assets/img/project-brightsites.jpg" alt="BrightSites Framer website" loading="lazy"></div>
        <div class="meta"><div><span class="cat">Web Design · Framer</span><h3>BrightSites — Agency Website in Framer</h3></div><span class="go">→</span></div>
      </a>
      <a class="work-card reveal-r" href="portfolio.html">
        <div class="thumb"><img src="assets/img/project-healthwell.jpg" alt="HealthWell website" loading="lazy"></div>
        <div class="meta"><div><span class="cat">Web Design · Health</span><h3>HealthWell — Wellness Platform in Framer</h3></div><span class="go">→</span></div>
      </a>
    </div>
  </div>
</section>

<!-- ================= PROCESS ================= -->
<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">How We Work</span>
      <h2>From idea to <span class="grad">launch</span> in four moves</h2>
    </div>
    <div class="process">
      <div class="p-step reveal d1"><h4>Discover</h4><p>We dig deep into your audience, goals and market to define a strategy that wins before design begins.</p></div>
      <div class="p-step reveal d2"><h4>Design</h4><p>Interactive prototypes in Figma &amp; Framer bring the experience to life so you can feel it before we build it.</p></div>
      <div class="p-step reveal d3"><h4>Build</h4><p>Pixel-perfect, responsive, accessible and SEO-ready development across Framer, WordPress, Webflow and Shopify.</p></div>
      <div class="p-step reveal d4"><h4>Grow</h4><p>Launch is just day one. Analytics, SEO, content and ongoing care keep your site compounding results.</p></div>
    </div>
  </div>
</section>

<!-- ================= TEAM PREVIEW ================= -->
<section style="background:linear-gradient(180deg,transparent,rgba(23,16,8,.5),transparent)">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">The Crew</span>
      <h2>Meet the minds behind <span class="grad">Efzyba</span></h2>
      <p>A compact, senior team across Lagos and the UK — design, data, experience and operations under one roof.</p>
    </div>
    <div class="team-grid">
      <div class="card tilt team-card reveal-zoom d1">
        <div class="ph"><img src="assets/img/team-emmanuel.jpg" alt="Emmanuel Akinola — Founder of Efzyba Studio"></div>
        <h3>Emmanuel Akinola</h3><span class="role">Founder · Web Designer &amp; Digital Marketer</span>
        <p>MBA in International Digital Marketing &amp; Business Transformation, Rome Business School.</p>
      </div>
      <div class="card tilt team-card reveal-zoom d2">
        <div class="ph"><img src="assets/img/team-victor.png" alt="Victor Akinola — UI/UX Designer"></div>
        <h3>Victor Akinola</h3><span class="role">UI/UX Designer</span>
        <p>Crafts intuitive interfaces and prototypes that make complex products feel effortless.</p>
      </div>
      <div class="card tilt team-card reveal-zoom d3">
        <div class="ph"><img src="assets/img/team-mayokun.png" alt="Mayokun Oluwajuyigbe — Data Analyst"></div>
        <h3>Mayokun Oluwajuyigbe</h3><span class="role">Data Analyst</span>
        <p>Transforms raw data into dashboards and insights that power smarter decisions.</p>
      </div>
      <div class="card tilt team-card reveal-zoom d4">
        <div class="ph"><img src="assets/img/team-loveth.png" alt="Loveth Toluwalope — Virtual Assistant"></div>
        <h3>Loveth Toluwalope</h3><span class="role">Virtual Assistant <span class="flag">· UK based</span></span>
        <p>Keeps projects, clients and communications running smoothly across time zones.</p>
      </div>
    </div>
  </div>
</section>

<!-- ================= TESTIMONIALS ================= -->
<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Social Proof</span>
      <h2>What clients <span class="grad">say about us</span></h2>
    </div>
    <div class="testi-grid">
      <div class="card tilt testi reveal d1">
        <div class="stars">★★★★★</div>
        <blockquote>"Emmanuel's design transformed our website! It's not just gorgeous, but incredibly user-friendly too. We've seen a huge jump in leads since launch, and customers love the easy navigation."</blockquote>
        <div class="who"><div class="av">SJ</div><div><b>Sarah Jones</b><span>Marketing Manager, Green Earth Solar</span></div></div>
      </div>
      <div class="card tilt testi reveal d2">
        <div class="stars">★★★★★</div>
        <blockquote>"Working with Emmanuel was a dream. He took time to understand our business and audience, and the website perfectly reflects our brand identity. The ongoing support gives us real peace of mind."</blockquote>
        <div class="who"><div class="av">DL</div><div><b>David Lee</b><span>CEO, Technovation Inc.</span></div></div>
      </div>
      <div class="card tilt testi reveal d3">
        <div class="stars">★★★★★</div>
        <blockquote>"As a small business owner I was nervous about a professional website, but the process was affordable and stress-free. I got a beautiful site that showcases my artwork perfectly."</blockquote>
        <div class="who"><div class="av">EG</div><div><b>Emily Garcia</b><span>Founder, The Painted Palette</span></div></div>
      </div>
    </div>
  </div>
</section>

<!-- ================= BLOG PREVIEW ================= -->
<section style="background:linear-gradient(180deg,transparent,rgba(23,16,8,.5),transparent)">
  <div class="container">
    <div class="sec-head split reveal">
      <div>
        <span class="eyebrow">Insights</span>
        <h2>Latest from the <span class="grad">blog</span></h2>
        <p>SEO-rich guides on web design, no-code, data and digital growth.</p>
      </div>
      <a href="blog.html" class="btn btn-ghost">All Articles <span class="arr">→</span></a>
    </div>
    <div class="blog-grid">
      <a class="blog-card reveal d1" href="blog-seo-small-business.html">
        <div class="thumb"><img src="assets/img/blog-seo.jpg" alt="SEO strategy illustration" loading="lazy"></div>
        <div class="body">
          <div class="meta"><span>SEO</span><span>8 min read</span></div>
          <h3>SEO for Small Businesses in 2026: The Complete Beginner's Playbook</h3>
          <p>Everything you need to rank higher on Google — keywords, on-page SEO, local search and link building, explained simply.</p>
          <span class="read">Read article →</span>
        </div>
      </a>
      <a class="blog-card reveal d2" href="blog-nocode-vs-code.html">
        <div class="thumb"><img src="assets/img/blog-nocode.jpg" alt="No-code website building illustration" loading="lazy"></div>
        <div class="body">
          <div class="meta"><span>Web Design</span><span>7 min read</span></div>
          <h3>No-Code vs. Custom Code in 2026: Which Is Right for Your Website?</h3>
          <p>Framer, Webflow, WordPress or custom development? A practical framework for choosing the right build for your budget and goals.</p>
          <span class="read">Read article →</span>
        </div>
      </a>
      <a class="blog-card reveal d3" href="blog-data-analytics.html">
        <div class="thumb"><img src="assets/img/blog-data.jpg" alt="Data analytics dashboards illustration" loading="lazy"></div>
        <div class="body">
          <div class="meta"><span>Data</span><span>6 min read</span></div>
          <h3>Data Analytics for Small Businesses: Turn Numbers into Revenue</h3>
          <p>You don't need a data science team to make data-driven decisions. Here's how small teams use analytics to grow faster.</p>
          <span class="read">Read article →</span>
        </div>
      </a>
    </div>
  </div>
</section>

<!-- ================= SEO CONTENT BLOCK ================= -->
<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Why Efzyba</span>
      <h2>Nigeria's forward-thinking <span class="grad">web design &amp; digital marketing</span> agency</h2>
    </div>
    <div class="cards-grid reveal">
      <article class="card tilt">
        <div class="icon">🇳🇬</div>
        <h3>Built in Nigeria, trusted worldwide</h3>
        <p>From our base in Lagos — with UK-based operations support — Efzyba Studio serves startups, SMEs and enterprises across Nigeria, Africa, Europe and beyond. Local insight, global standards.</p>
      </article>
      <article class="card tilt">
        <div class="icon">🏆</div>
        <h3>Results, not just websites</h3>
        <p>80+ happy clients and 120+ launches across Framer, WordPress, Webflow and Shopify. Our case studies show measurable outcomes: +64% donations, +85% qualified leads, +72% bookings.</p>
      </article>
      <article class="card tilt">
        <div class="icon">🧠</div>
        <h3>Strategy-grade marketing</h3>
        <p>Led by founder Emmanuel Akinola (MBA, International Digital Marketing &amp; Business Transformation — Rome Business School), every project pairs world-class design with SEO, data and growth strategy.</p>
      </article>
    </div>
  </div>
</section>

<!-- ================= CTA ================= -->
<section>
  <div class="container">
    <div class="cta-band reveal-zoom">
      <span class="eyebrow">Ready when you are</span>
      <h2>Let's build something the future will envy</h2>
      <p>Book a free strategy call or send us a brief — we usually reply within one business day.</p>
      <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
        <a href="contact.html" class="btn btn-primary">Start a Project <span class="arr">→</span></a>
        <a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener" class="btn btn-ghost">Book a Call</a>
      </div>
    </div>
  </div>
</section>
</main>
"""

SCHEMA = """
<link rel="canonical" href="https://efzybastudio.com/">
<meta property="og:url" content="https://efzybastudio.com/">
<meta property="og:image" content="https://efzybastudio.com/assets/img/icon.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="NG-LA">
<meta name="geo.placename" content="Lagos, Nigeria">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ProfessionalService",
      "@id": "https://efzybastudio.com/#organization",
      "name": "Efzyba Studio",
      "alternateName": "Efzybastudio",
      "url": "https://efzybastudio.com/",
      "logo": "https://efzybastudio.com/assets/img/icon.png",
      "image": "https://efzybastudio.com/assets/img/icon.png",
      "description": "Web design and digital marketing agency in Nigeria. Website design & development, e-commerce, UI/UX, SEO, data analytics and digital marketing for clients worldwide.",
      "telephone": "+2349034520821",
      "email": "emmanuel@efzybastudio.com",
      "priceRange": "$750 - $10000+",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Lagos",
        "addressCountry": "NG"
      },
      "areaServed": [
        {"@type": "Country", "name": "Nigeria"},
        {"@type": "Country", "name": "United Kingdom"},
        "Worldwide"
      ],
      "founder": {
        "@type": "Person",
        "name": "Emmanuel Akinola",
        "jobTitle": "Founder, Web Designer & Digital Marketer",
        "alumniOf": "Rome Business School",
        "email": "emmanuel@efzybastudio.com"
      },
      "sameAs": [
        "http://linktr.ee/emmanuelakinola",
        "https://emmanuelakinola.framer.website/"
      ],
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "reviewCount": "80"
      },
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Digital Services",
        "itemListElement": [
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Website Design & Development"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "E-commerce Website Development"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Landing Page Design"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "UI/UX Design & Prototyping"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "SEO & Digital Marketing"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Data Analytics & Reporting"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Brand Identity Design"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Virtual Assistance"}}
        ]
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://efzybastudio.com/#website",
      "url": "https://efzybastudio.com/",
      "name": "Efzyba Studio",
      "publisher": {"@id": "https://efzybastudio.com/#organization"},
      "inLanguage": "en"
    }
  ]
}
</script>
"""

html = page("home",
  "Web Design & Digital Marketing Agency in Nigeria | Efzyba Studio",
  "Efzyba Studio is a leading web design & digital marketing agency in Nigeria (Lagos) serving clients worldwide. Website design & development, e-commerce, UI/UX, SEO, data analytics. 80+ happy clients. Call +234 903 452 0821.",
  "web design agency Nigeria, website designer Lagos, digital marketing agency Nigeria, best web design company Nigeria, website development Lagos, SEO agency Nigeria, e-commerce website Nigeria, Framer designer, UI UX design Nigeria, Efzyba Studio, Emmanuel Akinola",
  body, extra_head=SCHEMA)

open("../index.html","w").write(html)
print("index.html written")
