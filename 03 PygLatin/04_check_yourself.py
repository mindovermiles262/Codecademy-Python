# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:48:03 2017

@author: mindovermiles262

Codecademy Python

Write an if statement that verifies that the string has characters.

Add an if statement that checks that len(original) is greater than zero. Don't 
forget the : at the end of the if statement!
If the string actually has some characters in it, print the user's word.
Otherwise (i.e. an else: statement), please print "empty".
You'll want to run your code multiple times, testing an empty string and a 
string with characters. When you're confident your code works, continue to the 
next exercise.

"""
print('Welcome to the Pig Latin Translator!')

try:
    original = raw_input("Enter a Word: ")
except NameError:
    original = input("Enter a Word: ")
    
if len(original) > 0:
    print(original)
else:
    print("empty")