#!/usr/bin/env python
version = "0.1"

import codecs
import os
import sys
import pip

from pip.req import parse_requirements
from setuptools import setup, find_packages
from os.path import abspath, dirname, join

here = abspath(dirname(__file__))

# Determine the python version.
IS_PYPY = hasattr(sys, 'pypy_version_info')

with codecs.open(join(here, 'README.md'), encoding='utf-8') as f:
    README = f.read()

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

install_reqs = parse_requirements('requirements.txt', session=pip.download.PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='check_bacula',
    version=version,
    maintainer="Rick van den Hof",
    maintainer_email='r.vandenhof@exonet.nl',
    url='https://github.com/exonet/check-bacula',
    description='This tool checks the status of the backup jobs on a Bacula server.',
    long_description=README,
    license='License :: OSI Approved :: MIT License',
    keywords='',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'Environment :: Console',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta'
    ],
    setup_requires=['nose', 'coverage'] + reqs,
    install_requires=reqs,
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='nose.collector',
    entry_points={'console_scripts': ['check_bacula = check_bacula:main']},
)
