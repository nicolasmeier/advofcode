import os
import sys
import collections 


os.chdir(os.path.dirname(sys.argv[0]))
li = []
with open("14.txt") as f:
    li = [x.strip() for x in f.readlines()]

res = li[0]
rep = dict()
for l in li[2:]:
    y,z = l.split(" -> ")
    rep[y] = z

word = dict()
for j in range(len(res)-1):
    x = res[j:j+2]
    if x in word:
        word[x] += 1
    else:
        word[x] = 1

print(word)

for i in range(41):
    n = dict()
    for k,v in word.items():
        a = k[0]+rep[k]
        b = rep[k]+k[1]
        if a in n:
            n[a] += v
        else:
            n[a] = v
        if b in n:
            n[b] += v
        else:
            n[b] = v
    word = n
    if i in [9,39]:
        CF = collections.Counter()
        for k in word:
            CF[k[0]] += word[k]
        CF[res[-1]] += 1
        print(max(CF.values())-min(CF.values()))
        