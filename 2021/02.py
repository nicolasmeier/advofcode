import os
import sys
import re
import numpy as np
import math
import functools


os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("02.txt") as f:
    l = [x.strip() for x in f.readlines()]


x,y = 0,0

for i in l:
    d,le = i.split(" ",2)
    le = int(le)
    if d == "forward":
        x += le
    elif d == "down":
        y += le
    elif d == "up":
        y -= le

print(x,y)
print(x*y)











