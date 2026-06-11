/* ============================================================
   EFZYBA STUDIO — interactions & 3D animations
   ============================================================ */
(function () {
  'use strict';

  /* ---------- preloader ---------- */
  window.addEventListener('load', function () {
    var pre = document.getElementById('preloader');
    if (pre) setTimeout(function () { pre.classList.add('done'); }, 500);
  });
  // fail-safe
  setTimeout(function () {
    var pre = document.getElementById('preloader');
    if (pre) pre.classList.add('done');
  }, 3000);

  /* ---------- custom cursor ---------- */
  var dot = document.querySelector('.cursor-dot');
  var ring = document.querySelector('.cursor-ring');
  if (dot && ring && window.matchMedia('(hover:hover)').matches) {
    var mx = -100, my = -100, rx = -100, ry = -100;
    document.addEventListener('mousemove', function (e) { mx = e.clientX; my = e.clientY; });
    (function loop() {
      rx += (mx - rx) * 0.16;
      ry += (my - ry) * 0.16;
      dot.style.transform = 'translate(' + mx + 'px,' + my + 'px) translate(-50%,-50%)';
      ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px) translate(-50%,-50%)';
      requestAnimationFrame(loop);
    })();
    document.querySelectorAll('a, button, .tilt, summary').forEach(function (el) {
      el.addEventListener('mouseenter', function () { ring.classList.add('hover'); });
      el.addEventListener('mouseleave', function () { ring.classList.remove('hover'); });
    });
  }

  /* ---------- sticky header ---------- */
  var header = document.querySelector('.site-header');
  function onScrollHeader() {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 40);
  }
  window.addEventListener('scroll', onScrollHeader, { passive: true });
  onScrollHeader();

  /* ---------- mobile nav ---------- */
  var burger = document.querySelector('.hamburger');
  var navLinks = document.querySelector('.nav-links');
  if (burger && navLinks) {
    burger.addEventListener('click', function () {
      burger.classList.toggle('open');
      navLinks.classList.toggle('open');
      document.body.style.overflow = navLinks.classList.contains('open') ? 'hidden' : '';
    });
    navLinks.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        burger.classList.remove('open');
        navLinks.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---------- scroll reveal ---------- */
  var revealEls = document.querySelectorAll('.reveal, .reveal-l, .reveal-r, .reveal-zoom');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* ---------- counters ---------- */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        var target = parseFloat(el.getAttribute('data-count'));
        var suffix = el.getAttribute('data-suffix') || '';
        var dur = 1800, t0 = null;
        function step(ts) {
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased) + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
        cio.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (c) { cio.observe(c); });
  }

  /* ---------- 3D tilt cards ---------- */
  var canTilt = window.matchMedia('(hover:hover) and (min-width:761px)').matches;
  document.querySelectorAll('.tilt').forEach(function (card) {
    card.addEventListener('mousemove', function (e) {
      var r = card.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width;
      var y = (e.clientY - r.top) / r.height;
      card.style.setProperty('--mx', (x * 100) + '%');
      card.style.setProperty('--my', (y * 100) + '%');
      if (!canTilt) return;
      var rotY = (x - 0.5) * 12;
      var rotX = (0.5 - y) * 10;
      card.style.transform = 'perspective(900px) rotateX(' + rotX + 'deg) rotateY(' + rotY + 'deg) translateY(-6px)';
    });
    card.addEventListener('mouseleave', function () {
      card.style.transform = '';
    });
  });

  /* ---------- hero parallax ---------- */
  var heroVisual = document.querySelector('.hero-visual');
  var heroLogo = document.querySelector('.hero-logo-3d');
  if (heroVisual && canTilt) {
    var hero = document.querySelector('.hero');
    hero.addEventListener('mousemove', function (e) {
      var r = hero.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      heroVisual.style.transform = 'rotateY(' + (x * 10) + 'deg) rotateX(' + (-y * 8) + 'deg)';
      document.querySelectorAll('.float-chip').forEach(function (chip, i) {
        var depth = (i % 2 === 0 ? 18 : -14);
        chip.style.translate = (x * depth) + 'px ' + (y * depth) + 'px';
      });
    });
    hero.addEventListener('mouseleave', function () { heroVisual.style.transform = ''; });
  }

  /* ---------- 3D torus particle ring (canvas) ---------- */
  var canvas = document.getElementById('torusCanvas');
  if (canvas) {
    var ctx = canvas.getContext('2d');
    var W, H, DPR = Math.min(window.devicePixelRatio || 1, 2);
    var pts = [];
    var R = 150, r2 = 52, N = 420;
    for (var i = 0; i < N; i++) {
      var u = Math.random() * Math.PI * 2;
      var v = Math.random() * Math.PI * 2;
      pts.push({ u: u, v: v, s: 0.4 + Math.random() * 1.4, gold: Math.random() > 0.55 });
    }
    function resize() {
      W = canvas.clientWidth; H = canvas.clientHeight;
      canvas.width = W * DPR; canvas.height = H * DPR;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    }
    resize();
    window.addEventListener('resize', resize);
    var t = 0;
    var scrollFactor = 0;
    window.addEventListener('scroll', function () {
      scrollFactor = window.scrollY * 0.0012;
    }, { passive: true });
    (function draw() {
      t += 0.0042;
      ctx.clearRect(0, 0, W, H);
      var cx = W / 2, cy = H / 2;
      var scale = Math.min(W, H) / 470;
      var a = t * 1.4 + scrollFactor;       // rotX
      var b = t * 0.9 + scrollFactor * 1.6; // rotY
      var sinA = Math.sin(a), cosA = Math.cos(a), sinB = Math.sin(b), cosB = Math.cos(b);
      for (var i = 0; i < N; i++) {
        var p = pts[i];
        var u = p.u + t * 0.6, v = p.v + t * 1.1;
        var x = (R + r2 * Math.cos(v)) * Math.cos(u);
        var y = (R + r2 * Math.cos(v)) * Math.sin(u);
        var z = r2 * Math.sin(v);
        // rotate X
        var y1 = y * cosA - z * sinA;
        var z1 = y * sinA + z * cosA;
        // rotate Y
        var x2 = x * cosB + z1 * sinB;
        var z2 = -x * sinB + z1 * cosB;
        var persp = 420 / (420 + z2);
        var sx = cx + x2 * persp * scale;
        var sy = cy + y1 * persp * scale;
        var alpha = Math.max(0.08, Math.min(0.9, (z2 + 220) / 420));
        ctx.beginPath();
        ctx.arc(sx, sy, p.s * persp * scale, 0, Math.PI * 2);
        ctx.fillStyle = p.gold
          ? 'rgba(244,196,48,' + alpha + ')'
          : 'rgba(232,137,59,' + alpha + ')';
        ctx.fill();
      }
      requestAnimationFrame(draw);
    })();
  }

  /* ---------- contact form (Netlify Forms with graceful fallback) ---------- */
  var form = document.getElementById('contactForm');
  if (form) {
    var isHosted = location.protocol === 'http:' || location.protocol === 'https:';

    function buildMailto() {
      var get = function (n) {
        var el = form.querySelector('[name=' + n + ']');
        return el ? el.value.trim() : '';
      };
      var subject = encodeURIComponent('New project enquiry from ' + get('name') + ' — efzybastudio.com');
      var body = encodeURIComponent(
        'Name: ' + get('name') +
        '\nEmail: ' + get('email') +
        (get('phone') ? '\nPhone: ' + get('phone') : '') +
        (get('company') ? '\nCompany: ' + get('company') : '') +
        (get('service') ? '\nService: ' + get('service') : '') +
        (get('budget') ? '\nBudget: ' + get('budget') : '') +
        (get('timeline') ? '\nTimeline: ' + get('timeline') : '') +
        '\n\nMessage:\n' + get('message')
      );
      return 'mailto:emmanuel@efzybastudio.com?subject=' + subject + '&body=' + body;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = document.getElementById('formNote');
      var btn = document.getElementById('contactSubmit');

      // basic validation feedback
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      if (!isHosted) {
        // local preview — hand off to the user's email app instead
        window.location.href = buildMailto();
        if (note) note.textContent = '✦ Preview mode: your email app should open now. On the live site this submits directly.';
        return;
      }

      // hosted: AJAX-submit to Netlify Forms
      if (btn) { btn.disabled = true; btn.innerHTML = 'Sending… ⏳'; }
      var data = new FormData(form);
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(data).toString()
      }).then(function (res) {
        if (res.ok) {
          window.location.href = 'thank-you.html';
        } else {
          throw new Error('Form submit failed: ' + res.status);
        }
      }).catch(function () {
        // network/host issue — fall back to email so the lead is never lost
        if (btn) { btn.disabled = false; btn.innerHTML = 'Send Message <span class="arr">→</span>'; }
        if (note) note.textContent = '⚠ Direct submit unavailable — opening your email app instead. Or write to emmanuel@efzybastudio.com';
        window.location.href = buildMailto();
      });
    });
  }

  /* ---------- footer year ---------- */
  document.querySelectorAll('.year').forEach(function (y) {
    y.textContent = new Date().getFullYear();
  });
})();
