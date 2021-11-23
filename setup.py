# -*- coding: utf-8 -*-

# Note: To import source files from the package piwik,
#       use editable installation with
#
#           $ python setup.py develop
#
#       or
#
#           $ pip install -e .
#
#       To uninstall, use
#
#           $ python setup.py develop --uninstall

from setuptools import setup, find_packages

# package meta-data
NAME = "SeemsPhishy"
PACKAGES = find_packages("src")  # required
PACKAGE_DIR = {"": "src"}
VERSION = '0.1.0'
DESCRIPTION = 'Seems Phishy'
AUTHOR = 'Lukas Benner'
LICENSE ="GNU General Public License v3.0"
REQUIRES_PYTHON = ">=3.6.4"

# install
setup(
    name=NAME,
    packages=PACKAGES,
    package_dir=PACKAGE_DIR,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    license=LICENSE,
    python_required=REQUIRES_PYTHON,
)
