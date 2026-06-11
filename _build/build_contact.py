from shared import page

contact_body = """
<main>
<section class="page-hero">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> &nbsp;/&nbsp; <b>Contact</b></p>
    <h1>Let's build the <span class="grad">future</span> together</h1>
    <p>Tell us about your project — we usually reply within one business day.</p>
  </div>
</section>

<section style="padding-top:20px">
  <div class="container contact-grid">
    <div class="contact-info reveal-l">
      <div class="item">
        <div class="ci">📞</div>
        <div><b>Call or WhatsApp</b><a href="tel:+2349034520821">+234 903 452 0821</a></div>
      </div>
      <div class="item">
        <div class="ci">✉️</div>
        <div><b>Email Us</b><a href="mailto:emmanuel@efzybastudio.com">emmanuel@efzybastudio.com</a></div>
      </div>
      <div class="item">
        <div class="ci">📅</div>
        <div><b>Book a Free Strategy Call</b><a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener">calendly.com/akinolaemmanuel5</a></div>
      </div>
      <div class="item">
        <div class="ci">🌍</div>
        <div><b>Where We Work</b><span>Lagos, Nigeria · London, UK · Worldwide (remote)</span></div>
      </div>
      <div class="item">
        <div class="ci">⏱️</div>
        <div><b>Response Time</b><span>Within 1 business day — usually much faster.</span></div>
      </div>
    </div>

    <div class="card contact-form reveal-r">
      <h3 style="margin-bottom:8px">Start a project</h3>
      <p style="color:var(--muted);font-size:.92rem;margin-bottom:26px">Tell us about your project — your message lands straight in our inbox and we reply within one business day.</p>
      <form id="contactForm" name="contact" method="POST" action="thank-you.html" data-netlify="true" netlify-honeypot="bot-field">
        <input type="hidden" name="form-name" value="contact">
        <p style="display:none"><label>Don't fill this out if you're human: <input name="bot-field"></label></p>
        <div class="frow">
          <div class="fgroup"><label for="cname">Your Name *</label><input id="cname" name="name" type="text" placeholder="Jane Doe" autocomplete="name" required></div>
          <div class="fgroup"><label for="cemail">Email *</label><input id="cemail" name="email" type="email" placeholder="jane@company.com" autocomplete="email" required></div>
        </div>
        <div class="frow">
          <div class="fgroup"><label for="cphone">Phone / WhatsApp</label><input id="cphone" name="phone" type="tel" placeholder="+234 ..." autocomplete="tel"></div>
          <div class="fgroup"><label for="ccompany">Company / Brand</label><input id="ccompany" name="company" type="text" placeholder="Acme Inc." autocomplete="organization"></div>
        </div>
        <div class="frow">
          <div class="fgroup">
            <label for="cservice">What do you need? *</label>
            <select id="cservice" name="service" required>
              <option value="" disabled selected>Select a service…</option>
              <option>Website Design &amp; Development</option>
              <option>E-commerce Website</option>
              <option>Landing Page</option>
              <option>UI/UX &amp; Prototyping</option>
              <option>SEO &amp; Digital Marketing</option>
              <option>Data Analytics</option>
              <option>Brand Identity</option>
              <option>Virtual Assistance</option>
              <option>Something else</option>
            </select>
          </div>
          <div class="fgroup">
            <label for="cbudget">Budget Range</label>
            <select id="cbudget" name="budget">
              <option value="" disabled selected>Select a range…</option>
              <option>Under $750</option>
              <option>$750 – $1,200</option>
              <option>$1,200 – $3,000</option>
              <option>$3,000 – $10,000</option>
              <option>$10,000+</option>
              <option>Not sure yet</option>
            </select>
          </div>
        </div>
        <div class="fgroup">
          <label for="ctimeline">Timeline</label>
          <select id="ctimeline" name="timeline">
            <option value="" disabled selected>When do you need it?</option>
            <option>ASAP (within 2 weeks)</option>
            <option>Within a month</option>
            <option>1–3 months</option>
            <option>Just exploring</option>
          </select>
        </div>
        <div class="fgroup"><label for="cmsg">Project Details *</label><textarea id="cmsg" name="message" placeholder="Tell us about your goals, what success looks like, and any links to your current site or inspiration..." required></textarea></div>
        <button type="submit" class="btn btn-primary" style="width:100%;justify-content:center" id="contactSubmit">Send Message <span class="arr">→</span></button>
        <p class="form-note" id="formNote">✦ Prefer talking? Call <a href="tel:+2349034520821" style="color:var(--gold)">+234 903 452 0821</a> or book a free call on Calendly.</p>
      </form>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="cta-band reveal-zoom">
      <span class="eyebrow">No pressure, just clarity</span>
      <h2>Free 30-minute strategy call</h2>
      <p>Walk away with a clear, honest roadmap for your digital presence — whether we work together or not.</p>
      <a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener" class="btn btn-primary">Book on Calendly <span class="arr">→</span></a>
    </div>
  </div>
</section>
</main>
"""

open("../contact.html","w").write(page("contact",
  "Contact Efzyba Studio — Start Your Project Today",
  "Contact Efzyba Studio: call +234 903 452 0821, email emmanuel@efzybastudio.com or book a free strategy call. Web design, data and digital marketing worldwide.",
  "contact web design agency, hire web designer, Efzyba Studio contact, web designer Nigeria UK",
  contact_body))
print("contact.html written")

# ============================ THANK YOU PAGE ============================
thanks_body = """
<main>
<section class="page-hero" style="min-height:62vh;display:flex;align-items:center">
  <div class="container" style="text-align:center">
    <div class="reveal-zoom in" style="font-size:4.5rem;margin-bottom:10px">🎉</div>
    <h1>Message <span class="grad">received!</span></h1>
    <p>Thanks for reaching out to Efzyba Studio. Your enquiry is safely in our inbox and we'll get back to you within <strong style="color:var(--gold)">one business day</strong> — usually much faster.</p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:38px">
      <a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener" class="btn btn-primary">Skip the Wait — Book a Call <span class="arr">→</span></a>
      <a href="index.html" class="btn btn-ghost">Back to Home</a>
    </div>
    <p style="margin-top:42px;color:var(--muted);font-size:.9rem">In a hurry? Call or WhatsApp <a href="tel:+2349034520821" style="color:var(--gold)">+234 903 452 0821</a></p>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="sec-head center reveal">
      <span class="eyebrow">While you wait</span>
      <h2>Explore our latest <span class="grad">insights</span></h2>
    </div>
    <div class="blog-grid">
      <a class="blog-card reveal d1" href="blog-seo-small-business.html">
        <div class="thumb"><img src="assets/img/blog-seo.jpg" alt="SEO playbook" loading="lazy"></div>
        <div class="body"><div class="meta"><span>SEO</span><span>8 min read</span></div>
        <h3>SEO for Small Businesses in 2026</h3><p>The complete beginner's playbook for ranking higher on Google.</p>
        <span class="read">Read article →</span></div>
      </a>
      <a class="blog-card reveal d2" href="blog-website-conversion.html">
        <div class="thumb"><img src="assets/img/blog-nocode.jpg" alt="Conversion fixes" loading="lazy"></div>
        <div class="body"><div class="meta"><span>Conversion</span><span>6 min read</span></div>
        <h3>Why Your Website Isn't Converting</h3><p>Nine proven fixes that turn traffic into enquiries.</p>
        <span class="read">Read article →</span></div>
      </a>
      <a class="blog-card reveal d3" href="portfolio.html">
        <div class="thumb"><img src="assets/img/project-fundjoy.jpg" alt="Our portfolio" loading="lazy"></div>
        <div class="body"><div class="meta"><span>Portfolio</span><span>Case studies</span></div>
        <h3>See What We've Built</h3><p>Six case studies with real results across six industries.</p>
        <span class="read">View portfolio →</span></div>
      </a>
    </div>
  </div>
</section>
</main>
"""

open("../thank-you.html","w").write(page("contact",
  "Thank You — Efzyba Studio",
  "Thanks for contacting Efzyba Studio. We'll reply within one business day.",
  "thank you, contact confirmation, Efzyba Studio",
  thanks_body, extra_head='<meta name="robots" content="noindex">'))
print("thank-you.html written")
