# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:35:20 2017

@author: mindovermiles262

Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.

For example: anti_vowel("Hey You!") should return "Hy Y!".

Don't count Y as a vowel.
Make sure to remove lowercase and uppercase vowels.

"""

def anti_vowel(text):
    text = str(text)
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in text:
        for j in vowels:
            if i == j:
                text = text.replace(j,"")
    return text