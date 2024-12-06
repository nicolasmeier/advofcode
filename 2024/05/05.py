import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x
    
li = []
with open("05.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


def cr(pg):
    b = set()
    for i,p in enumerate(pg):
        br = before.get(p,False)
        if br:
            if any([x in br for x in pg[i:]]):
                return False
            b.add(p)
    return True


def fixord(pg):
    n = pg.copy()
    while(not cr(n)):
        for i in range(1,len(pg)+1):
            if not cr(n[:i]):
                a = n[i-1]
                b = n[i-2]
                n[i-1] = b
                n[i-2] = a
    return n



part1 = 0
part2 = 0
isrules = True
before = dict()
after = dict()
for l in li:
    if l == '':
        isrules = False
    elif isrules:
        r,k = list(map(int,l.split("|",1)))
        v = set(before.get(k,set()))
        v.add(r)
        before[k] = v
        y = set(after.get(r,set()))
        y.add(k)
        after[r] = y
    else:
        pg = [int(x) for x in l.split(",")]
        if cr(pg):
            part1 += pg[len(pg) // 2]
        else:
            fixed = fixord(pg)
            part2 += fixed[len(fixed) // 2]


print(part1)
print(part2)