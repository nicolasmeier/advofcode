import re
import numpy as np
import math
import functools
import collections 

import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))



# Day 20

li = []
with open("20.txt") as f:
    li = f.read()
data = li.strip()

def enhance(lut, image, void=0):
    image = np.pad(image, 3, constant_values=void)
    if void == 0:
        out_image = np.zeros(image.shape, dtype=np.uint8)
    else:
        out_image = np.ones(image.shape, dtype=np.uint8)
    ylen,xlen = image.shape
    for i in range(1,ylen-1):
        for j in range(1,xlen-1):
            idx = image[i-1:i+2, j-1:j+2].flatten()
            idx = int("".join(map(str, idx)), 2)
            out_image[i,j] = lut[idx]
    return out_image[1:-1, 1:-1], lut[0] if void == 0 else lut[int("111111111", 2)]

def print_image(image):
    for line in image:
        print("".join({0: ".", 1: "#"}[x] for x in line))


# Part 1
mapping = {'.': 0, '#': 1}
lut, image = data.split('\n\n')
lut = np.array([mapping[x] for x in lut], dtype=np.uint8)
image = np.array([list(map(lambda z: mapping[z], x)) for x in image.splitlines()], np.uint8)
void = 0

for i in range(2):
    image, void = enhance(lut, image, void)

d20p1 = image.sum()
print(f'Day 20 Part 1: {d20p1}')

# Part 2
mapping = {'.': 0, '#': 1}
lut, image = data.split('\n\n')
lut = np.array([mapping[x] for x in lut], dtype=np.uint8)
image = np.array([list(map(lambda z: mapping[z], x)) for x in image.splitlines()], np.uint8)
void = 0

for i in range(50):
    image, void = enhance(lut, image, void)

d20p2 = image.sum()
print(f'Day 20 Part 2: {d20p2}')