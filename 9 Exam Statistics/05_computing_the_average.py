# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:13:20 2017

@author: mindovermiles262

Codecademy Python

Define a function grades_average(), below the grades_sum() function that does 
the following:

Has one argument, grades, a list
Calls grades_sum with grades
Computes the average of the grades by dividing that sum by float(len(grades)).
Returns the average.
Call the newly created grades_average() function with the list of grades and 
print the result.

"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
    total = 0
    for i in scores:
        total = total + i
    return total
    
def grades_average(grades):
    x = float(len(grades))
    avg = grades_sum(grades)/x
    return avg

print(grades_average(grades))