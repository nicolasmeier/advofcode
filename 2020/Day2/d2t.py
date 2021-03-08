f = open("Day2/input.txt", "r")
count = 0
for l in f:
    l = l.splitlines(False)[0]
    #print(l)
    s = l.split("-")
    z = s[1].split(":")
    #print(z)
    min = int(s[0])
    max = int(z[0].split(" ")[0])
    ch = z[0].split(" ")[1]
    pw = z[1].strip()
    a = pw[min-1]
    b = pw[max-1]
    #print(pw,ch,a,b)
    if ((ch == a) != (ch == b)):
        count += 1

print(count)
