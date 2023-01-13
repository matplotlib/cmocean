cmocean
=======

[![Build Status](https://img.shields.io/github/actions/workflow/status/matplotlib/cmocean/test.yaml?branch=main&logo=github&style=for-the-badge)](https://github.com/matplotlib/cmocean/actions/workflows/test.yaml)
[![Code Coverage](https://img.shields.io/codecov/c/github/matplotlib/cmocean.svg?style=for-the-badge)](https://codecov.io/gh/matplotlib/cmocean)
[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/cmocean.svg?style=for-the-badge)](https://anaconda.org/conda-forge/cmocean)
[![Python Package Index](https://img.shields.io/pypi/v/cmocean.svg?style=for-the-badge)](https://pypi.org/project/cmocean)
<!-- [![Documentation Status](https://img.shields.io/readthedocs/cmocean/latest.svg?style=for-the-badge)](https://cmocean.readthedocs.io/en/latest/?badge=latest) -->
<!-- [![Code Style Status](https://img.shields.io/github/actions/workflow/status/matplotlib/cmocean/linting.yaml?branch=main&label=Code%20Style&style=for-the-badge)](https://github.com/matplotlib/cmocean/actions/workflows/linting.yaml) -->

Documentation available: [http://matplotlib.org/cmocean/](http://matplotlib.org/cmocean/).

We have a paper with guidelines to colormap selection for your application and a description of the `cmocean` colormaps:
Thyng, K. M., Greene, C. A., Hetland, R. D., Zimmerle, H. M., & DiMarco, S. F. (2016). True colors of oceanography. Oceanography, 29(3), 10.
link: [http://tos.org/oceanography/assets/docs/29-3_thyng.pdf](http://tos.org/oceanography/assets/docs/29-3_thyng.pdf)

Besides Python, the cmocean colormaps are also available:

* For [MATLAB](http://www.mathworks.com/matlabcentral/fileexchange/57773-cmocean-perceptually-uniform-colormaps) by [Chad Greene](http://www.chadagreene.com/)
* For [R cmocean](https://github.com/aitap/cmocean), which includes [ggplot2](ggplot2.tidyverse.org/) compatible functions. Also included in [Oce](http://dankelley.github.io/oce/): an oceanographic analysis package by [Dan Kelley](http://www.dal.ca/faculty/science/oceanography/people/faculty/daniel-e-kelley.html) and [Clark Richards](http://clarkrichards.org/).
* For Julia, included in [Plots.jl](https://github.com/JuliaPlots/Plots.jl) and [Makie.jl](https://github.com/JuliaPlots/Makie.jl)
* For [Ocean Data Viewer](https://github.com/kthyng/cmocean-odv)
* For Generic Mapping Tools (GMT)  at [cpt-city](http://soliton.vm.bytemark.co.uk/pub/cpt-city/cmocean/index.html) and on [github](https://github.com/kthyng/cmocean-gmt)
* For [Paraview](https://github.com/kthyng/cmocean-paraview) inspired by [Phillip Wolfram](https://github.com/pwolfram)
* In [Plotly](https://plot.ly/python/cmocean-colorscales/)
* Chad Greene's [Antarctic Mapping Tools](http://www.mathworks.com/matlabcentral/fileexchange/47638-antarctic-mapping-tools) in Matlab uses `cmocean`
* For [Tableau](https://www.tableau.com) as a preferences file on [github](https://github.com/shaunwbell/cmocean_tableau)
* For [ImageJ](https://imagej.nih.gov/ij/) as [LUTs](https://github.com/mikeperrins/cmocean-LUT-ImageJ)
* For [ncview](http://meteora.ucsd.edu/~pierce/ncview_home_page.html) via [ncmaps](https://github.com/TomLav/ncmaps).
* For [SeaDAS](https://github.com/gertvd-stanford/cmocean_seadas), and should work with BEAM/SNAP as well.


To install:
``pip install cmocean``

To install with Anaconda:
``conda install -c conda-forge cmocean``

If you want to be able to use the `plots` submodule, you can instead install with:

`pip install "cmocean[plots]"`

which will also install `viscm` and `colorspacious`.
