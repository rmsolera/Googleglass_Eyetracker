#!/usr/bin/env python
from distutils.core import setup

setup(
    name='wearscript',
    version='0.1',
    packages=['wearscript'],
    author='Brandyn A. White',
    author_email='bwhite@dappervision.com',
    license='Apache 2.0',
    description='Python hooks for the WearScript Project',
    long_description=open('README.md').read(),
    install_requires=[
        'gevent',
        'gevent-websocket',
        'websocket-client',
        'msgpack-python'
    ]
)
