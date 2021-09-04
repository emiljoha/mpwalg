#!/usr/bin/env python3
from setuptools import setup

setup(name='mpwalg',
      version='0.2.1',
      description='Calculate a site\'s password',
      author='Emil Johansson',
      author_email='emil.sweden@gmail.com',
      url='https://github.com/emiljoha/pympw',
      py_modules=['mpw'],
      setup_requires=["pytest-runner"],
      install_requires=['scrypt', 'wheel'],
      tests_require=['pytest', 'pexpect']
)
