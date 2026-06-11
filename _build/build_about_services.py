from shared import page

# ============================ ABOUT ============================
about_body = """
<main>
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; <b>About</b></p>
    <h1>The studio behind the <span class="grad">spark</span></h1>
    <p>Design, data and marketing — fused into one agile team building the digital future for ambitious brands.</p>
  </div>
</section>

<section style="padding-top:20px">
  <div class="container about-grid">
    <div class="about-photo reveal-l">
      <div class="frame tilt"><img src="assets/img/team-emmanuel.jpg" alt="Emmanuel Akinola, founder of Efzyba Studio"></div>
      <div class="badge">6+ Years · 80+ Clients</div>
    </div>
    <div class="about-copy reveal-r">
      <span class="eyebrow">Our Story</span>
      <h2>Hi, I'm Emmanuel — founder of Efzyba Studio</h2>
      <p>I'm a passionate web designer inspired by the ever-evolving world of design, where creativity meets purpose. I thrive on transforming bold ideas into visually stunning, functional interfaces that not only look great but make a meaningful impact.</p>
      <p>With an MBA in International Digital Marketing and Business Transformation from Rome Business School, I blend design with strategy to create solutions that resonate with users and achieve real business goals. Efzyba Studio grew from that mission — a senior, multidisciplinary team delivering websites, data and growth under one roof.</p>
      <ul class="check-list">
        <li>No-code mastery: Framer, Webflow, WordPress, Wix &amp; Shopify</li>
        <li>Interface design in Figma, grounded in user research</li>
        <li>Growth stack: SEO, SEM, email marketing &amp; social strategy</li>
        <li>Data-driven decisions with analytics &amp; reporting baked in</li>
      </ul>
      <div style="display:flex;gap:14px;flex-wrap:wrap">
        <a href="https://drive.google.com/file/d/1HXndaicMaad2Vg4otse68SF3WvQSUTBq/view?usp=sharing" target="_blank" rel="noopener" class="btn btn-primary">Read My CV <span class="arr">→</span></a>
        <a href="contact.html" class="btn btn-ghost">Work With Us</a>
      </div>
    </div>
  </div>
</section>

<section style="background:linear-gradient(180deg,transparent,rgba(23,16,8,.5),transparent)">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">The Crew</span>
      <h2>Four specialists. <span class="grad">One mission.</span></h2>
    </div>
    <div class="team-grid">
      <div class="card tilt team-card reveal-zoom d1">
        <div class="ph"><img src="assets/img/team-emmanuel.jpg" alt="Emmanuel Akinola"></div>
        <h3>Emmanuel Akinola</h3><span class="role">Founder · Web Designer &amp; Digital Marketer</span>
        <p>Leads strategy, design and growth. Builder of 120+ websites across Framer, WordPress, Webflow and Shopify, with an MBA from Rome Business School.</p>
      </div>
      <div class="card tilt team-card reveal-zoom d2">
        <div class="ph"><img src="assets/img/team-victor.png" alt="Victor Akinola"></div>
        <h3>Victor Akinola</h3><span class="role">UI/UX Designer</span>
        <p>Owns research, wireframes and prototyping. Victor turns messy requirements into clean, intuitive interfaces users instantly understand.</p>
      </div>
      <div class="card tilt team-card reveal-zoom d3">
        <div class="ph"><img src="assets/img/team-mayokun.png" alt="Mayokun Oluwajuyigbe"></div>
        <h3>Mayokun Oluwajuyigbe</h3><span class="role">Data Analyst</span>
        <p>Builds dashboards, tracks performance and finds the stories hidden in your numbers — so every decision we make is backed by evidence.</p>
      </div>
      <div class="card tilt team-card reveal-zoom d4">
        <div class="ph"><img src="assets/img/team-loveth.png" alt="Loveth Toluwalope"></div>
        <h3>Loveth Toluwalope</h3><span class="role">Virtual Assistant · UK Based</span>
        <p>Your single point of contact. Loveth coordinates schedules, communications and project ops across time zones with effortless precision.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Our Stack</span>
      <h2>Tools we <span class="grad">master</span></h2>
      <p>The technologies powering every Efzyba build — chosen for speed, flexibility and results.</p>
    </div>
    <div class="stack-grid">
      <div class="stack-item reveal d1"><span class="si">⚡</span><div><h4>Framer</h4><p>A visual playground for crafting stunning, interactive websites — beyond a simple builder.</p></div></div>
      <div class="stack-item reveal d2"><span class="si">🎨</span><div><h4>Figma</h4><p>Our collaborative design platform for real-time feedback and rapid iterations.</p></div></div>
      <div class="stack-item reveal d3"><span class="si">📝</span><div><h4>Notion</h4><p>Project management, task tracking and a central documentation hub for every build.</p></div></div>
      <div class="stack-item reveal d4"><span class="si">🗃️</span><div><h4>Airtable</h4><p>Structured databases that keep complex project data organised and accessible.</p></div></div>
      <div class="stack-item reveal d1"><span class="si">🔁</span><div><h4>Zapier</h4><p>Automation that connects your tools and removes repetitive busywork from workflows.</p></div></div>
      <div class="stack-item reveal d2"><span class="si">🍋</span><div><h4>Lemon Squeezy</h4><p>Payments, subscriptions, tax compliance and fraud prevention for SaaS operations.</p></div></div>
      <div class="stack-item reveal d3"><span class="si">📧</span><div><h4>Mailchimp</h4><p>Engaging email campaigns, list management and performance analytics that convert.</p></div></div>
      <div class="stack-item reveal d4"><span class="si">💬</span><div><h4>Slack</h4><p>The cornerstone of our collaboration — ideas, files and feedback in real time.</p></div></div>
      <div class="stack-item reveal d1"><span class="si">🤖</span><div><h4>ChatGPT</h4><p>Content ideation, copywriting support and problem-solving that sharpens every project.</p></div></div>
      <div class="stack-item reveal d2"><span class="si">🎬</span><div><h4>Creative Cloud</h4><p>Photoshop, Illustrator and After Effects for visuals, branding and motion design.</p></div></div>
      <div class="stack-item reveal d3"><span class="si">🧱</span><div><h4>HTML5</h4><p>The semantic backbone of accessible, meaningful and future-proof websites.</p></div></div>
      <div class="stack-item reveal d4"><span class="si">💅</span><div><h4>CSS3</h4><p>Styling power — typography, colour, motion and responsive layouts on every screen.</p></div></div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="cta-band reveal-zoom">
      <span class="eyebrow">Join 80+ happy clients</span>
      <h2>Your project deserves this team</h2>
      <p>Tell us where you want to go. We'll map the route — and build the vehicle.</p>
      <a href="contact.html" class="btn btn-primary">Start the Conversation <span class="arr">→</span></a>
    </div>
  </div>
</section>
</main>
"""

open("../about.html","w").write(page("about",
  "About Efzyba Studio — Our Team, Story & Tech Stack",
  "Meet Efzyba Studio: founder Emmanuel Akinola (web designer & digital marketer), Victor Akinola (UI/UX), Mayokun Oluwajuyigbe (data analyst) and Loveth Toluwalope (UK-based virtual assistant).",
  "about Efzyba Studio, Emmanuel Akinola, web design team, UI UX designer, data analyst, virtual assistant UK",
  about_body))
print("about.html written")

# ============================ SERVICES ============================
services = [
 ("🖥️","Website Design & Development","Transform your vision into reality. We craft beautiful, user-friendly websites that captivate visitors and guide them toward action — purchases, sign-ups or enquiries. Our process combines deep audience understanding, UX design for intuitive navigation, and modern front-end development.",["UX Research","Front-end","Framer","WordPress"]),
 ("🎯","Landing Pages","Laser-focused on specific marketing goals. High-impact landing pages that grab attention, communicate your value proposition clearly and seamlessly convert visitors into leads — with optimised headlines, visuals, CTAs and lead-capture forms.",["CRO","Copywriting","A/B Testing"]),
 ("🛒","E-commerce Websites","Your online store should be a seamless shopping experience. User-friendly, visually appealing stores with clear product information, intuitive navigation, secure payment gateways and a streamlined checkout that maximises conversions.",["Shopify","WooCommerce","Payments"]),
 ("🧪","Interactive Prototyping","Don't wait for development to see your website come alive. Using Framer, we build interactive prototypes that simulate the final experience — test user flows, visualise interactions and gather feedback before any code is written.",["Framer","Figma","User Flows"]),
 ("📱","Responsive Design","Your website must look great and function flawlessly on every device. Our responsive approach adapts automatically to all screen sizes, delivering an optimal experience for every visitor, desktop to smartphone.",["Mobile-first","Cross-device"]),
 ("⚙️","CMS Integration","Manage your own content with ease. We integrate platforms like WordPress so you can update pages, publish posts and manage media without writing a single line of code — keeping your site fresh and engaging.",["WordPress","Headless CMS"]),
 ("🛡️","Maintenance & Support","Your website is an ongoing investment. Regular software updates, security scans, performance monitoring and rapid troubleshooting keep your site fast, safe and always available.",["Security","Monitoring","Updates"]),
 ("✨","Brand Identity Design","A cohesive identity beyond the website — logos, palettes, typography and design styles that create a consistent, memorable brand image across every digital touchpoint.",["Logo","Guidelines","Visual ID"]),
 ("🔍","SEO Optimization","Get found by your target audience. SEO best practices that improve rankings for the keywords that matter, driving organic traffic and qualified leads to your website.",["Keywords","On-page","Technical SEO"]),
 ("♿","Accessibility Audits","Websites should be usable by everyone. WCAG-standard audits that make your site accessible to people with disabilities, promoting inclusivity and expanding your reach.",["WCAG","Inclusive UX"]),
 ("🧩","Design Systems","Consistency across every platform. Reusable components, UI patterns and code snippets that streamline development and empower your team to build on-brand, forever.",["Components","Tokens","Docs"]),
 ("🔬","User Research & Testing","Put users at the centre. Research and usability testing reveal your audience's needs and pain points — data we use to optimise the experience until it converts.",["Interviews","Usability","Heatmaps"]),
 ("📊","Data Analytics & Reporting","Led by our data analyst Mayokun: dashboards, KPI tracking and insight reports that turn your traffic, sales and campaign data into clear, confident decisions.",["Dashboards","GA4","Insights"]),
 ("📈","Digital Marketing","SEO, SEM, email marketing and social media strategies engineered for measurable growth — backed by Emmanuel's MBA-grade marketing strategy and our analytics stack.",["SEM","Email","Social"]),
 ("🤝","Virtual Assistance & Ops","UK-based support from Loveth: inbox and calendar management, client communications, research and project coordination that keep your business moving.",["Admin","Scheduling","Ops"]),
]

cards = ""
for i,(ic,t,d,tags) in enumerate(services):
    delay = "d%d" % ((i % 3)+1)
    tagshtml = "".join('<span class="tag">%s</span>' % x for x in tags)
    cards += f"""
      <article class="card tilt reveal {delay}">
        <span class="num">0{i+1}</span>
        <div class="icon" style="margin-top:14px">{ic}</div>
        <h3>{t}</h3>
        <p>{d}</p>
        <div class="tags">{tagshtml}</div>
      </article>"""

services_body = f"""
<main>
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; <b>Services</b></p>
    <h1>Everything digital, <span class="grad">done brilliantly</span></h1>
    <p>Fifteen capabilities, one accountable studio. Strategy, design, build, data and growth — engineered to work together.</p>
  </div>
</section>

<section style="padding-top:20px">
  <div class="container">
    <div class="cards-grid">{cards}
    </div>
  </div>
</section>

<!-- PRICING -->
<section id="pricing" style="background:linear-gradient(180deg,transparent,rgba(23,16,8,.5),transparent)">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">Subscription Plans</span>
      <h2>Simple plans, <span class="grad">serious results</span></h2>
      <p>Predictable monthly pricing that covers design, development and ongoing care.</p>
    </div>
    <div class="pricing-grid">
      <div class="card tilt price-card reveal d1">
        <span class="plan">Essential Plan</span>
        <div class="amount">$750<small>/month</small></div>
        <p class="desc">Perfect for simple websites, blogs or landing pages.</p>
        <ul>
          <li>Website design &amp; development (up to 5 pages)</li>
          <li>Mobile-responsive design</li>
          <li>Stock photo integration</li>
          <li>Basic SEO optimisation</li>
          <li>Contact form integration</li>
          <li>Limited content updates (1 per month)</li>
          <li>Basic website security monitoring</li>
          <li>Ongoing bug fixes &amp; maintenance</li>
          <li>24/7 email support</li>
        </ul>
        <a href="https://flutterwave.com/pay/qbxsoq4asgbo" target="_blank" rel="noopener" class="btn btn-ghost" style="justify-content:center">Purchase Plan</a>
      </div>
      <div class="card tilt price-card featured reveal d2">
        <span class="badge-pop">Most Popular</span>
        <span class="plan">Growth Plan</span>
        <div class="amount">$1,200<small>/month</small></div>
        <p class="desc">Ideal for growing businesses and e-commerce websites.</p>
        <ul>
          <li>Everything in the Essential Plan</li>
          <li>Custom graphic design elements</li>
          <li>CMS access for content updates</li>
          <li>E-commerce functionality (optional add-on)</li>
          <li>Advanced SEO optimisation (ongoing)</li>
          <li>Google Analytics integration &amp; reporting</li>
          <li>Unlimited content updates (monthly allowance)</li>
          <li>Priority email &amp; phone support</li>
        </ul>
        <a href="https://flutterwave.com/pay/5v68rdq5cfin" target="_blank" rel="noopener" class="btn btn-primary" style="justify-content:center">Purchase Plan <span class="arr">→</span></a>
      </div>
      <div class="card tilt price-card reveal d3">
        <span class="plan">Custom Plan</span>
        <div class="amount">Let's talk</div>
        <p class="desc">Need something more? We craft custom plans to fit your website's specific needs.</p>
        <ul>
          <li>Multi-page platforms &amp; web apps</li>
          <li>Full brand identity systems</li>
          <li>Data analytics &amp; dashboard builds</li>
          <li>Dedicated virtual assistant support</li>
          <li>Full-funnel digital marketing</li>
          <li>SLA-backed priority support</li>
        </ul>
        <a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener" class="btn btn-ghost" style="justify-content:center">Book a Call</a>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section>
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">FAQ</span>
      <h2>Questions, <span class="grad">answered</span></h2>
    </div>
    <div class="faq reveal">
      <details class="faq-item"><summary>How long does a typical website project take?</summary><div class="fa-body">Most marketing websites launch in 2–4 weeks. E-commerce and larger platforms typically take 4–8 weeks, depending on scope. We share a clear timeline after discovery and keep you updated in Slack/Notion throughout.</div></details>
      <details class="faq-item"><summary>Which platform will my website be built on?</summary><div class="fa-body">We recommend the platform that fits your goals — Framer or Webflow for speed and stunning interactions, WordPress for content-heavy sites, Shopify or WooCommerce for stores. You'll always own your site and content.</div></details>
      <details class="faq-item"><summary>Do you handle SEO and marketing after launch?</summary><div class="fa-body">Yes. Every build ships with on-page SEO baked in, and our Growth Plan includes ongoing SEO, analytics reporting and content updates. We also run email and SEM campaigns as add-ons.</div></details>
      <details class="faq-item"><summary>Can I update the website myself?</summary><div class="fa-body">Absolutely. We integrate a CMS so you can edit text, images and posts without code — and we'll train you on it. Prefer hands-off? Our plans include managed content updates.</div></details>
      <details class="faq-item"><summary>How do payments work?</summary><div class="fa-body">Subscription plans are billed monthly via Flutterwave. Custom projects are typically split into milestone payments. No hidden fees, cancel any time with notice.</div></details>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="cta-band reveal-zoom">
      <span class="eyebrow">Free strategy call</span>
      <h2>Not sure what you need yet?</h2>
      <p>Book 30 minutes with Emmanuel — leave with a clear, honest roadmap whether we work together or not.</p>
      <a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener" class="btn btn-primary">Book a Free Call <span class="arr">→</span></a>
    </div>
  </div>
</section>
</main>
"""

open("../services.html","w").write(page("services",
  "Services & Pricing — Efzyba Studio | Web Design, SEO, Data & Marketing",
  "Explore Efzyba Studio services: website design & development, e-commerce, landing pages, UI/UX prototyping, SEO, data analytics, digital marketing and virtual assistance. Plans from $750/month.",
  "web design services, e-commerce development, landing pages, SEO services, data analytics, digital marketing agency, website pricing plans",
  services_body))
print("services.html written")
