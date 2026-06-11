# Shared header / footer templates for efzybastudio pages
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="Efzyba Studio">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Efzyba Studio">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{extra_head}
</head>
<body>

<div id="preloader"><img src="assets/img/icon.png" alt="Efzyba Studio loading"><span>EFZYBA STUDIO</span></div>
<div class="cursor-dot"></div><div class="cursor-ring"></div>
<div class="bg-grid"></div>
<div class="orb orb-1"></div><div class="orb orb-2"></div><div class="orb orb-3"></div>

<header class="site-header">
  <div class="container nav-wrap">
    <a class="brand" href="index.html"><img src="assets/img/icon.png" alt="Efzyba Studio logo">efzyba<b>studio</b></a>
    <nav class="nav-links" aria-label="Main navigation">
      <a href="index.html"{a_home}>Home</a>
      <a href="about.html"{a_about}>About</a>
      <a href="services.html"{a_services}>Services</a>
      <a href="portfolio.html"{a_portfolio}>Portfolio</a>
      <a href="blog.html"{a_blog}>Blog</a>
      <a href="contact.html"{a_contact}>Contact</a>
    </nav>
    <a href="contact.html" class="btn btn-primary btn-sm nav-cta">Start a Project <span class="arr">→</span></a>
    <button class="hamburger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
</header>
"""

FOOTER = """
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo-white.png" alt="Efzyba Studio">
        <p>A futuristic digital agency crafting high-converting websites, intelligent data solutions and memorable brand experiences for ambitious businesses worldwide.</p>
        <div class="socials">
          <a href="http://linktr.ee/emmanuelakinola" target="_blank" rel="noopener" aria-label="Linktree">🔗</a>
          <a href="mailto:emmanuel@efzybastudio.com" aria-label="Email">✉️</a>
          <a href="tel:+2349034520821" aria-label="Phone">📞</a>
          <a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener" aria-label="Book a call">📅</a>
        </div>
      </div>
      <div>
        <h4>Studio</h4>
        <a href="about.html">About Us</a>
        <a href="services.html">Services</a>
        <a href="portfolio.html">Portfolio</a>
        <a href="services.html#pricing">Pricing</a>
        <a href="blog.html">Blog</a>
      </div>
      <div>
        <h4>Services</h4>
        <a href="services.html">Web Design &amp; Development</a>
        <a href="services.html">E-commerce Solutions</a>
        <a href="services.html">UI/UX &amp; Prototyping</a>
        <a href="services.html">SEO &amp; Digital Marketing</a>
        <a href="services.html">Data Analytics</a>
      </div>
      <div>
        <h4>Contact</h4>
        <a href="tel:+2349034520821">+234 903 452 0821</a>
        <a href="mailto:emmanuel@efzybastudio.com">emmanuel@efzybastudio.com</a>
        <a href="https://calendly.com/akinolaemmanuel5" target="_blank" rel="noopener">Book a free strategy call</a>
        <a href="contact.html">Send a message →</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span class="year"></span> <b>Efzyba Studio</b>. All rights reserved.</span>
      <span>Designed &amp; engineered with ✦ in Lagos · London</span>
    </div>
  </div>
</footer>

<script src="assets/js/main.js"></script>
</body>
</html>
"""

def page(name, title, desc, keywords, body, extra_head=""):
    nav = {k: "" for k in ["home","about","services","portfolio","blog","contact"]}
    if name in nav: nav[name] = ' class="active"'
    html = HEAD.format(
        title=title, desc=desc, keywords=keywords, extra_head=extra_head,
        a_home=nav["home"], a_about=nav["about"], a_services=nav["services"],
        a_portfolio=nav["portfolio"], a_blog=nav["blog"], a_contact=nav["contact"]
    ) + body + FOOTER
    return html
