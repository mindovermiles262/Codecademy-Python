#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:17:37 2017

@author: mindovermiles262

Codecademy Python

Create a variable, backwards_by_tens, and set it equal to the result of going 
backwards through to_one_hundred by tens. Go ahead and print backwards_by_tens 
to the console.

"""

to_one_hundred = range(101)
# Add your code below!

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)