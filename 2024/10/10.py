import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    return list(map(int,[y for y in x]))
    
li = []
with open("10.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


grid = li


xmax = len(grid)
ymax = len(grid[0])

def ingrid(x,y):
    return (0 <= x < xmax and 0 <= y < ymax)

def search(x,y,t):
    if not ingrid(x,y):
        return False
    v = grid[x][y]
    if v == t == 9:
        return [(x,y)]
    if v == t: 
        r = [
        search(x+1,y,v+1),
        search(x-1,y,v+1),
        search(x,y+1,v+1),
        search(x,y-1,v+1)]
        return [j for u in r if u for j in u]
    return False

numth = 0
sump = 0
sump2 = 0
for a in range(xmax):
    for b in range(ymax):
        s = search(a,b,0) 
        if s:
            numth += 1
            sump += len(set(s))
            sump2 += len(s)
            print(numth, len(set(s)))
print(sump)
print(sump2)