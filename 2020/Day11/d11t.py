with open("Day11/input.txt", "r") as f:
    l = f.read().splitlines()


maxx = len(l)-1
maxy = len(l[0])-1

def inside(x,y):
    return (0 <= x <= maxx and 0 <= y <= maxy )

def getNeighbors(lay,i,j):
    m = max(maxx,maxy)
    r = range(1,m)
    neig = []
    # -------------------------------------
    for a in r:
        if inside(i-a,j):
            c = lay[i-a][j]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    # -------------------------------------
    for a in r:
        if inside(i+a,j):
            c = lay[i+a][j]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    # -------------------------------------
    for a in r:
        if inside(i,j-a):
            c = lay[i][j-a]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    # -------------------------------------
    for a in r:
        if inside(i,j+a):
            c = lay[i][j+a]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    # -------------------------------------
    for a in r:
        if inside(i-a,j-a):
            c = lay[i-a][j-a]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    # -------------------------------------
    for a in r:
        if inside(i-a,j+a):
            c = lay[i-a][j+a]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    # -------------------------------------
    for a in r:
        if inside(i+a,j-a):
            c = lay[i+a][j-a]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    # -------------------------------------
    for a in r:
        if inside(i+a,j+a):
            c = lay[i+a][j+a]
            if (c == "#"):
                neig.append(c)
                break
            elif (c == "L"):
                break
        else:
            break
    return neig


def roun(layout):
    ret = layout.copy()
    for i in range(len(layout)):
        newline = ""
        for j in range(len(layout[i])):
            if not layout[i][j] == ".":
                n = getNeighbors(layout,i,j)
                #print(n)
                if layout[i][j] == "L":
                    if (len(n) == 0):
                        newline += "#"
                    else:
                        newline += "L"
                elif layout[i][j] == "#":
                    if len(n) >= 5:
                        newline += "L"
                    else:
                        newline += "#"
            else:
                newline += "."
        ret[i] = newline
    return ret
last = []
c = 0

while last != l:
    last = l.copy()
    l = roun(l)
    c += 1

#roun(l)

#print(l)
#print(c)
bes = 0
for k in l:
    bes += k.count("#")

print(bes)    