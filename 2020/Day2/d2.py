f = open("Day2/input.txt", "r")
count = 0
for l in f:
    s = l.split("-")
    z = s[1].split(":")
    #print(z)
    min = int(s[0])
    max = int(z[0].split(" ")[0])
    ch = z[0].split(" ")[1]
    pw = z[1]
    c = pw.count(ch)
    if c == "n":
        print(pw,c)
    if (min <= c and c <= max):
        count += 1

print(count)
