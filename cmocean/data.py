'''
All functions related to actual data go in here. Probably only
people at TAMU will want to use this.
'''

import numpy as np
import matplotlib.pyplot as plt


# data files
fnames = ['MS09_L10.mat.txt', 'MS09_L05.mat.txt',
          'MS2_L10.mat.txt', 'MS08_L12.mat.txt']


def read(varin, fname='MS2_L10.mat.txt'):
    '''Read in dataset for variable var

    :param varin: Variable for which to read in data.

    '''

    # # fname = 'MS09_L10.mat.txt'
    # # fname = 'MS09_L05.mat.txt' # has PAR
    # fname = 'MS2_L10.mat.txt' # empty PAR

    d = np.loadtxt(fname, comments='*')

    if fname == 'MS2_L10.mat.txt':
        var = ['lat', 'lon', 'depth', 'temp', 'density', 'sigma', 'oxygen',
               'voltage 2', 'voltage 3', 'fluorescence-CDOM', 'fluorescence-ECO',
               'turbidity', 'pressure', 'salinity', 'RINKO temperature',
               'RINKO DO - CTD temp', 'RINKO DO - RINKO temp', 'bottom', 'PAR']
    elif (fname == 'MS09_L05.mat.txt') or (fname == 'MS09_L10.mat.txt') or (fname == 'MS08_L12.mat.txt'):
        var = ['lat', 'lon', 'depth', 'temp', 'density', 'sigma', 'oxygen',
               'voltage 2', 'voltage 3', 'voltage 4', 'fluorescence-CDOM', 'fluorescence-ECO',
               'turbidity', 'pressure', 'salinity', 'RINKO temperature',
               'RINKO DO - CTD temp', 'RINKO DO - RINKO temp', 'bottom', 'PAR']

    # return data for variable varin
    return d[:, 0], d[:, 1], d[:, 2], d[:, var.index(varin)]


def show(cmap, var, vmin=None, vmax=None):
    '''Show a colormap for a chosen input variable var side by side with
    black and white and jet colormaps.

    :param cmap: Colormap instance
    :param var: Variable to plot.
    :param vmin=None: Min plot value.
    :param vmax=None: Max plot value.

    '''

    # get variable data
    lat, lon, z, data = read(var)

    fig = plt.figure(figsize=(16, 12))

    # Plot with grayscale
    ax = fig.add_subplot(3, 1, 1)
    map1 = ax.scatter(lon, -z, c=data, cmap='gray', s=10, linewidths=0., vmin=vmin, vmax=vmax)
    plt.colorbar(map1, ax=ax)

    # Plot with jet
    ax = fig.add_subplot(3, 1, 2)
    map1 = ax.scatter(lon, -z, c=data, cmap='jet', s=10, linewidths=0., vmin=vmin, vmax=vmax)
    plt.colorbar(map1, ax=ax)

    # Plot with cmap
    ax = fig.add_subplot(3, 1, 3)
    map1 = ax.scatter(lon, -z, c=data, cmap=cmap, s=10, linewidths=0., vmin=vmin, vmax=vmax)
    ax.set_xlabel('Longitude [degrees]')
    ax.set_ylabel('Depth [m]')
    plt.colorbar(map1, ax=ax)

    plt.suptitle(var)


def plot_data():
    '''Plot sample data up with the fancy colormaps.

    '''

    var = ['temp', 'oxygen', 'salinity', 'fluorescence-ECO', 'density', 'PAR', 'turbidity', 'fluorescence-CDOM']
    # colorbar limits for each property
    lims = np.array([[26, 33], [0, 10], [0, 36], [0, 6], [1005, 1025], [0, 0.6], [0, 2], [0, 9]])  # reasonable values
    # lims = np.array([[20,36], [26,33], [1.5,5.6], [0,4], [0,9], [0,1.5]]) # values to show colormaps

    for fname in fnames:
        fig, axes = plt.subplots(nrows=4, ncols=2)
        fig.set_size_inches(20, 10)
        fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99, wspace=0.0, hspace=0.07)
        i = 0
        for ax, Var, cmap in zip(axes.flat, var, cmaps):  # loop through data to plot up

            # get variable data
            lat, lon, z, data = test.read(Var, fname)

            map1 = ax.scatter(lat, -z, c=data, cmap=cmap, s=10, linewidths=0., vmin=lims[i, 0], vmax=lims[i, 1])
            # no stupid offset
            y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)
            ax.xaxis.set_major_formatter(y_formatter)
            if i == 6:
                ax.set_xlabel('Latitude [degrees]')
                ax.set_ylabel('Depth [m]')
            else:
                ax.set_xticklabels([])
                ax.set_yticklabels([])
            ax.set_ylim(-z.max(), 0)
            ax.set_xlim(lat.min(), lat.max())
            cb = plt.colorbar(map1, ax=ax, pad=0.02)
            cb.set_label(cmap.name + ' [' + '$' + cmap.units + '$]')
            i += 1

        fig.savefig('figures/' + fname.split('.')[0] + '.png', bbox_inches='tight')
