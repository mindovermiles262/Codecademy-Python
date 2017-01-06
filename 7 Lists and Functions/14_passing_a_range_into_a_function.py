# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:44:50 2017

@author: mindovermiles262

Codecademy Python

On line 6, replace the ____ with a range() that returns a list 
containing [0, 1, 2].

ONLY WORKING ON PYTHON 2.7

"""

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
    
# TODO: Fix range error in Python 3.  Need to convert range to list
#  >>> range(10)
#  range(0, 10)
# >>> list(range(10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(my_function(range(3))) # Add your range between the parentheses!

