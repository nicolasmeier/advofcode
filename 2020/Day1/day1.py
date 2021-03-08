f = open("Day1/input.txt", "r")
for x in f:
    fy = open("Day1/input.txt", "r")
    for y in fy:
        if (int(x) + int(y) == 2020):
            print(f"{int(x)} * {int(y)} = {int(x) * int(y)}")

