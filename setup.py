#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
    name='nmap',
    description='Map numbers from one range to another',
    version='0.0.1',
    author='Anton Agestam',
    author_email='msn@antonagestam.se',
    packages=find_packages(),
    url='https://github.com/antonagestam/nmap/',
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Topic :: Utilities',
    ]
)
