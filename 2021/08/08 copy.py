import os
import sys
import re
import numpy as np
import math
import functools
import constraint as csp
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("08t.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
#l = [int(x) for x in li[0].split(",")]
#li = li[0:3]
sseg = dict()
sseg[0] = ["a","b","c","e","f","g"]
sseg[1] = ["c","f"]
sseg[2] = ["a","c","d","e","g"]
sseg[3] = ["a","c","d","f","g"]
sseg[4] = ["b","c","d","f"]
sseg[5] = ["a","b","d","f","g"]
sseg[6] = ["a","b","d","e","f","g"]
sseg[7] = ["a","c","f"]
sseg[8] = ["a","b","c","d","e","f","g"]
sseg[9] = ["a","b","c","d","f","g"]

def addPossib(i:int,s:str,seg_sol):
    c = [c for c in s]
    ch = []
    for k in c:
        n = True
        for x in ["a","b","c","d","e","f","g"]:
            if k in seg_sol[x]:
                n = False
        if n:
            ch.append(k)
    for k in ch:
        for x in sseg[i]:
            seg_sol[x].append(k)



        
def solver(seg_sol):
    prob = csp.Problem()
    for k,v in seg_sol.items():
        prob.addVariable(k,v)
    prob.addConstraint(csp.AllDifferentConstraint())
    s = prob.getSolutions()
    for x in s:
        print(x)
        print()


_seg_sol = dict()
for x in ["a","b","c","d","e","f","g"]:
    _seg_sol[x] = []
res = 0
for l in li:
    seg_sol = _seg_sol.copy()
    for x in sorted(l.split(), key=len):
        if len(x) == 2:
            addPossib(1,x,seg_sol)
        elif len(x) == 3:
            addPossib(7,x,seg_sol)
        elif len(x) == 4:
            addPossib(4,x,seg_sol)
        elif len(x) == 7:
            addPossib(8,x,seg_sol)
    solver(seg_sol)
#print(res)