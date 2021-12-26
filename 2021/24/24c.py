modelnr = "13579246899999"

def check(modelnr:str):
    if "0" in modelnr:
        return False
    v = dict()
    for c in range(len(modelnr)):
        v[c+1] = int(modelnr[c])

    x,y,z = 0,0,0

    w = v[1]
    z = w + 15
    w = v[2]
    z *= 26
    z += w + 10
    w = v[3]
    z *= 26
    z += w + 2
    w = v[4]
    x = 1
    z *= 26
    y = 0
    y += 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 16
    y *= x
    z += y
    w = v[5]
    x = 0
    x += z
    x = x %  26
    z /= 26
    x += -12
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 12
    y *= x
    z += y
    w = v[6]
    x = 0
    x += z
    x = x %  26
    z /= 1
    x += 10
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 11
    y *= x
    z += y
    w = v[7]
    x = 0
    x += z
    x = x %  26
    z /= 26
    x += -9
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    x += 5
    y *= x
    z += y
    w = v[8]
    x = 0
    x += z
    x = x %  26
    z /= 1
    x += 14
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 16
    y *= x
    z += y
    w = v[9]
    x = 0
    x += z
    x = x %  26
    z /= 1
    x += 13
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    x += 6
    y *= x
    z += y
    w = v[10]
    x = 0
    x += z
    x = x %  26
    z /= 26
    x += -14
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 15
    y *= x
    z += y
    w = v[11]
    x = 0
    x += z
    x = x %  26
    z /= 26
    x += -11
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    x += 3
    y *= x
    z += y
    w = v[12]
    x = 0
    x += z
    x = x %  26
    z /= 26
    x += -2
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 12
    y *= x
    z += y
    w = v[13]
    x = 0
    x += z
    x = x %  26
    z /= 26
    x += -16
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = 0
    y += w
    y += 10
    y *= x
    z += y
    w = v[14]
    x = 0
    x += z
    x = x %  26
    z /= 26
    x += -14
    if x != w:
        x = 1
    else:
        x = 0
    y = 25
    y *= x
    y += 1
    z *= y
    y = w + 13
    y *= x
    z += y
    return z == 0

for i in range(99999999999999,0,-1):
    if check(str(i)):
        print(i)
        quit()
        q = 0
    if i % 10000000 == 0:
        print(f"weitere {i}")