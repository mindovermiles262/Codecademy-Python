# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:02:25 2017

@author: mindovermiles262

Codecademy Python

Create a 5 x 5 grid initialized to all 'O's and store it in board.

Use range() to loop 5 times.
Inside the loop, .append() a list containing 5 "O"s to board, just like in 
the example above.
Note that these are capital letter "O" and not zeros.

"""

board = []
#initalize board
for i in range(0,5):
    board.append(["O"] * 5)
print(board)