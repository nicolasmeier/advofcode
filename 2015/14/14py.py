import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
os.chdir(os.path.dirname(sys.argv[0]))
lines = []
with open("14.txt") as f:
    lines = [x.strip() for x in f.readlines()]
#l = l[0]
sec = 2504

points = dict()
ss = dict()
for n in [x.split()[0] for x in lines]:
    points[n] = 0
    

for i in range(1,sec+1):
    sec = i
    speed = dict()
    for l in lines:
        #print(l.split())
        n = l.split()[0]
        s,d,r = [int(x) for x in l.split() if x.isdigit()]
        times = int(math.floor(sec/((d+r))))
        y = sec - ((d+r) * times)
        y = min(y,d)
        x = (s*d) * times + y*s
        if x in speed:
            speed[x].append(n)
        else:
            speed[x] = [n]
    for n in speed[max(speed.keys())]:
        points[n] += 1


print(points)
