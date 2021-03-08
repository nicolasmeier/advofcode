
with open("Day12/input.txt", "r") as f:
    l = f.read().splitlines()
facing = 1
facing_dir = ["N","E","S","W"]
px = 0
py = 0
for i in l:
    d = i[0].upper()
    x = int(i[1:])
    #print(d,x)
    if d == "N":
        py += x
    elif d == "S":
        py -= x
    elif d == "E":
        px += x
    elif d == "W":
        px -= x
    elif d == "L":
        facing = int(facing - x/90) % len(facing_dir)
    elif d == "R":
        facing = int(facing + x/90) % len(facing_dir)
    elif d == "F":
        #print(f"facing: {facing_dir[facing]}")
        if facing == 0:
            py += x
        elif facing == 2:
            py -= x
        elif facing == 1:
            px += x
        elif facing == 3:
            px -= x

 
print(f"east {px}, north {py}")
print(f"manhattan dist {abs(px) + abs(py)}")
