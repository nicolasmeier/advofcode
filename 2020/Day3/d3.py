f = open("Day3/input.txt", "r")
m = f.readlines()
n = len(m[0]) - 1
x = 0
y = 0
res =1

d = 1
x = 0
y = 0
count = 0
while y < len(m):
    if m[y][x] == "#":
        count += 1
    y += 1
    x = (x + d)%n
print(count)
res = res * count

d = 3
x = 0
y = 0
count = 0
while y < len(m):
    if m[y][x] == "#":
        count += 1
    y += 1
    x = (x + d)%n
print(count)
res = res * count


d = 5
x = 0
y = 0
count = 0
while y < len(m):
    if m[y][x] == "#":
        count += 1
    y += 1
    x = (x + d)%n
print(count)
res = res * count

d = 7
x = 0
y = 0
count = 0
while y < len(m):
    if m[y][x] == "#":
        count += 1
    y += 1
    x = (x + d)%n
print(count)
res = res * count


d = 1
x = 0
y = 0
count = 0
while y < len(m):
    if m[y][x] == "#":
        count += 1
    y += 2
    x = (x + d)%n
print(count)
res = res * count

print(res)
