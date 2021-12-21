import re
import numpy as np
import math
import functools
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))
li = []
b = []
with open("11.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
#l = [int(x) for x in li[0].split(",")]
#li = li[0:3]

b = np.zeros((12,12))
b -= 999
i = 1
for l in li:
    #print([(int)(y) for y in l])
    b[i][1:-1] = [(int)(y) for y in l]
    i += 1

print(b)



def flash(b,x,y):
    if b[x][y] <= 9:
        return 0
    f = 0
    b[x][y] = -20
    b[x-1][y-1] += 1
    f += flash(b,x-1,y-1)
    b[x][y-1] += 1
    f += flash(b,x,y-1)
    b[x+1][y-1] += 1
    f += flash(b,x+1,y-1)

    b[x-1][y] += 1
    f += flash(b,x-1,y)
    b[x+1][y] += 1
    f += flash(b,x+1,y)

    b[x-1][y+1] += 1
    f += flash(b,x-1,y+1)
    b[x][y+1] += 1
    f += flash(b,x,y+1)
    b[x+1][y+1] += 1
    f += flash(b,x+1,y+1)

    return 1 + f




def dostep(b):
    b +=1
    f = 0
    for x in range(1,len(b)-1):
        for y in range(1,len(b[x])-1):
            fl = flash(b,x,y)
            f += fl
    
    for x in range(1,len(b)-1):
        for y in range(1,len(b[x])-1):
            if b[x][y] < 0:
                b[x][y] = 0
    #print(b)
    return  f
                




f = 0
for i in range(1,200020):
    fl = dostep(b)
    print(f"step {i} flashes {fl}")
    if fl == 100:
        quit()
    f += fl

print(f)
