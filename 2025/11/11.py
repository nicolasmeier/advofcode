import os
import sys
import re
import numpy as np
import math
import functools
from collections import Counter
import itertools
from z3 import *
# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x):
    return x.replace("\n", "").strip()
    
li = []
with open("11.txt") as f:
    li = [trans(x) for x in f.readlines()]


paths = dict()

for line in li:
    a, b = line.split(":")
    a = a.strip()
    b = b.strip().split(" ")
    b = [x.strip() for x in b]
    if a  in paths:
        print("error")
    paths[a] = b


    
def dfs(cur):
    if cur == "out":
        return 1
    res = 0
    for nxt in paths[cur]:
        res += dfs(nxt)
    return res

def dfs2(cur, dac,fft):
    if cur == "out":
        if dac and fft:
            return 1
        return 0
    elif not dac and cur == "dac":
        dac = True
    elif not fft and cur == "fft":
        fft = True

    if dac or fft:
        print(cur, dac, fft)
    res = 0
    for nxt in paths[cur]:
        res += dfs2(nxt, dac,fft)
    return res

@functools.lru_cache(None)
def dfs2e(cur, dac,fft, end="out"):
    if cur == end:
        print("reached end", dac, fft)
        if dac and fft:
            return 1
        return 0
    elif not dac and cur == "dac":
        dac = True
    elif not fft and cur == "fft":
        fft = True
    elif cur == "out":
        return 0

    if dac or fft:
        print(cur, dac, fft)
    res = 0
    for nxt in paths[cur]:
        res += dfs2e(nxt, dac,fft, end)
    return res


ans = dfs("you")

print(ans)

ans2a = dfs2e("svr", False, False,"out")
print(ans2a)
