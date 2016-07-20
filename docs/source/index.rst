.. cmocean documentation master file, created by
   sphinx-quickstart on Fri Jul 17 19:43:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Beautiful colormaps for oceanography: `cmocean <http://github.com/matplotlib/cmocean>`_
=======================================================================================

This package contains colormaps for commonly-used oceanographic variables. Most of the colormaps started from `matplotlib <http://matplotlib.org/>`_ colormaps, but have now been adjusted using the `viscm tool <https://github.com/BIDS/viscm>`_ to be `perceptually uniform <http://bids.github.io/colormap/>`_.

Here is our gallery:

.. plot::
   :include-source:

   import cmocean
   cmocean.plots.plot_gallery()

These colormaps were chosen to be perceptually uniform and to reflect the data they are representing in terms of being sequential, divergent, or cyclic (phase colormap), and to be intuitive. For example, the *algae* colormap is  shades of green which could represent chlorophyll.

Here is the lightness of the colormaps:

.. plot::
   :include-source:

   import cmocean
   cmocean.plots.plot_lightness()


It is probably better to think in cam02ucs colorspace, in which Euclidean distance is made to be equivalent to changes in human perception. Plots of these colormaps in this colorspace and with some other important properties are seen using the `viscm tool <https://github.com/BIDS/viscm>`_.

Here are some properties from the *haline* colormap. We can see that the colormap prints nicely to grayscale, has consistent perceptual deltas across the colormap, and good viewability for people with color blindness. It has a smooth representation in its 3D colorspace, and detail in the images is clear.

.. plot::
   :include-source:

   import cmocean
   cmocean.plots.wrap_viscm(cmocean.cm.haline)


All of the evaluations of the colormaps using the viscm tool are shown in the page :ref:`colormaps_viscm`.

Colormap details
----------------

thermal
^^^^^^^

The *thermal* colormap is sequential with dark blue representing lower, cooler values and transitioning through reds to yellow representing increased warmer values.

.. figure:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_water_temp.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/
   :scale: 100 %

.. figure:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_water_temp.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/

   Glider data from Texas A&M's Geochemical and Environmental Research Group (`GERG <https://gerg.tamu.edu/>`_).


.. figure:: http://pong.tamu.edu/~kthyng/movies/txla_plots/temp/2004-07-30T00.png
   :target: http://kristenthyng.com/gallery/txla_temp.html

   Model output in the northwest Gulf of Mexico from the Physical Oceanography Numerical Group (`PONG <http://pong.tamu.edu>`_) at Texas A&M.


haline
^^^^^^

The *haline* colormap is sequential, and might be used with dark blue representing lower salinity or fresher water, transitioning through greens to light yellow representing increased salinity or saltier water. This colormap is based on matplotlib's YlGnBu, but was recreated from scratch using the viscm tool.

.. figure:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/calc_salinity.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/
   :scale: 100 %

.. figure:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/calc_salinity.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/
   :scale: 100 %

   Glider data from Texas A&M's Geochemical and Environmental Research Group (GERG).


.. figure:: http://pong.tamu.edu/~kthyng/movies/txla_plots/salt/2010-07-30T00.png
   :target: http://kristenthyng.com/gallery/txla_salinity.html
   :scale: 100 %

   Model output in the northwest Gulf of Mexico from the Physical Oceanography Numerical Group (PONG) at Texas A&M.


.. figure:: http://clarkrichards.org/figure/source/2016-04-25-making-section-plots/plot2-1.png
   :target: http://clarkrichards.org/r/oce/section/ctd/2016/04/25/making-section-plots/
   :scale: 100 %

   Plotting CTD data (temperature and salinity) with the R `oce` package, by `Clark Richards <http://clarkrichards.org/r/oce/section/ctd/2016/04/25/making-section-plots/>`_

solar
^^^^^

The *solar* colormap is sequential from dark brown for low values to increasingly bright yellow to potentially represent an increase in radiation in the water.

.. figure:: https://plot.ly/~empet/13620.png
   :target: https://plot.ly/~empet/13620/_2d-histogram-and-associated-marginals/#plot

   Histogram from `plotly <https://plot.ly/>`_.

ice
^^^

The *ice* colormap is sequential from very dark blue (almost black) to very light blue (almost white). A use for this could be representations of sea ice.

.. figure:: http://www.mathworks.com/matlabcentral/mlc-downloads/downloads/submissions/50126/versions/4/previews/seaice/html/SeaIceTimeSeries_20160620.gif
   :target: https://www.mathworks.com/matlabcentral/fileexchange/47638-antarctic-mapping-tools

   An example is provided by `Chad Greene <http://www.chadagreene.com/>`_ showing sea ice concentration around Antarctica.

gray
^^^^

The *gray* colormap is sequential from black to white, with uniform steps through perceptual colorspace. This colormap is generic to be used for any sequential dataset.

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.gray, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.gray, ax=ax)

oxy
^^^

The *oxy* colormap is sequential for most of the colormap, representing the normal range of oxygen saturation in ocean water, and diverging 80% of the way into the colormap to represent a state of supersaturation. The bottom 20% of the colormap is colored reddish to highlight hypoxic or low oxygen water, but to still print relatively seamlessly into grayscale in case the red hue is not important for an application. The top 20% of the colormap, after the divergence, is colored yellow to highlight the supersaturated water. The minimum and maximum values of this colormap are meant to be controlled in order to properly place the low oxygen and supersaturated oxygen states properly. This colormap was developed for the Mississippi river plume area where both low and supersaturated conditions are regularly seen and monitored.

.. figure:: https://cloud.githubusercontent.com/assets/3487237/16996267/85ac01ea-4e7e-11e6-9801-ee97f7e65940.png
   :target: https://cloud.githubusercontent.com/assets/3487237/16996267/85ac01ea-4e7e-11e6-9801-ee97f7e65940.png

   Model output in the northwest Gulf of Mexico from the Physical Oceanography Numerical Group (PONG) at Texas A&M. A simulation of bottom oxygen using a simple parameterization of bottom oxygen utilization reveals the complex structure of bottom oxygen. While the area affected by hypoxia stretches nearly 400 km along the shelf, variability on much smaller scales, down to a few kilometers, is also evident. The position of the Mississippi/Atchafalaya river plume, and instabilities present within the plume, determine the extent and structure of the hypoxic bottom waters. By `Veronica Ruiz <http://pong.tamu.edu/people.html#veronica>`_ at Texas A&M.

deep
^^^^

The *deep* colormap is sequential from light yellow to potentially represent shallower water through pale green to increasingly dark blue and purple to represent increasing depth.

.. figure:: https://cloud.githubusercontent.com/assets/3487237/16900541/4af66c4c-4bf5-11e6-92a9-82eaa39cb18b.png
   :target: http://iuryt.github.io/tutorial/Como_fazer_um_mapa02.html

   Bathymetry plot, by `Iury Sousa <http://iuryt.github.io/>`_

dense
^^^^^

The *dense* colormap is sequential with whitish-blue for low values and increasing in purple with increasing value, which could be used to represent an increase in water density. Two examples of this colormap are shown below, from Texas A&M University gliders. This colormap is based on matplotlib's Purples, but was recreated from scratch using the viscm tool.

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/calc_density.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/calc_density.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/calc_density.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/calc_density.png

algae
^^^^^

The *algae* colormap is sequential with whitish-green for low values and increasing in green with increasing value, which could be used to represent an increase in chlorophyll in the water. Two examples of this colormap are shown below, from Texas A&M University gliders. This colormap is based on matplotlib's Greens, but was recreated from scratch using the viscm tool.

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_chlor_units.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_chlor_units.png

matter
^^^^^^

The *matter* colormap is sequential with whitish-yellow for low values and increasing in pink with increasing value, and could be used to represent an increase in material in the water. Two examples of this colormap are shown below, from Texas A&M University gliders.

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_flbbcd_cdom_units.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_flbbcd_cdom_units.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_cdom_units.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_cdom_units.png

turbid
^^^^^^

The *turbid* colormap is sequential from light to dark brown and could be used to represent an increase in sediment in the water.

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.turbid, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.turbid, ax=ax)

speed
^^^^^

The *speed* colormap is sequential from light greenish yellow representing low values to dark yellowish green representing large values. This colormap is the positive half of the *delta* colormap. An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf.

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/speed/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/speed/2010.mp4

amp
^^^

The *amp* colormap is sequential from whitish to dark red and could be used to represent an increase in wave height values. This colormap is the positive half of the *balance* colormap.

.. figure:: https://cloud.githubusercontent.com/assets/3487237/16920916/840d91d4-4cdd-11e6-8db5-f93cd61b78c2.png
   :target: http://soliton.vm.bytemark.co.uk/pub/cpt-city/

   Earthquake magnitude, by `Natalie Accardo <http://www.natalieaccardo.com/>`_ using GMT.

tempo
^^^^^

The *tempo* colormap is sequential from whitish to dark teal and could be used to represent an increase in wave period values. This colormap is the negative half of the *curl* colormap.

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.tempo, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.tempo, ax=ax)

phase
^^^^^

The *phase* colormap is circular, spanning all hues at a set lightness value. This map is intended to be used for properties such as wave phase and tidal phase which wrap around from 0˚ to 360˚ to 0˚ and should be represented without major perceptual jumps in the colormap. An example for a circular plot is shown below.

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt
   import numpy as np

   azimuths = np.arange(0, 361, 1)
   zeniths = np.arange(40, 70, 1)
   values = azimuths * np.ones((30, 361))
   fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
   ax.pcolormesh(azimuths*np.pi/180.0, zeniths, values, cmap=cmocean.cm.phase)
   ax.set_yticks([])

balance
^^^^^^^

The *balance* colormap is diverging with dark blue to off-white to dark red representing negative to zero to positive values; this could be used to represent sea surface elevation, with deviations in the surface elevations as shades of color away from neutral off-white. In this case, shades of red have been chosen to represent sea surface elevation above the reference value (often mean sea level) to connect with warmer water typically being associated with an increase in the free surface, such as with the Loop Current in the Gulf of Mexico. An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf. This colormap is based on matplotlib's RdBu, but was recreated from scratch using the viscm tool.

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/ssh/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/ssh/2010.mp4

delta
^^^^^

The *delta* colormap is diverging from darker blues to just off-white through shades of yellow green and could be used to represent diverging velocity values around a critical value (usually zero). This colormap was inspired by `Francesca Samsel's <http://www.francescasamsel.com/>`_ similar colormap, but generated from scratch using the viscm tool.

.. figure:: https://pbs.twimg.com/media/CkIWDFRWkAEdArC.jpg
   :target: https://www.instagram.com/p/BGPoO-0Ryg8/

   From plotly.

.. figure:: http://pong.tamu.edu/~kthyng/movies/txla_plots/u/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/u/2010.mp4
   
   Model output in the northwest Gulf of Mexico from the Physical Oceanography Numerical Group (PONG) at Texas A&M.

curl
^^^^

The *curl* colormap is diverging from darker teal to just off-white through shades of magenta and could be used to represent diverging vorticity values around a critical value (usually zero). An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf.

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/vort/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/vort/2010.mp4


Capabilities
------------

The colormaps are all available in ``cmocean.cm``. They can be accessed, and simply plotted, as follows:

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.thermal, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.algae, ax=ax)

All available colormap names can be accessed with ``cmocean.cm.cmapnames``:

.. ipython:: python

   import cmocean

   cmocean.cm.cmapnames


The colormap instances can be accessed with:

.. ipython:: python

   import cmocean
   
   cmaps = cmocean.cm.cmap_d;

Print all of the available colormaps to text files with 256 rgb entries with:

``cmaps = cmocean.cm.cmap_d``

``cmocean.tools.print_colormaps(cmaps)``

Output a dictionary to define a colormap with:

.. ipython:: python

   import cmocean

   cmdict = cmocean.tools.get_dict(cmocean.cm.matter, N=9)
   print(cmdict)

Make a colormap instance with ``cmap = cmocean.tools.cmap(rgbin, N=10)`` given the rgb input array.

Reversed versions of all colormaps are available by appending "_r" to the colormap name, just as in matplotlib:

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.gray, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.test(cmocean.cm.gray_r, ax=ax)
   fig.tight_layout()


Resources
---------

Here are some of my favorite resources.

cmocean available elsewhere!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* For `MATLAB <http://www.mathworks.com/matlabcentral/fileexchange/57773-cmocean-perceptually-uniform-colormaps>`_ by `Chad Greene <http://www.chadagreene.com/>`_
* For R: `Oce <http://dankelley.github.io/oce/>`_ oceanographic analysis package by `Dan Kelley <http://www.dal.ca/faculty/science/oceanography/people/faculty/daniel-e-kelley.html>`_ and `Clark Richards <http://clarkrichards.org/>`_
* For `Ocean Data Viewer <https://github.com/kthyng/cmocean-odv>`_
* For Generic Mapping Tools (GMT)  at `cpt-city <http://soliton.vm.bytemark.co.uk/pub/cpt-city/cmocean/index.html>`_ and on `github <https://github.com/kthyng/cmocean-gmt>`_
* For `Paraview <https://github.com/kthyng/cmocean-paraview>`_, inspired by `Phillip Wolfram <https://github.com/pwolfram>`_.
* In `Plotly <https://plot.ly/python/cmocean-colorscales/>`_
* Chad Greene's `Antartic Mapping Tools <http://www.mathworks.com/matlabcentral/fileexchange/47638-antarctic-mapping-tools>`_ in Matlab uses cmocean
.. * In PyNcView: coming soon!

Examples of beautiful visualizations:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Earth wind/currents/temperature/everything `visualization <http://earth.nullschool.net/>`_: This is a wonderful visualization of worldwide wind and ocean dynamics and properties. It is also great for teaching, and seems to be continually under development and getting new fields as plotting options.
* This `fall foliage map <http://smokymountains.com/fall-foliage-map/>`_ is easy to use, clear, and eye-catching. It is what we all aspire to!
* A clever `visualization <http://www.nytimes.com/interactive/2014/07/08/upshot/how-the-year-you-were-born-influences-your-politics.html>`_ from The Upshot of political leaning depending on birth year. This is a perfect use of the diverging red to blue colormap.

Why jet is a bad colormap, and how to choose better:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* This is the article that started it all for me: `Why Should Engineers and Scientists Be Worried About Color? <http://www.research.ibm.com/people/l/lloydt/color/color.HTM>`_
* An excellent series on jet and choosing colormaps that will really teach you what you need to know, by `Matteo Niccoli <https://mycarta.wordpress.com/2012/05/29/the-rainbow-is-dead-long-live-the-rainbow-series-outline/>`_
* Nice summary of arguments against jet by `Jake Vanderplas <https://jakevdp.github.io/blog/2014/10/16/how-bad-is-your-colormap/>`_
* A good `summary <http://journals.ametsoc.org/doi/abs/10.1175/BAMS-D-13-00155.1>`_ in the Bulletin of the American Meteorological Society (BAMS) of visualization research and presentation of a tool for choosing good colormaps, aimed at atmospheric research but widely applicable.
* This `tool <http://www.etre.com/tools/colourblindsimulator/>`_ will convert your (small file size) image to how it would look to someone with various kinds of color blindness so that you can make better decisions about the colors you use.
* `Documentation <http://matplotlib.org/users/colormaps.html>`_ from the matplotlib plotting package site for choosing colormaps.
* Tips for choosing a good `scientific colormap <http://betterfigures.org/2015/06/23/picking-a-colour-scale-for-scientific-graphics/>`_
* `The end of the rainbow <http://www.climate-lab-book.ac.uk/2014/end-of-the-rainbow/>`_, a plea to stop using jet.
* Research shows that `jet is bad for your health! <http://phys.org/news/2011-10-heart-disease-visualization-experts-simpler.html>`_
* Reexamination of a previous study seems to show visual evidence indicating a front is really just an `artifact of the jet colormap <http://www.climate-lab-book.ac.uk/2016/why-rainbow-colour-scales-can-be-misleading/>`_

There is a series of talks from the SciPy conference from 2014 and 2015 talking about colormaps:

* `Damon McDougall <https://www.youtube.com/watch?v=Alnc9E1RnD8>`_ introducing the problem with jet for representing data.
* `Kristen Thyng <https://www.youtube.com/watch?v=rkDgBvT-giw>`_ following up with how to choose better colormaps, including using perceptually uniform colormaps and considering whether the information being represented is sequential or diverging in nature.
* `Nathaniel Smith and Stéfan van der Walt <https://www.youtube.com/watch?v=xAoljeRJ3lU&list=PLYx7XA2nY5Gcpabmu61kKcToLz0FapmHu&index=1>`_ explaining more about the jet colormap being bad, even bad for your health! They follow this up by proposing a new colormap for matplotlib, a Python plotting library.
* `Kristen Thyng <https://www.youtube.com/watch?v=XjHzLUnHeM0&list=PLYx7XA2nY5Gcpabmu61kKcToLz0FapmHu&index=35>`_ building off the work done by Nathaniel and Stéfan, a proposal of colormaps to plot typical oceanographic quantities (which led to cmocean!).

Other tips for making good figures:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* This `link <http://figuredesign.blogspot.com/2012/04/meeting-recap-colors-in-figures.html>`_ has a number of tips for choosing line color, colormaps, and using discrete vs. continuous colormaps.
* `How to graph badly or what not to do <http://www-personal.umich.edu/~jpboyd/sciviz_1_graphbadly.pdf>`_ has tips especially for line and bar plots and includes a summary of some of design guru `Edward Tufte's <http://www.edwardtufte.com/tufte/>`_ tips.

Tools for making nice figures:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `Seaborn <http://stanford.edu/~mwaskom/software/seaborn/>`_ will help you make very nice looking statistical plots.


Contact
-------

`Kristen Thyng <http://kristenthyng.com>`_ is the main developer of cmocean. Please email with questions, comments, and ideas. I'm collecting examples of the colormaps being used in action (see above) and also users of the colormaps, so I'd love to hear from you if you are using cmocean. kthyng at gmail.com

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

