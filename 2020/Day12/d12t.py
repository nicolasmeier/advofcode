
with open("Day12/input.txt", "r") as f:
    l = f.read().splitlines()

px = 0
py = 0
wx = 10
wy = 1

def rotr(a,wx,wy):
    for i in range(a):
        tmp = wx
        wx = wy
        wy = -tmp
    return [wx,wy]

for i in l:
    d = i[0].upper()
    x = int(i[1:])
    print(d,x)
    if d == "N":
        wy += x
    elif d == "S":
        wy -= x
    elif d == "E":
        wx += x
    elif d == "W":
        wx -= x
    elif d == "L":
        rot = int(x/90) % 4
        [wx,wy] = rotr(4 - rot,wx,wy)
    elif d == "R":
        rot = int(x/90) % 4
        [wx,wy] = rotr(rot,wx,wy)
    elif d == "F":
        print(f"waypoint east {wx}, north {wy}")
        px += x * wx
        py += x * wy
    print(f"east {px}, north {py}")

 
print(f"manhattan dist {abs(px) + abs(py)}")
print(f"east {px}, north {py}")
