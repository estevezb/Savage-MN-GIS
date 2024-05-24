from pelican import signals

AUTHOR = 'Brian Estevez'
SITENAME = 'Fly in the Ointment'
SITEURL = '/'

ARTICLE_URL= 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL= 'pages/{slug}.html'
PAGE_SAVE_AS= 'pages/{slug}.html'

OUTPUT_PATH = 'docs/'
PATH = "content"
THEME = "pelican-themes/pelican-bootstrap3"
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

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

I18N_TEMPLATES_LANG = 'en'

BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'monokai'
FAVICON = 'images/favicon.ico'