import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("07.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
l = [int(x) for x in li[0].split(",")]


x = (int)(np.median(l))
minfuel = 999*999*99
r = 0
for y in range(1,max(l)):
    f = sum([abs(z-y) for z in l])
    if minfuel > f:
        minfuel = f
        r = y
print(r,minfuel)

@functools.lru_cache()
def fuel(d: int) -> int:
    d = abs(d)
    return sum(range(d+1))

for i in range(10):
    print(i,fuel(i))


minfuel = 999*999*99
r = 0
for y in range(1,max(l)):
    f = sum([fuel(abs(z-y)) for z in l])
    if minfuel > f:
        minfuel = f
        r = y
print(r,minfuel)