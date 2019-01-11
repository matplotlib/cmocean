#!/usr/bin/env python

"""
setup.py for cmocean

"""
import sys
from setuptools import setup # to support "develop" mode
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.verbose = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

extras_require={
    'plots':  ["colorspacious", "viscm"],
}
# # in case I add more later
# extras_require['complete'] = sorted(set(sum(extras_require.values(), [])))

setup(
    name = "cmocean",
    version = "2.0",
    author = "Kristen Thyng",
    author_email = "kthyng@gmail.com",
    url = 'https://github.com/matplotlib/cmocean',
    download_url = 'https://github.com/matplotlib/cmocean/tarball/2.0',
    description = ("Colormaps for Oceanography"),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
                 "Development Status :: 3 - Alpha",
                 ],
    package_data={
        'cmocean': ['rgb/*.txt'],
    },
    packages = ["cmocean"],
    ext_package='cmocean',
    scripts = [],
    keywords = ['colormaps', 'oceanography', 'plotting', 'visualization'],
    tests_require=['pytest'],
    extras_require=extras_require
    )
