#-----------------------------------------------------------------------------
#  Copyright (C) 2013 Min RK
#
#  Distributed under the terms of the 2-clause BSD License.
#-----------------------------------------------------------------------------

from __future__ import print_function

import sys

from setuptools import setup
from setuptools.command.bdist_egg import bdist_egg


with open('appnope/__init__.py') as f:
    for line in f:
        if line.startswith('__version__'):
            __version__ = eval(line.split('=', 1)[1])
            break

class bdist_egg_disabled(bdist_egg):
    """Disabled version of bdist_egg

    Prevents setup.py install from performing setuptools' default easy_install,
    which it should never ever do.
    """
    def run(self):
        sys.exit("Aborting implicit building of eggs. Use `pip install .` to install from source.")


with open("README.md") as f:
    readme = f.read()


setup_args = dict(
    name="appnope",
    version=__version__,
    packages=["appnope"],
    author="Min Ragan-Kelley",
    author_email="benjaminrk@gmail.com",
    url="http://github.com/minrk/appnope",
    description="Disable App Nap on macOS >= 10.9",
    long_description=readme,
    long_description_content_type="text/markdown",
    license = "BSD",
    cmdclass = {
        'bdist_egg': bdist_egg if 'bdist_egg' in sys.argv else 'bdist_egg_disabled',
    },
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
)

setup(**setup_args)
