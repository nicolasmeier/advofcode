import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("10.txt") as f:
    l = [x.strip() for x in f.readlines()]
l = l[0]

def lookandsay(n):
    return ''.join( str(len(list(g))) + k for k, g in groupby(n))

def game(s:str) -> str:
    print([[k,g] for k, g in groupby(s)])
    out = ""
    i = 0
    while i < len(s):
        c = s[i]
        n = 1
        for j in range(i+1,len(s)):
            if c == s[j]:
                n += 1
                i += 1
            else:
                break
        out = out + str(n) + c 
        i += 1
    return out
s = l
print(s)
for x in range(50):
    s = lookandsay(s)
    #print(s)
print(len(s))

