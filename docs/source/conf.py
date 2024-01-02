# Daniel Fletcher
# Harvard CS50P 2024
# Final Project

# conf.py
# Configuration file for Sphinx documentation builder

# Configure path to include package parent directory
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# General documentation settings
author = 'Daniel Fletcher'
copyright = '2024, Daniel Fletcher'
project = 'color50'
release = '1.0.0'
version = '1.0.0'

# Configure extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

# Additional paths
templates_path = ['_templates']

# HTML output
html_theme = 'sphinx_rtd_theme'
html_title = 'color50 docs'

# PDF / EPUB output
epub_show_urls = 'footnote'
