# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:41:07 2017

@author: mindovermiles262

Codecademy Python

On line 2, fill in the if statement to check if answer is greater than 5.
On line 4, fill in the elif so that the function outputs -1 if answer is less 
than 5.

"""

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))