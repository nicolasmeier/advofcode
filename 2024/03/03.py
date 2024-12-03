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
with open("03.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

part1 = 0
for l in li:
    match = re.findall(r'mul\(\d{1,3},\d{1,3}\)',l)
    for m in match:
        a = list(map(int,m[4:-1].split(",",1)))
        x,y = a
        part1 += x * y

part2 = 0
do = True
for l in li:
    match = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))',l)
    print(match)
    for m in match:
        m = str(m)
        if m.startswith("mul") and do:
            a = list(map(int,m[4:-1].split(",",1)))
            x,y = a
            part2 += x * y
        elif m.startswith("do()"):
            do = True
        elif m.startswith("don't()"):
            do = False

print(part1)
print(part2)
    
