#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:42:46 2017

@author: mindovermiles262

Codecademy Python

Inside the Car class, add a method drive_car() that sets self.condition to 
the string "used".
Remove the call to my_car.display_car() and instead print only the condition 
of your car.
Then drive your car by calling the drive_car() method.
Finally, print the condition of your car again to see how its value changes.

"""

class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def display_car(self):
        return ("This is a %s %s with %s MPG." % (self.color, self.model, self.mpg))
    def drive_car(self):
        self.condition = "used"
        return self.condition

my_car = Car("DeLorean", "silver", 88)
print(my_car.condition)
print(my_car.drive_car())