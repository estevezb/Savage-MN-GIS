Title: Trusted GIS Data Sources
Date: 2024-07-11
Tags: GIS, data, search, brython
Category: GIS Data Sources
Slug: trusted-gis-data-sources
Image_URL: static/images/Data_icon.png
Author: Brian Estevez


![Data Sources]({static}/images/GIS_DataSources.png){style="width:350px; height:350px;"}

## Query Data Sources Below

<div id="search-container">
  <input id="search-input" type="text" placeholder="Type to search…" style="width:100%;padding:8px;margin-bottom:1em;" />
  <div id="search-results"></div>
</div>

<!-- Brython runtime -->
<script src="https://cdn.jsdelivr.net/npm/brython@3.9.5/brython.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/brython@3.9.5/brython_stdlib.js"></script>

<!-- Your Python code -->
<script type="text/python">
from browser import document, ajax, console, html
import json, difflib

gis_sources = []

def load_data(ev):
    def on_complete(req):
        if req.status in (200,0):
            gis_sources[:] = json.loads(req.text)
            console.log(f"Loaded {len(gis_sources)} sources")
        else:
            console.log("Fetch failed", req.status)
    req = ajax.Ajax()
    req.bind('complete', on_complete)
    # if this page is under /pages/, keep the "../"; else just "static/…"
    req.open('GET', '../static/data/gis_sources.json', True)
    req.send()

def render_results(ms):
    out = document['search-results']
    out.clear()
    for s in ms[:10]:
        d = html.DIV()
        d.innerHTML = (
          f"<strong>{s['name']}</strong>: {s.get('description','')}<br>"
          f"<a href='{s['url']}' target='_blank'>Visit</a>"
        )
        if 'tags' in s:
            d.innerHTML += "<br><em>Tags:</em> " + ", ".join(s['tags'])
        out <= d

def search(ev):
    q = document['search-input'].value.lower().strip()
    if not q:
        document['search-results'].clear()
        return
    names = [s['name'].lower() for s in gis_sources]
    close = difflib.get_close_matches(q, names, n=10, cutoff=0.3)
    matches = [s for s in gis_sources if s['name'].lower() in close]
    for s in gis_sources:
        if 'tags' in s and any(q in t.lower() for t in s['tags']) and s not in matches:
            matches.append(s)
        if 'description' in s and q in s['description'].lower() and s not in matches:
            matches.append(s)
    render_results(matches)

load_data(None)
document['search-input'].bind('input', search)
</script>

<!-- Initialize Brython _after_ your Python block -->
<script> brython(); </script>