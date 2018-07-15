.. _colormaps_viscm:

**cmocean** colormaps in viscm tool
===================================

.. plot::
   :include-source:

   import cmocean


   for cmapname in cmocean.cm.cmapnames:
      cmocean.plots.wrap_viscm(cmocean.cm.cmap_d[cmapname], saveplot=False)
