import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("07.txt") as f:
    l = [x.strip() for x in f.readlines()]
la = ["123 -> x",
"456 -> y",
"x AND y -> d",
"x OR y -> e",
"x LSHIFT 2 -> f",
"y RSHIFT 2 -> g",
"NOT x -> h",
"NOT y -> i"]
raw = dict()
for i in l:
    a,b = [x.strip() for x in i.split("->",2)]
    raw[b] = a

for i in range(1000):
    raw[i] = i
    raw[str(i)] = i

'''
    #print(a,b)
        '''

@functools.lru_cache()
def solve(a):
    #print("solve",a)
    if isinstance(a, int) or a.isdigit():
            raw[b] = int(a)
    elif "AND" in a:
        m,n = [x.strip() for x in a.split("AND",2)]
        m = solve(raw[m])
        n = solve(raw[n])
        raw[b] = m&n
    elif "OR" in a:
        m,n = [x.strip() for x in a.split("OR",2)]
        m = solve(raw[m])
        n = solve(raw[n])
        raw[b] = m|n
    elif "LSHIFT" in a:
        m,n = [x.strip() for x in a.split("LSHIFT",2)]
        m = solve(raw[m])
        n = solve(raw[n])
        raw[b] = m<<n
    elif "RSHIFT" in a:
        m,n = [x.strip() for x in a.split("RSHIFT",2)]
        m = solve(raw[m])
        n = solve(raw[n])
        raw[b] = m>>n
    elif "NOT" in a:
        m,n = [x.strip() for x in a.split("NOT",2)]
        n = solve(raw[n])
        raw[b] = ~n
    else:
        raw[b] = solve(raw[a])
    #print( raw[b])
    return raw[b]

#for w in sorted(raw.keys()):
    #print(f"{w}: {raw[w]}")
raw["a"] = solve(raw["a"])
print(raw["a"])

aaa = raw["a"]

raw = dict()
for i in l:
    a,b = [x.strip() for x in i.split("->",2)]
    raw[b] = a
    
for i in range(1000):
    raw[i] = i
    raw[str(i)] = i

solve.cache_clear()
raw["b"] = aaa
raw["a"] = solve(raw["a"])
print(raw["a"])
quit()
for w in sorted(raw.keys()):
    print(f"{w}: {raw[w]}")

