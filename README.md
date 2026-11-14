# Build & Reach

Static Australian business website for practical AI education, web design and personalised outreach. No framework, backend, analytics or tracking cookies.

## Files and editing
- `site/index.html`: generated, deployment-ready homepage.
- `site/styles.css`: responsive styles, self-hosted fonts and brand variables.
- `site/app.js`: accessible mobile navigation.
- `site/content.json`: edit all package prices and inclusions here, then run `python build_site.py`.
- `build_site.py`: edit homepage text, service lists and portfolio records, then regenerate. Existing `content.json` values are preserved.
- `site/assets/`: original light/dark SVG wordmarks and compact marks, favicon, social PNG (1200 x 630), screenshots, fonts and OFL licences.
- `site/privacy.html`: edit privacy text directly.
- `site/robots.txt`, `site/sitemap.xml`: crawler files.
- `.github/workflows/pages.yml`: automatic Pages deployment on pushes to main.

To add a portfolio example, add a record in the generator's `projects` list and a preview theme in CSS. Five thumbnails are genuine captures of the supplied public websites. Outreach Mania uses a typographic preview and has no repository link because public availability was not confirmed.

Update contact details in `build_site.py` and `site/privacy.html`. Update SVGs in assets and CSS variables for branding. Run `pwsh -File make-social.ps1` to regenerate the sharing image on Windows. Font files are self-hosted and licensed under the included OFL texts.

## Local preview
Run `python -m http.server 4174 --directory site` and visit http://127.0.0.1:4174/.

## GitHub Pages
Repository: https://github.com/BeatViral/build-and-reach

Public URL: https://beatviral.github.io/build-and-reach/

Pages uses GitHub Actions as its publishing source. The workflow uploads only `site/` and deploys it on every main push. No runtime build is necessary because generated HTML is committed. After content edits, regenerate before committing.

## Custom domain later
No DNS or custom-domain changes have been made. When approved, configure the domain in repository Pages settings and add `site/CNAME`. Update canonical, Open Graph, Twitter image and JSON-LD URLs in the generator, privacy page, robots.txt and sitemap.xml. Regenerate and deploy. Relative assets support both the repository subpath and domain root.

## Accuracy
Descriptions and outreach examples come from the owner. Outcomes distinguish discussions, submissions and interview interest from contracted partnerships. No testimonials, ratings, guaranteed leads, booking calendar or form backend are fabricated.
