import os
import sys
import re
import numpy as np
import math
import functools

os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("05.txt") as f:
    l = [x.strip() for x in f.readlines()]

re1 = re.compile(r"(.).\1")
re2 = re.compile(r"(.{2}).*\1")
def nicestr(s):
    r1 = re.search(re1,s)
    r2 = re.search(re2,s)
    print((bool)(r1 and r2 ))
    if r1 and r2 :
        return True
    return False
    
nicestr("qjhvhtzxzqqjkmpb")
nicestr("xxyxx")
nicestr("uurcxstgmygtbstg")
nicestr("ieodomkazucvgmuy")
nicestr("aaa")

nice, bad = 0,0
for s in l:
    if nicestr(s):
        nice += 1
    else:
        bad += 1

print(nice)