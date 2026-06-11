from shared import page
import datetime

# ============================ 404 PAGE ============================
body_404 = """
<main>
<section class="page-hero" style="min-height:70vh;display:flex;align-items:center">
  <div class="container" style="text-align:center">
    <h1 style="font-size:clamp(5rem,16vw,11rem);line-height:1;margin-bottom:8px">
      <span class="grad">4</span><span class="outline" style="color:transparent;-webkit-text-stroke:2px rgba(244,196,48,.6)">0</span><span class="grad">4</span>
    </h1>
    <h2 style="font-size:clamp(1.4rem,3vw,2rem);margin-bottom:14px">Lost in the future 🛸</h2>
    <p>This page doesn't exist — or it moved to a better dimension. Let's get you back on track.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:36px">
      <a href="/" class="btn btn-primary">Back to Home <span class="arr">→</span></a>
      <a href="/portfolio.html" class="btn btn-ghost">View Our Work</a>
      <a href="/contact.html" class="btn btn-ghost">Contact Us</a>
    </div>
    <p style="margin-top:46px;color:var(--muted);font-size:.9rem">Looking for something specific? Try
      <a href="/services.html" style="color:var(--gold)">Services</a> ·
      <a href="/blog.html" style="color:var(--gold)">Blog</a> ·
      <a href="/about.html" style="color:var(--gold)">About</a>
    </p>
  </div>
</section>
</main>
"""

open("../404.html","w").write(page("home",
  "Page Not Found (404) — Efzyba Studio",
  "The page you're looking for doesn't exist. Return to Efzyba Studio's homepage.",
  "404, page not found",
  body_404, extra_head='<meta name="robots" content="noindex">'))
print("404.html written")

# ============================ SITEMAP ============================
BASE = "https://efzybastudio.com"
today = "2026-06-11"

pages = [
    ("/",                              "1.0", "weekly"),
    ("/about.html",                    "0.9", "monthly"),
    ("/services.html",                 "0.9", "monthly"),
    ("/portfolio.html",                "0.9", "monthly"),
    ("/contact.html",                  "0.8", "monthly"),
    ("/blog.html",                     "0.8", "weekly"),
    ("/case-fundjoy.html",             "0.7", "monthly"),
    ("/case-hebe.html",                "0.7", "monthly"),
    ("/case-brightsites.html",         "0.7", "monthly"),
    ("/case-designcube.html",          "0.7", "monthly"),
    ("/case-healthwell.html",          "0.7", "monthly"),
    ("/case-thelist.html",             "0.7", "monthly"),
    ("/blog-web-design-agency-nigeria.html", "0.8", "monthly"),
    ("/blog-seo-small-business.html",  "0.7", "monthly"),
    ("/blog-nocode-vs-code.html",      "0.7", "monthly"),
    ("/blog-data-analytics.html",      "0.7", "monthly"),
    ("/blog-uiux-trends.html",         "0.7", "monthly"),
    ("/blog-website-conversion.html",  "0.7", "monthly"),
    ("/blog-virtual-assistant.html",   "0.7", "monthly"),
]

urls = ""
for path, prio, freq in pages:
    urls += f"""  <url>
    <loc>{BASE}{path}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{prio}</priority>
  </url>
"""

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>
"""
open("../sitemap.xml","w").write(sitemap)
print("sitemap.xml written")

# ============================ ROBOTS.TXT ============================
robots = """# Efzyba Studio — robots.txt
User-agent: *
Allow: /

# Keep utility pages out of the index
Disallow: /thank-you.html
Disallow: /404.html
Disallow: /_build/

Sitemap: https://efzybastudio.com/sitemap.xml
"""
open("../robots.txt","w").write(robots)
print("robots.txt written")

# ============================ NIGERIA KEYWORD ARTICLE ============================
article_head = """
<link rel="canonical" href="https://efzybastudio.com/blog-web-design-agency-nigeria.html">
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Choose the Best Web Design & Digital Marketing Agency in Nigeria (2026 Guide)",
  "description": "What to look for in a Nigerian web design and digital marketing agency: portfolio proof, pricing, SEO capability, platforms and red flags to avoid.",
  "image": "https://efzybastudio.com/assets/img/blog-nocode.jpg",
  "datePublished": "2026-06-11",
  "dateModified": "2026-06-11",
  "author": {"@type": "Person", "name": "Emmanuel Akinola", "url": "https://efzybastudio.com/about.html"},
  "publisher": {"@type": "Organization", "name": "Efzyba Studio", "logo": {"@type": "ImageObject", "url": "https://efzybastudio.com/assets/img/icon.png"}}
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "How much does a website cost in Nigeria?", "acceptedAnswer": {"@type": "Answer", "text": "Professional business websites in Nigeria typically range from about $750 for a simple 5-page site to $3,000-$10,000+ for e-commerce or custom platforms. Subscription models, like Efzyba Studio's plans from $750/month, bundle design, development, hosting guidance, SEO and ongoing maintenance into one predictable fee."}},
    {"@type": "Question", "name": "How long does it take to design a website in Nigeria?", "acceptedAnswer": {"@type": "Answer", "text": "A standard marketing website takes 2-4 weeks with a professional agency. E-commerce stores and larger platforms typically take 4-8 weeks depending on scope and content readiness."}},
    {"@type": "Question", "name": "What is the best web design agency in Nigeria?", "acceptedAnswer": {"@type": "Answer", "text": "The best agency is the one with verifiable case studies, transparent pricing, modern platform expertise (Framer, Webflow, WordPress, Shopify), built-in SEO, and responsive communication. Efzyba Studio combines all five with 80+ happy clients and measurable results like +85% qualified leads and +72% online bookings."}},
    {"@type": "Question", "name": "Do Nigerian businesses really need SEO?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. More Nigerians search Google for products and services every year, and ranking for searches like 'your service + your city' brings high-intent customers at zero cost per click. SEO compounds over time, unlike paid ads that stop the moment you stop paying."}}
  ]
}
</script>
"""

nigeria_article = """
<p><strong>Choosing a web design and digital marketing agency in Nigeria</strong> can feel like a gamble. The market is full of talented professionals — and, unfortunately, plenty of "agencies" that disappear after the deposit clears. This guide gives you a practical checklist for separating the real builders from the pretenders, whether you're in Lagos, Abuja, Port Harcourt or anywhere else.</p>

<h2>Why your website is your hardest-working employee</h2>
<p>Nigeria has one of the fastest-growing internet populations in the world, with well over 100 million people online. Your customers now research before they buy — even for offline businesses. A professional website works 24/7: it builds trust before the first call, answers questions while you sleep, and captures leads while your competitors' Instagram pages sit unanswered.</p>

<h2>The 7-point checklist for choosing an agency in Nigeria</h2>

<h3>1. Demand verifiable case studies, not just screenshots</h3>
<p>Anyone can show a pretty homepage. Ask for <strong>results</strong>: did enquiries increase? Did bookings grow? At Efzyba Studio, our <a href="portfolio.html" style="color:var(--gold)">case studies</a> publish the numbers — +64% donations for FundJoy, +85% qualified leads for Hebe Network, +72% online bookings for HealthWell. If an agency can't connect design to outcomes, they're selling decoration.</p>

<h3>2. Check the platform expertise</h3>
<p>Modern agencies should be fluent in modern tools — <strong>Framer, Webflow, WordPress and Shopify</strong> — and recommend based on your needs, not their comfort zone. A blog-heavy business needs WordPress; a design-led brand launching fast needs Framer; a store needs Shopify. Be wary of anyone with a one-size-fits-all answer.</p>

<h3>3. Insist on SEO being built in, not bolted on</h3>
<p>A beautiful website nobody finds is a billboard in the desert. Ask: will the site ship with proper title tags, meta descriptions, structured data, a sitemap, fast load times and mobile-first design? These should be standard, not an upsell. (Every Efzyba build includes them by default.)</p>

<h3>4. Look for strategy, not just design</h3>
<p>The difference between a freelancer and an agency is strategy. Who is your audience? What action should each page drive? How will success be measured? An agency led by marketing strategy — not just aesthetics — will ask these questions before opening Figma.</p>

<h3>5. Confirm post-launch support</h3>
<p>Websites need updates, security monitoring and fixes. Many Nigerian businesses get stranded when their "designer" vanishes after launch. Choose an agency with clear maintenance plans and response-time commitments.</p>

<h3>6. Expect transparent, written pricing</h3>
<p>Vague quotes invite scope drama later. Professional agencies publish or document pricing clearly. Our <a href="services.html#pricing" style="color:var(--gold)">plans</a> start at $750/month with everything itemised — design, development, SEO, updates and support.</p>

<h3>7. Test their communication before you pay</h3>
<p>How fast did they respond to your first enquiry? Was the proposal clear? Communication during the sales process is the <em>best</em> it will ever be — if it's poor now, walk away.</p>

<h2>Red flags to avoid 🚩</h2>
<ul>
<li><strong>No portfolio with live links</strong> — screenshots can be copied; live sites can't lie.</li>
<li><strong>100% payment upfront</strong> — milestone payments protect both sides.</li>
<li><strong>"We'll get you to #1 on Google in 2 weeks"</strong> — real SEO takes 3–6 months; instant-ranking promises mean spam tactics that get sites penalised.</li>
<li><strong>No contract or scope document</strong> — professionals put everything in writing.</li>
<li><strong>They own your domain and hosting</strong> — you should always control your own digital assets.</li>
</ul>

<h2>How much should a website cost in Nigeria?</h2>
<p>Rough 2026 market ranges for professional work:</p>
<ul>
<li><strong>Landing page:</strong> $300 – $800</li>
<li><strong>5-page business website:</strong> $750 – $2,500</li>
<li><strong>E-commerce store:</strong> $1,500 – $5,000+</li>
<li><strong>Custom platforms/web apps:</strong> $5,000 – $20,000+</li>
</ul>
<p>Subscription pricing is increasingly popular because it spreads cost and includes ongoing care — our Essential plan bundles design, development, SEO and maintenance from <strong>$750/month</strong>.</p>

<h2>Why clients choose Efzyba Studio</h2>
<ul>
<li><strong>Proven results:</strong> 80+ happy clients, 120+ projects launched, published case-study numbers.</li>
<li><strong>Strategy-grade leadership:</strong> founded by Emmanuel Akinola, MBA in International Digital Marketing &amp; Business Transformation (Rome Business School).</li>
<li><strong>Full-stack team:</strong> UI/UX design (Victor), data analytics (Mayokun), UK-based operations (Loveth) — one accountable studio.</li>
<li><strong>Modern platforms:</strong> Framer, Webflow, WordPress, Shopify — matched to your goals.</li>
<li><strong>Global standards, local insight:</strong> based in Lagos, serving Nigeria, the UK and clients worldwide.</li>
</ul>

<blockquote>The right agency doesn't just build you a website — it builds you a growth engine you actually own.</blockquote>

<h2>Ready to talk?</h2>
<p>Call or WhatsApp <a href="tel:+2349034520821" style="color:var(--gold)">+234 903 452 0821</a>, email <a href="mailto:emmanuel@efzybastudio.com" style="color:var(--gold)">emmanuel@efzybastudio.com</a>, or <a href="contact.html" style="color:var(--gold)">send us a brief</a>. We reply within one business day with honest, no-pressure advice — even if we're not the right fit.</p>
"""

art_body = f"""
<main>
<section class="article-hero">
  <div class="container">
    <p class="crumbs" style="margin-bottom:26px"><a href="index.html">Home</a> &nbsp;/&nbsp; <a href="blog.html">Blog</a> &nbsp;/&nbsp; <b>Agency Guide</b></p>
    <div class="meta"><span>Agency Guide</span><span>·</span><span>Jun 11, 2026</span><span>·</span><span>9 min read</span></div>
    <h1>How to Choose the Best Web Design &amp; Digital Marketing Agency in Nigeria (2026 Guide)</h1>
  </div>
</section>
<div class="container">
  <div class="article-cover reveal-zoom"><img src="assets/img/blog-nocode.jpg" alt="Choosing a web design and digital marketing agency in Nigeria"></div>
  <article class="article">
    {nigeria_article}
    <div class="author-box">
      <img src="assets/img/team-emmanuel.jpg" alt="Emmanuel Akinola">
      <div><b>Emmanuel Akinola</b><span>Founder, Efzyba Studio — Web Designer &amp; Digital Marketer (MBA, Rome Business School)</span></div>
    </div>
    <div style="margin:50px 0;display:flex;gap:14px;flex-wrap:wrap">
      <a href="blog.html" class="btn btn-ghost">← Back to Blog</a>
      <a href="contact.html" class="btn btn-primary">Work With Us <span class="arr">→</span></a>
    </div>
  </article>
</div>
</main>
"""

open("../blog-web-design-agency-nigeria.html","w").write(page("blog",
  "Best Web Design & Digital Marketing Agency in Nigeria — How to Choose (2026)",
  "How to choose the best web design and digital marketing agency in Nigeria: a 7-point checklist, 2026 pricing guide, red flags to avoid, and FAQs. By Efzyba Studio, Lagos.",
  "best web design agency Nigeria, web design company Lagos, digital marketing agency Nigeria, website cost Nigeria, hire web designer Nigeria, website design Abuja",
  art_body, extra_head=article_head))
print("blog-web-design-agency-nigeria.html written")
