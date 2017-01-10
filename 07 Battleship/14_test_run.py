# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:23:27 2017

@author: mindovermiles262

Codecademy Python

Thoroughly test your game. Make sure you try a variety of different guesses 
and look for any errors in the syntax or logic of your program.

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

# set row and col for debugging purposes
ship_row = 2
ship_col = 3

guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print("Ship Row: ",ship_row)
print("Ship Col: ",ship_col)

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
else: 
    if guess_row > 5 or guess_col > 5:
        print("Oops, that\'s not even in the ocean.")
    elif board[guess_row-1][guess_col-1] == "X":
        print("You guessed that one already.")
    else:
        print("You missed my battleship!")
        board[guess_row-1][guess_col-1] = "X"
        print_board(board)