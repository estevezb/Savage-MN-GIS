Title: Trusted GIS Data Sources
Date: 2024-07-11
Tags: GIS, data, search, brython
Category: GIS Data Sources
Slug: trusted-gis-data-sources
Image_URL: static/images/Data_icon.png
Author: Brian Estevez


<img src= "{static}/images/GIS_DataSources.png" alt ="Data Sources Used in Geographic Information Sciences" style= " width 350px; height: 350px;">


## **Disaster in Dominica**

This page provides an interactive interface to search and filter a curated collection of trusted GIS data sources. Use the search box to find sources by name, description, or tags (e.g., "Hydrology", "Minnesota", "National").

<div id="search-container">
  <input id="search-input" type="text" placeholder="Type to search GIS sources..." style="width: 100%; padding: 8px; margin-bottom: 1em;" />
  <div id="search-results"></div>
  <!-- Hidden container (optional) to keep raw data if needed -->
  <div id="data-container" style="display: none;"></div>
</div>

<!-- Include Brython libraries -->
<script src="https://cdn.jsdelivr.net/npm/brython@3.9.5/brython.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/brython@3.9.5/brython_stdlib.js"></script>

<!-- Brython code to load data, perform fuzzy search via difflib, and render results -->
<script type="text/python">
from browser import document, ajax, console, html
import json, difflib

# Global variable to hold our GIS data sources
gis_sources = []

def load_data(ev):
    def on_complete(req):
        if req.status in (200, 0):
            try:
                global gis_sources
                gis_sources = json.loads(req.text)
                console.log("GIS data loaded successfully!")
            except Exception as e:
                console.log("Error parsing JSON data:", e)
        else:
            console.log("Failed to load GIS data, status code:", req.status)
    req = ajax.Ajax()
    req.bind('complete', on_complete)
    # Ensure the path here correctly points to the JSON file relative to your site's root.
    req.open('GET', '/GIS_Data_Sources/data/gis_sources.json', True)
    req.send()

def render_results(matches):
    results_div = document['search-results']
    results_div.clear()
    # Display up to a maximum of 10 results at a time.
    for source in matches[:10]:
        entry = html.DIV()
        entry.innerHTML = (
            f"<strong>{source['name']}</strong>: {source.get('description', 'No description available.')}"
            f" <br> <a href='{source['url']}' target='_blank'>Visit</a>"
        )
        if 'tags' in source:
            tags_str = ", ".join(source['tags'])
            entry.innerHTML += f"<br><em>Tags:</em> {tags_str}"
        entry.style.marginBottom = "1em"
        results_div <= entry

def search(ev):
    query = document['search-input'].value.lower().strip()
    if not query:
        document['search-results'].clear()
        return

    # Use difflib to attempt fuzzy matching on source names
    names = [source['name'].lower() for source in gis_sources]
    close_matches = difflib.get_close_matches(query, names, n=10, cutoff=0.3)
    matches = [source for source in gis_sources if source['name'].lower() in close_matches]

    # Additionally, check if the query is present in any tags or descriptions.
    for source in gis_sources:
        # Search within tags
        if 'tags' in source and any(query in tag.lower() for tag in source['tags']):
            if source not in matches:
                matches.append(source)
        # Search within the description text
        if 'description' in source and query in source['description'].lower():
            if source not in matches:
                matches.append(source)
                
    render_results(matches)

# Initialize the data loading and bind the search event to the input.
load_data(None)
document['search-input'].bind('input', search)
</script>