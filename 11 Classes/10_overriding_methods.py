#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 18:05:37 2017

@author: mindovermiles262

Codecademy Python

Inside ElectricCar add a new method drive_car() that changes the car's 
condition to the string "like new".
Then, outside of ElectricCar, print the condition of my_car
Next, drive my_car by calling the drive_car() function
Finally, print the condition of my_car again

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
        return inheret_str + "It has a %s battery." % self.battery_type
        
    def drive_car(self):
        self.condition = "like new"
        return self.condition

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
print(my_car.condition)
print(my_car.drive_car())