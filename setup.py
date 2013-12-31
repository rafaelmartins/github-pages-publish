#!/usr/bin/env python

from setuptools import setup
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(current_dir, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='github-pages-publish',
    version='0.1',
    license='BSD',
    description=('A script that commits files from a directory to the '
                 'gh-pages branch of the current Git repository.'),
    long_description=long_description,
    author='Rafael Goncalves Martins',
    author_email='rafael@rafaelmartins.eng.br',
    url='https://github.com/rafaelmartins/github-pages-publish',
    install_requires=[
        'pygit2 >= 0.20.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    scripts=['github-pages-publish'],
)
