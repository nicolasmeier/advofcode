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
for x in range(len(lit)):
    for y in range(len(lit[x])+1):
        try:
            if lit[x][y] == 'M' and lit[x][y+2] == 'M' and lit[x+1][y+1] == 'A' and lit[x+2][y] == 'S' and lit[x+2][y+2] == 'S':
                res +=1 
        except:
            pass
        try:
            if lit[x][y] == 'S' and lit[x][y+2] == 'M' and lit[x+1][y+1] == 'A' and lit[x+2][y] == 'S' and lit[x+2][y+2] == 'M':
                res +=1 
        except:
            pass
        try:
            if lit[x][y] == 'S' and lit[x][y+2] == 'S' and lit[x+1][y+1] == 'A' and lit[x+2][y] == 'M' and lit[x+2][y+2] == 'M':
                res +=1 
        except:
            pass
        try:
            if lit[x][y] == 'M' and lit[x][y+2] == 'S' and lit[x+1][y+1] == 'A' and lit[x+2][y] == 'M' and lit[x+2][y+2] == 'S':
                res +=1 
        except:
            pass

print(res)
    
