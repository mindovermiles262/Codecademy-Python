# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:04:43 2017

@author: mindovermiles262

Codecademy Python

Inside your function, inside your for loop, use " " as the separator to .join 
the elements of each row.

"""

board = []
for i in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(board[i]))
        
print_board(board)