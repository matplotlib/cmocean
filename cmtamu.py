'''
Standardized colormaps for TAMU oceanography plots.
'''

from matplotlib import cm, colors
import test
import numpy as np


## Colormaps ##

def make_salinity_cmap():
    cmap = cm.YlGnBu_r
    cmap.name = 'Salinity'
    cmap.units = 'g/kg'
    cmap.author = 'kmt'
    return cmap

def make_temperature_cmap():
    rgb = np.array([[49,54,149], [61,91,167], [245,117,71], [254,235,161]])
    cmap = test.cmap(rgb)
    cmap.name = 'Temperature'
    cmap.units = 'C'
    cmap.author = 'kmt'
    return cmap

def make_oxygen_cmap(hypo_low  = [0.39, 0.0, 0.15],
                hypo_high = [0.5, 0.28, 0.31],
                norm_low  = [0.35, 0.35, 0.35],
                norm_high = [0.94, 0.94, 0.95], bpt=0.2,
                sup_low  = [1.0, 1.0, 0.4],
                sup_high = [0.73, 0.87, 0.4], bpth=0.8):
    '''
    The colormap has hue breaks for hypoxic, normal, and supersaturated levels 
    of oxygen. Reasonable lightness functions though.
    '''


    cdict = {'red':   ((0.0, 0.0, hypo_low[0]),
                       (bpt, hypo_high[0], norm_low[0]),
                       (bpth, norm_high[0], sup_low[0]),
                       (1.0, sup_high[0], 1.0)),
             'green':((0.0, 0.0, hypo_low[1]),
                       (bpt, hypo_high[1], norm_low[1]),
                       (bpth, norm_high[1], sup_low[1]),
                       (1.0, sup_high[1], 1.0)),
             'blue':  ((0.0, 0.0, hypo_low[2]),
                       (bpt, hypo_high[2], norm_low[2]),
                       (bpth, norm_high[2], sup_low[2]),
                       (1.0, sup_high[2], 1.0))}

    cmap = colors.LinearSegmentedColormap('Oxygen', cdict, 256)
    cmap.units = '?'
    cmap.author = 'rdh'
    return cmap

def make_chlorophyll_cmap():
    cmap = cm.Greens
    cmap.name = 'Chlorophyll'
    cmap.units = '?'
    cmap.author = 'kmt'
    return cmap

def make_CDOM_cmap():
    cmap = cm.RdPu
    cmap.name = 'CDOM'
    cmap.units = '?'
    cmap.author = 'kmt'
    return cmap

def make_turbidity_cmap():
    cmap = cm.YlOrBr
    cmap.name = 'Turbidity'
    cmap.units = '?'
    cmap.author = 'kmt'
    return cmap


salinity = make_salinity_cmap()
salt = make_salinity_cmap()
temperature = make_temperature_cmap()
temp = make_temperature_cmap()
oxygen = make_oxygen_cmap()
o2 = make_oxygen_cmap()
chl = make_chlorophyll_cmap()
chloro = make_chlorophyll_cmap()
cdom = make_CDOM_cmap()
CDOM = make_CDOM_cmap()
turbidity = make_turbidity_cmap()
turb = make_turbidity_cmap()



if __name__ == '__main__':

    pass