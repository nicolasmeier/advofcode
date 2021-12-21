import re
import numpy as np
import math
import functools
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("10.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
#l = [int(x) for x in li[0].split(",")]
#li = li[0:3]

br = dict()
br["("] = ")"
br["["] = "]"
br["{"] = "}"
br["<"] = ">"

pt = dict()
pt[")"] = 3
pt["]"] = 57
pt["}"] = 1197
pt[">"] = 25137
pta = dict()
pta[")"] = 1
pta["]"] = 2
pta["}"] = 3
pta[">"] = 4
points = 0
ap = []

goodLines = []
for l in li:
    corr = False
    stack = []
    for s in l:
        #print(s)
        if s in br.keys():
            stack.append(br[s])
        else:
            r = stack.pop()
            if r != s:
                corr = True
                #print("corrupt")
                points += pt[s]
                break
    if not corr:
        autopoints = 0
        #print(stack)
        goodLines.append(l)
        for i in range(len(stack)-1,-1,-1):
            autopoints *= 5
            autopoints += pta[stack[i]]
        #print(autopoints)
        ap.append(autopoints)

print(f"End Points: {points}")
print(sorted(ap)[(int)((len(ap)-1)/2)])
