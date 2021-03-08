import re
with open("Day19/input.txt", "r") as f:
    l = f.read().splitlines()
i = l.index('')
ru = l[:i]
m = l[i+1:]

rules = {}
for r in ru:
    s = r.split(":",1)
    rules[int(s[0])] = s[1].strip()

rules[8] = "42 | 42 8"
rules[11] = "42 31 | 42 11 31"

def rulz(p,d):
    if d > 100:
        return ""
    p = str(p)
    res = ""
    for x in p.split(" "):
        if x.startswith('"'):
            res += x[1:-1]
        elif x == "|":
            res += x
        elif x.isalnum():
            r = rules[int(x)]
            if p == r:
                res += rulz(r,d+1)
            else:
                res += rulz(r,0)
    if res.count("|") > 0:
        res = "(" + res + ")"
    return res

mastarule = "^"+rulz(rules[0],0)+"$"

for r in rules.keys():
    print(r,":",rules[r])

print(mastarule)
valid = 0
for n in m:
    x = re.match(mastarule,n)
    if x:
        valid += 1
        print(n,"valid")

print(valid)
