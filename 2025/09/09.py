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

xgt = dict()
ygt = dict()
for (x,y) in gt:
    if x not in xgt:
        xgt[x] = set()
    if y not in ygt:
        ygt[y] = set()
    xgt[x].add(y)
    ygt[y].add(x)


print("red tiles; ", len(rt), rt[:5])


ra = dict()
maxd = 0
max_pair = None
for a,b in itertools.combinations(rt,2):
    
    d = (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
    if d not in ra:
        ra[d] = list()
    ra[d].append((a,b))
    if d > maxd:
        maxd = d
        max_pair = (a,b)


print("res1:",sorted(ra.keys())[-1])

res2 = 0


import matplotlib.pyplot as plt

#fig = plt.figure(figsize=(10,10))
#plt.scatter([x[0] for x in gt], [y[1] for y in gt], color='green', s=30)
#plt.scatter([x[0] for x in rt], [y[1] for y in rt], color='red', s=40)
#plt.scatter([max_pair[0][0], max_pair[1][0]], [max_pair[0][1], max_pair[1][1]], color='blue', s=100, marker='x')
#plt.title('Red and Green Tiles')
#plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.grid(True)
#plt.show()

        
print("res2:", res2)

# ---------------------------------------------------------
# Part 2: Largest rectangle using only red and green tiles
# ---------------------------------------------------------

# combine red + green tiles into a single set for fast lookup
all_tiles = set(gt) | set(rt)

res2 = 1351617690
best_pair2 = None

for a, b in itertools.combinations(rt, 2):
    #print("Res2:",res2,"Checking pair:", a, b)
    # rectangle bounding box
    minx = min(a[0], b[0])
    maxx = max(a[0], b[0])
    miny = min(a[1], b[1])
    maxy = max(a[1], b[1])
    if minx == maxx or miny == maxy:
        #print("  Skipping degenerate rectangle")
        continue  # skip degenerate rectangles
    
    area = (maxx - minx + 1) * (maxy - miny + 1)
    if area < res2:
        #print("  Skipping smaller area rectangle")
        continue  # skip smaller rectangles
    ok = True
    # check every tile inside the rectangle
    for xx in range(minx+1, maxx):
        if xgt[xx]:
            ys_in_column = xgt[xx]
            if any(y > miny and y < maxy for y in ys_in_column):
                ok = False
                break
    #for yy in range(miny+1, maxy):
    #    if ygt[yy]:
    #        xs_in_row = ygt[yy]
    #        if any(x >= minx and x <= maxx for x in xs_in_row):
    #            ok = False
    #            break
    if False:
        for xx in [minx, maxx]:
            for yy in range(miny+1, maxy):
                contblank = False
                contred = False
                contgreen = False
                if (xx, yy) in rt:
                    break
                    contred = True
                elif (xx, yy) in gt:
                    contgreen = True
                else:
                    contblank = True
            ok = (contblank and not contred and not contgreen) or (not contblank and not contred and contgreen) or ( contblank and contred and  contgreen)
            if not ok:
                break
        for xx in range(minx+1, maxx):
            for yy in [miny, maxy]:
                contblank = False
                contred = False
                contgreen = False
                if (xx, yy) in rt:
                    break
                    contred = True
                elif (xx, yy) in gt:
                    contgreen = True
                else:
                    contblank = True
        ok = (contblank and not contred and not contgreen) or (not contblank and not contred and contgreen) or ( contblank and contred and  contgreen)
        if not ok:
            break

    if ok:
        if area > res2:
            print("  New best area:", area, "with pair:", a, b)
            res2 = area
            best_pair2 = (a, b)

print("res2:", res2)
if best_pair2:
    print("res2 pair:", best_pair2)


if best_pair2:
    fig = plt.figure(figsize=(10,10))
    plt.scatter([p[0] for p in gt], [p[1] for p in gt], color='green', s=30)
    plt.scatter([p[0] for p in rt], [p[1] for p in rt], color='red', s=40)

    a, b = best_pair2
    rect_x = [a[0], b[0]]
    rect_y = [a[1], b[1]]
    plt.scatter(rect_x, rect_y, color='blue', s=120, marker='s')

    plt.title('Part 2: Best Rectangle (Red+Green)')
    plt.grid(True)
    plt.show()

