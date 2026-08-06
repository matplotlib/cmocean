#!/usr/bin/env python

"""
setup.py for cmocean

"""
from setuptools import setup # to support "develop" mode

extras_require={
    'plots':  ["colorspacious", "viscm"],
    'test':  ["pytest"],
}
# # in case I add more later
# extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))

setup(
    name = "cmocean",
    version = "v4.0.3",
    author = "Kristen Thyng",
    author_email = "kthyng@gmail.com",
    url = 'https://github.com/matplotlib/cmocean',
    # download_url = 'https://github.com/matplotlib/cmocean/tarball/2.0',
    description = ("Colormaps for Oceanography"),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
                 "Development Status :: 3 - Alpha",
                 ],
    package_data={
        'cmocean': ['rgb/*.txt', 'rgb/inverted/*.txt'],
    },
    packages = ["cmocean"],
    ext_package='cmocean',
    scripts = [],
    keywords = ['colormaps', 'oceanography', 'plotting', 'visualization'],
    install_requires=['matplotlib', 'numpy', 'packaging'],
    python_requires=">=3.8",
    extras_require=extras_require
    )
