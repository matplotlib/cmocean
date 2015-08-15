#!/usr/bin/env python

"""
setup.py for cmocean

"""
# import shutil
from setuptools import setup # to support "develop" mode
# from numpy.distutils.core import setup, Extension

# cmocean_mod = Extension(name = "cmocean",
#                          sources=['rgb/*',
#                                   ],
#                       )

# print cmocean_mod

setup(
    name = "cmocean",
    version = "0.01",
    author = "Kristen Thyng",
    author_email = "kthyng@gmail.com",
    description = ("Colormaps for Oceanography"),
    long_description=open('README.md').read(),
    classifiers=[
                 "Development Status :: 3 - Alpha",
    #             "Topic :: Utilities",
                 ],
    package_data={
        'cmocean': ['rgb/*.txt'],
    },    
    packages = ["cmocean"],
    # py_modules = cmocean_mod,
    ext_package='cmocean', 
    # ext_modules = [cmocean_mod],
    scripts = [],
    )
