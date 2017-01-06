# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:03:43 2017

@author: mindovermiles262

Codecademy Python

First, delete your existing print statement.
Then, define a function named print_board with a single argument, board.
Inside the function, write a for loop to iterates through each row in board 
and print it to the screen.
Call your function with board to make sure it works.

"""

board = []
for i in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(board[i])
        
print_board(board)