#!/usr/bin/env python
"""
Install script for the snakefood dependency graph tool.
"""

__author__ = "Martin Blais <blais@furius.ca>"

import os
from os.path import join, isfile
from distutils.core import setup


# Install all scripts under bin.
scripts = filter(isfile, [join('bin', x) for x in os.listdir('bin')])

def read_version():
    try:
        return open('VERSION', 'r').readline().strip()
    except IOError, e:
        raise SystemExit(
            "Error: you must run setup from the root directory (%s)" % str(e))

setup(name="snakefood",
      version=read_version(),
      description=\
      "Dependency Graphing for Python",
      long_description="""
Generate dependencies from Python code, filter, cluster and generate graphs
from the dependency list.
""",
      license="GPL",
      author="Martin Blais",
      author_email="blais@furius.ca",
      url="http://furius.ca/snakefood",
      package_dir = {'': 'lib/python'},
      packages = ['snakefood'],
      scripts=scripts
     )


