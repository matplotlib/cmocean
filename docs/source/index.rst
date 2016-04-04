.. cmocean documentation master file, created by
   sphinx-quickstart on Fri Jul 17 19:43:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Beautiful colormaps for oceanography: `cmocean <http://github.com/matplotlib/cmocean>`_
=======================================================================================

This package contains colormaps for standardizing commonly-plotting oceanographic variables. Most of the colormaps started from `matplotlib <http://matplotlib.org/>`_ colormaps, but have now been adjusted using the `viscm tool <https://github.com/BIDS/viscm>`_ to be `perceptually uniform <http://bids.github.io/colormap/>`_.

Here is our gallery:

.. plot::
   :include-source:

   import cmocean
   cmocean.plots.plot_gallery()

These colormaps were chosen to be perceptually uniform and to reflect the data they are representing in terms of being sequential, divergent, or cyclic (Phase colormap), and to be intuitive. For example, chlorophyll is represented by shades of green, turbidity is shades of brown, and temperature goes from cool blues to warm yellows.

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

Colormap details
----------------

Bathymetry
^^^^^^^^^^

The Bathymetry colormap is sequential from light yellow for shallower water through pale green to increasingly dark blue and purple to represent increasing depth. Nicknames for this colormap are 'bathymetry' and 'bathy', and the units are typically given as [m].

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.bathy, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.bathy, ax=ax)

CDOM
^^^^

The Colored Dissolved Organic Matter (CDOM) colormap is sequential with whitish-yellow for low values and increasing in pink with increasing value to represent an increase in material in the water. Two examples of this colormap are shown below, from Texas A&M University gliders. Nicknames for this colormap are 'CDOM' and 'cdom', and the units are typically given as [mg/m^3].

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_flbbcd_cdom_units.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_flbbcd_cdom_units.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_cdom_units.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_cdom_units.png

Chlorophyll
^^^^^^^^^^^

The Chlorophyll colormap is sequential with whitish-green for low values and increasing in green with increasing value to represent an increase in this green material in the water. Two examples of this colormap are shown below, from Texas A&M University gliders. Nicknames for this colormap are 'chl', 'chloro', and 'chlorophyll', and the units are typically given as [mg/m^3]. This colormap is based on matplotlib's Greens, but was recreated from scratch using the viscm tool.

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_flbbcd_chlor_units.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_flbbcd_chlor_units.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_chlor_units.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_flbbcd_chlor_units.png

Density
^^^^^^^

The Density colormap is sequential with whitish-blue for low values and increasing in purple with increasing value to represent an increase in water density. Two examples of this colormap are shown below, from Texas A&M University gliders. Nicknames for this colormap are 'density' and 'rho', and the units are typically given as [kg/m^3]. This colormap is based on matplotlib's Purples, but was recreated from scratch using the viscm tool.

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/calc_density.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/calc_density.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/calc_density.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/calc_density.png

Free Surface
^^^^^^^^^^^^

The Free Surface colormap is diverging with dark blue to off-white to dark red representing negative to zero to positive sea surface elevation, with deviations in the surface elevations as shades of color away from neutral off-white. Shades of red have been chosen to represent sea surface elevation above the reference value (often mean sea level) to connect with warmer water typically being associated with an increase in the free surface, such as with the Loop Current in the Gulf of Mexico. An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf. Nicknames for this colormaps are 'seasurface', 'freesurface', 'zeta', and 'eta', and the units are typically given as [m]. This colormap is based on matplotlib's RdBu, but was recreated from scratch using the viscm tool.

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/ssh/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/ssh/2010.mp4

Gray
^^^^

The Gray colormap is sequential from white to black, with uniform steps through perceptual colorspace. This colormap is generic to be used for any sequential dataset. Nicknames for this colormap are 'Gray', 'Grays', 'Grey', 'Greys', 'gray', 'grays', 'grey', and 'greys'.

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.grey, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.grey, ax=ax)

Oxygen
^^^^^^

The Oxygen colormap is sequential for most of the colormap, representing the normal range of oxygen saturation in ocean water, and diverging 80% of the way into the colormap to represent a state of supersaturation. The bottom 20% of the colormap is colored reddish to highlight hypoxic or low oxygen water, but to still print relatively seamlessly into grayscale in case the red hue is not important for an application. The top 20% of the colormap, after the divergence, is colored yellow to highlight the supersaturated water. The minimum and maximum values of this colormap are meant to be controlled in order to properly place the low oxygen and supersaturated oxygen states properly. This colormap was developed for the Mississippi river plume area where both low and supersaturated conditions are regularly seen and monitored. Examples of this colormap (without colorbar limits being controlled to set the values of the red and yellow regions) are shown from Texas A&M University gliders. Nicknames for this colormap are 'oxygen' and 'o2', and the units are typically given as [m/l].

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_oxy4_oxygen.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_oxy4_oxygen.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_oxy4_oxygen.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_oxy4_oxygen.png

PAR
^^^

The Photosynthetically Available Radiation (PAR) colormap is sequential from dark brown for low values to increasingly bright yellow to represent an increase in radiation in the water. Nicknames for this colormap are 'PAR' and 'par', and the units are typically given as [W/m^2].

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.par, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.par, ax=ax)

Phase
^^^^^

The Phase colormap is circular, spanning all hues at a set lightness value. This map is intended to be used for properties such as wave phase and tidal phase which wrap around from 0˚ to 360˚ to 0˚ and should be represented without major jumps in the colormap. Nicknames for this colormap are 'phase', 'direction', and 'direct', and the units are typically given as [˚]. An example for a circular plot is shown below.

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

Salinity
^^^^^^^^

The Salinity colormap is sequential with dark blue representing lower salinity or fresher water, transitioning through greens to light yellow representing increased salinity or saltier water. Several examples of this colormap are shown below, from Texas A&M University gliders and a simulation of the Texas and Louisiana shelf region. Nicknames for this colormap are 'salt' and 'salinity', and the units are typically given as [g/kg] or [ppt]. This colormap is based on matplotlib's YlGnBu, but was recreated from scratch using the viscm tool.

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/calc_salinity.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/calc_salinity.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/calc_salinity.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/calc_salinity.png
.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/salt/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/salt/2010.mp4

Speed
^^^^^

The Speed colormap is sequential from light greenish yellow representing low values to  with dark yellowish green representing large values. This colormap is the positive half of the velocity colormap, for consistency. An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf. Nicknames for this colormaps are 'speed' and 's', and the units are typically given as [m/s].

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/speed/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/speed/2010.mp4

Temperature
^^^^^^^^^^^

The Temperature colormap is sequential with dark blue representing lower temperature, transitioning through reds to yellow representing increased temperature. This colormap is meant to appeal to intuition of cooler colors representing cooler temperature and warmer colors as warmer temperature, but to be a sequential colormap to represent data between two temperatures (instead of a diverging, blue to white to red diverging colormap, for example). Several examples of this colormap are shown below, from Texas A&M University gliders and a simulation of the Texas and Louisiana shelf region. Nicknames for this colormap are 'temp' and 'temperature', and the units are typically given as [˚ Celsius]. This colormap is based on matplotlib's YlGnBu, but was recreated from scratch using the viscm tool.

.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_water_temp.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_540/plots/sci_water_temp.png
.. image:: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_water_temp.png
   :target: http://gcoos2.tamu.edu/gandalf_data/deployments/tamu/unit_541/plots/sci_water_temp.png
.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/temp/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/temp/2010.mp4

Turbidity
^^^^^^^^^

The Turbidity colormap is sequential from light to dark brown to represent an increase in sediment in the water. Nicknames for this colormap are 'turbidity' and 'turb', and the units are typically given as [NTU].

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.turb, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.turb, ax=ax)

Velocity
^^^^^^^^

The Velocity colormap is diverging from darker blues to just off-white through shades of yellow green representing diverging velocity values around a critical value (usually zero). The speed colormap is the positive half of this colormap, for consistency. An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf. Nicknames for this colormaps are 'velocity', 'vel', 'u', and 'v', and the units are typically given as [m/s]. This colormap was inspired by `Francesca Samsel's <http://www.francescasamsel.com/>`_ similar colormap, but generated from scratch using the viscm tool.

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/u/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/u/2010.mp4

Vorticity
^^^^^^^^^

The Vorticity colormap is diverging from darker teal to just off-white through shades of magenta representing diverging vorticity values around a critical value (usually zero). The Wave Period colormap is the negative half of this colormap (with inverse units). An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf. Nicknames for this colormaps are 'vorticity' and 'vort', and the units are typically given as [1/s].

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/vort/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/vort/2010.mp4

Wave Height
^^^^^^^^^^^

The Wave Height colormap is sequential from whitish to dark red representing an increase in wave height values. The Wave Height colormap is the positive half of the Free Surface colormap to be consistent with units. Nicknames for this colormaps are 'waveheight', 'waveheight', 'swh', and 'height', and the units are typically given as [m].

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.swh, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.swh, ax=ax)

Wave Period
^^^^^^^^^^^

The Wave Period colormap is sequential from whitish to dark teal representing an increase in wave period values. This colormap is the negative half of the Vorticity colormap, with inverse units. Nicknames for this colormaps are 'waveperiod' and 'period', and the units are typically given as [s].

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   cmocean.plots.test(cmocean.cm.period, ax=ax)
   ax = fig.add_subplot(1, 2, 2)
   cmocean.plots.quick_plot(cmocean.cm.period, ax=ax)


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

