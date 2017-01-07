#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:47:14 2017

@author: mindovermiles262

Codecademy Python

For each key in my_dict: print out the key , then a space, then the value 
stored by that key.

(You should use print a, b rather than print a + " " + b.)

"""

mmy_dict = {
    "Name": "ERIK",
    "Age": 27,
    "Loved": True   
}
for key in my_dict:
    print key, my_dict[key] # Use with Python 2
    #print(key, my_dict[key], sep=' ') #Use for Python 3