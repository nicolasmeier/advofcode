def house(x,y):
    return f"n{x}e{y}"

def add(h,x,y):
    hn = house(x,y)
    if hn in h:
        h[hn] += 1
    else:
        h[hn] = 1

with open("03.txt") as f:
    l = [x.strip() for x in f.readlines()]
    l = l[0]
    #print(l)

    #l = "^>v<"
    robo = False
    h = dict()
    x,y = 0,0
    m,n = 0,0
    add(h,x,y)
    for i in l:
        if robo:
            #print(i)
            if i == ">":
                m += 1
            elif i == "<":
                m -= 1
            elif i == "^":
                n += 1
            elif i == "v":
                n -= 1
            add(h,m,n)
            robo = False
        else:
            #print(i)
            if i == ">":
                x += 1
            elif i == "<":
                x -= 1
            elif i == "^":
                y += 1
            elif i == "v":
                y -= 1
            add(h,x,y)
            robo = True
            
    mt1 = 0
    for v in h.values():
        if v >= 1:
            mt1 += 1


    print(h)
    print(mt1)
    print(len(h))
