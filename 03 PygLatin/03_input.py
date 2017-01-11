# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:44:55 2017

@author: mindovermiles262

Codecademy Python

On line 4, use raw_input("Enter a word:") to ask the user to enter a word. 
Save the results of raw_input() in a variable called original.
Click Save & Submit Code
Type a word in the console window and press Enter (or Return).

"""
print('Welcome to the Pig Latin Translator!')

try:
    original = raw_input("Enter a Word: ")
except NameError:
    original = input("Enter a Word: ")
