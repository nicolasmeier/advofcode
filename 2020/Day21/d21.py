import re
import math
with open("Day21/input.txt", "r") as f:
    l = f.read().splitlines()

ingr = {}
allergens = {}

for j in l:
    x = j.split("(")
    y = x[0].strip().split(" ")
    i = set()
    for z in y:
        i.add(z)
        if ingr.get(z):
            ingr[z] += 1
        else:
            ingr[z] = 1
    a = x[1].strip()[9:-1].split(",")
    for b in a:
        b = b.strip()
        if allergens.get(b):
            allergens[b] = i.intersection(allergens[b])
        else:
            allergens[b] = i

#print(allergens)

def removeexcept(k,val):
    rem = set()
    rem.add(val)
    for a in allergens.keys():
        if k != a:
            allergens[a] = set(allergens[a]).difference(rem)

for i in range(len(allergens)):
    for k in allergens.keys():
        if len(allergens[k]) == 1:
            removeexcept(k,set(allergens[k]).copy().pop())
        

#print(allergens)

allergen_ingr = set()
for a in allergens.values():
    allergen_ingr = allergen_ingr.union(a)
    
non_allergen = set(ingr.keys()).difference(allergen_ingr)

#print(non_allergen)
sumnon = 0
for n in non_allergen:
    sumnon += ingr[n]

print("part 1:",sumnon)

print("part 2:")
ak = list(allergens.keys())
ak.sort()
p2 = ""
for k in ak:
    p2 += allergens[k].pop() + ","
p2 = p2[:-1]
print(p2)