import re


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
        l = l.strip();
        byri = l.find("byr:") 
        iyri = l.find("iyr:")
        eyri = l.find("eyr:")
        hgti = l.find("hgt:")
        hcli = l.find("hcl:")
        ecli = l.find("ecl:")
        pidi = l.find("pid:")
        if byri > -1:
            if (1920 <= int(l[byri+4:].split(" ")[0]) <= 2002):
                byr = 1
        if iyri > -1:
            if (2010 <= int(l[iyri+4:].split(" ")[0]) <= 2020):
                iyr = 1
        if eyri > -1:
            if (2020 <= int(l[eyri+4:].split(" ")[0]) <= 2030):
                eyr = 1
        if hgti > -1:
            h = l[hgti+4:].split(" ")[0]
            if h.endswith("cm"):
                if (150 <= int(h[:-2]) <= 193):
                    hgt = 1
            elif h.endswith("in"):
                if (59 <= int(h[:-2]) <= 76):
                    hgt = 1
        if hcli > -1:
            h = l[hcli+4:].split(" ")[0]
            x = re.search("^#[0-9a-f]{6}$",h)
            if x:
                hcl = 1
        if ecli > -1:
            h = l[ecli+4:].split(" ")[0]
            if (h == "amb" or
                h == "blu" or
                h == "brn" or
                h == "gry" or
                h == "grn" or
                h == "hzl" or
                h == "oth"):
                ecl = 1
        if pidi > -1:
            h = l[pidi+4:].split(" ")[0]
            x = re.search("^[0-9]{9}$",h)
            if x:
                pid = 1
            
        

print(valid)
    