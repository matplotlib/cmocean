cmtamu
======

Colormap setup for standardizing commonly-plotting oceanographic variables, especially at Texas A&M. Most of the colormaps are straight from [matplotlib](http://matplotlib.org/).

Here is our gallery: [<img src="figures/gallery.png" class="picFloat">](figures/gallery.png)

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

## To use:

* `git clone git@github.com:kthyng/cmtamu.git`
* `pip install -e .` in the cloned directory to install a link to this package to where your site packages are stored. You might need to figure out permissions or prefixes, etc.
* Now you can import the package from wherever and use the awesome colormaps! That is, `from cmtamu import cmtamu' and get your salinity colormap instance with `cmap = cmtamu.salinity`. 

## Functions available:

### test:
* Generate a colormap that is linearly interpolated between input rgb or hex colors.
* Check the lightness values of a colormap.
* Read in a sample data set to then plot the data with grayscale, jet, and the same colormap.

### tools:
* Plot lightness of colormaps.
* Print the rgb of the colormaps to text files.
* Plot sample data up with colormaps.
* Plot a matplotlib-style gallery of the colormaps, including the grayscale equivalent.

### cmtamu:
* Functions that specify colormaps for each of eight oceanographic fields: salinity, temperature, density, PAR, oxygen, CDOM, chlorophyll, and turbidity.
* Can be imported and used directly to access colormaps by property.
