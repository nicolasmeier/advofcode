import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("13.txt") as f:
    l = [x.strip() for x in f.readlines()]
#l = l[0]
#print(l)

p = dict()
p["me"] = dict()
for i in l:
    y = i.split()
    a,b,g,v = y[0],y[10][:-1],y[2],y[3]
    #print(a,b,g,v)
    p[a] = dict()
    p[b] = dict()
for i in l:
    y = i.split()
    a,b,g,v = y[0],y[10][:-1],y[2],int(y[3])
    #print(a,b,g,v)
    if g == "lose":
        v = v * -1
    p[a][b] = v


n = list(p.keys())

for m in n:
    p["me"][m] = 0
    p[m]["me"] = 0

#print(n)
seatings = []

def gs(f:list,o:list):
    if len(o) == 0:
        seatings.append(f)
    else:
        for i in o:
            oo = o.copy()
            ff = f.copy()
            oo.remove(i)
            ff.append(i)
            gs(ff,oo)

gs([],n)

#print(len(seatings))

def cs(s:list):
    c = 0
    for i in range(len(s)):
        a,b = s[i],s[i-1]
        #print(a,b)
        c += p[a][b]
        c += p[b][a]
    return c

k = 0
for s in seatings:
    l = cs(s)
    if l > k:
        k = l

    
print(k)
