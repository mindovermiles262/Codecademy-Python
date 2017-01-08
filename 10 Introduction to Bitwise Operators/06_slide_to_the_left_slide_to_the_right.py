#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:36:24 2017

@author: mindovermiles262

Codecademy Python

Shift the variable shift_right to the right twice (>> 2) and shift the 
variable shift_left to the left twice (<< 2). Try to guess what the printed 
output will be!

"""

shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))