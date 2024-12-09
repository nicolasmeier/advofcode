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
    return list(x)
    
li = []
with open("06.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


grid = li

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
grid = li
v = set()
for x,r in enumerate(li):
    if "G" in r:
        gx = x
        gy = r.index("G")

v.add((gx,gy))
ogx = gx
ogy = gy

def checkLoop(ld,lx,ly):
    loop = set()
    loop.add((ld,lx,ly))
    #ld = (ld + 1) % 4
    while(0 <= lx+direction[ld][0] < mx and 0 <= ly+direction[ld][1] < my):
        if grid[lx+direction[ld][0]][ly+direction[ld][1]] == '#':
            ld = (ld + 1) % 4
        else:
            lx = lx+direction[ld][0]
            ly = ly+direction[ld][1]

        if (ld,lx,ly) in loop:
            return True
        loop.add((ld,lx,ly))
    return False

barriar = set()
p = set()

while(0 <= gx+direction[cd][0] < mx and 0 <= gy+direction[cd][1] < my):
    p.add((cd,gx,gy))
    if grid[gx+direction[cd][0]][gy+direction[cd][1]] == '#':
        cd = (cd + 1) % 4
    else:
        gx = gx+direction[cd][0]
        gy = gy+direction[cd][1]
        v.add((gx,gy))



for x,y in v:
    grid[x][y] = '#'
    if checkLoop(0,ogx,ogy):
        barriar.add((x,y))
    
    grid[x][y] = '.'
    grid[ogx][ogy] = 'G'



print(len(v))
print(len(barriar))