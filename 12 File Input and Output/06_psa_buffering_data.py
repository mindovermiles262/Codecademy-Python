# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:03:52 2017

@author: mindovermiles262

Codecademy Python

Add a write_file.close() call on line 9.
Add a read_file.close() on line 13.
Run the code again.
This time, you'll see the data come through!

"""

# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print(read_file.read())
read_file.close()