import os
import sys
import re
import numpy as np
import math
import functools
from pyDatalog import pyDatalog
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("09.txt") as f:
    l = [x.strip() for x in f.readlines()]

paths = dict()

for i in l:
    *a,d = [x.strip() for x in i.split(" ")]
    d = int(d)
    froma, to = a[0],a[2]
    paths[froma] = dict()
    paths[to] = dict()

towns = list(paths.keys())
print(towns)

for t in towns:
    paths[t] = dict()

for i in l:
    *a,d = [x.strip() for x in i.split(" ")]
    d = int(d)
    froma, to = a[0],a[2]
    paths[froma][to] = d
    paths[to][froma] = d

print(paths)

BIG = 0

def search(vis:list,tv:list,c:int,s:int):
    #print(vis,tv,c,s)
    if len(tv) == 0:
        return [vis,c]
    tvv = tv.copy()
    shortest = s
    shortestp = []
    f = False
    for t in tv:
        tvv = tv.copy()
        tvv.remove(t)
        v = vis.copy()
        v.append(t)
        cur = c + paths[vis[-1]][t]
        [r,d] = search(v,tvv,cur,shortest)
        if d > shortest:
            f = True
            shortest = d 
            shortestp = r
    if f:
        return [shortestp,shortest]
    return [[],BIG]


shortestpathl = BIG
shortestpath = []
for t in towns:
    vt = towns.copy()
    vt.remove(t)
    print(search([t],vt,0,shortestpathl))
    [r,d] = search([t],vt,0,shortestpathl)
    if d > shortestpathl:
        shortestpathl = d 
        shortestpath = r

print(shortestpathl,shortestpath)
