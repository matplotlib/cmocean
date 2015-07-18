'''
Plot up stuff with colormaps:
colormap gallery
lightness
sample MCH data with each colormap.
'''

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import cmocean
from skimage import color
import test
import os

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

# list of colormaps for several functions
cmaps = [cmocean.temp, cmocean.o2, cmocean.salinity, cmocean.chl,
         cmocean.rho, cmocean.par, cmocean.turb, cmocean.cdom]
            # cmocean.bathy, cmocean.s, cmocean.v, cmocean.vort,
            # cmocean.eta]

# data files
fnames = ['MS09_L10.mat.txt', 'MS09_L05.mat.txt',
          'MS2_L10.mat.txt', 'MS08_L12.mat.txt']


def plot_lightness():
    '''Plot lightness of colormaps together.

    '''

    dc = 1.
    x = np.linspace(0.0, 1.0, 256)
    locs = []  # locations for text labels

    fig = plt.figure(figsize=(16, 6))
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.1, 8.1)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Lightness for each colormap')

    for j, cmap in enumerate(cmaps):
        rgb = cmap(x)[np.newaxis, :, :3]
        lab = color.rgb2lab(rgb)
        L = lab[0, :, 0]
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

    fig.savefig('figures/lightness.png', bbox_inches='tight')
    fig.savefig('figures/lightness.pdf', bbox_inches='tight')


def print_colormaps():
    '''Print colormaps in 256 RGB colors to text files.

    '''

    if not os.path.exists('rgb'):
        os.makedirs('rgb')

    for cmap in cmaps:

        np.savetxt('rgb/' + cmap.name + '-rgb.txt', cmap(np.linspace(0, 1, 256))[np.newaxis, :, :3][0])


def plot_gallery():
    '''Make plot of colormaps and labels, like in the matplotlib
    gallery.

    '''

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    x = np.linspace(0.0, 1.0, 256)

    fig, axes = plt.subplots(nrows=len(cmaps), ncols=1)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99, wspace=0.05)
    fig.suptitle('Texas A&M Oceanography colormaps', fontsize=16, y=1.0, x=0.6)

    for ax, cmap in zip(axes, cmaps):

        rgb = cmap(x)[np.newaxis, :, :3]
        # Get colormap in CIE LAB. We want the L here.
        lab = color.rgb2lab(rgb)
        L = lab[0, :, 0]
        L = np.float32(np.vstack((L, L, L)))

        ax.imshow(gradient, aspect='auto', cmap=cmap)

        pos1 = ax.get_position()  # get the original position
        pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height / 4.0]
        axbw = fig.add_axes(pos2)  # colorbar axes
        axbw.set_axis_off()
        axbw.imshow(L, aspect='auto', cmap='binary_r', vmin=0, vmax=100.)
        # ax[1].imshow(L, aspect='auto', cmap='binary_r', vmin=0., vmax=100.)
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, cmap.name, va='center', ha='right')

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    fig.savefig('figures/gallery.pdf', bbox_inches='tight')
    fig.savefig('figures/gallery.png', bbox_inches='tight')


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
    R = zip(x, r2, r3)
    G = zip(x, g2, g3)
    B = zip(x, b2, b3)

    # Creating dictionary
    k = ['red', 'green', 'blue']
    LinearL = dict(zip(k, [R, G, B]))

    return LinearL


def cmap(rgbin, N=10):
    '''Input an array of rgb values to generate a colormap.

    :param rgbin: An [mx3] array, where m is the number of input color triplets which
         are interpolated between to make the colormap that is returned. hex values
         can be input instead, as [mx1] in single quotes with a #.
    :param N: The number of levels to be interpolated to.

    '''

    # rgb inputs here
    if not mpl.cbook.is_string_like(rgbin[0]):
        # normalize to be out of 1 if out of 256 instead
        if rgbin.max() > 1:
            rgbin = rgbin/256.

    cmap = mpl.colors.LinearSegmentedColormap.from_list('mycmap', rgbin)

    return cmap


def test(cmap):
    '''Test colormap by plotting.

    :param cmap: A colormap instance. Use a named one with cm.get_cmap(colormap)

    '''

    # indices to step through colormap
    x = np.linspace(0.0, 1.0, 100)

    # will plot colormap and lightness
    rgb = cmap(x)[np.newaxis, :, :3]
    # rgb = cm.get_cmap(cmap)(x)[np.newaxis,:,:3]
    lab = color.rgb2lab(rgb)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, lab[0, :, 0], c=x, cmap=cmap, s=300, linewidths=0.)


def eval(cmap, dpi=100):
    '''Evaluate goodness of colormap using perceptual deltas.

    :param cmap: Colormap instance.
    :param dpi=100: dpi for saved image.

    '''

    import viscm

    viscm(cmap)
    fig = plt.gcf()
    fig.set_size_inches(22, 10)
    plt.show()
    fig.savefig('figures/eval_' + cmap.name + '.png', bbox_inches='tight', dpi=dpi)
    fig.savefig('figures/eval_' + cmap.name + '.pdf', bbox_inches='tight', dpi=dpi)


def quick_plot(cmap, fname=None):
    '''Show quick test of a colormap.

    '''

    x = np.arange(10)
    X, _ = np.meshgrid(x, x)

    plt.figure()
    plt.pcolor(X, cmap=cmap)
    plt.colorbar()
    plt.show()

    if fname is not None:
        plt.savefig(fname + '.png', bbox_inches='tight')
