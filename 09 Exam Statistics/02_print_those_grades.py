# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:11:16 2017

@author: mindovermiles262

Codecademy Python

Define a function on line 3 called print_grades() with one argument, a list 
called grades.
Inside the function, iterate through grades and print each item on its own 
line.
After your function, call print_grades() with the grades list as the parameter.

"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for i in grades:
        print i
print_grades(grades)