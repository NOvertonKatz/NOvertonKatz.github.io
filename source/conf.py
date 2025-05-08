### Project information
project = "Nate Overton-Katz site"
copyright = "2025, Nate Overton-Katz"
author = "Nate Overton-Katz"
html_title = "Nate Overton-Katz site"


#file system and favicon:
html_static_path = ["_static"]
templates_path = ["_templates"]
html_css_files = ["css/custom.css"]
#html_favicon = "_static/images/logo.ico"

html_sidebars = {
    "index": ["about.html"],
    "about": ["about.html"],
    "projects": ["about.html"],
    "blog": ["ablog/categories.html", "ablog/tagcloud.html", "ablog/archives.html"],
    "blog/**": ["ablog/postcard.html", "ablog/recentposts.html", "ablog/archives.html"],
}

# load extensions
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'ablog', # blog setup
    "myst_parser" # support markdown
    ]

# specify project details
master_doc = "index"

# basic build settings
exclude_patterns = [
    "_build"
]

nitpicky = True

# Add theme
html_theme = "pydata_sphinx_theme"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/NOvertonKatz",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/nate-overton-katz-phd-66278591",
            "icon": "fa-brands fa-linkedin",
        },
    ],
}

### MyST
myst_enable_extensions = [
    "colon_fence", # ::: syntax
    "deflist", #Definitiopn lists
    "html_image", # to add <html> tags with more flexibility
    "tasklist" #Dynamic lists
]

### ABlog

blog_title = "Nate Overton-Katz site"
blog_path = "posts"
blog_post_pattern = "posts/*/*"
blog_feed_fulltext = True
blog_feed_subtitle = "Data Analysis, GIS and career transition advice."
fontawesome_included = True
post_redirect_refresh = 1
post_auto_image = 1
post_auto_excerpt = 2
