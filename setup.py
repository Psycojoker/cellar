#!/usr/bin/python
# -*- coding:Utf-8 -*-

from setuptools import setup

setup(name='cellar',
      version='0.1.2',
      description='pkg manager for salt formulas',
      author='Laurent Peuch',
      #long_description='',
      author_email='cortex@worlddomination.be',
      url='https://github.com/Psycojoker/cellar',
      install_requires=['argh>=0.24.1', 'requests', 'pyyaml'],
      packages=[],
      license='MIT',
      scripts=['cellar'],
      keywords='salt pip pkg formula',
      )
