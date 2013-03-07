#!/usr/bin/env python

from setuptools import setup

setup(
    name='FragDenStaat.at',
    version='1.0',
    description='Froide Theming for FragDenStaat.at',
    author='Markus Hametner',
    author_email='fin+fragdenstaatat@fin.io',
    url='https://fragdenstaat.at',
    packages=['fragdenstaat_at'],
    package_data={
        'fragdenstaat_at': [
            'templates/*',
            'locale/*/LC_MESSAGES/*',
            'static/*'
        ]
    },
)
