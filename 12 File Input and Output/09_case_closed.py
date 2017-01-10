# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:10:15 2017

@author: mindovermiles262

Codecademy Python

Check if the file is not .closed.
If that's the case, call .close() on it.
(You don't need an else here, since your if statement should do nothing 
if .closed is True.)
After your if statement, print out the value of my_file.closed to make sure 
your file is really closed.

"""

with open("text.txt", "w") as my_file:
    my_file.write("Hello, world!")
    
if my_file.closed == False:
    my_file.close()
    
print(my_file.closed)