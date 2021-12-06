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



d = []
e = dict()

#print(b)
for l in li:
    l = l.replace(","," ")
    x1,y1,x2,y2 = [int(x) for x in l.split() if x.isdigit()]
    if x1 == x2 or y1 == y2:
        x1,x2 = min(x1,x2),max(x1,x2)
        y1,y2 = min(y1,y2),max(y1,y2)
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                if f"{x},{y}" in d:
                    e[f"{x},{y}"] = 1
                else:
                    d.append(f"{x},{y}")


# ast
print(len(e.keys()))
