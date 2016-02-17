'''
cmocean is a package to help standardize colormaps for commonly-plotted
oceanographic properties.

See README.md for an overview on instructions.
'''

from __future__ import absolute_import

# from cmocean import *
from . import cm, tools, plots, data

__all__ = ['cm',
           'tools',
           'plots',
           'data']

__authors__ = ['Kristen Thyng <kthyng@tamu.edu>']

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
