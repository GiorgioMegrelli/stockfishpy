import codecs
import os
import sys
from distutils.util import convert_path
from fnmatch import fnmatchcase

from setuptools import find_packages, setup


def read(f_name):
    return codecs.open(os.path.join(os.path.dirname(__file__), f_name)).read()


# Provided as an attribute, so you can append to these instead
# of replicating them:
STANDARD_EXCLUDE = ["*.py", "*.pyc", "*$py.class", "*~", ".*", "*.bak"]
STANDARD_EXCLUDE_DIRECTORIES = [
    ".*",
    "CVS",
    "_darcs",
    "./build",
    "./dist",
    "EGG-INFO",
    "*.egg-info",
]


# (c) 2005 Ian Bicking and contributors; written for Paste (http://pythonpaste.org)
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
# Note: you may want to copy this into your setup.py file verbatim, as
# you can't import this from another package, when you don't know if
# that package is installed yet.
def find_package_data(
    where=".",
    package="",
    exclude=None,
    exclude_directories=None,
    only_in_packages=True,
    show_ignored=False,
):
    """
    Return a dictionary suitable for use in ``package_data``
    in a distutils ``setup.py`` file.
    The dictionary looks like::
        {"package": [files]}
    Where ``files`` is a list of all the files in that package that
    don"t match anything in ``exclude``.
    If ``only_in_packages`` is true, then top-level directories that
    are not packages won"t be included (but directories under packages
    will).
    Directories matching any pattern in ``exclude_directories`` will
    be ignored; by default directories with leading ``.``, ``CVS``,
    and ``_darcs`` will be ignored.
    If ``show_ignored`` is true, then all the files that aren"t
    included in package data are shown on stderr (for debugging
    purposes).
    Note patterns use wildcards, or can be exact paths (including
    leading ``./``), and all searching is case-insensitive.
    """
    if exclude_directories is None:
        exclude_directories = STANDARD_EXCLUDE_DIRECTORIES
    if exclude is None:
        exclude = STANDARD_EXCLUDE

    out = {}
    stack = [(convert_path(where), "", package, only_in_packages)]
    while stack:
        where, prefix, package, only_in_packages = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if fnmatchcase(name, pattern) or fn.lower() == pattern.lower():
                        bad_name = True
                        if show_ignored:
                            print(
                                "Directory {} ignored by pattern {}".format(
                                    fn, pattern
                                ),
                                file=sys.stderr,
                            )
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, "__init__.py")) and not prefix:
                    if not package:
                        new_package = name
                    else:
                        new_package = package + "." + name
                    stack.append((fn, "", new_package, False))
                else:
                    stack.append((fn, prefix + name + "/", package, only_in_packages))
            elif package or not only_in_packages:
                # is a file
                bad_name = False
                for pattern in exclude:
                    if fnmatchcase(name, pattern) or fn.lower() == pattern.lower():
                        bad_name = True
                        if show_ignored:
                            print(
                                "File {} ignored by pattern {}".format(fn, pattern),
                                file=sys.stderr,
                            )
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix + name)
    return out


PACKAGE = "stockfishpy"
NAME = "stockfishpy"
DESCRIPTION = "Simple python Stockfish wrapper"
AUTHOR = "dani4kor"
AUTHOR_EMAIL = "dani4kor@gmail.com"
URL = "https://github.com/Dani4kor/stockfishpy"
VERSION = __import__(PACKAGE).__version__


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="GPLv3",
    url=URL,
    packages=find_packages(exclude=["tests.*", "tests"]),
    package_data=find_package_data(PACKAGE, only_in_packages=False),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False,
)
