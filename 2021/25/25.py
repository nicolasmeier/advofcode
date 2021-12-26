import numpy as np
import math
import functools
import collections 
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("25.txt") as f:
    li = [x.strip() for x in f.readlines()]
#li = li[0]
east = set()
south = set()
maxx = len(li)
maxy = len(li[0])
for x in range(maxx):
    for y in range(maxy):
        if li[x][y] == ">":
            east.add((y,x))
        elif li[x][y] == "v":
            south.add((y,x))

def move():
    m = False
    e,s = set(),set()
    for c in east:
        y,x = c
        y = (y+1)%maxy
        if (y,x) not in east and (y,x) not in south: 
            m = True
            e.add((y,x))
        else:
            e.add(c)
    for c in south:
        y,x = c
        x = (x+1)%maxx
        if (y,x) not in e and (y,x) not in south: 
            m = True
            s.add((y,x))
        else:
            s.add(c)
    return [e,s,m]
def pr():
    return
    for y in range(maxy-1):
        for x in range(maxx+1):
            if (x,y) in east:
                print(">",end="")
            elif (x,y) in south:
                print("v",end="")
            else:
                print(".",end="")
        print()

pr()
print()
for i in range(1,1000):
    east,south,m = move()
    pr()
    print()
    if not m:
        print(i)
        quit()