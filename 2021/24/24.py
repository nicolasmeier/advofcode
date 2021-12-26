import numpy as np
import math
import functools
import collections 
import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("24.txt") as f:
    li = [x.strip() for x in f.readlines()]
#li = li[0]
def isNumber(x:str):
    is_positive_integer = x.isdigit()
    is_negative_integer =  x.startswith("-") and x[1:].isdigit()
    return is_positive_integer or is_negative_integer


def checkMONAD(modelnumber, instructions):
    if "0" in modelnumber:
        return False
    vars = dict()
    vars["w"] = 0
    vars["x"] = 0
    vars["y"] = 0
    vars["z"] = 0
    i = 0
    for l in instructions:
        instr, *p = l.split()
        if instr == "inp":
            #print(instr,p[0],int(modelnumber[i]))
            vars[p[0]] = int(modelnumber[i])
            i += 1
        elif instr == "add":
            a,b = p
            if isNumber(b):
                vars[a] = vars[a] + int(b)
            else:
                vars[a] = vars[a] + vars[b]
        elif instr == "mul":
            a,b = p
            if isNumber(b):
                if int(b) != 0:
                    vars[a] = vars[a] * int(b)
            else:
                vars[a] = vars[a] * vars[b]
        elif instr == "div":
            a,b = p
            if isNumber(b):
                if int(b) != 0:
                    vars[a] = int(vars[a] / int(b))
            else:
                if vars[b] != 0:
                    vars[a] = int(vars[a] / vars[b])
        elif instr == "mod":
            a,b = p
            if vars[a] >= 0:
                if isNumber(b):
                    if int(b) > 0:
                        vars[a] = int(vars[a] % int(b))
                else:
                    if vars[b] > 0:
                        vars[a] = int(vars[a] % vars[b])
        elif instr == "eql":
            a,b = p
            if isNumber(b):
                if vars[a] == int(b):
                    vars[a] = 1
                else:
                    vars[a] = 0
            else:
                if vars[a] == vars[b]:
                    vars[a] = 1
                else:
                    vars[a] = 0   
    #print(vars) 
    return vars["z"] == 0
for i in range(99999999999999,0,-1):
    if checkMONAD(str(i),li):
        print(i)
        quit()
        q = 0
    