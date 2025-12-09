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
    return x.replace("\n", "")
    
li = []
with open("08.txt") as f:
    li = [trans(x) for x in f.readlines()]

jbox = list()

for line in li:
    x = line.split(",",3)

    jbox.append((int(x[0]),int(x[1]),int(x[2])))




def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

# shortest distance between any two jboxes
dd = dict()
for a,b in itertools.combinations(jbox,2):
    d = dist(a,b)
    if d in dd:
        print("duplicate distance!", d, dd[d], (a,b))
    dd[d] = (a,b)

res1 = 0    
res2 = 0

conn = list()
sorted_keys = sorted(dd.keys())
print("total distances:", len(sorted_keys))

for k in sorted_keys[:1000]:
    a,b = dd[k]
    found_a = None
    found_b = None
    for c in conn:
        if a in c:
            found_a = c
        if b in c:
            found_b = c
    if found_a is None and found_b is None:
        conn.append(set([a,b]))
    elif found_a is not None and found_b is None:
        found_a.add(b)
    elif found_a is None and found_b is not None:
        found_b.add(a)
    elif found_a is not found_b:
        # merge
        found_a.update(found_b)
        conn.remove(found_b)
    # else: both found and same set, do nothing
    #else:
        #print("both found and same set?", a,b)
    if len(conn) == 1 and len(conn[0]) == len(jbox):
        print("last connection between:", a,b)
        res2 = a[0] * b[0]
        break

res1 = np.prod((sorted([len(c) for c in conn], reverse=True)[:3]))

print("res1:", res1)

idx = 0
for k in sorted_keys:
    a,b = dd[k]
    found_a = None
    found_b = None
    for c in conn:
        if a in c:
            found_a = c
        if b in c:
            found_b = c
    if found_a is None and found_b is None:
        conn.append(set([a,b]))
    elif found_a is not None and found_b is None:
        found_a.add(b)
    elif found_a is None and found_b is not None:
        found_b.add(a)
    elif found_a is not found_b:
        # merge
        found_a.update(found_b)
        conn.remove(found_b)
    # else: both found and same set, do nothing
    #else:
        #print("both found and same set?", a,b)
    idx += 1
    if len(conn) == 1 and len(conn[0]) == len(jbox):
        print("last connection between:", a,b)
        print("at index:", idx)
        res2 = a[0] * b[0]
        break
print("res2:", res2)