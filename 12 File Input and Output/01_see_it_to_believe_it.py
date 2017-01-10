# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:46:05 2017

@author: mindovermiles262

Codecademy Python

Click Save & Submit Code, then check out the output.txt tab to see Python's 
file I/O powers in action.

"""

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()