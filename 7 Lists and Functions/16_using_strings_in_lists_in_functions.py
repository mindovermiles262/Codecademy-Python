# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 09:57:30 2017

@author: mindovermiles262

Codecademy Python

Create a function that concatenates strings.

Define a function called join_strings accepts an argument called words. 
It will be a list.
Inside the function, create a variable called result and set it to "", 
an empty string.
Iterate through the words list and append each word to result.
Finally, return the result.
Don't add spaces between the joined strings!

"""

n = ["Michael", "Lieberman"]
def join_strings(words):
    result = ""
    for i in words:
        result = result + i
    return result


print(join_strings(n))