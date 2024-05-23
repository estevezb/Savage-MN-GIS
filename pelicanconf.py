AUTHOR = 'Brian Estevez'
SITENAME = 'Fly in the Ointment'
SITEURL = "/"

ARTICLE_URL= 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'
PAGE_URL= 'pages/{slug}.html'
PAGE_SAVE_AS= 'pages/{slug}.html'

OUTPUT_PATH = 'docs/'
PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("NOAA Stprm Prediction Center", "https://www.spc.noaa.gov/"),
    ("Active Weather Hazards", "https://www.weather.gov/"),
    ("My Github Page", "https://github.com/estevezb"),
    #("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("https://x.com/bestevez100", "#"),
    #("Another social link", "#"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True