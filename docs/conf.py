"""Sphinx configuration."""

project = "The Python OCSF Library"
author = "River Studio"
copyright = "2025, River Studio"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
