# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ennoia'
copyright = 'Copyright &#169; Jake Tanis'
author = 'Jacob Kenneth Tanis'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.openapi',
    'sphinx_copybutton',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'shibuya'
html_theme_options = {
    'color_mode': 'light',
    'accent_color': 'gold',
    'nav_socials': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/jaketanis/ennoia',
            'icon': 'simple-icons:github',
        }
    ]
}
html_static_path = ['_static']

html_css_files = [
    'custom.css',
]
