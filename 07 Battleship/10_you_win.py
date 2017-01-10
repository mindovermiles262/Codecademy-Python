# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:15:11 2017

@author: mindovermiles262

Codecademy Python

On line 29, add an if guess_row equals ship_row and guess_col equals ship_col.
If that is the case, please print out 
"Congratulations! You sank my battleship!"

"""

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)
try:
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
except NameError:
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

print(ship_row)
print(ship_col)

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")