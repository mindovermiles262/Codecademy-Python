# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:19:07 2017

@author: mindovermiles262

Codecademy Python

Add a new if: statement that is nested under the else.
Like the example above, it should check if guess_row is not in range(5) or 
guess_col is not in range(5).
If that is the case, print out "Oops, that's not even in the ocean."
After your new if: statement, add an else: that contains your existing handler 
for an incorrect guess. Don't forget to indent the code!

WORKING FOR PYTHON 2 ONLY

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

guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print(ship_row)
print(ship_col)

# Write your code below!
if guess_row == ship_row | guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
else: 
    if guess_row > 5 or guess_col > 5:
        print("Oops, that\'s not even in the ocean.")
    else:
        print("You missed my battleship!")
        board[guess_row-1][guess_col-1] = "X"
        print_board(board)
