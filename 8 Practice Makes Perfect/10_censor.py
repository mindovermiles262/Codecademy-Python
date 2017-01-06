# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:37:29 2017

@author: mindovermiles262

Write a function called censor that takes two strings, text and word, as 
input. It should return the text with the word you chose replaced with 
asterisks.

For example:

censor("this hack is wack hack", "hack") 
should return: "this **** is wack ****"

Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in 
the censored word.

"""

def censor(text, word):
    #replace letters in word with *
    for i in word:
        censored_word = "*" * len(word)
        
    # Split text into individual words
    uncensored_text = text.split()
    

    censored_text = ""
    for i in uncensored_text:
        if i == word:
            i = censored_word
            censored_text = censored_text + " " + i
        else:
            censored_text = censored_text + " " + i
    return censored_text.lstrip()