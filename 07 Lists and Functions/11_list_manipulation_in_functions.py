# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:42:05 2017

@author: mindovermiles262

Codecademy Python

Define a function called list_extender that has one parameter lst.
Inside the function, append the number 9 to lst.
Then return the modified list.

"""

n = [3, 5, 7]
# Add your function here
def list_extender(lst):
    lst.append(9)
    return lst


print(list_extender(n))