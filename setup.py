#!/usr/bin/env python
import os.path

from setuptools import setup, find_packages

here = os.path.dirname(__file__)
readme = open(os.path.join(here, 'README.rst')).read()

setup(
    name='check_bacula',
    use_scm_version=True,
    maintainer="Rick van den Hof",
    maintainer_email='r.vandenhof@exonet.nl',
    url='https://github.com/exonet/check-bacula',
    description='This tool checks the status of the backup jobs on a Bacula server.',
    long_description=readme,
    license='MIT',
    keywords='',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta'
    ],
    setup_requires=['setuptools_scm'],
    install_requires=['MySQL-python'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='nose.collector',
    entry_points={'console_scripts': ['check_bacula = check_bacula:main']},
)
