# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:58:28 2017

@author: mindovermiles262

Codecademy Python

Create a function that joins two lists together.

On line 4, define a function called join_lists that has two arguments, x and y.
They will both be lists.
Inside that function, return the result of concatenating x and y together.

"""

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
    combined = []
    combined = x + y
    return combined

print(join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]