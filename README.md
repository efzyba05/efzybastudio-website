# Efzyba Studio — Agency Website

Futuristic multi-page agency website for **Efzyba Studio** (efzybastudio.com).
Pure static HTML/CSS/JS — no build step, no dependencies. Deploys anywhere.

## Structure

| Path | What it is |
|---|---|
| `index.html` | Home page (3D hero, services, portfolio, team, blog previews) |
| `about.html` | Story, team, tech stack |
| `services.html` | 15 services + pricing + FAQ |
| `portfolio.html` + `case-*.html` | Portfolio grid + 6 case studies |
| `blog.html` + `blog-*.html` | Blog index + 6 SEO articles |
| `contact.html` | Contact info + form (mailto) |
| `assets/css/style.css` | All styling (brand colors, animations, responsive) |
| `assets/js/main.js` | Interactions: 3D torus, tilt cards, cursor, reveals, counters |
| `assets/img/` | Logo, team photos, project & blog images |
| `_build/` | Optional Python generators used to create the pages (not required for hosting) |

## Editing

Small edits: open any `.html` file and edit the text directly — every page is plain HTML.

Colors / fonts / spacing: edit the CSS variables at the top of `assets/css/style.css` (`:root` block).

Regenerating pages (optional): the `_build/*.py` scripts can rebuild pages from templates.
Run them from inside `_build/`: `python3 build_index.py` etc.

## Deploy

Connected to Netlify — every push to `main` auto-deploys.
