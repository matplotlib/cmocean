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
    '''
    Plot lightness of colormaps together.
    '''

    dc = 1.
    x = np.linspace(0.0, 1.0, 256)
    locs = [] # locations for text labels

    fig = plt.figure(figsize=(16,6)) #(24,6))
    ax = fig.add_subplot(111)
    ax.set_xlim(-0.1, 8.1) #13.1)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Lightness for each colormap')

    for j, cmap in enumerate(cmaps):
        rgb = cmap(x)[np.newaxis,:,:3]
        lab = color.rgb2lab(rgb)
        L = lab[0,:,0]
        if L[-1] > L[0]:
            ax.scatter(x+j*dc, L, c=x, cmap=cmap, s=300, linewidths=0.)
        else:
            ax.scatter(x+j*dc, L[::-1], c=x[::-1], cmap=cmap, s=300, linewidths=0.)
        locs.append(x[-1]+j*dc) # store locations for colormap labels

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
    '''
    Print colormaps in 256 RGB colors to text files.
    '''

    if not os.path.exists('rgb'):
        os.makedirs('rgb')

    for cmap in cmaps:

        np.savetxt('rgb/' + cmap.name + '-rgb.txt', cmap(np.linspace(0,1,256))[np.newaxis,:,:3][0])


def plot_data():
    '''
    Plot sample data up with the fancy colormaps.
    '''

    var = ['temp', 'oxygen', 'salinity', 'fluorescence-ECO', 'density', 'PAR', 'turbidity', 'fluorescence-CDOM']
    # colorbar limits for each property
    lims = np.array([[26,33], [0,10], [0,36], [0,6], [1005, 1025], [0,0.6], [0,2], [0,9]]) # reasonable values
    # lims = np.array([[20,36], [26,33], [1.5,5.6], [0,4], [0,9], [0,1.5]]) # values to show colormaps

    for fname in fnames:
        fig, axes = plt.subplots(nrows=4, ncols=2)
        fig.set_size_inches(20,10)
        fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99, wspace=0.0, hspace=0.07)
        i = 0
        for ax, Var, cmap in zip(axes.flat, var, cmaps): # loop through data to plot up

            # get variable data
            lat, lon, z, data = test.read(Var, fname)

            map1 = ax.scatter(lat, -z, c=data, cmap=cmap, s=10, linewidths=0., vmin=lims[i,0], vmax=lims[i,1])
            # no stupid offset
            y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)
            ax.xaxis.set_major_formatter(y_formatter)
            if i==6:
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


def plot_gallery():
    '''
    Make plot of colormaps and labels, like in the matplotlib 
    gallery.
    '''

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))
    x = np.linspace(0.0, 1.0, 256)

    fig, axes = plt.subplots(nrows=len(cmaps), ncols=1)
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


def get_dict(cmap, N=256):
    '''
    Change from rgb to dictionary that LinearSegmentedColormap expects. 
    Code from https://mycarta.wordpress.com/2014/04/25/convert-color-palettes-to-python-matplotlib-colormaps/
    and http://nbviewer.ipython.org/github/kwinkunks/notebooks/blob/master/Matteo_colourmaps.ipynb
    '''

    rgb = cmap(np.arange(N))

    b3 = rgb[:,2] # value of blue at sample n
    b2 = rgb[:,2] # value of blue at sample n
    b1 = np.linspace(0, 1, len(b2)) # position of sample n - ranges from 0 to 1

    # Setting up columns for tuples
    g3 = rgb[:,1]
    g2 = rgb[:,1]
    g1 = np.linspace(0,1,len(g2))

    r3 = rgb[:,0]
    r2 = rgb[:,0]
    r1 = np.linspace(0,1,len(r2))

    # Creating tuples
    R = zip(r1,r2,r3)
    G = zip(g1,g2,g3)
    B = zip(b1,b2,b3)

    # Transposing
    RGB = zip(R,G,B)
    rgb = zip(*RGB)

    # Creating dictionary
    k = ['red', 'green', 'blue']
    LinearL = dict(zip(k,rgb))

    return LinearL