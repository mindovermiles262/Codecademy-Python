# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 07:53:12 2017

@author: mindovermiles262

Codecademy Python

Now it's your turn! We have ___ in the code to show you what you need to change!

Inside the string, replace the three ___ with %s.
After the string but before the three variables, replace the final ___ with a %.
Hit Save & Submit Code.
Answer the questions in the console as they pop up! Type in your answer and 
hit Enter.

"""
# Fix compatability with Py3
try:     
    name = raw_input("What is your name?")
    quest = raw_input("What is your quest?")
    color = raw_input("What is your favorite color?")
except NameError:
    name = input("What is your name?")
    quest = input("What is your quest?")
    color = input("What is your favorite color?")

print("Ah, so your name is %s, your quest is %s, " % (name, quest))
print("and your favorite color is %s." % (color))