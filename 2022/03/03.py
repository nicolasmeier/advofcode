import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))


def trans(x):
    return x

score = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()

li = []
with open("03.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]
#li = li[0]
out = 0
for l in li:
    le = int(len(l) / 2)
    #print(l,l[:le],l[le:])
    com = set(l[:le])
    rest = set(l[le:])
    for c in com:
        if c in rest:
            print(c)
            out += score.index(c) + 1


print(out)
