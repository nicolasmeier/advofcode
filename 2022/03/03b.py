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
for j in range(0,len(li),3):
    print(li[j:j+3])
    g = li[j:j+3]
    a,b,c = g
    for aa in set(a):
        if aa in b and aa in c:
            print(aa)
            out += score.index(aa) + 1
    print()


print(out)
