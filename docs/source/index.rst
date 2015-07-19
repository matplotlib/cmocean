.. cmocean documentation master file, created by
   sphinx-quickstart on Fri Jul 17 19:43:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Beautiful colormaps for oceanography: **cmocean**
=================================================

Contents:

.. toctree::
   :maxdepth: 2

This package contains colormaps for standardizing commonly-plotting oceanographic variables. Most of the colormaps started from `matplotlib <http://matplotlib.org/>`_ colormaps, but have now been adjusted using the `viscm tool <https://github.com/BIDS/viscm>`_ to be `perceptually uniform <http://bids.github.io/colormap/>`_.

Here is our gallery:

.. plot::
   :include-source:
   
   import cmocean
   cmocean.plots.plot_gallery()


Lightness plots of the colormaps: [<img src="figures/lightness.png" class="picFloat">](figures/lightness.png)

Sample data plots of the colormaps: [<img src="figures/MS2_L10.png" class="picFloat">](figures/MS2-L10.png)
[<img src="figures/MS08_L12.png" class="picFloat">](figures/MS08-L12.png)
[<img src="figures/MS09_L05.png" class="picFloat">](figures/MS09-L05.png)
[<img src="figures/MS09_L10.png" class="picFloat">](figures/MS09-L10.png)

Evaluations of the perceptual accuracy of the colormaps (see http://bids.github.io/colormap/): [<img src="figures/eval_Temperature.png" class="picFloat">](figures/eval_Temperature.png)
[<img src="figures/eval_Oxygen.png" class="picFloat">](figures/eval_Oxygen.png)
[<img src="figures/eval_Salinity.png" class="picFloat">](figures/eval_Salinity.png)
[<img src="figures/eval_Chlorophyll.png" class="picFloat">](figures/eval_Chlorophyll.png)
[<img src="figures/eval_Density.png" class="picFloat">](figures/eval_Density.png)
[<img src="figures/eval_PAR.png" class="picFloat">](figures/eval_PAR.png)
[<img src="figures/eval_Turbidity.png" class="picFloat">](figures/eval_Turbidity.png)
[<img src="figures/eval_CDOM.png" class="picFloat">](figures/eval_CDOM.png)



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

