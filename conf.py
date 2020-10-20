# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from builtins import str
import re
#import sphinx_rtd_theme
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = u'NVIDIA Cloud Native Technologies'
copyright = u'2018-2020, NVIDIA Corporation'
author = u'NVIDIA Corporation'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
copybutton_prompt_text = "$ "
copybutton_only_copy_prompt_lines = False
extensions = [
    'sphinx.ext.ifconfig',
    'sphinx.ext.extlinks',
    'sphinx_copybutton',    
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# -- Options for Napoleon ----------------------------------------------------

napoleon_custom_sections = ['Supported backends']



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_logo = "assets/NVLogo_H_B&W.png"
html_theme_options = {
    'canonical_url': 'https://docs.nvidia.com/deeplearning/sdk/dali-developer-guide/',
    'collapse_navigation': False,
    'display_version': False,
    'logo_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# We remove the `_static` as we do not use it
html_static_path = []

# Download favicon and set it (the variable `html_favicon`) for this project.
# It must be relative path.
favicon_rel_path = "assets/nvidia.ico"
html_favicon = favicon_rel_path

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = [
    'js/google-analytics/google-analytics-tracker.js',
    'js/google-analytics/google-analytics-write.js',
    '//assets.adobedtm.com/b92787824f2e0e9b68dc2e993f9bd995339fe417/satelliteLib-7ba51e58dc61bcb0e9311aadd02a0108ab24cc6c.js',
]

def setup(app):
    count_unique_visitor_script = os.getenv("ADD_NVIDIA_VISITS_COUNTING_SCRIPT")
    if count_unique_visitor_script:
        app.add_js_file(count_unique_visitor_script)