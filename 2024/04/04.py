import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x
    
li = []
with open("04.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

res = 0

lit = np.array(li)
xlen = len(lit)
ylen = len(lit[0])
for x in range(xlen):
    for y in range(ylen):
        if (x+3)<xlen                and lit[x][y] == 'X' and lit[x+1][y] == 'M' and lit[x+2][y] == 'A' and lit[x+3][y] == 'S':
            res +=1 
        if (x-3)>=0                  and lit[x][y] == 'X' and lit[x-1][y] == 'M' and lit[x-2][y] == 'A' and lit[x-3][y] == 'S':
            res +=1 
        if (y+3)<ylen                and lit[x][y] == 'X' and lit[x][y+1] == 'M' and lit[x][y+2] == 'A' and lit[x][y+3] == 'S':
            res +=1 
        if (y-3)>=0                  and lit[x][y] == 'X' and lit[x][y-1] == 'M' and lit[x][y-2] == 'A' and lit[x][y-3] == 'S':
            res +=1 
        if (x+3)<xlen and (y+3)<ylen and lit[x][y] == 'X' and lit[x+1][y+1] == 'M' and lit[x+2][y+2] == 'A' and lit[x+3][y+3] == 'S':
            res +=1 
        if (x-3)>=0 and (y+3)<ylen   and lit[x][y] == 'X' and lit[x-1][y+1] == 'M' and lit[x-2][y+2] == 'A' and lit[x-3][y+3] == 'S':
            res +=1
        if (x-3)>=0 and (y-3)>=0     and lit[x][y] == 'X' and lit[x-1][y-1] == 'M' and lit[x-2][y-2] == 'A' and lit[x-3][y-3] == 'S':
            res +=1 
        if (x+3)<xlen and (y-3)>=0   and lit[x][y] == 'X' and lit[x+1][y-1] == 'M' and lit[x+2][y-2] == 'A' and lit[x+3][y-3] == 'S':
            res +=1

print(res)
    
