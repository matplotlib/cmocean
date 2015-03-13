'''
Plot up stuff with colormaps:
colormap gallery
lightness
sample MCH data with each colormap.
'''

from matplotlib import cm, colors
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import cmtamu
from skimage import color

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


def plot_lightness():
    '''
    Plot lightness of colormaps together.
    '''

# Print colormaps in text 256 colors rgb


def plot_gallery():
    '''
    Make plot of colormaps and labels, like in the matplotlib 
    gallery.
    '''

    cmaps = [cmtamu.salinity, cmtamu.temp, cmtamu.o2, cmtamu.chl, cmtamu.cdom, cmtamu.turb]

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    x = np.linspace(0.0, 1.0, 100)

    fig, axes = plt.subplots(nrows=6, ncols=1)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99, wspace=0.05)
    fig.suptitle('Texas A&M Oceanography colormaps', fontsize=16, y=1.0, x=0.6)

    for ax, cmap in zip(axes, cmaps):

        rgb = cmap(x)[np.newaxis,:,:3]
        # Get colormap in CIE LAB. We want the L here.
        lab = color.rgb2lab(rgb)
        L = lab[0,:,0]
        L = np.float32(np.vstack((L, L, L)))

        ax.imshow(gradient, aspect='auto', cmap=cmap)

        pos1 = ax.get_position() # get the original position 
        pos2 = [pos1.x0, pos1.y0,  pos1.width, pos1.height / 4.0]
        axbw = fig.add_axes(pos2) #colorbar axes
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
