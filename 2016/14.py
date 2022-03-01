import os
import sys
import re
import numpy as np
import math
import functools
import hashlib

def hash(a,b) -> str:
    return hashlib.md5(f"{a}{b}".encode('utf-8')).hexdigest()

def istripple(h):
    m = re.search("(.)\\1\\1", h)
    if m is not None:
        return m.group(0)[0]
    return False

def is5(h):
    m = re.search("(.)\\1\\1\\1\\1", h)
    if m is not None:
        return m.group(0)[0]
    return False

os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("14.txt") as f:
    l = [x.strip() for x in f.readlines()]
    l = l[0]

#l = "abc"
print(l)

trips = list()
nrkey = 0
keys = list()

for i in range(10000000000000000):
    h = hash(l,i)
    stretch = h
    for what in range(2016):
        stretch = hash(stretch,"")
    h = stretch
    #print(h,istripple(h))
    if istripple(h):
        x = istripple(h)
        trips.append([h,x,i])
        if is5(h):
            y = is5(h)
            for k in trips:
                kh,kl,ki = k
                if kl == y and kh not in keys and ki + 1001 >= i and ki != i:
                    nrkey += 1
                    keys.append(kh)
                    print(nrkey,ki)
                    if nrkey == 64:
                        quit()

    

print(trips)