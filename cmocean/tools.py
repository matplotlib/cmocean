'''
Plot up stuff with colormaps.
'''

import sys

import numpy as np
import matplotlib as mpl


_string_types = (str, np.str_)


def print_colormaps(cmaps, N=256, returnrgb=True, savefiles=False):
    '''Print colormaps in 256 RGB colors to text files.

    :param returnrgb=False: Whether or not to return the rgb array. Only makes sense to do if print one colormaps' rgb.

    '''

    rgb = []

    for cmap in cmaps:

        rgbtemp = cmap(np.linspace(0, 1, N))[np.newaxis, :, :3][0]
        if savefiles:
            np.savetxt(cmap.name + '-rgb.txt', rgbtemp)
        rgb.append(rgbtemp)

    if returnrgb:
        return rgb


def get_dict(cmap, N=256):
    '''Change from rgb to dictionary that LinearSegmentedColormap expects.
    Code from https://mycarta.wordpress.com/2014/04/25/convert-color-palettes-to-python-matplotlib-colormaps/
    and http://nbviewer.ipython.org/github/kwinkunks/notebooks/blob/master/Matteo_colourmaps.ipynb
    '''

    x = np.linspace(0, 1, N)  # position of sample n - ranges from 0 to 1

    rgb = cmap(x)

    # flip colormap to follow matplotlib standard
    if rgb[0, :].sum() < rgb[-1, :].sum():
        rgb = np.flipud(rgb)

    b3 = rgb[:, 2]  # value of blue at sample n
    b2 = rgb[:, 2]  # value of blue at sample n

    # Setting up columns for tuples
    g3 = rgb[:, 1]
    g2 = rgb[:, 1]

    r3 = rgb[:, 0]
    r2 = rgb[:, 0]

    # Creating tuples
    R = list(zip(x, r2, r3))
    G = list(zip(x, g2, g3))
    B = list(zip(x, b2, b3))

    # Creating dictionary
    k = ['red', 'green', 'blue']
    LinearL = dict(zip(k, [R, G, B]))

    return LinearL


def cmap(rgbin, N=256):
    '''Input an array of rgb values to generate a colormap.

    :param rgbin: An [mx3] array, where m is the number of input color triplets which
         are interpolated between to make the colormap that is returned. hex values
         can be input instead, as [mx1] in single quotes with a #.
    :param N=10: The number of levels to be interpolated to.

    '''

    # rgb inputs here
    if not isinstance(rgbin[0], _string_types):
        # normalize to be out of 1 if out of 256 instead
        if rgbin.max() > 1:
            rgbin = rgbin/256.

    cmap = mpl.colors.LinearSegmentedColormap.from_list('mycmap', rgbin, N=N)

    return cmap


def lighten(cmapin, alpha):
    '''Lighten a colormap by adding alpha < 1.

    :param cmap: A colormap object, like cmocean.cm.matter.
    :param alpha: An alpha or transparency value to assign the colormap. Alpha
        of 1 is opaque and of 1 is fully transparent.

    Outputs resultant colormap object.

    This will lighten the appearance of a plot you make using the output
        colormap object. It is also possible to lighten many plots in the
        plotting function itself (e.g. pcolormesh or contourf).
    '''

    # set the alpha value while retaining the number of rows in original cmap
    return cmap(cmapin(np.linspace(0,1,cmapin.N), alpha))


def crop(cmapin, vmin, vmax, pivot, N=None, dmax=None):
    '''Crop end or ends of a diverging colormap by vmin/vmax values.

    :param cmap: A colormap object, like cmocean.cm.matter.
    :param vmin/vmax: vmin/vmax for use in plot with colormap.
    :param pivot: center point to be used in plot with diverging colormap.
    :param N=None: User can specify the number of rows for the outgoing colormap.
        If unspecified, N from incoming colormap will be used and values will
        be interpolated as needed to fill in rows.
    :param dmax=None: dmax is the highest number to be included in a plot with
        the colormap; values higher in magnitude than dmax are removed from both
        ends of colormap. It should be less than abs(vmin) and abs(vmax), which
        should be equal for this parameter to be used.

    Outputs resultant colormap object.

    This function can be used for sequential and other non-diverging colormaps
        but it is easier to use that way through crop_by_percent().
    This should be useful for plotting bathymetry and topography data with the
        topo colormap when max bathymetry value is different from max topography.

    Example usage:
        # example for crop on min end of diverging colormap
        vmin = -2; vmax = 5; pivot = 0
        newcmap = crop(cmocean.cm.curl, vmin, vmax, pivot)
        A = np.random.randint(vmin, vmax, (5,5))
        plt.pcolormesh(A, vmin=vmin, vmax=vmax, cmap=newcmap)
        plt.colorbar()

        # example for crop on max end of diverging colormap
        vmin = -10; vmax = 8; pivot = 0
        newcmap = crop(cmocean.cm.delta, vmin, vmax, pivot)
        A = np.random.randint(vmin, vmax, (5,5))
        plt.pcolormesh(A, vmin=vmin, vmax=vmax, cmap=newcmap)
        plt.colorbar()

    '''

    assert pivot >= vmin and pivot <= vmax

    # dmax used if and only if ends are equal
    if vmax-pivot == pivot-vmin:
        assert dmax is not None

    # allow user to input N, but otherwise use N for incoming colormap
    if N is None:
        N = cmapin.N
    else:
        N = N

    # ratio of the colormap to remove
    below = pivot - vmin  # below pivot
    above = vmax - pivot  # above pivot

    ranges = (above, below)
    half_range = max(ranges)
    full_range = half_range*2
    reduced_range = min(ranges)
    range_to_keep = half_range + reduced_range

    ratio = (full_range-range_to_keep)/full_range


    if below < above:  # reducing colormap on side below pivot
        # start colormap partway through
        shortcmap = cmapin(np.linspace(0,1,N))[int(np.ceil(N*ratio)):]

    elif above < below:  # reducing colormap on side above pivot
        # end colormap early
        shortcmap = cmapin(np.linspace(0,1,N))[:-int(np.ceil(N*ratio))]

    elif (below == above) and (dmax is not None):  # equal
        ratio = dmax/full_range
        shortcmap = cmapin(np.linspace(0,1,N))[int(np.ceil(N*ratio)):-int(np.ceil(N*ratio))]

    # interpolate to original number of rows in colormap
    newrgb = np.zeros((N, 4))
    shnum = shortcmap.shape[0]
    for i in range(4):  # loop through each column of cmap
        newrgb[:,i] = np.interp(np.linspace(0,shnum,N), np.arange(0,shnum), shortcmap[:,i])

    newcmap = cmap(newrgb)

    return newcmap


def crop_by_percent(cmap, per, which='both', N=None):
    '''Crop end or ends of a colormap by per percent.

    :param cmap: A colormap object, like cmocean.cm.matter.
    :param per: Percent of colormap to remove. If which=='both', take this
        percent off both ends of colormap. If which=='min' or which=='max',
        take percent only off the specified end of colormap.
    :param which='both': which end or ends of colormap to cut off. which='both'
        removes from both ends, which='min' from bottom end, and which='max'
        from top end.
    :param N=None: User can specify the number of rows for the outgoing colormap.
        If unspecified, N from incoming colormap will be used and values will
        be interpolated as needed to fill in rows.

    Outputs resultant colormap object.

    This is a wrapper around crop() to make it easier to use for cropping
        based on percent.

    Examples:
        # example with oxy map: cut off yellow part which is top 20%
        # compare with full colormap
        vmin = 0; vmax = 10; pivot = 5
        A = np.random.randint(vmin, vmax, (5,5))
        fig, axes = plt.subplots(1, 2)
        mappable = axes[0].pcolormesh(A, vmin=vmin, vmax=vmax, cmap=cmocean.cm.oxy)
        fig.colorbar(mappable, ax=axes[0])
        vmin = 0; vmax = 8; pivot = 5
        newcmap = crop_by_percent(cmocean.cm.oxy, 20, which='max', N=None)
        plt.figure()
        plt.pcolormesh(A, vmin=vmin, vmax=vmax, cmap=newcmap)
        plt.colorbar()

        # example with oxy map: cut off red part which is bottom 20%
        # compare with full colormap
        vmin = 0; vmax = 10; pivot = 5
        A = np.random.randint(vmin, vmax, (5,5))
        fig, axes = plt.subplots(1, 2)
        mappable = axes[0].pcolormesh(A, vmin=vmin, vmax=vmax, cmap=cmocean.cm.oxy)
        fig.colorbar(mappable, ax=axes[0])
        vmin = 2; vmax = 10; pivot = 5
        A = np.random.randint(vmin, vmax, (5,5))
        newcmap = crop_by_percent(cmocean.cm.oxy, 20, which='min', N=None)
        plt.figure()
        plt.pcolormesh(A, vmin=vmin, vmax=vmax, cmap=newcmap)
        plt.colorbar()

        # crop both dark ends off colormap to reduce range
        newcmap = crop_by_percent(cmocean.cm.balance, 10, which='both', N=None)
        plt.figure()
        A = np.random.randint(-5, 5, (5,5))
        plt.pcolormesh(A, vmin=vmin, vmax=vmax, cmap=newcmap)
        plt.colorbar()

    '''

    if which == 'both':  # take percent off both ends of cmap
        vmin = -100; vmax = 100; pivot = 0
        dmax = per

    elif which == 'min':  # take percent off bottom of cmap
        vmax = 10; pivot = 5
        vmin = (0 + per/100)*2*pivot
        dmax = None

    elif which == 'max':  # take percent off top of cmap
        vmin = 0; pivot = 5
        vmax = (1 - per/100)*2*pivot
        dmax = None

    newcmap = crop(cmap, vmin, vmax, pivot, dmax=dmax, N=N)

    return newcmap
