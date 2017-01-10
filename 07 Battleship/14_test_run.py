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
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# For testing purposes
#ship_row=2
#ship_col=2

try:
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
except NameError:
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))
    
# Convert guess to index
guess_row -= 1
guess_col -= 1

# For debugging purposes
#print(ship_row)
#print(ship_col)
#print(guess_row)
#print(guess_col)

# Write your code below!
if guess_row == ship_row | guess_col == ship_col:
    print("Congratulations! You sank my battleship!")
else: 
    if guess_row > 4 or guess_col > 4:
        print("Oops, that\'s not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print("You guessed that one already.")        
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
