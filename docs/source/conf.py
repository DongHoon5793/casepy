# Configuration file for the Sphinx documentation builder.

import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.join("..", "..")))
sys.path.append(os.path.abspath("../../src"))
import casepy as casepy

print(casepy.__version__)

# -- Project information

project = "casepy"
copyright = "2024, DongHoon Kim"
author = "DongHoon Kim"

release = "0.2"
version = "0.2.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"
