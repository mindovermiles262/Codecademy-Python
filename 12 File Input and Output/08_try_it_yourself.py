# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:08:00 2017

@author: mindovermiles262

Codecademy Python

Now you try: write any data you like to the text.txt file using with...as. 
Give your file object the usual name: my_file.

"""

with open("text.txt", "w") as my_file:
    my_file.write("Hello, world!")