import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("06.txt") as f:
    l = [x.strip() for x in f.readlines()]

#print(l)

f = dict()

for x in range(1000):
    f[x] = dict()
    for y in range(1000):
        f[x,y] = False

def ton(a,b,c,d):
    #print(a,b,c,d)
    for x in range(a,c):
        for y in range(b,d):
            f[x,y] = True

def toff(a,b,c,d):
    for x in range(a,c):
        for y in range(b,d):
            f[x,y] = False

def toggle(a,b,c,d):
    for x in range(a,c):
        for y in range(b,d):
            f[x,y] = not f[x,y]

#l = ["turn on 0,0 through 999,999"]

for i in l:
    #print(i)
    ab, cd = i.split(" through ",2)
    aa,bb = [x for x in ab.split(",",2)]
    cc,dd = [x for x in cd.split(",",2)]
    a = [int(s) for s in aa.split() if s.isdigit()][0]
    b = [int(s) for s in bb.split() if s.isdigit()][0]
    c = [int(s) for s in cc.split() if s.isdigit()][0]+1
    d = [int(s) for s in dd.split() if s.isdigit()][0]+1
    x = [a,b,c,d]
    #print(a,b,c,d)
    if i.startswith("turn on"):
        ton(*x)
    elif i.startswith("turn off"):
        toff(*x)
    elif i.startswith("toggle"):
        toggle(*x)
    else:
        print("error",i)

o = 0
for x in range(1000):
    for y in range(1000):
        if f[x,y]:
            o += 1

print(o)