#!/usr/bin/env python

'''
Setup.py script (uses setuptools) for building, testing, and installing simple_simulation.
'''

_VERSION="0.0.1"

from setuptools import setup
setup(name = 'simple_simulation',
    version = _VERSION,
    description = 'Simple genetic simulator',
    author = 'Gerald A McCollam',
    author_email = 'gerald.mccollam@gmail.com',
    url = '',
    download_url = 'https://github.com/atallah-lab/simple_simulation/tarball/' + _VERSION,
    platforms = 'Tested on Mac OS X.',
    package_dir = {'simple_simulation':'src'},
    packages = ['simple_simulation', 'tests'],
    package_data = {'tests': ['freqFiles/*', 'evolFiles/*']},
    install_requires=['numpy>=1.7', 'scipy', 'Biopython'],
    test_suite = "tests"
)
