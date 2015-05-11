'''
Making and testing colormaps.
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from skimage import color


def cmap(rgbin, N=10):
    '''
    Input an array of rgb values to generate a colormap.

    Inputs:
        rgbin is an [mx3] array, where m is the number of input color triplets which 
         are interpolated between to make the colormap that is returned. hex values
         can be input instead, as [mx1] in single quotes with a #.
        N is the number of levels to be interpolated to.
    '''

    # rgb inputs here
    if not mpl.cbook.is_string_like(rgbin[0]):
        # normalize to be out of 1 if out of 256 instead
        if rgbin.max() > 1:
            rgbin = rgbin/256.

    cmap = mpl.colors.LinearSegmentedColormap.from_list('mycmap', rgbin)

    return cmap


def test(cmap):
    '''
    Test colormap by plotting.
    Input a colormap instance. Use a named one with cm.get_cmap(colormap)
    '''

    # indices to step through colormap
    x = np.linspace(0.0, 1.0, 100)

    # will plot colormap and lightness
    rgb = cmap(x)[np.newaxis,:,:3]
    # rgb = cm.get_cmap(cmap)(x)[np.newaxis,:,:3]
    lab = color.rgb2lab(rgb)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, lab[0,:,0], c=x, cmap=cmap, s=300, linewidths=0.)


def read(varin):
    '''
    Read in dataset for variable var
    '''

    fname = 'MS09_L10.mat.txt'
    # fname = 'MS09_L05.mat.txt' # has PAR
    # fname = 'MS2_L10.mat.txt' # empty PAR

    d = np.loadtxt(fname, comments='*')

    if fname == 'MS2_L10.mat.txt':
        var = ['lat', 'lon', 'depth', 'temp', 'density', 'sigma', 'oxygen', 
                'voltage 2', 'voltage 3', 'fluorescence-CDOM', 'fluorescence-ECO', 
                'turbidity', 'pressure', 'salinity', 'RINKO temperature', 
                'RINKO DO - CTD temp', 'RINKO DO - RINKO temp', 'bottom', 'PAR']
    elif (fname == 'MS09_L05.mat.txt') or (fname == 'MS09_L10.mat.txt'):
        var = ['lat', 'lon', 'depth', 'temp', 'density', 'sigma', 'oxygen', 
                'voltage 2', 'voltage 3', 'voltage 4', 'fluorescence-CDOM', 'fluorescence-ECO', 
                'turbidity', 'pressure', 'salinity', 'RINKO temperature', 
                'RINKO DO - CTD temp', 'RINKO DO - RINKO temp', 'bottom', 'PAR']

    # return data for variable varin
    return d[:,0], d[:,1], d[:,2], d[:,var.index(varin)]


def show(cmap, var, vmin=None, vmax=None):
    '''
    Show a colormap for a chosen input variable var side by side with 
    black and white and jet colormaps.
    Inputs:
        cmap    colormap instance
        var     variable to plot. Choose from: 
    '''

    # get variable data
    lat, lon, z, data = read(var)

    fig = plt.figure(figsize=(16,12))

    # Plot with grayscale
    ax = fig.add_subplot(3,1,1)
    map1 = ax.scatter(lon, -z, c=data, cmap='gray', s=10, linewidths=0., vmin=vmin, vmax=vmax)
    plt.colorbar(map1, ax=ax)

    # Plot with jet
    ax = fig.add_subplot(3,1,2)
    map1 = ax.scatter(lon, -z, c=data, cmap='jet', s=10, linewidths=0., vmin=vmin, vmax=vmax)
    plt.colorbar(map1, ax=ax)

    # Plot with cmap
    ax = fig.add_subplot(3,1,3)
    map1 = ax.scatter(lon, -z, c=data, cmap=cmap, s=10, linewidths=0., vmin=vmin, vmax=vmax)
    ax.set_xlabel('Longitude [degrees]')
    ax.set_ylabel('Depth [m]')
    plt.colorbar(map1, ax=ax)

    plt.suptitle(var)
