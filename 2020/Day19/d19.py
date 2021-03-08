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

def rulz(p):
    p = str(p)
    res = ""
    for x in p.split(" "):
        if x.startswith('"'):
            res += x[1:-1]
        elif x == "|":
            res += x
        elif x.isalnum():
            res += rulz(rules[int(x)])
    if res.count("|") > 0:
        res = "(" + res + ")"
    return res

mastarule = "^"+rulz(rules[0])+"$"

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
