import os
import sys
import re
import numpy as np
import math
import functools
from collections import Counter
# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x
    
li = []
with open("04.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


def g(grid, r, c):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        if grid[r][c] == "@":
            return 1
    return 0

res1 = 0    
res2 = 0

grid = [list(x) for x in li]
rows = len(grid)
cols = len(grid[0])
for r in range(rows):
    for c in range(cols):
        curr = grid[r][c]
        if curr == "@":
            sur = g(grid, r-1, c) + g(grid, r+1, c) + g(grid, r, c-1) + g(grid, r, c+1) + g(grid, r-1, c-1) + g(grid, r-1, c+1) + g(grid, r+1, c-1) + g(grid, r+1, c+1)
            if sur < 4:
                res1 += 1
        else:
            continue


print("res1:", res1)

grid = [list(x) for x in li]
rows = len(grid)
cols = len(grid[0])
ab = 1
while ab != 0:
    ab = 0
    for r in range(rows):
        for c in range(cols):
            curr = grid[r][c]
            if curr == "@":
                sur = g(grid, r-1, c) + g(grid, r+1, c) + g(grid, r, c-1) + g(grid, r, c+1) + g(grid, r-1, c-1) + g(grid, r-1, c+1) + g(grid, r+1, c-1) + g(grid, r+1, c+1)
                if sur < 4:
                    ab = 1
                    res2 += 1
                    grid[r][c] = "*"
            else:
                continue


print("res2:", res2)