import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    return list(map(int,[y for y in x.split()]))
    
li = []
with open("11.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


nu = dict()
for l in li[0]:
    nu[l] = nu.get(l,0) + 1

def blink(nu:dict) -> dict:
    nn = dict()
    for n,v in nu.items():
        if n == 0:
            nn[1] = nn.get(1,0) + v
        elif len(str(n)) % 2 == 0:
            l = len(str(n)) // 2
            a = int(str(n)[:l])
            b = int(str(n)[l:])
            nn[a] = nn.get(a,0) + v
            nn[b] = nn.get(b,0) + v
        else:
            nn[n*2024] = nn.get(n*2024,0) + v
    return nn

for k in range(76):
    print(k,sum(nu.values()))
    nu = blink(nu)