# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:55:50 2017

@author: mindovermiles262

Codecademy Python

When you're sure your translator is working just the way you want it, click 
Save & Submit Code to finish this project.

"""

pyg = 'ay'

try:
    original = raw_input("Enter a Word: ")
except NameError:
    original = input("Enter a Word: ")

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    #new_word = word + first + pyg
    new_word = word[1:] + first + pyg
    print("Original: ", original)
    print("Pyglatin: ", new_word)
else:
    print('empty')