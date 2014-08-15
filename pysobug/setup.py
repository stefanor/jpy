#!/usr/bin/env python3

from distutils.core import setup
from distutils.extension import Extension

extension = Extension('mypymod', sources=['mypymod.c'], libraries=['python3.4m'])
setup(name='mypymod', ext_modules=[extension])
