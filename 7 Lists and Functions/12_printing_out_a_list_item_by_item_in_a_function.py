# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:42:51 2017

@author: mindovermiles262

Codecademy Python

Define a function called print_list that has one argument called x.
Inside that function, print out each element one by one. Use the existing code as a scaffold.
Then call your function with the argument n.

"""

n = [3, 5, 7]
def print_list(x):
    for i in range(0, len(x)):
        print(x[i])

print (print_list(n))