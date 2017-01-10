# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:39:29 2017

@author: mindovermiles262

Codecademy Python

In the example above, we define a function called first_item. It has one 
argument called items.
Inside the function, we print out the item stored at index zero of items.
After the function, we create a new list called numbers.
Finally, we call the first_item function with numbers as its argument, which 
prints out 2.

"""

def list_function(x):
    return x[1]

n = [3, 5, 7]
print(list_function(n))