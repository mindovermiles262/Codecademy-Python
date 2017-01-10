#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:34:21 2017

@author: mindovermiles262

Codecademy Python

Inside the Car class, add a method named display_car() to Car that will 
reference the Car's member variables to return the string, "This is a [color] 
[model] with [mpg] MPG." You can use the str() function to turn your mpg into 
a string when creating the display string.
Replace the individual print statements with a single print command that 
displays the result of calling my_car.display_car()

"""

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return ("This is a %s %s with %s MPG." % (self.color, self.model, self.mpg))

my_car = Car("DeLorean", "silver", 88)

print(my_car.display_car())