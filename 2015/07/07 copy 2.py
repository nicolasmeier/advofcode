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


'''
    #print(a,b)
        '''

#@functools.lru_cache()
def solve(a):
    #print("solve",a)
    if isinstance(a, int) or a.isdigit():
        return a
    elif "AND" in a:
        m,n = [x.strip() for x in a.split("AND",2)]
        if m.isdigit():
            m = int(m)
        else:
            m = solve(raw[m])
        if n.isdigit():
            n = int(n)
        else:
            n = solve(raw[n])
        return f"{solve(m)} AND {solve(n)}"
    elif "OR" in a:
        m,n = [x.strip() for x in a.split("OR",2)]
        if m.isdigit():
            m = int(m)
        else:
            m = solve(raw[m])
        if n.isdigit():
            n = int(n)
        else:
            n = solve(raw[n])
        return f"{solve(m)} OR {solve(n)}"
    elif "LSHIFT" in a:
        m,n = [x.strip() for x in a.split("LSHIFT",2)]
        if m.isdigit():
            m = int(m)
        else:
            m = solve(raw[m])
        if n.isdigit():
            n = int(n)
        else:
            n = solve(raw[n])
        return f"{solve(m)} LSHIFT {solve(n)}"
    elif "RSHIFT" in a:
        m,n = [x.strip() for x in a.split("RSHIFT",2)]
        if m.isdigit():
            m = int(m)
        else:
            m = solve(raw[m])
        if n.isdigit():
            n = int(n)
        else:
            n = solve(raw[n])
        return f"{solve(m)} RSHIFT {solve(n)}"
    elif "NOT" in a:
        m,n = [x.strip() for x in a.split("NOT",2)]
        if n.isdigit():
            n = int(n)
        else:
            n = solve(raw[n])
        return f"NOT {solve(n)}"
    else:
        return solve(raw[a])
    #print( raw[b])
    return raw[b]

#for w in sorted(raw.keys()):
    #print(f"{w}: {raw[w]}")
print(solve(raw["a"]))
