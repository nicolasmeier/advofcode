import os
import sys
import re
import numpy as np
import math
import functools
os.chdir(os.path.dirname(sys.argv[0]))

x1,y1 = 9,7
x2,y2 = 7,9
xstep = int((x2-x1)/abs((x2-x1)))
ystep = int((y2-y1)/abs((y2-y1)))
x,y = x1,y1
for i in range(abs((y2-y1))+1):
    xx = x + xstep*i
    yy = y + ystep*i
    print(f"{xx},{yy}")

