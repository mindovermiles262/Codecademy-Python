#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:29:54 2017

@author: mindovermiles262

Codecademy Python

First, inside your PartTimeEmployee class:

Add a new method called full_time_wage with the arguments self and hours.
That method should return the result of a super call to the calculate_wage 
method of PartTimeEmployee's parent class. Use the example above for help.
Then, after your class:

Create an instance of the PartTimeEmployee class called milton. Don't forget t
o give it a name.
Finally, print out the result of calling his full_time_wage method. You should 
see his wage printed out at $20.00 per hour! (That is, for 10 hours, the 
result should be 200.00.)

"""

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
        
milton = PartTimeEmployee("Milton")
print(milton.full_time_wage(10))