# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:54:21 2017

@author: mindovermiles262

Codecademy Python

Set new_word equal to the slice from the 1st index all the way to the end of 
new_word. Use [1:len(new_word)] to do this.

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
    print(original)
else:
    print('empty')