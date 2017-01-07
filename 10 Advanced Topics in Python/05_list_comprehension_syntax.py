#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:31:50 2017

@author: mindovermiles262

Codecademy Python

Use a list comprehension to build a list called even_squares in the editor.
Your even_squares list should include the squares of the even numbers between 
1 to 11. Your list should start [4, 16, 36...] and go from there.

"""

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Complete the following line. Use the line above for help.
even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

print(even_squares)