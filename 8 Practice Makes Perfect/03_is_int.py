# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:25:48 2017

@author: mindovermiles262

Define a function is_int that takes a number x as an input.
Have it return True if the number is an integer (as defined above) and False otherwise.
For example:

is_int(7.0)   # True
is_int(7.5)   # False
is_int(-1)    # True      
"""

def is_int(x):
    if x == int(x):
        return True
    else: return False