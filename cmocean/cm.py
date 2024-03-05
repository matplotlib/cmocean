'''
Standardized colormaps for oceanography plots.

Used tool from http://bids.github.io/colormap/ to make perceptually correct
colormaps.

Created by Kristen Thyng
2016-06-18
'''

from __future__ import absolute_import

import numpy as np
import os
from matplotlib import colors
import matplotlib as mpl
from packaging.version import Version
from importlib.metadata import version
from . import tools

# Location of rgb files
datadir = os.path.join(os.path.split(__file__)[0], 'rgb')

# List of colormap names
cmapnames = ['thermal', 'haline', 'solar', 'ice', 'gray', 'oxy', 'deep',
             'dense', 'algae', 'matter', 'turbid', 'speed', 'amp', 'tempo',
             'rain', 'phase', 'topo', 'balance', 'delta', 'curl', 'diff', 'tarn']

# initialize dictionary to contain colormaps
cmap_d = dict()


# a comparable version object
MPL_VERSION = Version(version("matplotlib"))

def _register_cmap(cmap, *, name):
    # wrap matplotlib.cm API, use non-deprecated API when available
    if MPL_VERSION >= Version("3.5"):
        mpl.colormaps.register(cmap, name=name)
    else:
        # deprecated API
        mpl.cm.register_cmap(name=name, cmap=cmap)

# add colormaps and reversed to dictionary
for cmapname in cmapnames:
    rgb = np.loadtxt(os.path.join(datadir, cmapname + '-rgb.txt'))
    cmap_d[cmapname] = tools.cmap(rgb, N=256)
    cmap_d[cmapname].name = cmapname
    cmap_d[cmapname + '_r'] = tools.cmap(rgb[::-1, :], N=256)
    cmap_d[cmapname + '_r'].name = cmapname + '_r'

    # Register the cmap with matplotlib
    rgb_with_alpha = np.zeros((rgb.shape[0],4))
    rgb_with_alpha[:,:3] = rgb
    rgb_with_alpha[:,3]  = 1.  #set alpha channel to 1
    reg_map = colors.ListedColormap(rgb_with_alpha, N=rgb.shape[0])
    _register_cmap(reg_map, name=f'cmo.{cmapname}')

    # Register the reversed map
    reg_map_r = colors.ListedColormap(rgb_with_alpha[::-1,:], N=rgb.shape[0])
    _register_cmap(reg_map_r, name=f'cmo.{cmapname}_r')

    # Load inverted cmaps
    rgb_i = np.loadtxt(os.path.join(datadir, 'inverted', cmapname + '_i-rgb.txt'))
    cmap_d[cmapname + '_i'] = tools.cmap(rgb_i, N=256)
    cmap_d[cmapname + '_i'].name = cmapname + '_i'
    cmap_d[cmapname + '_r_i'] = tools.cmap(rgb_i[::-1, :], N=256)
    cmap_d[cmapname + '_r_i'].name = cmapname + '_r_i'
    rgb_with_alpha = np.zeros((rgb_i.shape[0],4))
    rgb_with_alpha[:,:3] = rgb_i
    rgb_with_alpha[:,3]  = 1.  #set alpha channel to 1

    # Register inverted cmaps
    reg_map_i = colors.ListedColormap(rgb_with_alpha, N=rgb_i.shape[0])
    _register_cmap(reg_map_i, name=f'cmo.{cmapname}_i')
    reg_map_r_i = colors.ListedColormap(rgb_with_alpha[::-1,:], N=rgb_i.shape[0])
    _register_cmap(reg_map_r_i, name=f'cmo.{cmapname}_r_i')

    # order shouldn't matter
    cmap_d[cmapname + '_i_r'] = cmap_d[cmapname + '_r_i']
    _register_cmap(reg_map_r_i, name=f'cmo.{cmapname}_i_r')

# make colormaps available to call
locals().update(cmap_d)
