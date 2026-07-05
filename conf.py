import os
import sys


for _candidate in ['../fenn', 'fenn']:
    _p = os.path.abspath(_candidate)
    if os.path.exists(os.path.join(_p, 'fenn', '__init__.py')):
        sys.path.insert(0, _p)
        break

# -- Project information -----------------------------------------------------
project = "fenn"
copyright = "2026, pyfenn"
author = "pyfenn"
master_doc = "index"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.inheritance_diagram",
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
    "sphinxcontrib.mermaid",
]

# MyST Parser settings — enable all common extensions
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
]

# Tell Sphinx to look in src/ for the existing MkDocs markdown content
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

autodoc_typehints = "description"
autodoc_type_aliases = {}
autosummary_generate = True
autosummary_imported_members = False
inheritance_graph_attrs = {"rankdir": "TB"}

html_css_files = ["custom.css"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_title = "Fenn Documentation"
html_logo = "_static/logo.png"
html_favicon = "_static/icon.svg"
html_theme_options = {
    "source_repository": "https://github.com/pyfenn/dev-docs",
    "source_branch": "main",
    "source_directory": "",
    "light_css_variables": {
        "color-brand-primary": "#00A86B",
        "color-brand-content": "#00A86B",
    },
    "dark_css_variables": {
        "color-brand-primary": "#00C887",
        "color-brand-content": "#00C887",
    },
}