import cmocean

cmaps = cmocean.cm.cmall

for cmap in cmaps:
   cmocean.plots.wrap_viscm(cmap)