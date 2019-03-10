#!/usr/bin/env python

from setuptools import setup

setup(name='test_multiphate',
	version='0.1.13',
	description='Phage annotation pipeline',
	author='Carol Zhou',
	author_email='zhou4@llnl.gov',
	url='https://github.com/carolzhou/test_multiphate',
        entry_points={
            'console_scripts': [
                'test_multiphate=test_multiphate.__main__:main',
            ],
        },
)
