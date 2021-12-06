import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("05.txt") as f:
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
    if x1 == x2 or y1 == y2:
        x1,x2 = min(x1,x2),max(x1,x2)
        y1,y2 = min(y1,y2),max(y1,y2)
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                b[x][y] += 1
    else:
        xstep = int((x2-x1)/abs((x2-x1)))
        ystep = int((y2-y1)/abs((y2-y1)))
        x,y = x1,y1
        for i in range(abs((y2-y1))+1):
            xx = x + xstep*i
            yy = y + ystep*i
            b[xx][yy] += 1

c = np.array(b)
res = 0
for x in range(1000):
    for y in range(1000):
        if b[x][y] > 1:
            res += 1

#print(b[0:10][0:10])
'''
for x in range(10):
    for y in range(10):
        print(b[y][x],end = " ")
    print()
'''
print(res)