import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
os.chdir(os.path.dirname(sys.argv[0]))
lines = []
ingr = dict()
with open("15.txt") as f:
    lines = [x.strip() for x in f.readlines()]
#l = l[0]
sec = 2504


for l in lines:
    i,c,cn,d,dn,f,fn,t,tn,cal,caln = l.split()
    ingr[i] = dict()
    ingr[i][c] = cn
    ingr[i][d] = dn
    ingr[i][f] = fn
    ingr[i][t] = tn
    ingr[i][cal] = caln


print(ingr.keys())
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            for d in range(101-a-b-c):
                if a + b + c + d == 100:
                    print(a,b,c,d)
                    for k in ingr:
                        