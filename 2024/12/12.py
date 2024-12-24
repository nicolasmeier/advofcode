import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    return list(map(str,[y for y in x]))
    
li = []
with open("12.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

grid = li


xmax = len(grid)
ymax = len(grid[0])

def ingrid(x,y):
    return (0 <= x < xmax and 0 <= y < ymax)

vis = set()

def plot(x,y,v):
    if not ingrid(x,y):
        return (0, 1)
    if grid[x][y] == v and (x,y) in vis:
        return (0,0)
    elif grid[x][y] != v:
        return (0,1)
    elif grid[x][y] == v:
        vis.add((x,y))
        (n, nn) = plot(x+1,y,v)
        (o, oo) = plot(x-1,y,v)
        (s, ss) = plot(x,y+1,v)
        (w, ww) = plot(x,y-1,v)
        return (1+n+o+s+w,nn+oo+ss+ww)


part1 = 0
part2 = 0
for a in range(xmax):
    for b in range(ymax):
        cv = grid[a][b]
        (nf,nw) = plot(a,b,cv)
        if nf + nw > 0:
            print(cv,(nf,nw))
            part1 += nf * nw

print(part1)


