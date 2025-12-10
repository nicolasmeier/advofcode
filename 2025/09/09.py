import os
import sys
import re
import numpy as np
import math
import functools
from collections import Counter
import itertools
# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x.replace("\n", "").strip()
    
li = []
with open("09.txt") as f:
    li = [trans(x) for x in f.readlines()]

rt = list()
gt = list()
firstline = li[0].split(",",2)
first = (int(firstline[0]),int(firstline[1]))
last = None
for line in li:
    x = line.split(",",2)

    rt.append((int(x[0]),int(x[1])))
    gt.append((int(x[0]),int(x[1])))
    if last is not None:
        # fill in gaps
        if last[0] == int(x[0]):
            for yy in range(min(last[1],int(x[1]))+1, max(last[1],int(x[1]))):
                gt.append((int(x[0]),yy))
        elif last[1] == int(x[1]):
            for xx in range(min(last[0],int(x[0]))+1, max(last[0],int(x[0]))):
                gt.append((xx,int(x[1])))
        else:
            print("diagonal line?", last, (int(x[0]),int(x[1])))
            print("diagonal line?", last, (int(x[0]),int(x[1])))
            print("diagonal line?", last, (int(x[0]),int(x[1])))
            print("diagonal line?", last, (int(x[0]),int(x[1])))
            print("diagonal line?", last, (int(x[0]),int(x[1])))
    last = (int(x[0]),int(x[1]))


# fill in gaps
if last[0] == first[0]:
    for yy in range(min(last[1],first[1])+1, max(last[1],first[1])):
        gt.append((int(first[0]),yy))
elif last[1] == first[1]:
    for xx in range(min(last[0],first[0])+1, max(last[0],first[0])):
        gt.append((xx,int(first[1])))

# Fill in green tiles if they are inside the red and green line
min_x = min([x[0] for x in gt])
max_x = max([x[0] for x in gt])
min_y = min([x[1] for x in gt])
max_y = max([x[1] for x in gt])
for x in range(min_x, max_x+1):
    paint = False
    pb = list()
    for y in range(min_y, max_y+1):
        p = (x,y)
        if paint and p not in gt:
            pb.append(p)
        elif paint and p in gt:
            gt.extend(pb)
            pb = list()
        elif not paint and p in gt:
            paint = True


print("red tiles; ", len(rt), rt[:5])


ra = dict()
for a,b in itertools.combinations(rt,2):
    
    d = (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
    if d not in ra:
        ra[d] = list((a,b))
    ra[d].append((a,b))


print("res1:",sorted(ra.keys())[-1])

res2 = 0

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))
plt.scatter([x[0] for x in gt], [y[1] for y in gt], color='green', s=30)
plt.scatter([x[0] for x in rt], [y[1] for y in rt], color='red', s=40)
plt.title('Red and Green Tiles')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()

        
print("res2:", res2)

