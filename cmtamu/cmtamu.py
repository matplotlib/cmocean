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
    rgb = np.array([[20,30,120], [55,85,161], [245,117,71], [254,235,161]])
    cmap = test.cmap(rgb)
    cmap.name = 'Temperature'
    cmap.units = 'C'
    cmap.author = 'kmt'
    return cmap

def make_oxygen_cmap(hypo_low  = [0.30, 0.1, 0.1],
                hypo_high = [0.6, 0.1, 0.1],
                norm_low  = [0.3, 0.3, 0.3],
                norm_high = [0.80, 0.80, 0.80], bpt=0.2,
                sup_high  = [1.0, 1.0, 0.4],
                sup_low = [0.73, 0.85, 0.4], bpth=0.8):
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
    cmap.units = 'm/l'
    cmap.author = 'rdh'
    return cmap

def make_chlorophyll_cmap():
    cmap = cm.Greens
    cmap.name = 'Chlorophyll'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap

def make_CDOM_cmap():
    cmap = cm.RdPu
    cmap.name = 'CDOM'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap

def make_turbidity_cmap():
    cmap = test.cmap(['#FEEBB7', '#B0911E', '#4F3F18'])
    # cmap = cm.YlOrBr
    cmap.name = 'Turbidity'
    cmap.units = 'NTU'
    cmap.author = 'kmt'
    return cmap

def make_PAR_cmap():
    # cmap = test.cmap(['#7B6316', '#A37F13', '#BF910C', '#FCB413', '#FFCC48', '#F8DF8C', '#F7E7AA'])
    # cmap = test.cmap(['#685739', '#8C7440', '#B89A5D', '#C6AB72', '#DAC496', '#E5D2AA', '#F3E8CB'])
    # cmap = test.cmap(['#4F3F18', '#B0911E', '#FEEBB7'])
    cmap = cm.YlOrBr_r
    cmap.name = 'PAR'
    cmap.units = 'W/m^2'
    cmap.author = 'kmt'
    return cmap

def make_density_cmap():
    cmap = cm.BuPu
    cmap.name = 'Density'
    cmap.units = 'kg/m^3'
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
PAR = make_PAR_cmap()
par = make_PAR_cmap()
density = make_density_cmap()
rho = make_density_cmap()



if __name__ == '__main__':

    pass