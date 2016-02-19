#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

ARTICLE_PATHS= ['blog']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
AUTHOR = 'Linux Audio Users Berlin'
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
SITENAME = 'linuxaudio.berlin'
SITEURL = 'http://linuxaudio.berlin'
SITESUBTITLE = "Linux Audio Users Berlin"

PATH = 'content'
PATH_METADATA = 'pages/(?P<path>.*)\..*' # Make pages top-level (remove /pages/ from each URL)

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Linux Audio', 'http://linuxaudio.org/'),
         ('Linux Audio Conference', 'http://lac.linuxaudio.org/'),
         ('miniLAC', 'http://minilac.linuxaudio.org/'),
         ('c-base', 'http://c-base.org'),
         ('Mailing list', 'http://linuxaudio.berlin/mailman/listinfo/discuss'),)

# Social widget
SOCIAL = (('LAUB Twitter', 'https://twitter.com/LAudioBerlin'),
        ('Linux Audio Twitter', 'https://twitter.com/LinuxAudio'),
        ('LAUB Github', 'https://github.com/linux-audio-berlin/'),)

LOAD_CONTENT_CACHE = False
MENUITEMS = ()
DEFAULT_PAGINATION = 10

# Plugins
PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['pelican-page-hierarchy']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
SLUGIFY_SOURCE = 'basename'

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
