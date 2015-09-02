.. cmocean documentation master file, created by
   sphinx-quickstart on Fri Jul 17 19:43:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Beautiful colormaps for oceanography: **cmocean**
=================================================

This package contains colormaps for standardizing commonly-plotting oceanographic variables. Most of the colormaps started from `matplotlib <http://matplotlib.org/>`_ colormaps, but have now been adjusted using the `viscm tool <https://github.com/BIDS/viscm>`_ to be `perceptually uniform <http://bids.github.io/colormap/>`_.

Here is our gallery:

.. plot::
   :include-source:

   import cmocean
   cmocean.plots.plot_gallery()

These colormaps were chosen to be perceptually uniform and to reflect the data they are representing in terms of being sequential or divergent, and to be intuitive. For example, chlorophyll is represented by shades of green, turbidity is shades of brown, and temperature goes from cool blues to warm yellows.

Here is the lightness of the colormaps:

.. plot::
   :include-source:

   import cmocean
   cmocean.plots.plot_lightness()


It is probably better to think in cam02ucs colorspace, in which Euclidean distance is made to be equivalent to changes in human perception. Plots of these colormaps in this colorspace and with some other important properties are seen using the `viscm tool <https://github.com/BIDS/viscm>`_.

Here are some properties from the Salinity colormap. We can see that the colormap prints nicely to grayscale, has consistent perceptual deltas across the colormap, and good viewability for people with color blindness. It has a smooth representation in its 3D colorspace, and detail in the images is clear.

.. plot::
   :include-source:

   import cmocean
   cmocean.plots.wrap_viscm(cmocean.cm.salt)


All of the evaluations of the colormaps using the viscm tool are shown in the page :ref:`colormaps_viscm`.


Capabilities
------------

The colormaps are all available in ``cmocean.cm``. They can be accessed, and simply plotted, as follows:

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.temp, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.chl, ax=ax)

All available nicknames of the colormaps can be accessed with ``cmocean.cm.cmnames``:

.. ipython:: python

   import cmocean

   cmocean.cm.cmnames


The distinct colormap instances can be accessed with:

.. ipython:: python

   import cmocean
   
   cmaps = cmocean.cm.cmall;

Print all of the available colormaps to text files with 256 rgb entries with:

``cmaps = cmocean.cm.cmall``

``cmocean.tools.print_colormaps(cmaps)``

Output a dictionary to define a colormap with:

.. ipython:: python

   import cmocean

   cmdict = cmocean.tools.get_dict(cmocean.cm.cdom, N=9)
   print cmdict

Make a colormap instance with ``cmap = cmocean.tools.cmap(rgbin, N=10)`` given the rgb input array.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

