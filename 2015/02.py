with open("02.txt") as f:
    l = [x.strip() for x in f.readlines()]

    tt = 0
    rr = 0
    for x in l:
        y = [int(y) for y in x.split("x")]
        #print(y)
        a =  y[0] * y[1]
        b =  y[1] * y[2]
        c =  y[2] * y[0]
        m,n,o = y
        t = min(a,b,c) + 2*(a+b+c)
        r = 2*(m+n+o) - 2*max(m,n,o) + m*n*o
        tt += t
        rr += r

    print(tt,rr)