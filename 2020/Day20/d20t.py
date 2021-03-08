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
#print(p[0][0] *p[di][0] *p[0][di] *p[di][di])
#print(pt)

def removeborders(t):
    res = []
    for i in range(1,len(t)-1):
        res.append(t[i][1:-1])
    return res

def oneimage(pt):
    d = dim * 8
    image = []
    for i in range(d):
        image.append("")
    for x in range(dim):
        for y in range(dim):
            b = removeborders(pt[x][y])
            for xx in range(8):
                image[x*8+xx] += b[xx]
    return image

image = oneimage(pt)
#printtile(image)

monster = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]

monre = []
for m in monster:
    monre.append(m.replace(" ","."))

print("x"*10)
print(monre)
print("x"*10)

for i in range(8):
    im = fl(image,i)
    f = 0
    for i in range(len(im)-2):
        s = 0
        m = re.search(monre[0],im[i])
        while m:
            [b,e] = m.span()
            b = b+s
            e = e+s
            m2 = re.search(monre[1],im[i+1][b:e])
            if m2:
                m3 = re.search(monre[2],im[i+2][b:e])
                if m3:
                    f += 1
                    s1 = im[i][:b]
                    s2 = im[i+1][:b]
                    s3 = im[i+2][:b]
                    for j in range(len(monster[0])):
                        if monster[0][j] == "#":
                            s1 += "O"
                        else:
                            s1 += im[i][b+j]
                        if monster[1][j] == "#":
                            s2 += "O"
                        else:
                            s2 += im[i+1][b+j]
                        if monster[2][j] == "#":
                            s3 += "O"
                        else:
                            s3 += im[i+2][b+j]
                    im[i] = s1 + im[i][e:]
                    im[i+1] = s2 + im[i+1][e:]
                    im[i+2] = s3 + im[i+2][e:]
                    """
                    print(im[i],i)
                    print(im[i+1][b-1:e+1])
                    print(len(im[i+1][b-1:e+1]))
                    print("found",i)
                    """
            [s,e] = [s+1,len(im[i])]
            m = re.search(monre[0],im[i][s:e])
            #print(s,e,m)
    print(f)
    if f > 0:
        printtile(im)
        cnt = 0
        for i in im:
            cnt += str(i).count("#")
        print(f"count: {cnt}")

