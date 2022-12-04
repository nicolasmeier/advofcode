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
    if (al >= bl and au <= bu) or (al <= bl and au >= bu):
        out += 1

print(out)
