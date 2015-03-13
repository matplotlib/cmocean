#!/usr/bin/env python

"""
setup.py for cmtamu

"""
# import shutil
from setuptools import setup # to support "develop" mode
# from numpy.distutils.core import setup, Extension

setup(
    name = "cmtamu",
    version = "0.01",
    author = "Kristen Thyng",
    author_email = "",
    description = ("Colormaps for Texas A&M Oceanography"),
    long_description=open('README.md').read(),
    classifiers=[
                 "Development Status :: 3 - Alpha",
    #             "Topic :: Utilities",
                 ],
    packages = ["cmtamu"],
    # py_modules = modules,
    ext_package='cmtamu', 
    scripts = [],
    )
