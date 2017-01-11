# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 08:11:37 2017

@author: mindovermiles262

Codecademy Python

Print the current date in the form of mm/dd/yyyy.

Change the string so that it uses a / character in between the %s placeholders 
instead of a - character.
Re-arrange the parameters to the right of the % operator so that you print 
now.month, then now.day, then now.year.

"""
from datetime import datetime
now = datetime.now()

print('%s/%s/%s' % (now.month, now.day, now.year))