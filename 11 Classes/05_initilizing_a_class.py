#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:28:24 2017

@author: mindovermiles262

Codecademy Python

Define the __init__() function of the Car class to take four inputs: self, 
model, color, and mpg. Assign the last three inputs to member variables of 
the same name by using the self keyword.

Then, modify the object my_car to provide the following inputs at 
initialization:

model = "DeLorean"
color = "silver"
mpg = 88

You don't need to include the self keyword when you create an instance of a 
class, because self gets added to the beginning of your list of inputs 
automatically by the class definition.

"""

class Car(object):
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
    condition = "new"
my_car = Car("DeLorean", "silver", 88)

print(my_car.condition)