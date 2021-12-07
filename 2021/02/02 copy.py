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
aim = 0
for i in l:
    d,le = i.split(" ",2)
    le = int(le)
    if d == "forward":
        x += le
        y += aim * le
    elif d == "down":
        aim += le
    elif d == "up":
        aim -= le

print(aim)
print(x,y)
print(x*y)











