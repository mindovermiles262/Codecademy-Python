#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 18:30:25 2017

@author: mindovermiles262

Codecademy Python

In the console are several different ways that you can use the int function's s
econd parameter.

On line 7, use int to print the base 10 equivalent of the binary 
number 11001001.

"""

print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("11001001", 2))