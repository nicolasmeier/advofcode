import numpy as np
import math
import functools
import collections 
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("22.txt") as f:
    li = [x.strip() for x in f.readlines()]


on = set()

for l in li:
    inst, coords = l.split()
    x,y,z = [y for y in coords.split(",")]
    x = [int(y) for y in  x[2:].split("..")]
    y = [int(a) for a in  y[2:].split("..")]
    z = [int(y) for y in  z[2:].split("..")]
    if inst == "on":
        on.update(set([f"{a};{b};{c}" for a in range(x[0],x[1]+1) for b in range(y[0],y[1]+1) for c in range(z[0],z[1]+1)]))
    else:
        on = on.difference(set([f"{a};{b};{c}" for a in range(x[0],x[1]+1) for b in range(y[0],y[1]+1) for c in range(z[0],z[1]+1)]))
print(len(on))

