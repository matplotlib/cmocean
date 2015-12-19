'''
Plots with colormaps.
'''

from __future__ import absolute_import

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
# from skimage import color

from . import cm
from . import tools


mpl.rcParams.update({'font.size': 14})
mpl.rcParams['font.sans-serif'] = 'Arev Sans, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Helvetica, Avant Garde, sans-serif'
mpl.rcParams['mathtext.fontset'] = 'custom'
mpl.rcParams['mathtext.cal'] = 'cursive'
mpl.rcParams['mathtext.rm'] = 'sans'
mpl.rcParams['mathtext.tt'] = 'monospace'
mpl.rcParams['mathtext.it'] = 'sans:italic'
mpl.rcParams['mathtext.bf'] = 'sans:bold'
mpl.rcParams['mathtext.sf'] = 'sans'
mpl.rcParams['mathtext.fallback_to_cm'] = 'True'

# import pdb; pdb.set_trace()
# # list of colormaps for several functions
# cmaps = [cmocean.temp, cmocean.o2, cmocean.salinity, cmocean.chl,
#          cmocean.rho, cmocean.par, cmocean.turb, cmocean.cdom]
            # cmocean.bathy, cmocean.s, cmocean.v, cmocean.vort,
            # cmocean.eta]

cmaps = cm.cmall


def plot_lightness(saveplot=False):
    '''Plot lightness of colormaps together.

    '''

    from colorspacious import cspace_converter

    dc = 1.
    x = np.linspace(0.0, 1.0, 256)
    locs = []  # locations for text labels

    fig = plt.figure(figsize=(16, 6))
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.1, len(cmaps) + 0.1)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Lightness for each colormap')

    for j, cmap in enumerate(cmaps):
        rgb = cmap(x)[np.newaxis, :, :3]
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        # lab = color.rgb2lab(rgb)
        L = lab[0, :, 0]
        # import pdb; pdb.set_trace()
        # L = lab[0, :, 0]
        if L[-1] > L[0]:
            ax.scatter(x+j*dc, L, c=x, cmap=cmap, s=300, linewidths=0.)
        else:
            ax.scatter(x+j*dc, L[::-1], c=x[::-1], cmap=cmap, s=300, linewidths=0.)
        locs.append(x[-1]+j*dc)  # store locations for colormap labels

    # Set up labels for colormaps
    ax.xaxis.set_ticks_position('top')
    ticker = mpl.ticker.FixedLocator(locs)
    ax.xaxis.set_major_locator(ticker)
    formatter = mpl.ticker.FixedFormatter([cmap.name for cmap in cmaps])
    ax.xaxis.set_major_formatter(formatter)
    labels = ax.get_xticklabels()
    for label in labels:
        label.set_rotation(60)

    if saveplot:
        fig.savefig('figures/lightness.png', bbox_inches='tight')
        fig.savefig('figures/lightness.pdf', bbox_inches='tight')

    plt.show()


def plot_gallery(saveplot=False):
    '''Make plot of colormaps and labels, like in the matplotlib
    gallery.

    :param saveplot=False: Whether to save the plot or not.

    '''

    from colorspacious import cspace_converter

    # don't have reverse colormaps built in yet
    rgb = tools.print_colormaps([cm.gray], returnrgb=True)
    gcmap = tools.cmap(rgb[::-1, :])

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    x = np.linspace(0.0, 1.0, 256)

    fig, axes = plt.subplots(nrows=len(cmaps), ncols=1, figsize=(6, 12))
    fig.subplots_adjust(top=0.99, bottom=0.01, left=0.2, right=0.99, wspace=0.05)
    # fig.suptitle('Oceanography colormaps', fontsize=16, y=1.0, x=0.6)

    for ax, cmap in zip(axes, cmaps):

        rgb = cmap(x)[np.newaxis, :, :3]

        # Find a good conversion to grayscale
        jch = cspace_converter("sRGB1", "CAM02-UCS")(rgb)  # Not sure why to use JCh instead so using this.
        # jch = cspace_converter("sRGB1", "JCh")(rgb)
        L = jch[0, :, 0]
        # # Get colormap in CIE LAB. We want the L here.
        # lab = color.rgb2lab(rgb)
        # L = lab[0, :, 0]
        L = np.float32(np.vstack((L, L, L)))

        ax.imshow(gradient, aspect='auto', cmap=cmap)

        pos1 = ax.get_position()  # get the original position
        pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height / 3.0]
        axbw = fig.add_axes(pos2)  # colorbar axes
        axbw.set_axis_off()
        axbw.imshow(L, aspect='auto', cmap=gcmap, vmin=0, vmax=100.)
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, cmap.name, va='center', ha='right')

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    if saveplot:
        fig.savefig('figures/gallery.pdf', bbox_inches='tight')
        fig.savefig('figures/gallery.png', bbox_inches='tight')

    plt.show()


def wrap_viscm(cmap, dpi=100, saveplot=False):
    '''Evaluate goodness of colormap using perceptual deltas.

    :param cmap: Colormap instance.
    :param dpi=100: dpi for saved image.
    :param saveplot=False: Whether to save the plot or not.

    '''

    from viscm import viscm

    viscm(cmap)
    fig = plt.gcf()
    fig.set_size_inches(22, 10)
    plt.show()

    if saveplot:
        fig.savefig('figures/eval_' + cmap.name + '.png', bbox_inches='tight', dpi=dpi)
        fig.savefig('figures/eval_' + cmap.name + '.pdf', bbox_inches='tight', dpi=dpi)


def test(cmap, fig=None, ax=None):
    '''Test colormap by plotting.

    :param cmap: A colormap instance. Use a named one with cm.get_cmap(colormap)

    '''

    from colorspacious import cspace_converter

    # indices to step through colormap
    x = np.linspace(0.0, 1.0, 100)

    # will plot colormap and lightness
    rgb = cmap(x)[np.newaxis, :, :3]
    # rgb = cm.get_cmap(cmap)(x)[np.newaxis,:,:3]
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
    # lab = color.rgb2lab(rgb)

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
    ax.scatter(x, lab[0, :, 0], c=x, cmap=cmap, s=300, linewidths=0.)
    ax.set_title(cmap.name)
    ax.set_ylabel('Lightness')
    ax.set_xticks([])


def quick_plot(cmap, fname=None, fig=None, ax=None, N=10):
    '''Show quick test of a colormap.

    '''

    x = np.linspace(0, 10, N)
    X, _ = np.meshgrid(x, x)

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111)
    mappable = ax.pcolor(X, cmap=cmap)
    ax.set_title(cmap.name)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.colorbar(mappable)
    plt.show()

    if fname is not None:
        plt.savefig(fname + '.png', bbox_inches='tight')
