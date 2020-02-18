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
import os, sys
import os.path
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('../src/'))
sys.path.insert(0, os.path.abspath('../src/func/'))
sys.path.insert(0, os.path.abspath('../comps/'))


# -- Project information -----------------------------------------------------

project = 'Mechatronic'
copyright = '2020, David Muñoz Bernal, Universidad Rey Juan Carlos'
author = 'David Muñoz Bernal'

version = '12 Sep 2019'
release = '0.2.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_rtd_theme', #tema
              'sphinx.ext.todo',
              'sphinx.ext.githubpages',
              'sphinx.ext.autodoc', #lectura automática desde la documentación en código
              'sphinx.ext.autosummary'] #generación automática de tablas con la documentación
              # 'sphinxcontrib.contentui'] #permite cambio desplegables y cambio de idioma

# The master toctree document.
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '../comps/doc', '../comps/freecad', '../comps/step', '../comps/stl']

# List of Imports to ignore
autodoc_mock_imports = ["PySide",
                        "FreeCAD",
                        "FreeCADGui",
                        "Part",
                        "Draft",
                        "DraftVecUtils",
                        "DraftGeomUtils",
                        "Mesh",
                        "MeshPart"]
autoclass_content = "both"


# lenguage = 'es'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_logo = '../icons/Mechatronic.png'
logo_only = True 