#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:36:58 2017

@author: mindovermiles262

Codecademy Python

Use a list comprehension to create a list, threes_and_fives, that consists 
only of the numbers between 1 and 15 (inclusive) that are evenly divisible by 
3 or 5.

"""

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]