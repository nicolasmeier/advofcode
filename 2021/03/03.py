import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))


li = []
with open("03.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
res = ""
eps = ""
for i in range(len(li[0])):
    is1 = 0
    for l in li:
        is1 += int(l[i])
    if is1 > len(li)/2:
        res += "1"
        eps += "0"
    else:
        res += "0"
        eps += "1"

print(res)
ri = int(res, 2)
epsi = int(eps, 2)
print(ri,epsi)
print(ri*epsi)