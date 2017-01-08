#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:33:44 2017

@author: mindovermiles262

Codecademy Python

Create a list, squares, that consists of the squares of the numbers 1 to 10. 
A list comprehension could be useful here!
Use filter() and a lambda expression to print out only the squares that are 
between 30 and 70 (inclusive).

"""

squares = [x ** 2 for x in range(1,11)]
print(filter(lambda y: y > 29 and y < 71, squares))