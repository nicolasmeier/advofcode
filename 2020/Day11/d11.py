with open("Day11/input.txt", "r") as f:
    l = f.read().splitlines()

def getNeighbors(lay,i,j):
    neig = []
    mini = i-1
    maxi = i+1
    minj = j-1
    maxj = j+1
    if (i == 0):
        mini = 0
    elif (i == len(lay)-1):
        maxi = i
    if (j == 0):
        minj = 0
    elif (j == len(lay[i])-1):
        maxj = j
    for a in range(mini,maxi + 1):
        for b in range(minj,maxj + 1):
            if not (a == i and b == j):
                if (lay[a][b] == "#"):
                    neig.append(lay[a][b])
    return neig


def roun(layout):
    ret = layout.copy()
    for i in range(len(layout)):
        newline = ""
        for j in range(len(layout[i])):
            if not layout[i][j] == ".":
                n = getNeighbors(layout,i,j)
                if layout[i][j] == "L":
                    if (len(n) == 0):
                        newline += "#"
                    else:
                        newline += "L"
                elif layout[i][j] == "#":
                    if len(n) >= 4:
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
    l = roun(l.copy()).copy()
    c += 1

#print(l)
#print(c)
bes = 0
for k in l:
    bes += k.count("#")

print(bes)    