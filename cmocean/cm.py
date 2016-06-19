'''
Standardized colormaps for oceanography plots.

Used tool from http://bids.github.io/colormap/ to make perceptually correct
colormaps.

Created by Kristen Thyng
2016-06-18
'''

from __future__ import absolute_import

import matplotlib
import numpy as np
import os

from . import tools

# Location of rgb files
datadir = os.path.join(os.path.split(__file__)[0], 'rgb')


def make_thermal_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'thermal-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'thermal'
    cmap.author = 'kmt'
    return cmap


def make_haline_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'haline-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'haline'
    cmap.author = 'kmt'
    return cmap


def make_solar_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'solar-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'solar'
    cmap.author = 'kmt'
    return cmap


def make_ice_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'ice-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'ice'
    cmap.author = 'kmt'
    return cmap


def make_gray_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'gray-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'gray'
    cmap.author = 'kmt'
    return cmap


def make_oxy_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'oxy-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'oxy'
    cmap.author = 'kmt'
    return cmap


def make_deep_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'deep-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'deep'
    cmap.author = 'kmt'
    return cmap


def make_dense_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'dense-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'dense'
    cmap.author = 'kmt'
    return cmap


def make_algae_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'algae-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'algae'
    cmap.author = 'kmt'
    return cmap


def make_matter_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'matter-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'matter'
    cmap.author = 'kmt'
    return cmap


def make_turbid_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'turbid-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'turbid'
    cmap.author = 'kmt'
    return cmap


def make_speed_cmap():
    # Uses positive part of delta colormap
    rgb = np.loadtxt(os.path.join(datadir, 'speed-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'speed'
    cmap.author = 'kmt'
    return cmap


def make_amp_cmap():
    # Uses positive part of balance colormap
    rgb = np.loadtxt(os.path.join(datadir, 'amp-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'amp'
    cmap.author = 'kmt'
    return cmap


def make_tempo_cmap():
    # Uses negative part of curl colormap
    rgb = np.loadtxt(os.path.join(datadir, 'tempo-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'tempo'
    cmap.author = 'kmt'
    return cmap


def make_phase_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'phase-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'phase'
    cmap.author = 'kmt'
    return cmap


def make_balance_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'balance-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'balance'
    cmap.author = 'kmt'
    return cmap


def make_delta_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'delta-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'delta'
    cmap.author = 'kmt'
    return cmap


def make_curl_cmap():
    rgb = np.loadtxt(os.path.join(datadir, 'curl-rgb.txt'))
    cmap = tools.cmap(rgb, N=256)
    cmap.name = 'curl'
    cmap.author = 'kmt'
    return cmap


thermal = make_thermal_cmap()
haline = make_haline_cmap()
solar = make_solar_cmap()
ice = make_ice_cmap()
gray = make_gray_cmap()
oxy = make_oxy_cmap()
deep = make_deep_cmap()
dense = make_dense_cmap()
algae = make_algae_cmap()
matter = make_matter_cmap()
turbid = make_turbid_cmap()
speed = make_speed_cmap()
amp = make_amp_cmap()
tempo = make_tempo_cmap()
phase = make_phase_cmap()
balance = make_balance_cmap()
delta = make_delta_cmap()
curl = make_curl_cmap()


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
        cmapdict[rcmapnickname].author = cmap.author

    return cmapdict


reversed_cmaps = reverse_colormaps()
locals().update(reversed_cmaps)  # this makes the new colormaps from the dict available to call

cmnames = all_colormap_names(dir())  # update nickname list with reversed colormaps


if __name__ == '__main__':

    make_salinity_cmap()
    # pass
