#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 08:30:41 2017

@author: mindovermiles262

Codecademy Python

Check out the examples in the editor. See how __init__() "boots up" each 
object to expect a name and an age, then uses self.name and self.age to assign 
those names and ages to each object? Add a third attribute, is_hungry 
to __init__(), and click Save & Submit Code to see the results.

"""

# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry