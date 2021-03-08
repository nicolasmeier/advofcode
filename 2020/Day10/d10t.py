with open("Day10/input.txt", "r") as f:
    l = f.read().splitlines()
    l = map(int,l)
    l = list(l)
    l.append(0)
    l.append(max(l) + 3)
    l.sort(reverse=True)

lmax = max(l)
v = {}

def test(i):
    if i not in l:
        return 0
    if i == lmax:
        return 1;
    pos = 0
    if (i + 1) in v.keys():
        pos += v[i+1]
    if (i + 2) in v.keys():
        pos += v[i+2]
    if (i + 3) in v.keys():
        pos += v[i+3]
    return pos;

for j in l:
    v[j] = test(j)

print(v)
print(v.values())
print(max(v.values()))
    