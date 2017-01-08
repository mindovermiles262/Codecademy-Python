#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:04:45 2017

@author: mindovermiles262

Codecademy Python

In the editor is a variable, a. Use a bitmask and the value a in order to 
achieve a result where the third bit from the right of a is turned on. 
Be sure to print your answer as a bin() string!

"""

a = 0b10111011
mask = 0b100
print(bin(a | mask))