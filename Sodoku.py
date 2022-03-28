from logging.config import valid_ident
from msilib.schema import Billboard
from multiprocessing.sharedctypes import Value
from os import system
from random import randint
from tabnanny import check
from tkinter import Grid
from turtle import pos


board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 5, 0, 2, 0],
    [0, 1, 0, 7, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def printBoard(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        
        for col in range (len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")
            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")
    
def valid(board, pos, num):
    # Check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def checkForEmptySpots(board):
    for row in range (len(board)):
        for col in range (len(board)):
            if board[row][col] == 0:
                return (row, col)
    return None

def solve(board):
    find = checkForEmptySpots(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
        
solve(board)
printBoard(board)