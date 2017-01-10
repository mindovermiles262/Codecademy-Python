# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:48:10 2017

@author: mindovermiles262

Codecademy Python

Create a variable, my_file, and set it equal to calling the open() function on 
output.txt. In this case, pass "r+" as a second argument to the function so 
the file will allow you to read and write to it! (See the Hint for details.)

HINT:
You can open files in write only mode ("w"), read only mode ("r"), read AND
write mode ("r+"), and append mode ("a"), which adds any new data you write to
the file to the end of the file.

"""

my_file = open("output.txt", "r+")