# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:10:33 2017

@author: mindovermiles262

Codecademy Python

Create a new variable called guess_row and set it to 
int(raw_input("Guess Row: ")).
Create a new variable called guess_col and set it to 
int(raw_input("Guess Col: ")).
Click Save & Submit and then answer the prompts by typing in a number and 
pressing Enter (or Return on some computers).

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
# Define raw_input for Python 3 compatability
def raw_input(x):
    x = input(x)
    return x
    
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))