import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))


li = []
with open("03.txt") as f:
    li = [x.strip() for x in f.readlines()]
    #li = [int(x.strip()) for x in f.readlines()]
res = ""
eps = ""
def fres():
    res = ""
    for i in range(len(li[0])):
        is1 = 0
        ll = 0
        lic = li.copy()
        lica = li.copy()
        for l in lic:
            if l.startswith(res):
                ll += 1
                is1 += int(l[i])
            else:
                lica.remove(l)
        lic = lica
        if ll == 1:
            for l in li:
                if l.startswith(res):
                    return l
        if is1 >= ll/2.0:
            res += "1"
        else:
            res += "0"
        print(res)
    return res
def feps():
    res = ""
    for i in range(len(li[0])):
        is1 = 0
        ll = 0
        lic = li.copy()
        lica = li.copy()
        for l in lic:
            if l.startswith(res):
                ll += 1
                is1 += int(l[i])
            else:
                lica.remove(l)
        lic = lica
        if ll == 1:
            for l in li:
                if l.startswith(res):
                    return l
        if is1 >= ll/2.0:
            res += "0"
        else:
            res += "1"
    return res
res = fres()
eps = feps()
ri = int(res, 2)
epsi = int(eps, 2)
print(ri,epsi)
print(ri*epsi)