import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("04.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]

nums = [int(x.strip()) for x in li[0].split(",")]
print(nums)

boards = []
b = []
for l in li[2:]:
    if l == "":
        boards.append(np.array(b))
        b = []
    else:
        b.append([int(x.strip()) for x in l.split()])
if len(b) >0:
    boards.append(np.array(b))

def removenum(board: np.ndarray,num:int):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y]==num:
                board[x][y]= -1
    return board
def cb(board: np.ndarray):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y]==-1:
                board[x][y]= 0
    return board
def eb(board: np.ndarray):
    for x in range(len(board)):
        for y in range(len(board[x])):
            board[x][y]= -3
    return board
def checkwin(board: np.ndarray):
    if -5 in np.sum(board,axis=0) or -5 in np.sum(board,axis=1):
        return True
    return False

winners = []
last = np.zeros((2,2))
for n in nums:
    for b in boards:
        b = removenum(b,n)
        if checkwin(b):
            winners.append(b)
            last = b.copy()
            b = eb(b)
    print(len(winners) , len(boards),len(winners) == len(boards))
    if len(winners) == len(boards):
        print(np.sum(cb(last)),n,"","",np.sum(cb(last))*n)
        quit()

