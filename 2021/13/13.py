import re
import numpy as np
import math
import functools
import os
import sys


os.chdir(os.path.dirname(sys.argv[0]))
dot = []
ins = []
with open("a.txt") as f:
    d,i = [x.strip() for x in f.read().split("\n\n")]
    dot = [x.strip() for x in d.split("\n")]
    ins = [x.strip() for x in i.split("\n")]



dots = set()
for l in dot:
    x,y = l.split(",")
    dots.add((int(x), int(y)))

def foldx(p, x):
    res = set()
    for pos in p:
        if pos[0]<x:
            res.add(pos)
        else:
            res.add((2*x-pos[0], pos[1]))
    return res

def foldy(p, y):
    res = set()
    for pos in p:
        if pos[1]<y:
            res.add(pos)
        else:
            res.add((pos[0], 2*y-pos[1]))
    return res
p1 = True
for inst in ins:
    d,amt = inst.split()[2].split("=")
    if d == 'x':
        dots = foldx(dots, int(amt))
    else:
        dots = foldy(dots, int(amt))
    if p1:
        print("part1",len(dots))
        p1 = False

#print(dots)
yy = [pos[1] for pos in dots]
xx = [pos[0] for pos in dots]
#print(max(yy),max(xx))
for y in range(max(yy)+1):
    for x in range(max(xx)+1):
        if (x,y) in dots:
            print("#",end="")
        else:
            print(" ",end="")
    print()

