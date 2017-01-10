# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:56:43 2017

@author: mindovermiles262

Codecademy Python

Create a function that returns the sum of a list of numbers.

On line 3, define a function called total that accepts one argument called 
numbers. It will be a list.
Inside the function, create a variable called result and set it to zero.
Using one of the two methods above, iterate through the numbers list.
For each number, add it to result.
Finally, return result.
Create a function called total that adds up all the elements of an arbitrary 
list and returns that count, using the existing code as a hint. Use a for 
loop so it can be used for any size list.

"""

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in numbers:
        print("Number: ", i)
        result = result + i
        print(result)
    return result

total(n)