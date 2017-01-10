# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:29:36 2017

@author: mindovermiles262

Write a function called digit_sum that takes a positive integer n as input and 
returns the sum of all that number's digits.

For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.

(Assume that the number you are given will always be positive.)

"""

def digit_sum(n):
    n = str(n)
    count = 0
    for i in n:
        count = count + int(i)
    return count