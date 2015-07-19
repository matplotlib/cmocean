.. cmocean documentation master file, created by
   sphinx-quickstart on Fri Jul 17 19:43:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Beautiful colormaps for oceanography: **cmocean**
=================================================

This package contains colormaps for standardizing commonly-plotting oceanographic variables. Most of the colormaps started from `matplotlib <http://matplotlib.org/>`_ colormaps, but have now been adjusted using the `viscm tool <https://github.com/BIDS/viscm>`_ to be `perceptually uniform <http://bids.github.io/colormap/>`_.

Here is our gallery:

.. plot::

   import cmocean
   import matplotlib.pyplot as plt
   import numpy as np

   plt.figure()
   x = np.arange(10)
   X, _ = np.meshgrid(x, x)

   plt.pcolor(X, cmap=cmocean.cm.salt)
   plt.show()


.. ipython:: python

   import cmocean

   cmdict = cmocean.tools.get_dict(cmocean.cm.salt)
   print cmdict.keys()
   'plotting' in dir(cmocean)
   'tools' in dir(cmocean)
   'data' in dir(cmocean)
   print cmocean.__file__
   print dir(cmocean)
   print dir(cmocean.cm)
   print dir(cmocean.tools)

.. .. plot::
..    :include-source:

..    import cmocean
..    cmocean.plots.plot_gallery()


If you think about CIELAB colorspace, here is the lightness of the colormaps:

.. .. plot::
..    :include-source:

..    import cmocean
..    cmocean.plots.plot_lightness()


It is probably better to think in cam02ucs colorspace, in which Euclidean distance is made to be equivalent to changes in human perception. Plots of these colormaps in this colorspace and with some other important properties are seen using the `viscm tool <https://github.com/BIDS/viscm>`_.

Here are some properties from the Salinity colormap. We can see that the colormap prints nicely to grayscale, has consistent perceptual deltas across the colormap, and good viewability for people with color blindness. It has a smooth representation in its 3D colorspace, and detail in the images is clear.

.. .. plot::
..    :include-source:

..    import cmocean
..    cmocean.plots.wrap_viscm(cmocean.salt)


The other colormaps are shown below.

.. .. plot::
..    :include-source:

..    import cmocean

..    cmaps = cmocean.cmall_unique

..    for cmap in cmaps:
..       cmocean.plots.wrap_viscm(cmap)



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

