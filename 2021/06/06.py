import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("06.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
l = [int(x) for x in li[0].split(",")]
b = np.zeros((10,10),dtype=int)

def doday(l :list):
    
    r = []
    for i in range(len(l)):
        l[i] -= 1
        if l[i] < 0:
            l[i] = 6
            r.append(8)
    for e in r:
        l.append(e)
    return l



for i in range(81):
    #print(f"Day {i} State: {l}")
    print(f"Day {i} amount: {len(l)}")
    l = doday(l)
