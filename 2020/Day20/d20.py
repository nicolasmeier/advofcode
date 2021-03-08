import re
import math
with open("Day20/input.txt", "r") as f:
    l = f.read().splitlines()

tiles = {}
tile = []
tilenr = -1
for j in l:
    if j.startswith("Tile"):
        if tilenr > 0:
            tiles[tilenr] = tile
        tilenr = int(j[5:-1])
        tile = []
    else:
        if not j == "":
            tile.append(j.strip())
tiles[tilenr] = tile

dim = int(math.sqrt(len(tiles)))

# ---------------------------------

def printtile(tile):
    for r in tile:
        print(r)

def fliph(til):
    til = list(til)
    til.reverse()
    return til

def flipv(til):
    res = []
    for t in til:
        res.append(str(t)[::-1])
    til = res
    return res

def rot(til):
    res = []
    for i in range(len(til)):
        res.append("")
    for t in til:
        for i in range(len(t)):
            res[i] += t[i]
    return res

def fl(t,i):
    t = t.copy()
    if i == 0:
        return t
    if i == 1:
        return fliph(t)
    if i == 2:
        return flipv(t)
    if i == 3:
        return flipv(fliph(t))
    if i == 4:
        return rot(t)
    if i == 5:
        return fliph(rot(t))
    if i == 6:
        return flipv(rot(t))
    if i == 7:
        return flipv(fliph(rot(t)))

def getboarder(border,tile):
    if not tile:
        return ""
    border = str(border).upper()
    tile = list(tile)
    if border == "TOP":
        return tile[0]
    if border == "BOTTOM":
        return tile[-1]
    if border == "LEFT":
        r = ""
        for t in tile:
            r += t[0]
        return r
    if border == "RIGHT":
        r = ""
        for t in tile:
            r += t[-1]
        return r

def getdef(p,x,y):
    if p.get(x):
        if p.get(x).get(y):
            return p.get(x).get(y)
    return

def aslist(p):
    r = []
    for x in p.values():
        for y in x.values():
            r.append(y)
    return r

def constructimage(pic,pict,l):
    if l == dim * dim:
        return [pic,pict]
    pic = pic.copy()
    pict = pict.copy()
    row = int(l/dim)
    col = int(l % dim)
    #print(pic)
    tb = getboarder("BOTTOM",getdef(pict,row-1,col))
    lb = getboarder("RIGHT",getdef(pict,row,col-1))
    for k in tiles.keys():
        if not k in aslist(pic):
            for i in range(8):
                ti = fl(tiles[k],i)
                leftmatch = False
                topmatch = False
                if tb == "":
                    topmatch = True
                else:
                    if tb == getboarder("TOP",ti):
                        topmatch = True
                if lb == "":
                    leftmatch = True
                else:
                    if lb == getboarder("LEFT",ti):
                        leftmatch = True
                if leftmatch and topmatch:
                    pic[row][col] = k
                    pict[row][col] = ti
                    c = constructimage(pic,pict,l+1)
                    if c:
                        return c
                    pic[row][col] = -1
                    pict[row][col] = []
    return
"""
test = ["123","456","789"]
for i in range(8):
    printtile(fl(test,i))
    print("-"*4)
"""


pic = {}
pict = {}
for i in range(dim):
    pic[i] = {}
    pict[i] = {}

def findimg():
    for k in tiles.keys():
        for i in range(8):
            pic[0][0] = k
            pict[0][0] = fl(tiles[k],i)
            c = constructimage(pic,pict,1)
            if c:
                return c
            for i in range(dim):
                pic[i] = {}
                pict[i] = {}
            
[p, pt] = findimg()
di = dim-1
print(p[0][0] *p[di][0] *p[0][di] *p[di][di])
exit()
t = tiles.get(1951)
printtile(t)
print()
print(getboarder("TOP",t))
print(getboarder("BOTTOM",t))
print(getboarder("LEFT",t))
print(getboarder("RIGHT",t))


