"""
# File          : setup.py
# Created       : 06/09/22 11:48 am
# Author        : Ron Greego
# Version       : v1.0.0
# Description   :
#
"""
from setuptools import find_packages, setup

setup(
    name='ukpcvalidationlib',
    packages=find_packages(include=['ukpcvalidationlib']),
    description='A library that supports validating and formatting postcodes for the UK',
    author='Ron Greego',
    license='MIT',
    install_requires=[],
    tests_require=['pytest==7.1.3'],
    test_suite='tests',
)