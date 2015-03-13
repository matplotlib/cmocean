cmtamu
======

Colormap setup for standardizing commonly-plotting oceanographic variables, especially at Texas A&M. Most of the colormaps are straight from [matplotlib](http://matplotlib.org/).

Here is our gallery: [<img src="figures/gallery.png" class="picFloat">](figures/gallery.png)

## To use:

* `git clone git@github.com:kthyng/cmtamu.git`
* `pip install -e .` in the cloned directory to install a link to this package to where your site packages are stored. You might need to figure out permissions or prefixes, etc.
* Now you can import the package from wherever and use the awesome colormaps! That is, `from cmtamu import cmtamu' and get your salinity colormap instance with `cmap = cmtamu.salinity`. 