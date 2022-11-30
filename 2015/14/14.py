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
sec = 2503

speed = dict()
for l in lines:
    #print(l.split())
    s,d,r = [int(x) for x in l.split() if x.isdigit()]
    times = int(math.floor(sec/((d+r))))
    y = sec - ((d+r) * times)
    print(l[0:5],s,d,r,s*d,d+r,int(math.floor(sec/((d+r)))),y)
    y = min(y,d)
    speed[l[0:5]] = (s*d) * int(math.floor(sec/((d+r)))) + y*s


print(max(speed.values()))
