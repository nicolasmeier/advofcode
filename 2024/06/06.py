import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    x = x.replace("^","G")
    return x
    
li = []
with open("06.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


grid = np.array(li)
[print(l) for l in grid]

direction = {
    0: (-1,0),
    1: (0,1),
    2: (1,0),
    3: (0,-1)
}
mx = len(grid)
my = len(grid[0])
cd = 0
gx = 0
gy = 0
part2 = 0
grid = np.array(li)
v = set()
for x,r in enumerate(li):
    if "G" in r:
        gx = x
        gy = r.index("G")

print((gx,gy),li[gx][gy])
v.add((gx,gy))

while(0 <= gx+direction[cd][0] < mx and 0 <= gy+direction[cd][1] < my):
    if grid[gx+direction[cd][0]][gy+direction[cd][1]] == '#':
        cd = (cd + 1) % 4
    else:
        gx = gx+direction[cd][0]
        gy = gy+direction[cd][1]
        cl = len(v)
        v.add((gx,gy))
        if cl == len(v):
            part2 += 1

print(len(v))
print(part2)