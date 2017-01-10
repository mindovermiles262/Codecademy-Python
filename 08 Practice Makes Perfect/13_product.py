# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:50:01 2017

@author: mindovermiles262

Define a function called product that takes a list of integers as input and 
returns the product of all of the elements in the list.

For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

Don't worry about the list being empty.
Your function should return an integer.

"""

def product(numbers):
    total = 1
    for i in numbers:
        total = total * i
    return total
    
print(product([4,5,5]))