# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:42:00 2017

@author: mindovermiles262

Codecademy Python

When you are done playing Battleship! and are ready to move on, 
click Save & Submit Code.

"""

from random import randint

# Initalize board
board = []
for x in range(5):
    board.append(["O"] * 5)
def print_board(board):
    for row in board:
        print(" ".join(row))
print("Let's play Battleship!")
print_board(board)


# Set battleship location
def random_row(board):
    return randint(1, len(board))
def random_col(board):
    return randint(1, len(board[0]))
ship_row = random_row(board)
ship_col = random_col(board)

# Define raw_input for Py 3 compatability
def raw_input(x):
    x = input(x)
    return x

# Board Control
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row-1][guess_col-1] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row-1][guess_col-1] = "X"
            print_board(board)
        if turn == 3: print("Game Over")
        if turn < 3: print ("Turn", turn + 1) 
        