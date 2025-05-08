# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import ablog

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# The "title" for the blog, used in active pages.  Default is ``'Blog'``.
blog_title = "Nate Overton-Katz site"

# Base URL for the website, required for generating feeds.
blog_baseurl = "https::/example.com"


project = 'Nate Overton-Katz site'
copyright = '2025, Nate Overton-Katz'
author = 'Nate Overton-Katz'
#release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.extlinks',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'ablog', # blog setup
              "myst_parser" # support markdown
              ]

templates_path = ['_templates']
exclude_patterns = []
# default coding language
highlight_language = 'c++'

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# -- Blog Post Related --------------------------------------------------------

#post_date_format = '%%m %%d, %%Y'
post_auto_excerpt = 1
# html_sidebars = {'**': ["about.html",
#                         'ablog/postcard.html', 'navigation.html',
#                         'ablog/recentposts.html', 'ablog/tagcloud.html',
#                         'ablog/categories.html',  'ablog/archives.html',
#                         'searchfield.html']
#     }
html_sidebars = {'**': ['ablog/postcard.html',
                        'ablog/recentposts.html', 'ablog/tagcloud.html',
                        'ablog/categories.html',  'ablog/archives.html',
                        ]
    }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_documatt_theme'
#html_theme = 'alabaster'
#html_theme = 'furo'
html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
