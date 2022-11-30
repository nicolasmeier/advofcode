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

def nicestr(s):
    r1 = re.search(".*[aeiou].*[aeiou].*[aeiou].*",s)
    r2 = re.search("(aa|bb|cc|dd|ee|ff|gg|hh|ii|jj|kk|ll|mm|nn|oo|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz)",s)
    r3 = re.search("(ab|cd|pq|xy)",s)
    print((bool)(r1 and r2 and not r3))
    if r1 and r2 and not r3:
        return True
    return False
    
nicestr("ugknbfddgicrmopn")
nicestr("aaa")
nicestr("jchzalrnumimnmhp")
nicestr("haegwjzuvuyypxyu")
nicestr("dvszwmarrgswjxmb")

nice, bad = 0,0
for s in l:
    if nicestr(s):
        nice += 1
    else:
        bad += 1

print(nice)