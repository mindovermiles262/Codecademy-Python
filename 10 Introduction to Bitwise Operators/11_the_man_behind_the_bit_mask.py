#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:46:40 2017

@author: mindovermiles262

Codecademy Python

Define a function, check_bit4, with one argument, input, an integer.
It should check to see if the fourth bit from the right is on.
If the bit is on, return "on" (not print!)
If the bit is off, return "off".
Check the Hint for some examples!

"""

def check_bit4(input):
    mask = 8
    desired = input & mask
    if desired > 0:
        return "on"
    else: return "off"