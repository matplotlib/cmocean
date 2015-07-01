'''
Standardized colormaps for TAMU oceanography plots.

Colormaps are available for:
    salinity, salt
    temperature, temp
    oxygen, o2
    chlorophyll, chl, chloro
    cdom, CDOM
    turbidity, turb
    PAR, par
    density, rho
    # the following haven't been vetted well yet:
    bathymetry, bathy
    speed, s
    velocity, vel, u, v
    vorticity, vort
    seasurface, freesurface, zeta, eta

Used tool from http://bids.github.io/colormap/ to redo colormaps to be more perceptually correct.
'''

from matplotlib import cm, colors
import test
import numpy as np
import os


def make_salinity_cmap():
    rgb = np.load('rgb/Salinity.npy')
    cmap = test.cmap(rgb, N=256)
    cmap.name = 'Salinity'
    cmap.units = 'g/kg'
    cmap.author = 'kmt'
    return cmap


def make_temperature_cmap():
    rgb = np.load('rgb/Temperature.npy')
    cmap = test.cmap(rgb, N=256)
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
    rgb = np.load('rgb/Chlorophyll.npy')
    cmap = test.cmap(rgb[::-1], N=256)
    cmap.name = 'Chlorophyll'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_CDOM_cmap():
    rgb = np.load('rgb/CDOM.npy')
    cmap = test.cmap(rgb[::-1], N=256)
    cmap.name = 'CDOM'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_turbidity_cmap():
    rgb = np.load('rgb/turbidity.npy')
    cmap = test.cmap(rgb[::-1], N=256)
    cmap.name = 'Turbidity'
    cmap.units = 'NTU'
    cmap.author = 'kmt'
    return cmap


def make_PAR_cmap():
    rgb = np.load('rgb/PAR.npy')
    cmap = test.cmap(rgb, N=256)
    cmap.name = 'PAR'
    cmap.units = 'W/m^2'
    cmap.author = 'kmt'
    return cmap


def make_density_cmap():
    rgb = np.load('rgb/Density.npy')
    cmap = test.cmap(rgb[::-1], N=256)
    cmap.name = 'Density'
    cmap.units = 'kg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_bathymetry_cmap():  
    rgb = np.load('rgb/Bathymetry.npy')
    cmap = test.cmap(rgb, N=256)
    cmap.name = 'Bathymetry' 
    cmap.units = 'm'
    cmap.author = 'kmt'
    return cmap

def make_speed_cmap():
    rgb = np.load('rgb/Speed.npy')
    cmap = test.cmap(rgb, N=256)
    cmap.name = 'Speed'
    cmap.units = 'm/s'
    cmap.author = 'kmt'
    return cmap

def make_velocity_cmap():
    cmap = cm.PuOr
    cmap.name = 'Velocity'
    cmap.units = 'm/s'
    cmap.author = 'kmt'
    return cmap

def make_vorticity_cmap():
    cmap = cm.PiYG  # BrBG
    cmap.name = 'Vorticity'
    cmap.units = '1/s'
    cmap.author = 'kmt'
    return cmap

def make_seasurface_cmap():
    cmap = cm.RdBu
    cmap.name = 'Sea surface'
    cmap.units = 'm'
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
chlorophyll = make_chlorophyll_cmap()
cdom = make_CDOM_cmap()
CDOM = make_CDOM_cmap()
turbidity = make_turbidity_cmap()
turb = make_turbidity_cmap()
PAR = make_PAR_cmap()
par = make_PAR_cmap()
density = make_density_cmap()
rho = make_density_cmap()
bathymetry = make_bathymetry_cmap()
bathy = make_bathymetry_cmap()
speed = make_speed_cmap()
s = make_speed_cmap()
velocity = make_velocity_cmap()
vel = make_velocity_cmap()
u = make_velocity_cmap()
v = make_velocity_cmap()
vorticity = make_vorticity_cmap()
vort = make_vorticity_cmap()
seasurface = make_seasurface_cmap()
freesurface = make_seasurface_cmap()
zeta = make_seasurface_cmap()
eta = make_seasurface_cmap()



if __name__ == '__main__':

    make_salinility_cmap()
    # pass