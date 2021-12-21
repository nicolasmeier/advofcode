import re
import numpy as np
import math
import functools
import collections 

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("19t.txt") as f:
    li = [x.strip() for x in f.readlines()]
#li = li[0]

#print(li)
x = 0
scanner = dict()

s = ""
for l in li:
    #print(l)
    if l != "":
        if l.startswith("--"):
            #print(l.split()[2])
            s = l.split()[2]
            scanner[s] = []
            x += 1
        else:
            #print(l.split(","))
            scanner[s].append([int(x) for x in l.split(",")])

def dif(x,y):
    a = abs(x[0] - y[0])
    b = abs(x[1] - y[1])
    c = abs(x[2] - y[2])
    x = sorted([a,b,c])
    return f"{x[0]}:{x[1]}:{x[2]}:"

def abs_dif(x,y:str):
    y = y[1:-1]
    y = [int(g) for g in y.split(",")]
    a = (int(x[0]) - int(y[0]))
    b = (int(x[1]) - int(y[1]))
    c = (int(x[2]) - int(y[2]))
    return [a,b,c]

#print(scanner)
scd = dict()
for k,v in scanner.items():
    scd[k] = dict()
    for x in v:
        for y in v:
            #print(x != y)
            if x == y:
                #print(x,y,dif(x,y))
                asfeiewutwiefsidof = 0
            else:
                #print(x,y,dif(x,y))
                scd[k][dif(x,y)] = (x,y)
#print(scd.keys())
overlap = dict()
for a in scd.keys():
    for b in scd.keys():
        if a != b:
            overlap[f"{a}{b}"] = []
            c = 0
            for x in scd[a]:
                if x in scd[b]:
                    c += 1
                    aa = scd[a][x]
                    bb = scd[b][x]
                    overlap[f"{a}{b}"].append((aa,bb))
            #print(a,b,c)

#print(overlap["01"])
becon= []
for x in scanner["0"]:
    becon.append(x)
x = overlap["01"][0]
#print(x)
(a,b),(c,d) = x
#print(a,b,c,d)
cand = collections.Counter()
cnt = 0
for x in overlap["01"]:
    if a in x[0] or a in x[1]:
        #print(x[1][0],x[1][1])
        cnt += 1
        cand[str(x[1][0])] += 1
        cand[str(x[1][1])] += 1
print(cnt)
print(cand)
conv01 = []
if cnt > 1:
    for k,v in cand.items():
        if cnt == v:
            print(a,k,abs_dif(a,k))
            conv01 = abs_dif(a,k)

for b in becon:
    print(b)

def conv(x,conv):
    a = x[0] + conv[0]
    b = x[1] + conv[1]
    c = x[2] + conv[2]
    return [a,b,c]
asdasd = 0
for s in scanner["1"]:
    print(s,conv(s,conv01))
    if conv(s,conv01) in becon:
        asdasd += 1
print(asdasd)