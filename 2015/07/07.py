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
wire = dict()

for i in [y for y in l if re.search("^[0-9]+ ->",y)]:
    a,b = [x.strip() for x in i.split("->",2)]
    #print(a,b)
    if "AND" in a:
        m,n = [x.strip() for x in a.split("AND",2)]
        #print(m,n)
        if m.isdigit():
            m = int(m)
        else:
            m = wire[m]
        if n.isdigit():
            n = int(n)
        else:
            n = wire[n]
        wire[b] = m&n
    elif "OR" in a:
        m,n = [x.strip() for x in a.split("OR",2)]
        #print(m,n)
        if m.isdigit():
            m = int(m)
        else:
            m = wire[m]
        if n.isdigit():
            n = int(n)
        else:
            n = wire[n]
        wire[b] = m|n
    elif "LSHIFT" in a:
        m,n = [x.strip() for x in a.split("LSHIFT",2)]
        #print(m,n)
        if m.isdigit():
            m = int(m)
        else:
            m = wire[m]
        if n.isdigit():
            n = int(n)
        else:
            n = wire[n]
        wire[b] = m<<n
    elif "RSHIFT" in a:
        m,n = [x.strip() for x in a.split("RSHIFT",2)]
        #print(m,n)
        if m.isdigit():
            m = int(m)
        else:
            m = wire[m]
        if n.isdigit():
            n = int(n)
        else:
            n = wire[n]
        wire[b] = m>>n
    elif "NOT" in a:
        m,n = [x.strip() for x in a.split("NOT",2)]
        #print(m,n)
        if n.isdigit():
            n = int(n)
        else:
            n = wire[n]
        wire[b] = ~n
    else:
        wire[b] = int(a)

k = list(wire.keys())
for w in sorted(wire.keys()):
    print(f"{w}: {wire[w]}")
