import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))


sts = []
for i in range(9):
    sts.append([])

sts[0].append("R")
sts[0].append("P")
sts[0].append("C")
sts[0].append("D")
sts[0].append("B")
sts[0].append("G")


sts[1].append("H")
sts[1].append("V")
sts[1].append("G")

sts[2].append("N")
sts[2].append("S")
sts[2].append("Q")
sts[2].append("D")
sts[2].append("J")
sts[2].append("P")
sts[2].append("M")

sts[3].append("P")
sts[3].append("S")
sts[3].append("L")
sts[3].append("G")
sts[3].append("D")
sts[3].append("C")
sts[3].append("N")
sts[3].append("M")


sts[4].append("J")
sts[4].append("B")
sts[4].append("N")
sts[4].append("C")
sts[4].append("P")
sts[4].append("F")
sts[4].append("L")
sts[4].append("S")


sts[5].append("Q")
sts[5].append("B")
sts[5].append("D")
sts[5].append("Z")
sts[5].append("V")
sts[5].append("G")
sts[5].append("T")
sts[5].append("S")


sts[6].append("B")
sts[6].append("Z")
sts[6].append("M")
sts[6].append("H")
sts[6].append("F")
sts[6].append("T")
sts[6].append("Q")


sts[7].append("C")
sts[7].append("M")
sts[7].append("D")
sts[7].append("B")
sts[7].append("F")


sts[8].append("F")
sts[8].append("C")
sts[8].append("Q")
sts[8].append("G")






def trans(x):
    return x

li = []
with open("05.txt") as f:
    li = [x.strip() for x in f.readlines()]

def move(n,f,t):
    f = f-1
    t = t-1
    for j in range(n):
        tmp = sts[f].pop()
        sts[t].append(tmp)
    pass

#li = li[0]
init = True
out = 0
for l in li:
    if init:
        if l.strip() == "":
            init = False
            pass
    else:
        print(l)
        l = l[5:]
        l = l.replace("f","")
        l = l.replace("r","")
        l = l.replace("o","")
        l = l.replace("m","")
        l = l.replace("t","")
        m,f,t = [int(x) for x in l.split()]
        print(m,f,t)
        move(m,f,t)

print()

for s in sts:
    print(s.pop(),end="")
