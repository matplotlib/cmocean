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
from matplotlib import colors, cm

from . import tools

# Location of rgb files
datadir = os.path.join(os.path.split(__file__)[0], 'rgb')

# List of colormap names
cmapnames = ['thermal', 'haline', 'solar', 'ice', 'gray', 'oxy', 'deep',
             'dense', 'algae', 'matter', 'turbid', 'speed', 'amp', 'tempo',
             'rain', 'phase', 'topo', 'balance', 'delta', 'curl', 'diff', 'tarn']

# initialize dictionary to contain colormaps
cmap_d = dict()

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
    reg_map = colors.ListedColormap(rgb_with_alpha, 'cmo.' + cmapname, rgb.shape[0])
    cm.register_cmap(cmap = reg_map)

    # Register the reversed map
    reg_map_r = colors.ListedColormap(rgb_with_alpha[::-1,:], 'cmo.' + cmapname + '_r', rgb.shape[0])
    cm.register_cmap(cmap = reg_map_r)

# make colormaps available to call
locals().update(cmap_d)
