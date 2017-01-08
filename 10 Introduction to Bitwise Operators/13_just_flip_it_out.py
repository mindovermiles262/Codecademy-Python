#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:06:45 2017

@author: mindovermiles262

Codecademy Python

In the editor is the 8 bit variable a. Use a bitmask and the value a in order 
to achieve a result where all of the bits in a are flipped. Be sure to 
print your answer as a bin() string!

"""

a = 0b11101110
mask = 0b11111111
print(bin(a ^ mask))