# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:38:40 2017

@author: mindovermiles262

Define a function called purify that takes in a list of numbers, removes all 
odd numbers in the list, and returns the result.

For example, purify([1,2,3]) should return [2].

Do not directly modify the list you are given as input; instead, return a new 
list with only the even numbers.

"""

def purify(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return even
        


print(purify([1, 2, 3]))
print(purify([0,1, 2, 3,4,5,6,7,8,9,10]))