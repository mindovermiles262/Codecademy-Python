# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:16:14 2017

@author: mindovermiles262

Codecademy Python

Define a function grades_std_deviation(variance).
return the result of variance ** 0.5
After the function, create a new variable called variance and store the result 
of calling grades_variance(grades).
Finally print the result of calling grades_std_deviation(variance).

"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print (grade)

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for i in scores:
        variance += (average - i)**2
    variance = variance / (float(len(scores)))
    return variance
    
def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print(grades_std_deviation(variance))
    
print(grades_variance(grades))