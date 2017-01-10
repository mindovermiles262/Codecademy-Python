#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:42:46 2017

@author: mindovermiles262

Codecademy Python

Create a class ElectricCar that inherits from Car. Give your new class an 
__init__() method of that includes a "battery_type" member variable in 
addition to the model, color and mpg.

Then, create an electric car named "my_car" with a "molten salt" battery_type. 
Supply values of your choice for the other three inputs (model, color and mpg).

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

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type
        
    def display_car(self):
        inheret_str = super(ElectricCar, self).display_car()
        return inheret_str + " It has a %s battery." % self.battery_type

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print(my_car.display_car())