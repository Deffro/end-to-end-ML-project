#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = 'end-to-end-ML-project'
DESCRIPTION = "End to End ML Project"
URL = "https://github.com/Deffro/end-to-end-ML-project"
EMAIL = "dimitris.effrosynidis@gmail.com"
AUTHOR = "Dimitris Effrosynidis"
REQUIRES_PYTHON = ">=3.7.0"


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
# Trove Classifier for that!
long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).resolve().parent
REQUIREMENTS_DIR = ROOT_DIR / 'requirements'
PACKAGE_DIR = ROOT_DIR / 'src'
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


# What packages are required for this module to be executed?
def list_reqs(fname="production.txt"):
    with open(REQUIREMENTS_DIR / fname) as fd:
        reqs = fd.read().splitlines()
    # remove empty line
    reqs = list(filter(None, reqs))

    # add the packages from the -r requirement.txt in production.txt
    for req in reqs:
        if '-r' in req:
            with open(f"{REQUIREMENTS_DIR}/{req.split(' ')[1]}") as fd:
                extra_reqs = fd.read().splitlines()
            reqs.remove(req)
    return extra_reqs+reqs


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    package_data={"src": ["VERSION"]},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
