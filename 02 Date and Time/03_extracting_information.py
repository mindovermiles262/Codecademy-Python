# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:10:45 2017

@author: mindovermiles262

Codecademy Python

On a new line, print now.year. Make sure you do it after setting the now 
variable!
Then, print out now.month.
Finally, print out now.day.

"""
from datetime import datetime

now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)