#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:09:56 2017

@author: mindovermiles262

Codecademy Python

Define a function called flip_bit that takes the inputs (number, n).
Flip the nth bit (with the ones bit being the first bit) and store it in result.
Return the result of calling bin(result).

"""

def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = number ^ mask
    return bin(result)