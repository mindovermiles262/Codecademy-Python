# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 07:50:19 2017

@author: mindovermiles262

Write a function called median that takes a list as an input and returns the 
median value of the list.

For example: median([1,1,2]) should return 1.

The list can be of any size and the numbers are not guaranteed to be in any 
particular order.

If the list contains an even number of elements, your function should return 
the average of the middle two.

"""

def median(original_data):
    sorted_data = sorted(original_data)
    length = len(sorted_data)
    if length % 2 == 0:
        low = int(length/2)-1
        high = low + 1
        med = (float(sorted_data[low]) + sorted_data[high])/2
    if length % 2 != 0:
        index = int(length/2)
        med = sorted_data[index]
    return med