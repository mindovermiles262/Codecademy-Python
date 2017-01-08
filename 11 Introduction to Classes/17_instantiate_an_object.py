#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:53:59 2017

@author: mindovermiles262

Codecademy Python

Create a variable named my_triangle and set it equal to a new instance of your 
Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
Print out my_triangle.number_of_sides
Print out my_triangle.check_angles()

"""

class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3==180:
            return True
        else: return False
        
my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())