# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

<<<<<<< HEAD
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'galmorph'
copyright = '2025, Priyatam Kumar, Shahd Moghazy and Mitali Damle'
author = 'Priyatam Kumar, Shahd Moghazy and Mitali Damle'
=======
import os
import sys
sys.path.insert(0, os.path.abspath('../galmorph/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GalMorph'
copyright = '2025, Mitali Damle'
author = 'Mitali Damle'
root_doc = 'index'

>>>>>>> refs/remotes/origin/main
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

<<<<<<< HEAD
extensions = []
=======
extensions = ['sphinx.ext.autodoc','sphinx.ext.napoleon']
>>>>>>> refs/remotes/origin/main

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

<<<<<<< HEAD
html_theme = 'alabaster'
=======
html_theme = "sphinx_rtd_theme"
>>>>>>> refs/remotes/origin/main
html_static_path = ['_static']
