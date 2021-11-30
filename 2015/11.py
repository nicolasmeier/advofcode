import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("11.txt") as f:
    l = [x.strip() for x in f.readlines()]
l = l[0]
print(l)

def increment(pw: str):
    if pw[-1] != "z":
        return pw[:-1]+chr(ord(pw[-1])+1)
    else:
        return increment(pw[:-1]) + "a"


r1 = "("
for i in range(ord("a"),ord("z")-1):
    x = chr(i)+chr(i+1)+chr(i+2)
    r1 = r1 +x+ "|"
r1r = r1[:-1] + ")"

print(r1r)
r1 = re.compile(r1r)
r2 = re.compile(r"(.)\1.*(.)\2")
def validpw(pw):
    for x in ["i","o","l"]:
        if x in pw:
            return False
    a,b = False, False
    if re.search(r1,pw):
        a = True
    if re.search(r2,pw):
        b = True
    return a and b
def genpw(oldpw):
    pw = increment(oldpw)
    while(not validpw(pw)):
        pw = increment(pw)
    return pw

print(genpw("cqjxxyzz"))
