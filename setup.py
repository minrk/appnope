#-----------------------------------------------------------------------------
#  Copyright (C) 2013 Min RK
#
#  Distributed under the terms of the 2-clause BSD License.
#-----------------------------------------------------------------------------

from distutils.core import setup
from distutils.extension import Extension

extensions = [
    Extension('nonap._nonap',
        sources = ['src/_nonap.m'],
        extra_link_args = ['-framework', 'Foundation']
    )
]

setup_args = dict(
    name = "nonap",
    version = '0.0.1',
    ext_modules = extensions,
    packages = ["nonap"],
    author = "Min Ragan-Kelley",
    author_email = "benjaminrk@gmail.com",
    url = 'http://github.com/minrk/nonap',
    download_url = 'http://github.com/minrk/nonap/releases',
    description = "Disable App Nap on OS X",
    long_description = "",
    license = "BSD",
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

