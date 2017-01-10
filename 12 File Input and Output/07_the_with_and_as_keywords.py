# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:05:14 2017

@author: mindovermiles262

Codecademy Python

Check out the example in the editor. Note that we don't explicitly close() our 
file, and remember that if we don't close a file, our data will get stuck in 
the buffer. Click Save & Submit Code and check out text.txt to see the results.

"""

with open("text.txt", "w") as textfile:
	textfile.write("Success!")
 
 # Outputs single line "Success!" in file text.txt