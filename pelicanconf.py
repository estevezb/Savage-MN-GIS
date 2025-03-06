from pelican import signals
from pelican_jupyter import markup as nb_markup
AUTHOR = 'Brian Estevez'
SITENAME = 'Savage, MN GIS'
SITEURL = '/'

ARTICLE_URL= 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL= 'pages/{slug}.html'
PAGE_SAVE_AS= 'pages/{slug}.html'

# CATEGORY_URL = 'category/{slug}.html'  # will use category as a page 
# CATEGORY_SAVE_AS = 'category/{slug}.html'

# Pelican writes the categories listing to docs/index.html
CATEGORIES_SAVE_AS = 'index.html'    

# categories page is served at the root URL (/), effectively becoming the home page.
CATEGORIES_URL = ''


OUTPUT_PATH = 'docs/'
PATH = "content"
THEME = "notmyidea"
TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("NOAA Storm Prediction Center", "https://www.spc.noaa.gov/products/outlook/day1otlk.html"),
    ("Active Weather Hazards", "https://www.weather.gov/"),
    ("My Github Page", "https://github.com/estevezb"),
    #("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Twitter/X", "https://x.com/bestevez100"),
    #("Another social link", "#"),
)

DEFAULT_PAGINATION = 5

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

# MENUITEMS = (
#     ('About Me', 'pages/about-me.html'),
#     ('Python Examples', 'category/python-examples.html'),
#     ('Tornado Analysis', 'category/tornado-analysis.html'),
# )
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

MARKUP = ("md", "ipynb")

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites', nb_markup]
IGNORE_FILES = [".ipynb_checkpoints"]
IPYNB_MARKUP_USE_FIRST_CELL = True








STATIC_PATHS = ['static', 'images']

I18N_TEMPLATES_LANG = 'en'

BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'
FAVICON = 'static/images/favicon-48x48.png'

EXTRA_PATH_METADATA = {
    'static/images/favicon-48x48.png': {'path': 'favicon-48x48.png'}
}



IGNORE_FILES = ["map.html", "map_template.html"]

# Disable the default blog index
# INDEX_SAVE_AS = 'index.html' # disabled to prevent recent blog page format being created

INDEX_SAVE_AS = '' 
INDEX_URL = ''
#tells Pelican not to create index.html for recent posts

THEME_TEMPLATES_OVERRIDES = ['templates']