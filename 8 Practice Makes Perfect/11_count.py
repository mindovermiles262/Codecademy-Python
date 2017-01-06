# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:20:45 2017

@author: mindovermiles262
"""

def count(sequence, item):
    item_count = 0
    for i in sequence:
        if i == item:
            item_count = item_count + 1
    return int(item_count)