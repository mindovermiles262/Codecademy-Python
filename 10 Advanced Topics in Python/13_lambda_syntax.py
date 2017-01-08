#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:30:55 2017

@author: mindovermiles262

Codecademy Python

Fill in the first part of the filter function with a lambda. The lambda 
should ensure that only "Python" is returned by the filter.
Fill in the second part of the filter function with languages, the list to 
filter.

"""

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x is "Python", languages)