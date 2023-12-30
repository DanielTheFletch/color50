# Daniel Fletcher
# Harvard CS50P 2023
# Final Project

# conf.py
# Configuration file for Sphinx documentation builder

import os
import sys
sys.path.insert(0, os.path.abspath('../../color50/'))

# General configuration
project = 'color50'
copyright = '2023, Daniel Fletcher'
author = 'Daniel Fletcher'
version = '1.0'
release = '1.0'

# Extension settings
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# Path settings
templates_path = ['_templates']

# Output settings
html_theme = 'sphinx_rtd_theme'
epub_show_urls = 'footnote'
