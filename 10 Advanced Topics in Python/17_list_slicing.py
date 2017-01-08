#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 16:37:33 2017

@author: mindovermiles262

Codecademy Python

The string in the editor is garbled in two ways:

First, our message is backwards;
Second, the letter we want is every other letter.
Use list slicing to extract the message and save it to a variable called 
message.

"""

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print(message)