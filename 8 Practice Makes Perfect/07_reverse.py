# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:34:29 2017

@author: mindovermiles262

Define a function called reverse that takes a string textand returns that string in reverse.

For example: reverse("abcd") should return "dcba".

You may not use reversed or [::-1] to help you with this.
You may get a string containing special characters (for example, !, @, or #).

"""

def reverse(x):
    x = str(x)
    index = len(x) - 1
    reversed_output = []
    for i in x:
        reversed_output.append(x[index])
        index = index - 1
    return(''.join(reversed_output))