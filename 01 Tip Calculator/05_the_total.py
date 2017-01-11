# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 07:27:40 2017

@author: mindovermiles262

Codecademy Python

Assign the variable total to the sum of meal + meal * tip on line 8. Now you 
have the total cost of your meal!

"""

# Assign the variable total on line 8!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)