.. _colormaps_viscm:

**cmocean** colormaps in viscm tool
===================================

.. plot::
   :include-source:

   import cmocean

   cmaps = cmocean.cm.cmall

   for cmap in cmaps:
      cmocean.plots.wrap_viscm(cmap)
