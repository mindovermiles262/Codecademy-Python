# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:40:39 2017

@author: mindovermiles262

Codecademy Python

Change list_function so that:

Add 3 to the item at index one of the list.
Store the result back into index one.
Return the list.

"""

def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print(list_function(n))