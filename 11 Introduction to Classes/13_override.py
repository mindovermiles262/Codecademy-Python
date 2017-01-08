#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 09:05:44 2017

@author: mindovermiles262

Codecademy Python

Create a new class, PartTimeEmployee, that inherits from Employee.
Give your derived class a calculate_wage method that overrides Employee's. 
It should take self and hours as arguments.
Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, 
it still needs to set self.hours = hours.
It should return the part-time employee's number of hours worked multiplied 
by 12.00 (that is, they get $12.00 per hour instead of $20.00).

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