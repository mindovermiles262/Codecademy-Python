#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:31:01 2017

@author: mindovermiles262

Codecademy Python

Now that you've created my_car print its member variables:

First print the model of my_car. Click "Stuck? Get a hint!" for an example.
Then print out the color of my_car.
Then print out the mpg of my_car.

"""

class Car(object):
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    condition = "new"
my_car = Car("DeLorean", "silver", 88)

print(my_car.model)
print(my_car.color)
print(my_car.mpg)