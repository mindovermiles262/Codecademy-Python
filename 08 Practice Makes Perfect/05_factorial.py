# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:32:42 2017

@author: mindovermiles262

Define a function factorial that takes an integer x as input.

Calculate and return the factorial of that number.

"""

def factorial(x):
    x = int(x)
    fac = 1
    while x > 0:
        fac = fac * x
        x = x-1
    return fac