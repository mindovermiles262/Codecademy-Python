#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 19:36:29 2017

@author: mindovermiles262

Codecademy Python

Pass __init__() a second parameter, name.
In the body of __init__(), let the function know that name refers to the 
created object's name by typing self.name = name. (This will become crystal 
clear in the next section.)

"""

class Animal(object):
    def __init__(self, name):
        self.name = name