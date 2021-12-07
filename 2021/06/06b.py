import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("06.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
l = [int(x) for x in li[0].split(",")]
b = np.zeros((10,10),dtype=int)

l = np.array(l)
d = dict()
for i in range(9):
    d[i] = 0

for i in l:
    d[i] += 1



def doday(d :dict) -> dict:
    z = d[0]
    d[0] = d[1]
    d[1] = d[2]
    d[2] = d[3]
    d[3] = d[4]
    d[4] = d[5]
    d[5] = d[6]
    d[6] = d[7] + z
    d[7] = d[8]
    d[8] = z
    return d



for i in range(256):
    #print(f"Day {i} State: {l}")
    #print(f"Day {i} amount: {sum(d.values())}")
    d = doday(d)

print(f"amount: {sum(d.values())}")