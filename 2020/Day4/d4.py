f = open("Day4/input.txt", "r")
byr = -1
iyr = -1
eyr = -1
hcl = -1
hgt = -1
ecl = -1
pid = -1

valid = 0

for l in f:
    if l == "\n":
        if min(byr,iyr,eyr,hcl,hgt,ecl,pid) > -1:
            valid += 1
        byr = -1
        iyr = -1
        eyr = -1
        hcl = -1
        hgt = -1
        ecl = -1
        pid = -1
    else:
        byr = max(l.find("byr:"),byr) 
        iyr = max(l.find("iyr:"),iyr)
        eyr = max(l.find("eyr:"),eyr)
        hgt = max(l.find("hgt:"),hgt)
        hcl = max(l.find("hcl:"),hcl)
        ecl = max(l.find("ecl:"),ecl)
        pid = max(l.find("pid:"),pid)
        

print(valid)
    