#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 08:33:30 2017

@author: mindovermiles262

Codecademy Python



"""

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print(self.name)
        print(self.age)
        
hippo = Animal("Hank", 100)
print(hippo.description())