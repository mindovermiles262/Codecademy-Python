# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:05:36 2017

@author: mindovermiles262

Codecademy Python

Define two new functions, random_row and random_col, that each take board as 
input.
These functions should return a random row index and a random column index 
from your board, respectively. Use randint(0, len(board) - 1).
Call each function on board.

"""

from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

# Add your code below!
def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

random_row(board)
random_col(board)
print_board(board)