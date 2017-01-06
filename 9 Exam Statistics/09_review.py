# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:17:16 2017

@author: mindovermiles262

Codecademy Python

Print out the following:

-all of the grades
-sum of grades
-average grade
-variance
-standard deviation

"""

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print(grade)

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
    dev = variance ** 0.5
    return dev
    
variance = grades_variance(grades)
    

total = grades_sum(grades)
av = grades_average(grades)
va = grades_variance(grades)
stdev = grades_std_deviation(variance)
  
print_grades(grades)  
print(total)
print(av)
print(va)
print(stdev)