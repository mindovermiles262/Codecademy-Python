#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 08:23:11 2017

@author: mindovermiles262

Codecademy Python

Outside the Animal class definition, create a variable named zebra and set it 
equal to Animal("Jeffrey").
Then print out zebra's name.

"""

class Animal(object):
    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")
print zebra.name