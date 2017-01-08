#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:39:41 2017

@author: mindovermiles262

Codecademy Python

Create a new variable called message.
Set it to the result of calling filter() with the appropriate lambda that will 
filter out the "X"s. The second argument will be garbled.
Finally, print your message to the console.
?


"""

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x is not "X", garbled)
print(message)