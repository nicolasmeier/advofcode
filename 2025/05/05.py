import os
import sys
import re
import numpy as np
import math
import functools
from collections import Counter
import itertools
# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x
    
li = []
with open("05.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

res1 = 0    
res2 = 0

rgs = []
pr = []
rangesread = True
for line in li:
    if rangesread:
        if line == "":
            rangesread = False
            continue
        a,b = line.split("-",2)
        rgs.append( range(int(a), int(b)+1))
        pr.append( (int(a), int(b)) )
    else:
        if any(int(line) in rg for rg in rgs):
            res1 += 1
    

print("res1:", res1)

# sort ranges by start
pr.sort()

merged = []
start, end = pr[0]

for s, e in pr[1:]:
    if s <= end + 1:           # overlapping or touching
        end = max(end, e)
    else:
        merged.append((start, end))
        start, end = s, e

merged.append((start, end))

# Count total IDs in merged ranges
res2 = sum(e - s + 1 for s, e in merged)

print("res2:", res2)


print("res2:", res2)