import os
import sys
import re
import numpy as np
import math
import functools
from itertools import groupby
import json

os.chdir(os.path.dirname(sys.argv[0]))
l = []
with open("12.txt") as f:
    l = [x.strip() for x in f.readlines()]
l = l[0]
y = json.loads(l)
#y = json.loads(r'{"a":{"b":4},"c":-1}')


def td(y:dict):
    if "red" in list(y.keys()):
        return 0
    c = 0
    for k,v in y.items():
        if isinstance(v,dict):
            c  += td(v)
        elif isinstance(v,list):
            c  += tl(v)
        elif isinstance(v,str):
            if v == "red":
                return 0
            #print(v,"str")
        elif isinstance(v,int):
            c += v
        else:
            print(type(v))
            print("os.error")
            quit()
    return c
            
def tl(y:list):
    c = 0
    for v in y:
        if isinstance(v,dict):
            c  += td(v)
        elif isinstance(v,list):
            c  += tl(v)
        elif isinstance(v,str):
            c += 0
            #print(v,"str")
        elif isinstance(v,int):
            c += v
        else:
            print(type(v))
            print("os.error")
            quit()
    return c
    



print(td(y))
