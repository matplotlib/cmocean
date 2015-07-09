#!/usr/bin/env python

"""
setup.py for cmtamu

"""
# import shutil
from setuptools import setup # to support "develop" mode
# from numpy.distutils.core import setup, Extension

# cmtamu_mod = Extension(name = "cmtamu",
#                          sources=['rgb/*',
#                                   ],
#                       )

# print cmtamu_mod

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
    data_files=[('rgb', '*')],
    packages = 'cmtamu',
    # py_modules = cmtamu_mod,
    # ext_package='cmtamu', 
    # ext_modules = [cmtamu_mod],
    scripts = [],
    )
