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
with open("02.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]


ranges = li[0].split(",")
res1 = 0
for r in ranges:
    a,b = r.split("-")
    if len(a) == len(b) and len(a) % 2 == 1:
        #print(f"Range from {a} to {b} keine.")
        continue
    x = a[0:len(a)//2]
    if len(x) == 0:
        x = "1"
    a = int(a)
    b = int(b)
    print(f"Range from {a} to {b} includes {x} numbers.")
    while int(x + x) <= b:
        if int(x + x) >= a:
            res1 += int(x + x)
            print(int(x + x))
        x = str(int(x) + 1)

print("Part 1 "+str(res1))



res2 = 0
for r in ranges:
    a,b = r.split("-")
    x = "1"
    a = int(a)
    b = int(b)
    print(f"Range from {a} to {b} includes {x} numbers.")
    added = set()
    for i in range(2,10):
        x = "1"
        while int(x*i) <= b:
            if int(x*i) >= a:
                if int(x*i) not in added:
                    added.add(int(x*i))
                    res2 += int(x*i)
                    print(int(x*i))
            x = str(int(x) + 1)

print("Part 2 "+str(res2))