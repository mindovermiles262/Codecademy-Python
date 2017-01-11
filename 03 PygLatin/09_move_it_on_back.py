# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:53:04 2017

@author: mindovermiles262

Codecademy Python

On a new line after where you created the first variable:

Create a new variable called new_word and set it equal to the concatenation of 
word, first, and pyg.

"""

pyg = 'ay'

try:
    original = raw_input("Enter a Word: ")
except NameError:
    original = input("Enter a Word: ")

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    print(original)
else:
    print('empty')