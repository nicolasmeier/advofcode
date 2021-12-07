import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("05t.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]

b = []
for x in range(1000):
    b.append([])
    for y in range(1000):
        b[x].append(0)

#print(b)
for l in li:
    l = l.replace(","," ")
    x1,y1,x2,y2 = [int(x) for x in l.split() if x.isdigit()]
    xr = []
    if x1 <= x2:
        xr = range(x1,x2+1)
    else:
        xr = range(x1,x2-1,-1)
    if y1 <= y2:
        yr = range(y1,y2+1)
    else:
        yr = range(y1,y2-1,-1)
    for x in xr:
        for y in yr:
            b[x][y] += 1

c = np.array(b)
res = 0
for x in range(1000):
    for y in range(1000):
        if b[x][y] > 1:
            res += 1

for x in range(10):
    for y in range(10):
        print(b[x][y],end = " ")
    print()
print(res)