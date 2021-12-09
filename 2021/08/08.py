import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("08.txt") as f:
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
for i in range(10):
    print(i,len(sseg[i]))
res = 0
for l in li:
    l = l.split("|")[1]

    for le in [len(x) for x in l.split()]:
        if le in [2,4,3,7]:
            res += 1
print(res)