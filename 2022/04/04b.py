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

li = []
with open("04.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]
#li = li[0]
out = 0
for l in li:
    a,b = l.split(",")
    al,au = a.split("-")
    bl,bu = b.split("-")
    al = int(al)
    au = int(au)
    bl = int(bl)
    bu = int(bu)
    print(a,b)

    if al in range(bl,bu+1) or au in range(bl,bu+1) or bl in range(al,au+1) or bu in range(al,au+1):
        out += 1

print(out)
