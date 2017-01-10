# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:13:58 2017

@author: mindovermiles262

Codecademy Python

Print the value of ship_col.
Print the value of ship_row.

"""

from random import randint

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
try:
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
except NameError:
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
print(ship_col)
print(ship_row)