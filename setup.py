#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='minesweeper-py',
    version='1.0.0',
    description=u'A command line minesweeper game',
    long_description=open('README.rst').read(),
    license='GPLv3',
    author=u'Ton van der Lee',
    author_email='t0m.vd.l33@gmail.com',
    url='http://github.com/tomvanderlee/minesweeper-py',
    packages= find_packages(),
    entry_points={
        'console_scripts': [
            'minesweeper-py = minesweeper.__main__:main',
        ]
    }
)
