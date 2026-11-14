from pathlib import Path
import re,json,xml.etree.ElementTree as ET
from html.parser import HTMLParser
class Check(HTMLParser):
 def __init__(self): super().__init__();self.ids=set();self.links=[];self.h1=0;self.schema=False
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d: assert d['id'] not in self.ids; self.ids.add(d['id'])
  if tag=='h1':self.h1+=1
  if tag=='a':self.links.append(d.get('href',''))
  if tag in ['img','script','link']:
   target=d.get('src',d.get('href',''))
   if target and not re.match(r'https?:|mailto:|#',target):assert (Path('site')/target).exists(),target
  if tag=='img': assert d.get('alt') is not None
h=Path('site/index.html').read_text(encoding='utf-8');c=Check();c.feed(h)
assert c.h1==1
for x in c.links:
 if x.startswith('#'):assert x[1:] in c.ids,x
 if x.startswith('mailto:'):assert x.startswith('mailto:mahmoodkhanteam@gmail.com')
json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',h).group(1))
ET.parse('site/sitemap.xml')
assert h.count('class="package"')==4
assert h.count('class="project"')==6
assert 'outreach-mania' not in h
assert 'https://fonts.googleapis.com' not in Path('site/styles.css').read_text()
print('PASS: assets, anchor targets, unique H1/IDs, mailto URLs, structured data, sitemap, four packages and six projects')
