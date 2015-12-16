'''
Standardized colormaps for oceanography plots.

Colormaps are available for:
    salinity, salt
    temperature, temp
    oxygen, o2
    chlorophyll, chl, chloro
    cdom, CDOM
    turbidity, turb
    PAR, par
    density, rho
    bathymetry, bathy
    speed, s
    velocity, vel, u, v
    vorticity, vort
    seasurface, freesurface, zeta, eta

Used tool from http://bids.github.io/colormap/ to redo colormaps to be more perceptually correct.
'''

from __future__ import absolute_import

# from matplotlib import cm, colors
import matplotlib
# import plotting
# import data
import numpy as np
import os

from . import tools

# Location of rgb files
datadir = os.path.join(os.path.split(__file__)[0], 'rgb')


def make_salinity_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Salinity-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Salinity'
    cmap.long_name = 'Salinity'
    cmap.units = 'g/kg'
    cmap.author = 'kmt'
    return cmap


def make_temperature_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Temperature-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Temperature'
    cmap.long_name = 'Temperature'
    cmap.units = 'C'
    cmap.author = 'kmt'
    return cmap


def make_oxygen_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Oxygen-rgb.txt'))
    # # Did the following originally to set up the text file, but now it has already been done.
    # l = rgb.shape[0]*(5./4)  # total number of entries in final colormap
    # num = int(l/5.)  # 20% of colormap
    # # Take last 1/5 of colormap and save since I want it, flipped, at the end, keeping the full lightness range in the middle 3/5
    # yellow = rgb[-num:, :].copy()
    # from colorspacious import cspace_converter
    # cam = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
    # rgb_gray = cmocean.cm.gray(np.linspace(1,0,256))
    # cam_gray = cspace_converter("sRGB1", "CAM02-UCS")(rgb_gray[np.newaxis, :, :3])[0,:]
    # # Use gray colormap to interpolate and find the best rgb values for the lightness values in the middle of the colormap
    # rgb[num:num+num*3, 0] = np.interp(cam[num:num+num*3,0], cam_gray[:,0], rgb_gray[:,0])
    # rgb[num:num+num*3, 1] = np.interp(cam[num:num+num*3,0], cam_gray[:,0], rgb_gray[:,1])
    # rgb[num:num+num*3, 2] = np.interp(cam[num:num+num*3,0], cam_gray[:,0], rgb_gray[:,2])
    # # Add back in flipped yellow part to be divergent super saturated state
    # rgb = np.vstack((rgb, yellow[::-1, :]))  # yellow part flipped and added on the end of colormap
    cmap = tools.cmap(rgb, N=320)  # the 320 keeps the interpolation correct
    cmap.name = 'Oxygen'
    cmap.long_name = 'Oxygen'
    cmap.units = 'ml/l'
    cmap.author = 'kmt'
    return cmap


def make_chlorophyll_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Chlorophyll-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Chlorophyll'
    cmap.long_name = 'Chlorophyll'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_CDOM_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'CDOM-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'CDOM'
    cmap.long_name = 'Colored Dissolved Organic Matter'
    cmap.units = 'mg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_turbidity_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Turbidity-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Turbidity'
    cmap.long_name = 'Turbidity'
    cmap.units = 'NTU'
    cmap.author = 'kmt'
    return cmap


def make_PAR_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'PAR-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'PAR'
    cmap.long_name = 'Photosynthetically Available Radiation'
    cmap.units = 'W/m^2'
    cmap.author = 'kmt'
    return cmap


def make_density_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Density-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Density'
    cmap.long_name = 'Density'
    cmap.units = 'kg/m^3'
    cmap.author = 'kmt'
    return cmap


def make_bathymetry_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Bathymetry-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Bathymetry'
    cmap.long_name = 'Bathymetry'
    cmap.units = 'm'
    cmap.author = 'kmt'
    return cmap


def make_speed_cmap():
    # Uses positive part of velocity colormap
    rgb = np.loadtxt(os.path.join(datadir, 'Speed-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Speed'
    cmap.long_name = 'Speed'
    cmap.units = 'm/s'
    cmap.author = 'kmt'
    return cmap


def make_velocity_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Velocity-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Velocity'
    cmap.long_name = 'Velocity'
    cmap.units = 'm/s'
    cmap.author = 'kmt'
    return cmap


def make_vorticity_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Vorticity-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Vorticity'
    cmap.long_name = 'Vertical Vorticity'
    cmap.units = '1/s'
    cmap.author = 'kmt'
    return cmap


def make_freesurface_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'FreeSurface-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'FreeSurface'
    cmap.long_name = 'Free Surface'
    cmap.units = 'm'
    cmap.author = 'kmt'
    return cmap


def make_phase_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Phase-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Phase'
    cmap.long_name = 'Phase'
    cmap.units = 'degrees'
    cmap.author = 'kmt'
    return cmap


def make_waveheight_cmap():
    # Uses positive part of free surface colormap
    rgb = np.loadtxt(os.path.join(datadir, 'WaveHeight-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'WaveHeight'
    cmap.long_name = 'Wave Height'
    cmap.units = 'meters'
    cmap.author = 'kmt'
    return cmap


def make_waveperiod_cmap():
    # Uses negative part of vorticity colormap
    rgb = np.loadtxt(os.path.join(datadir, 'WavePeriod-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'WavePeriod'
    cmap.long_name = 'Wave Period'
    cmap.units = 'seconds'
    cmap.author = 'kmt'
    return cmap


def make_gray_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'Gray-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'Gray'
    cmap.long_name = 'Gray'
    cmap.units = ''
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
seasurface = make_freesurface_cmap()
freesurface = make_freesurface_cmap()
zeta = make_freesurface_cmap()
eta = make_freesurface_cmap()
phase = make_phase_cmap()
direction = make_phase_cmap()
direct = make_phase_cmap()
waveheight = make_waveheight_cmap()
swh = make_waveheight_cmap()
waveheights = make_waveheight_cmap()
height = make_waveheight_cmap()
waveperiod = make_waveperiod_cmap()
period = make_waveperiod_cmap()
gray = make_gray_cmap()
Gray = make_gray_cmap()
grey = make_gray_cmap()
Grey = make_gray_cmap()
grays = make_gray_cmap()
Grays = make_gray_cmap()
greys = make_gray_cmap()
Greys = make_gray_cmap()


def all_colormap_names(methods):
    '''Return all names available to refer to colormaps.
    This includes duplicates.

    '''

    cmall = []
    cmnames = []

    # loop through all the methods
    for method in methods:

        # see if method is a colormap
        if type(eval(method)) == matplotlib.colors.LinearSegmentedColormap:
            # import pdb; pdb.set_trace()
            cmnames.append(method)  # add on colormap nickname

    return cmnames

cmnames = all_colormap_names(dir())


def all_colormaps(cmnames):
    '''All available unique colormaps with names. Excludes reversed versions.

    '''

    cmallname = []
    cmall = []
    for cmname in cmnames:
        thisname = eval(cmname).name
        if thisname not in cmallname:
            cmall.append(eval(cmname))
            cmallname.append(thisname)

    # To sort both names and colormaps alphabetically
    # http://stackoverflow.com/questions/7851077/how-to-return-index-of-a-sorted-list/7851186#7851186
    inds = sorted(range(len(cmallname)), key=lambda k: cmallname[k])
    cmallname.sort()
    # sort the colormap objects using the indices just found
    cmall2 = []
    [cmall2.append(cmall[ind]) for ind in inds]
    return cmall2


cmall = all_colormaps(cmnames)


def reverse_colormaps():
    '''Provide reversed versions of all colormaps, accessible by appending '_r'

    '''

    x = np.linspace(1, 0, 256)  # to reverse the order of the colormap
    cmapdict = dict()

    # loop through all colormap nicknames
    for cmnickname in cmnames:
        if '_r' in cmnickname:
            continue
        cmap = eval(cmnickname)
        rcmapnickname = cmnickname + '_r'
        cmapdict[rcmapnickname] = tools.cmap(cmap(x), N=256)
        cmapdict[rcmapnickname].name = cmap.name + ' reversed'
        cmapdict[rcmapnickname].long_name = cmap.long_name + ' reversed'
        cmapdict[rcmapnickname].units = cmap.units
        cmapdict[rcmapnickname].author = cmap.author

    return cmapdict


reversed_cmaps = reverse_colormaps()
locals().update(reversed_cmaps)  # this makes the new colormaps from the dict available to call

cmnames = all_colormap_names(dir())  # update nickname list with reversed colormaps


if __name__ == '__main__':

    make_salinity_cmap()
    # pass
