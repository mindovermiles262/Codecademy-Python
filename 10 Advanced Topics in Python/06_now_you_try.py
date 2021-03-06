#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:05:37 2017

@author: mindovermiles262

Codecademy Python

Use a list comprehension to create a list, cubes_by_four.
The comprehension should consist of the cubes of the numbers 1 through 10 only 
if the cube is evenly divisible by four.
Finally, print that list to the console.
Note that in this case, the cubed number should be evenly divisible by 4, not 
the original number.

"""

cubes_by_four = [x ** 3 for x in range(1,11) if x**3 % 4 == 0]
print cubes_by_four