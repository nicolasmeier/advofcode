import os
import sys
import re
import numpy as np
import math
import functools

# run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x:str):
    x = x.replace("L","-")
    x = x.replace("R","")
    return int(x)
    
li = []
with open("01.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

x = 50
z = 0
for l in li:
    if (x + l) % 100 == 0:
        z += 1
    x = (x + l) % 100
    
# part 1
print(z)



# part 2
x = 50
y = 0
for l in li:
    if (x + l) // 100 != 0:
        y += abs((x + l) // 100)
    x = (x + l) % 100

print("Part 2 "+str(y))


for i in range(-1000,1000,50):
    print(i,i//100)