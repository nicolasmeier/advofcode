import os
import sys
import re
import numpy as np
import math
import functools
from collections import Counter
# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x
    
li = []
with open("03.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

res1 = 0    
res2 = 0
for line in li:
    a = max(list(line))
    idx = line.index(max(list(line)))
    x = line[idx+1:]
    if x:
        b = max(list(x))
        res1 += int(a+b)
    else:
        x = line[:-1]
        b = max(list(x))
        res1 += int(b+a)

print("res1:", res1)

res2 = 0
for line in li:

    num = ""
    x = line
    for i in range(11,-1,-1):
        mx = max(list(x[:-i])) if i != 0 else max(list(x))
        num += mx
        x = x[x.index(mx)+1:]
    print("num:", num)
    res2 += int(num)
    if False:
        alltimebest = 0
        best1 = "0"
        for a1 in range(len(line)):
            if line[a1] < best1:
                continue
            best1 = line[a1]
            best2 = "0"
            for a2 in range(a1+1, len(line)):
                if line[a2] < best2:
                    continue
                best2 = line[a2]
                best3 = "0"
                for a3 in range(a2+1, len(line)):
                    if line[a3] < best3:
                        continue
                    best3 = line[a3]
                    best4 = "0"
                    for a4 in range(a3+1, len(line)):
                        if line[a4] < best4:
                            continue
                        best4 = line[a4]
                        best5 = "0"
                        for a5 in range(a4+1, len(line)):
                            if line[a5] < best5:
                                continue
                            best5 = line[a5]
                            best6 = "0"
                            for a6 in range(a5+1, len(line)):
                                if line[a6] < best6:
                                    continue
                                best6 = line[a6]
                                best7 = "0"
                                for a7 in range(a6+1, len(line)):
                                    if line[a7] < best7:
                                        continue
                                    best7 = line[a7]
                                    best8 = "0"
                                    for a8 in range(a7+1, len(line)):
                                        if line[a8] < best8:
                                            continue
                                        best8 = line[a8]
                                        best9 = "0"
                                        for a9 in range(a8+1, len(line)):
                                            if line[a9] < best9:
                                                continue
                                            best9 = line[a9]
                                            best10 = "0"
                                            for a10 in range(a9+1, len(line)):
                                                if line[a10] < best10:
                                                    continue
                                                best10 = line[a10]
                                                best11 = "0"
                                                for a11 in range(a10+1, len(line)):
                                                    if line[a11] < best11:
                                                        continue
                                                    best11 = line[a11]
                                                    best12 = "0"
                                                    for a12 in range(a11+1, len(line)):
                                                        if line[a12] < best12:
                                                            continue
                                                        best12 = line[a12]
                                                        best = int(best1+best2+best3+best4+best5+best6+best7+best8+best9+best10+best11+best12)
                                                        if best > alltimebest:
                                                            alltimebest = best
                                                        
        print("alltimebest:", alltimebest)

        res2 += alltimebest

print("res2:", res2)