.. cmocean documentation master file, created by
   sphinx-quickstart on Fri Jul 17 19:43:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Beautiful colormaps for oceanography: `cmocean <http://github.com/matplotlib/cmocean>`_
=======================================================================================

This package contains colormaps for commonly-used oceanographic variables. Most of the colormaps started from `matplotlib <http://matplotlib.org/>`_ colormaps, but have now been adjusted using the `viscm tool <https://github.com/BIDS/viscm>`_ to be `perceptually uniform <http://bids.github.io/colormap/>`_.


.. note::  This is a new version of `cmocean` with four new colormaps!


.. note::  We have a paper with guidelines to colormap selection for your application and a description of the `cmocean` colormaps:

    Thyng, K. M., Greene, C. A., Hetland, R. D., Zimmerle, H. M., & DiMarco, S. F. (2016). True colors of oceanography. Oceanography, 29(3), 10.

    link: `<http://tos.org/oceanography/assets/docs/29-3_thyng.pdf>`_

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
   cmocean.plots.wrap_viscm(cmocean.cm.haline, saveplot=False)


All of the evaluations of the colormaps using the viscm tool are shown in the page :ref:`colormaps_viscm`.


Installation
------------

To install:
``pip install cmocean``

To install with Anaconda:
``conda install -c conda-forge cmocean``

If you want to be able to use the `plots` submodule, you can instead install with:

``pip install "cmocean[plots]"``

which will also install ``viscm`` and ``colorspacious``.


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


You can lighten a colormap using an alpha value below 1 with the `cmocean.tools.lighten()` function so that you can overlay contours and other lines that are more easily visible:

.. plot::
   :include-source:

   import cmocean
   import cmocean.cm as cmo
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(8, 3))
   ax = fig.add_subplot(1, 2, 1)
   Z = np.random.randn(10,10)
   ax.pcolormesh(Z, cmap=cmo.matter)

   ax = fig.add_subplot(1, 2, 2)
   lightcmap = cmocean.tools.lighten(cmo.matter, 0.5)
   ax.pcolormesh(Z, cmap=lightcmap)
   fig.tight_layout()


`cmocean` will register its colormaps with `matplotlib` so you can call them with, for example, 'cmo.amp':

.. plot::
   :include-source:

   import cmocean
   import matplotlib.pyplot as plt

   fig = plt.figure(figsize=(4, 3))
   ax = fig.add_subplot(111)
   Z = np.random.randn(10,10)
   ax.pcolormesh(Z, cmap='cmo.amp')


Clipping a colormap
^^^^^^^^^^^^^^^^^^^

You can clip off one or both ends of a colormap, either by the values you intend to plot with or by percent. For example, you can crop off both ends of a colormap by percent to reduce the lightness range and not have the very darkest values:

.. plot::
    :include-source:

    import cmocean
    import matplotlib.pyplot as plt

    cmap = cmocean.cm.tarn
    fig, axes = plt.subplots(1, 2, figsize=(8,4))
    A = np.random.randint(-5, 6, (10,10))
    mappable = axes[0].pcolormesh(A, cmap=cmap)
    axes[0].set_title('Full diverging colormap')
    fig.colorbar(mappable, ax=axes[0])

    newcmap = cmocean.tools.crop_by_percent(cmap, 30, which='both', N=None)
    mappable = axes[1].pcolormesh(A, cmap=newcmap)
    axes[1].set_title('Same colormap,\n30% removed from each end')
    fig.colorbar(mappable, ax=axes[1])


You can clip off one end of a colormap by percent. For example, you can crop the top part of the `oxy` colormap off, in case you are not considering super-saturated conditions (top 20% of the colormap), you can remove it from the colormap as follows:

.. plot::
    :include-source:

    import cmocean
    import matplotlib.pyplot as plt

    cmap = cmocean.cm.oxy
    fig, axes = plt.subplots(1, 2, figsize=(8,4))
    A = np.random.randint(0, 101, (10,10))
    mappable = axes[0].pcolormesh(A, vmin=0, vmax=100, cmap=cmap)
    axes[0].set_title('Values go to super-saturated')
    fig.colorbar(mappable, ax=axes[0])

    newcmap = cmocean.tools.crop_by_percent(cmap, 20, which='max', N=None)
    A[A>80] = 80
    mappable = axes[1].pcolormesh(A, vmin=0, vmax=80, cmap=newcmap)
    axes[1].set_title('Values are all\nbelow super-saturated')
    fig.colorbar(mappable, ax=axes[1])


You can remove part of one end of a colormap by inputting the values you intend to use in your plot and let the function figure out how much to crop off the colormap. This could be particularly useful if you have combined bathymetry and topography (sea and land elevations) data to plot with the `topo` colormap, but you want the maximum magnitudes to be different for water and land, and have this reflected in the colormap.

.. plot::
    :include-source:

    import cmocean
    import matplotlib.pyplot as plt

    cmap = cmocean.cm.topo
    fig, axes = plt.subplots(1, 2, figsize=(8,4))
    A = np.random.randint(-50, 201, (10,10))
    mappable = axes[0].pcolormesh(A, vmin=-200, vmax=200, cmap=cmap)
    axes[0].set_title('No values<-50, but still\nshow possibility in colorbar')
    fig.colorbar(mappable, ax=axes[0])

    newcmap = cmocean.tools.crop(cmap, -50, 200, 0)
    mappable = axes[1].pcolormesh(A, vmin=-50, vmax=200, cmap=newcmap)
    axes[1].set_title('Colorbar only shows color\nrange used by data')
    fig.colorbar(mappable, ax=axes[1])


Colormap details
----------------

thermal
^^^^^^^

The *thermal* colormap is sequential with dark blue representing lower, cooler values and transitioning through reds to yellow representing increased warmer values.

.. figure:: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/sci_water_temp.png
   :target: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/

   Glider data from Texas A&M's Geochemical and Environmental Research Group (`GERG <https://gerg.tamu.edu/>`_).


.. figure::  https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41598-017-16760-0/MediaObjects/41598_2017_16760_Fig5_HTML.jpg
   :target: https://www.nature.com/articles/s41598-017-16760-0

   Data from publication: Kenel, C., Grolimund, D., Li, X., Panepucci, E., Samson, V. A., Sanchez, D. F., ... & Leinenbach, C. (2017). In situ investigation of phase transformations in Ti-6Al-4V under additive manufacturing conditions combining laser melting and high-speed micro-X-ray diffraction. Scientific reports, 7(1), 16358.


.. figure:: http://www.mdpi.com/sensors/sensors-17-02679/article_deploy/html/images/sensors-17-02679-g002-550.jpg
   :target: http://www.mdpi.com/1424-8220/17/11/2679/htm

   Usamentiaga, R., Ibarra-Castanedo, C., Klein, M., Maldague, X., Peeters, J., & Sanchez-Beato, A. (2017). Nondestructive evaluation of carbon fiber bicycle frames using infrared thermography. Sensors, 17(11), 2679.


.. figure:: https://user-images.githubusercontent.com/3487237/42728531-d732b9ee-8781-11e8-90da-6f54007fe142.png

   Temperature plot of CTD data for the upper ocean; made by Luz Zarate Jimenez.


.. figure:: https://user-images.githubusercontent.com/3487237/42728546-16b3a448-8782-11e8-8971-f1e11631645d.png

   pH plot of full water depth bottle data, where the dots represent the depths where bottle water was collected; made by Luz Zarate Jimenez.


.. figure:: https://www.tandfonline.com/na101/home/literatum/publisher/tandf/journals/content/zela20/2018/zela20.v070.i01/16000870.2018.1471911/20180605/images/large/zela_a_1471911_f0001_c.jpeg
  :target: https://www.tandfonline.com/doi/abs/10.1080/16000870.2018.1471911

  WUNSCH, C. (2018). Towards determining uncertainties in global oceanic mean values of heat, salt, and surface elevation. Tellus A: Dynamic Meteorology and Oceanography, 70(1), 1-14.


.. figure:: https://pbs.twimg.com/media/Cxjs6Z8WQAAc_uX.jpg
   :target: https://twitter.com/mrtnrey/status/799651484686315524

   Showing temperature in meteorology work, by Maarten Reyniers.


.. figure:: https://pbs.twimg.com/media/CxtJS8eW8AEGmIm.jpg
   :target: https://twitter.com/seb_steinke/status/800315004297838592

   MODIS sea surface temperature from NASA OBPG, by Sebastian Steinke.


.. figure:: https://data.ioos.us/gliders/status/summary/static/profiles/drudnick/sp069-20181109T1607/temperature.png
  :target: http://oceansmap.maracoos.org/#

  Glider data from Mid-Atlantic Regional Association Coastal Ocean Observing System (`MARACOOS <https://maracoos.org/>`_).


.. figure:: https://www.tecplot.com/wp-content/gallery/geoscience/pugetsound_webimage.jpg
    :target: https://www.tecplot.com/applications/geoscience/

Ocean model visualization from `tecplot <https://www.tecplot.com/>`_.


.. figure:: https://ars.els-cdn.com/content/image/1-s2.0-S0967063718301638-gr2.jpg
    :target: https://www.sciencedirect.com/science/article/pii/S0967063718301638

Potter, H. (2018). The cold wake of typhoon Chaba (2010). Deep Sea Research Part I: Oceanographic Research Papers, 140, 136-141.

haline
^^^^^^

The *haline* colormap is sequential, and might be used with dark blue representing lower salinity or fresher water, transitioning through greens to light yellow representing increased salinity or saltier water. This colormap is based on matplotlib's YlGnBu, but was recreated from scratch using the viscm tool.

.. figure:: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/calc_salinity.png
   :target: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/

   Glider data from Texas A&M's Geochemical and Environmental Research Group (GERG).


.. figure:: http://pong.tamu.edu/~kthyng/movies/txla_plots/salt/2010-07-30T00.png
   :target: http://kristenthyng.com/gallery/txla_salinity.html

   Model output in the northwest Gulf of Mexico from the Physical Oceanography Numerical Group (PONG) at Texas A&M.


.. figure:: http://clarkrichards.org/figure/source/2016-04-25-making-section-plots/plot2-1.png
   :target: http://clarkrichards.org/r/oce/section/ctd/2016/04/25/making-section-plots/

   Plotting CTD data (temperature and salinity) with the R `oce` package, by `Clark Richards <http://clarkrichards.org/r/oce/section/ctd/2016/04/25/making-section-plots/>`_


.. figure:: https://user-images.githubusercontent.com/3487237/42728526-cd276e68-8781-11e8-9d77-db486b479a6d.png

   Alkalinity plot of full water depth bottle data, where the dots represent the depths where bottle water was collected; made by Luz Zarate Jimenez.


.. figure:: https://user-images.githubusercontent.com/3487237/42728535-df605f5e-8781-11e8-973e-0f7385daef3c.png

   Salinity plot of CTD data for the upper ocean; made by Luz Zarate Jimenez.


.. figure:: https://data.ioos.us/gliders/status/summary/static/profiles/drudnick/sp069-20181109T1607/salinity.png
   :target: http://oceansmap.maracoos.org/

Glider data from Mid-Atlantic Regional Association Coastal Ocean Observing System (`MARACOOS <https://maracoos.org/>`_).



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

.. figure:: https://media.giphy.com/media/26xBFRODTXDBKSmVa/giphy.gif
  :target: https://www.youtube.com/watch?v=Im-v6w5_NFw

  Arctic sea ice thickness by Nikolay Koldunov.


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


.. figure:: https://user-images.githubusercontent.com/3487237/42728540-0d24e28e-8782-11e8-8874-82e65d76ef34.png

   Oxygen plot of CTD data for the upper ocean; made by Luz Zarate Jimenez.


deep
^^^^

The *deep* colormap is sequential from light yellow to potentially represent shallower water through pale green to increasingly dark blue and purple to represent increasing depth.

.. figure:: https://cloud.githubusercontent.com/assets/3487237/16900541/4af66c4c-4bf5-11e6-92a9-82eaa39cb18b.png
   :target: http://iuryt.github.io/tutorial/Como_fazer_um_mapa02.html

   Bathymetry plot, by `Iury Sousa <http://iuryt.github.io/>`_


.. figure:: https://user-images.githubusercontent.com/3487237/42728981-de0d3ee4-878e-11e8-89ca-b124c49d5d0e.png

   Somov Sea bathymetry, by Josué Martinez Moreno, in `blender <https://www.blender.org/>`_


.. figure:: https://media.springernature.com/lw900/springer-static/image/art%3A10.1038%2Fs41467-018-05618-2/MediaObjects/41467_2018_5618_Fig1_HTML.png
    :target: https://www.nature.com/articles/s41467-018-05618-2

Gwyther, D. E., O’Kane, T. J., Galton-Fenzi, B. K., Monselesan, D. P., & Greenbaum, J. S. (2018). Intrinsic processes drive variability in basal melting of the Totten Glacier Ice Shelf. Nature communications, 9(1), 3141.



dense
^^^^^

The *dense* colormap is sequential with whitish-blue for low values and increasing in purple with increasing value, which could be used to represent an increase in water density. Two examples of this colormap are shown below, from Texas A&M University gliders. This colormap is based on matplotlib's Purples, but was recreated from scratch using the viscm tool.

.. image:: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/calc_density.png
   :target: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/


.. figure:: https://user-images.githubusercontent.com/3487237/42728541-11ed4d7e-8782-11e8-945c-1e2dcdb61ace.png

   Potential density plot of CTD data for the upper ocean; made by Luz Zarate Jimenez.


.. figure:: http://www.sfestuary.org/wp-content/uploads/2012/09/nut-500model_nh4-landsatgray.jpg
   :target: http://www.sfestuary.org/estuary-news-nutrient-nuances-modeled/

   Estimated ammonium in San Francisco Bay by Rusty Holleman.


algae
^^^^^

The *algae* colormap is sequential with whitish-green for low values and increasing in green with increasing value, which could be used to represent an increase in chlorophyll in the water. Two examples of this colormap are shown below, from Texas A&M University gliders. This colormap is based on matplotlib's Greens, but was recreated from scratch using the viscm tool.

.. image:: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/sci_flbbcd_chlor_units.png
   :target: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/


.. figure:: https://rbr-global.com/wp-content/uploads/2016/09/WireWalker_data_wide_zoom.png
   :target: https://rbr-global.com/products/systems/wirewalker

   Example data from RBR's Del Mar Oceanographic (DMO) Wirewalker, a wave-powered profiling system.


.. figure:: https://pbs.twimg.com/media/Cs_3GXbXgAAPwFQ.png
   :target: https://twitter.com/FJPavia/status/779113245063933952

   Satellite-derived Chl-a with sites indicated, by Frankie Pavia.



matter
^^^^^^

The *matter* colormap is sequential with whitish-yellow for low values and increasing in pink with increasing value, and could be used to represent an increase in material in the water. Two examples of this colormap are shown below, from Texas A&M University gliders.

.. image:: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/sci_flbbcd_cdom_units.png
   :target: http://gandalf.gcoos.org/data/gandalf/tamu/unit_307/2017/2017_12_18/plots/


.. figure:: http://www.sfestuary.org/wp-content/uploads/2012/09/Nut-model_din-landsatgray-500.jpg
   :target: http://www.sfestuary.org/estuary-news-nutrient-nuances-modeled/

   Estimated dissolved nitrogen in San Francisco Bay by Rusty Holleman.

turbid
^^^^^^

The *turbid* colormap is sequential from light to dark brown and could be used to represent an increase in sediment in the water.

.. figure:: https://user-images.githubusercontent.com/3487237/42729003-c604db6c-878f-11e8-97e8-978d6c172f3e.png

   Data of Queensland, by Emilia P. (`@mathinpython <https://twitter.com/mathinpython>`_).


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

.. figure:: https://media.springernature.com/lw900/springer-static/image/art%3A10.1038%2Fs41598-018-35936-w/MediaObjects/41598_2018_35936_Fig2_HTML.png
  :target: https://www.nature.com/articles/s41598-018-35936-w

  Baumgartner, B. L., O’Laughlin, R., Jin, M., Tsimring, L. S., Hao, N., & Hasty, J. (2018). Flavin-based metabolic cycles are integral features of growth and division in single yeast cells. Scientific reports, 8(1), 18045.


.. figure:: https://www.frontiersin.org/files/Articles/422317/fmars-05-00447-HTML/image_m/fmars-05-00447-g004.jpg
    :target: https://www.frontiersin.org/articles/10.3389/fmars.2018.00447/full

Lenhart, H. J., & Große, F. (2018). Assessing the effects of WFD nutrient reductions within an OSPAR frame using trans-boundary nutrient modeling. Frontiers in Marine Science, 5, 447.


.. figure:: https://ars.els-cdn.com/content/image/1-s2.0-S0380133018301321-gr4_lrg.jpg
    :target: https://www.sciencedirect.com/science/article/pii/S0380133018301321

Grunert, B. K., Brunner, S. L., Hamidi, S. A., Bravo, H. R., & Klump, J. V. (2018). Quantifying the influence of cold water intrusions in a shallow, coastal system across contrasting years: Green Bay, Lake Michigan. Journal of Great Lakes Research, 44(5), 851-863.


tempo
^^^^^

The *tempo* colormap is sequential from whitish to dark teal and could be used to represent an increase in wave period values. This colormap is the negative half of the *curl* colormap.


.. figure:: http://www.sfestuary.org/wp-content/uploads/2012/09/nut500-model_no3-landsatgray.png
   :target: http://www.sfestuary.org/estuary-news-nutrient-nuances-modeled/

   Estimated nitrate in San Francisco Bay by Rusty Holleman.


rain
^^^^

The *rain* colormap is sequential from light, dry colors to blue, wet colors, and could be used to plot amounts of rainfall.


.. figure:: https://user-images.githubusercontent.com/3487237/51001559-092d8800-14f6-11e9-93d4-57379b4c7701.png
   :target: https://user-images.githubusercontent.com/3487237/51001559-092d8800-14f6-11e9-93d4-57379b4c7701.png

   Rainfall, by Chad Greene.


phase
^^^^^

The *phase* colormap is circular, spanning all hues at a set lightness value. This map is intended to be used for properties such as wave phase and tidal phase which wrap around from 0˚ to 360˚ to 0˚ and should be represented without major perceptual jumps in the colormap.

.. figure:: https://user-images.githubusercontent.com/3487237/42728991-41ed6e0c-878f-11e8-80ad-4623b26de2cc.png

   Tidal phase in the North Atlantic ocean, by Kristen Thyng.


topo
^^^^

The *topo* colormap has two distinct parts: one that is shades of blue and yellow to represent water depths (this is the *deep* colormap) and one that is shades of browns and greens to represent land elevation.


.. figure:: https://user-images.githubusercontent.com/3487237/51001557-0894f180-14f6-11e9-9f8e-94fc0ffcfe11.png
   :target: https://user-images.githubusercontent.com/3487237/51001557-0894f180-14f6-11e9-9f8e-94fc0ffcfe11.png

   Bathymetry and topography, by Chad Greene.


balance
^^^^^^^

The *balance* colormap is diverging with dark blue to off-white to dark red representing negative to zero to positive values; this could be used to represent sea surface elevation, with deviations in the surface elevations as shades of color away from neutral off-white. In this case, shades of red have been chosen to represent sea surface elevation above the reference value (often mean sea level) to connect with warmer water typically being associated with an increase in the free surface, such as with the Loop Current in the Gulf of Mexico. An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf. This colormap is based on matplotlib's RdBu, but was recreated from scratch using the viscm tool.

.. image:: http://pong.tamu.edu/~kthyng/movies/txla_plots/ssh/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/ssh/2010.mp4


.. figure:: https://pbs.twimg.com/media/CsWzox7UsAAeKwS.jpg
   :target: http://stoqs.mbari.org:8000/stoqs_simz_oct2014/query/?permalink_id=N4IgDgNghgLgZgewE4FsD6BjCBLDBrAZxAC4BtEAYgFkBGNKhZbAOwHMACAIwFcYYFmAOgL8AjgQC0%2FVqwgBTYhgEwoLAgAoAOiFr1GSFq20BKEAF0ANCCy5CJcizC9SMAJ5g5AXm1IoAE2wEbTNSZigUL20CAAsEAHc%2FWCgoAmDSADcoCG5IkAIMWBg5JGCQK0dnNw9vEF8AoPNQ8NylCGQUKDBMWNw5NMzs3M4sqGYMPvMykAqYF3dcusC0sIiasChfCKKkAjRIBBh%2BrJyagCYaUvLmJ1mqhf8lxpXcgHkPZgAZKFdigkEAYWUSAQEEEXx%2BSAAynFsDAMNFimgAKwABjQwwIcnBvyOgxq7AAopCAEoASXYL3Go0u02ulXmNUWDRCzxq218LDQ6WwcjiuJO2mifDAxAA9KK%2FAg%2FH8UMMDIJkKxRezVMxRQAPADMflFDGY2zkrlOSLQNBR6t1ymKhuNpvNaHycmYckEWr8NJmc2q2nhcnwnAQ6uWzXxkKdBGQ7BgvnwqUaAwFIHYYeYEaQUZjhA9dNuDJ9CP9geDq20GagACs%2FfwDHI4yEE7ky5WMNWeXWpp67jVfYWg08Q6WRLBAqn%2BY2hzAR%2B2rjcvS0C3gA32WQOQGOagJs7Ou%2Fm%2FYui%2F2S2v48dcpvJjP6d7rAul8XcuvtOezB2c3Pu7eDyujyrOfCEL0j4gEKMAiuKkrSoIsobNgCpIEqv5qm6lr6taRommaFp6ga6F2uqDrjM6rraluV7znud6HrkUAttg3JuA6cjyC2mCcEBLyQvQdCnCiNAACwogA7DQABssTcEgECuGg%2FxUJCAAqABqghjKRubXj2%2B7Lk0R5Ac%2Br7bnmN4UV%2BOkPieeJPswanvruvZpNgfg1G8TrYjsAJAiCYLfMU0Kwr6SDImiMxoMm4aRtGNFZhetKGRpn7aY5znvG5fyAvqwKgm5flwgigWomgIVNlWTC1jZO7GfZjRJdoLmfD57npdGXnZTCuWIgVRUTlO5VGZplEhDVIAAF6MCg%2FByOqRT6gI3BgIkRS9fFJnaay2h6dZMWdn1CX3jUG1LeRVWDU561bW%2BFX9aZQ2HR%2BK0Oad4BgBIODOhsEhIHIrCfQQBAjrddlaQ9azPQQ4SQHIL0IAUk4CO2lggEUU1EGQ5AUBgKASBjLBTBIPHmBYaMY1jHTqlM%2BOWGjBDPdjzBTATVM06T9OU5QKBMzjVgM2zTNQGTXNmAjmLMTAKOkGjzDcOgrTIEQVjGiJ5gIzRShIPUzBoAg7xyH49jWCC0BgJi8lyOzyBZFMrSG5iEhQNw6SWwbnQ2yg%2BiGI7EDW5DMTYGAHte5C6yThbVhW87chNSCBCagAIlMC1QLH%2FvhxIugMEwbDJ0bkOSnUCAEyAKvIOrDqxHEdNkPrbSoJ0ttjLESAe%2B0tejP%2BjcIyonBi4zw5ZPJUBd2UKKsxQP0IBJ4z94PFjD4TlDUxICcq7WBCSuXbT%2BJ3cuz2j7OL0ky%2B%2FWvzAb34W9DyPRRm74EBT9vI8X3PFCFAYPBFAQd%2FaBfQsqEgMASKbFG%2FEaCalASJESKJIGQKsE6PwACUBAL4vxFEPEIFQJRFYIcf9F5yDADAaIJA8aCCRDA5gcC%2FC4PwSQVEGCQAdBpk6bYJBQBtBPrAZhIBWGEJAUiAAHHxTUfFeGCCEgIkSmorDQBgCQPiAkkTGmEZqESglTi8M1AATgAL5WFGggFAJAaC8O0XQ2u0AIRiyTESMkFIqR0ysGFVMEVMxyyTJFZsrZaxTHYN1OG5hNFAAAA%3D%3D

   Spatial Temporal Oceanographic Query System `(STOQS) <http://www.stoqs.org/>`_

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

The *curl* colormap is diverging from darker teal to just off-white through shades of magenta and could be used to represent diverging vorticity values around a critical value (usually zero).

.. figure:: http://pong.tamu.edu/~kthyng/movies/txla_plots/vort/2010-07-30T00.png
   :target: http://pong.tamu.edu/~kthyng/movies/txla_plots/vort/2010.mp4

   An example of this colormap is from a numerical simulation of the Texas and Louisiana shelf.


.. figure:: https://pbs.twimg.com/media/CuqlwdJWIAA1wT1.jpg
   :target: https://plot.ly/~empet/13557/cmoceanvorticity-colorscale

   Julia Set fractal in `plotly <https://plot.ly/>`_


diff
^^^^

The *diff* colormap is diverging, with one side shades of blues and one side shades of browns.


.. figure:: https://user-images.githubusercontent.com/3487237/51001561-092d8800-14f6-11e9-868b-009e947ed5eb.png
   :target: https://user-images.githubusercontent.com/3487237/51001561-092d8800-14f6-11e9-868b-009e947ed5eb.png

   Surface pressure anomaly for December 2017, by Chad Greene.


tarn
^^^^

The *tarn* colormap is diverging, with one side dry shades of browns and the other a range of greens and blues. The positive end of the colormap is meant to reflect the colors in *rain* and thus be a complementary colormap to *rain* for rain anomaly (around 0 or some other critical value).


.. figure:: https://user-images.githubusercontent.com/3487237/51001558-0894f180-14f6-11e9-91e1-3ef9e28fcc81.png
   :target: https://user-images.githubusercontent.com/3487237/51001558-0894f180-14f6-11e9-91e1-3ef9e28fcc81.png

   Rain anomaly, by Chad Greene.


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
* For `Tableau <https://www.tableau.com>`_ as a preferences file on `github <https://github.com/shaunwbell/cmocean_tableau>`_
* For `ImageJ <https://imagej.nih.gov/ij/>`_ as a preferences file on `LUTs <https://github.com/mikeperrins/cmocean-LUT-ImageJ>`_
* In `iGOTM <https://igotm.bolding-bruggeman.com/>`_, which simulates a water column anywhere in the world.
* cmocean colormaps are included in the following packages:
 * `colormap <https://github.com/bpostlethwaite/colormap>`_
 * `julia <http://docs.juliaplots.org/latest/colors/>`_
 * Spatial Temporal Oceanographic Query System `(STOQS) <http://www.stoqs.org/>`_ is a geospatial database software package designed for providing efficient access to in situ oceanographic measurement data.


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

`Kristen Thyng <http://kristenthyng.com>`_ is the main developer of cmocean. Please email with questions, comments, and ideas. I'm collecting examples of the colormaps being used in action (see above) and also users of the colormaps, so I'd love to hear from you if you are using cmocean. kthyng at gmail.com or on twitter @thyngkm.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
