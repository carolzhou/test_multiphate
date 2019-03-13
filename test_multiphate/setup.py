#!/usr/bin/env python

from setuptools import setup

setup(name='test_multiphate',
	version='0.1.15',
	description='Phage annotation pipeline',
	author='Carol Zhou',
	author_email='zhou4@llnl.gov',
	url='https://github.com/carolzhou/test_multiphate',
        license='BSD-3',
        keywords='phage genome annotation bioinformatics',
        install_requires=[
            'biopython',
            'trnascan-se',
            'glimmer',
            'prodigal',
            'hmmer',
        ],
        python_requires='~=3.4',
        entry_points={
            'console_scripts': ['test_multiphate=__main__:main'],
            'scripts': ['multiPhate'],
        },
)