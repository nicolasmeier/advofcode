import re
import numpy as np
import math
import functools
import os
import sys


os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("erm.txt") as f:
    li = [x.strip() for x in f.readlines()]

lines = li
adj = dict()

places = set()
for l in li:
    a,b = l.split("-")
    places = places | {a}
    places = places | {b}

for p in places:
    adj[p] = []

for line in lines:
    a, b = line.split("-")
    adj[a].append(b)
    adj[b].append(a)

def paths(cur: str, seen: set) -> int:
    if cur == 'end':
        print(seen)
        return 1
    if cur.islower() and cur in seen:
        return 0
    seen = seen | {cur}
    out = 0
    for a in adj[cur]:
        out += paths(a, seen)
    return out

out = paths("start", set())
print(out)

def paths2(cur: str, seen: set, dup:str) -> int:
    if cur == 'end':
        return 1
    if cur == "start" and seen:
        return 0
    if cur.islower() and cur in seen:
        if dup is None:
            dup = cur
        else:
            return 0
    seen = seen | {cur}
    out = 0
    for a in adj[cur]:
        out += paths2(a, seen, dup)
    return out

out = paths2("start", set(), None)
print(out)