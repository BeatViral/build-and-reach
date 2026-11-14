"""Generate the static homepage from editable copy and package configuration."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json

root = Path(__file__).resolve().parent
site = root / 'site'
config = json.loads((site / 'content.json').read_text(encoding='utf-8'))
email = config['email']
def contact(subject):
    return f'mailto:{email}?subject={quote(subject)}'

cards = []
summary = []
for pkg in config['packages']:
    update = pkg.get('update')
    update_html = ''
    if update:
        update_html = f'<div class="update-offer"><h4>Need an update later?</h4><p><strong>{escape(update["price"])} per small update.</strong> {escape(update["text"])}</p></div>'
    cards.append(f'''<article class="service package">
      <div class="card-top"><span>{escape(pkg['label'])}</span><span aria-hidden="true">↗</span></div>
      <h3>{escape(pkg['title'])}</h3>
      <p class="service-intro">{escape(pkg['intro'])}</p>
      <div class="service-package"><h4>{escape(pkg['name'])}</h4><div class="price">{escape(pkg['price'])}</div><p class="price-unit">{escape(pkg['unit'])}</p></div>
      <ul>{''.join('<li>'+escape(item)+'</li>' for item in pkg['items'])}</ul>
      {update_html}<p class="package-note">{escape(pkg['note'])}</p>
      <a class="button" href="{contact(pkg['subject'])}">{escape(pkg['cta'])}<span aria-hidden="true">↗</span></a>
    </article>''')
    summary.append(f'<a href="{contact(pkg["subject"])}"><strong>{escape(pkg["price"])}</strong><span>{escape(pkg["name"])}</span></a>')
html = (root / 'homepage.template.html').read_text(encoding='utf-8')
html = html.replace('{{SERVICE_CARDS}}', ''.join(cards)).replace('{{PRICE_SUMMARY}}', ''.join(summary))
# Keep every public enquiry address in sync with the configuration.
html = html.replace('mahmoodkhanteam@gmail.com', email)
(site / 'index.html').write_text(html, encoding='utf-8')
print('Generated homepage with three clear service packages.')
