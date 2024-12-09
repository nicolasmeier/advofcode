import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    return np.array(x)
    
li = []
with open("08.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


grid = np.array(li)
[print(l) for l in grid]

antennas = dict()
antinode = set()
antinode2 = set()
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] != '.':
            a = antennas.get(grid[x][y],set())
            a.add((x,y))
            antennas[grid[x][y]] = a

for k,val in antennas.items():
    for v in val:
        for w in val:
            if v != w:
                ax = v[0] + 2*(w[0] - v[0])
                ay = v[1] + 2*(w[1] - v[1])
                if 0 <= ax < len(grid) and 0 <= ay < len(grid[0]):
                    antinode.add((ax,ay))
                ani = 0
                while True:
                    ax = v[0] + ani*(w[0] - v[0])
                    ay = v[1] + ani*(w[1] - v[1])
                    if 0 <= ax < len(grid) and 0 <= ay < len(grid[0]):
                        antinode2.add((ax,ay))
                    else:
                        break
                    ani += 1

print(len(antinode))
print(len(antinode2))

# 3  5