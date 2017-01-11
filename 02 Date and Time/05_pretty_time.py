# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:12:12 2017

@author: mindovermiles262

Codecademy Python

Similar to the last exercise, print the current time in the pretty form 
of hh:mm:ss.

Change the string that you are printing so that you have a : character in 
between the %s placeholders.
Change the three things that you are printing from month, day, and year to 
now.hour, now.minute, and now.second.

"""

from datetime import datetime
now = datetime.now()

print('%s:%s:%s' % (now.hour, now.minute, now.second))