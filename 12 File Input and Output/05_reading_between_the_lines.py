# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 08:57:29 2017

@author: mindovermiles262

Codecademy Python

Declare a new variable my_file and store the result of calling open() on 
the "text.txt" file in "r"ead-only mode.
On three separate lines, print out the result of calling my_file.readline(). 
See how it gets the next line each time?
Don't forget to close() your file when you're done with it!)

"""
# Write text.txt to bypass codecademy "No such file or directory" error
my_file = open("text.txt", "w")
my_file.write("I'm the first line of the file!\nI'm the second line.\nThird line here, boss.")
my_file.close()


my_file = open("text.txt", "r")
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()