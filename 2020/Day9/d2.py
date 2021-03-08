with open("Day9/input.txt", "r") as f:
    l = f.read().splitlines()
    l = map(int,l)
    l = list(l)
preamble = 25
for i in range(len(l)):
    pre = l[:i]
    pre = pre[-preamble:]
    s = False
    if i > preamble:
        for j in range(len(pre)):
            for k in range(j+1,len(pre)):
                #print(pre[j] , pre[k], pre[j] + pre[k], l[i])
                if (pre[j] + pre[k] == l[i]):
                    #print(pre[j] , pre[k])
                    s = True
        
        if not s:
            print(l[i])
            b = l[:i]
            for j in range(len(b)):
                su = 0
                for k in range(j,len(b)):
                    su += b[k]
                    if su == l[i]:
                        c = b[j:k+1]

                        print(min(c),max(c),min(c)+max(c))
                    elif su > l[i]:
                        pass
        



    