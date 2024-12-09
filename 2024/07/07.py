import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    return x
    
li = []
with open("07.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

def check(res:int,acc:int,opr:list) -> bool:
    if opr == []:
        return res == acc
    n = opr.pop(0)
    return check(res,acc+n,opr.copy()) or check(res,acc*n,opr.copy())
 
def check2(res:int,acc:int,opr:list) -> bool:
    if opr == []:
        return res == acc
    n = opr.pop(0)
    return check2(res,acc+n,opr.copy()) or check2(res,acc*n,opr.copy()) or check2(res,int(str(acc)+str(n)),opr.copy()) 

part1 = 0
part2 = 0
for l in li:
    res, opr = l.split(":",1)
    res = int(res)
    abc = [int(x) for x in opr.split()]

    if check(res,0,abc.copy()):
        part1 += res
    if check2(res,0,abc.copy()):
        part2 += res


print(f"part1 = {part1}")
print(f"part2 = {part2}")