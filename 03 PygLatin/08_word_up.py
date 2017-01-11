# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:51:52 2017

@author: mindovermiles262

Codecademy Python

Create a new variable called word that holds the .lower()-case conversion of 
original.
Create a new variable called first that holds word[0], the first letter of 
word.

"""

pyg = 'ay'

try:
    original = raw_input("Enter a Word: ")
except NameError:
    original = input("Enter a Word: ")

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    print(original)
else:
    print('empty')