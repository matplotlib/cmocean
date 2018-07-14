'''
Test some basic functions of the colormaps.
'''

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def test_cmap_import():
    '''Can we import colormaps and make basic plot.

    '''

    from cmocean import cm
    # Loop through all methods in cmocean.
    for name, cmap in vars(cm).items():
        # See if it is a colormap.
        if isinstance(cmap, matplotlib.colors.LinearSegmentedColormap):
            print(name)
            x = np.linspace(0, 10)
            X, _ = np.meshgrid(x, x)
            plt.figure()
            plt.pcolor(X, cmap=cmap)
            plt.title(name)
            plt.close(plt.gcf())
