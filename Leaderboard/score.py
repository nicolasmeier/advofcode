import json
import os
import sys
from datetime import datetime

import pandas as pd

os.chdir(os.path.dirname(sys.argv[0]))
import leaderboardapi as leaderboardapi

leaderboardapi.getLeaderboard()

PLOT_QUALITY = 240 * 1
markers = ['o', 'x', '+', 'v', '^', '<', '>', 's', 'd', 'p']

lastupdated = datetime.today().strftime('Last updated at %H:%M %d.%m.')
currentday = int(datetime.today().strftime('%d'))

j = ""
with open("leaderboard.json") as f:
    l = f.read()
j = json.loads(l)
year = int(j['event'])

members = []
for i in j['members']:
    members.append(dict(j['members'][i]))

days = range(1, 26)
usertimes = dict()
userscore = dict()
for m in members:
    username = m["name"]
    localscore = m["local_score"]
    userscore[username] = localscore
    time = dict()
    completion_day = dict(m["completion_day_level"])
    for d in completion_day:
        r = dict(completion_day[str(d)])
        star = "1"
        if "1" in r.keys():
            star = "1"
            st = datetime.utcfromtimestamp(r[star]["get_star_ts"]).strftime('%Y:%m:%d:%H:%M:%S')
            jahr, month, day, h, m, s = [int(y) for y in st.split(":")]
            if month == 12 and jahr == year:
                h = h - 5
                day = day - int(d)
                t = s + m * 60 + h * 60 * 60 + day * 60 * 60 * 24
                time[f"{int(d)}-1"] = t
        star = "1"
        if "2" in r.keys():
            star = "2"
            st = datetime.utcfromtimestamp(r[star]["get_star_ts"]).strftime('%Y:%m:%d:%H:%M:%S')
            jahr, month, day, h, m, s = [int(y) for y in st.split(":")]
            if month == 12 and jahr == year:
                h = h - 5
                day = day - int(d)
                t = s + m * 60 + h * 60 * 60 + day * 60 * 60 * 24
                time[f"{int(d)}-2"] = t
    usertimes[username] = time

table = []
cols = ["username"]
for d in days:
    cols.append(f"day{d}-1")
    cols.append(f"day{d}-2")
cols.append("localscore")
for k, time in usertimes.items():
    row = []
    row.append(k)
    for d in days:

        if f"{d}-1" in time.keys():
            row.append(time[f"{d}-1"])
        else:
            row.append(0)
        if f"{d}-2" in time.keys():
            row.append(time[f"{d}-2"])
        else:
            row.append(0)
    # Score
    row.append(userscore[k])
    table.append(row)

df = pd.DataFrame(table, columns=cols)
df = df.sort_values("localscore", ascending=False)
# print(df)

df.to_excel("Advent-of-Code-Data/times.xlsx")

# Rankings

userrank = dict()
for n in usertimes.keys():
    userrank[n] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for d in range(1, 26):
    # print(d)
    ds = df[df[f"day{d}-1"] > 0]
    ds = ds.sort_values(f"day{d}-1", ascending=True)
    r = 56
    # 1 0 2 2 3 4 4 6
    for n in ds["username"]:
        userrank[n][(d - 1) * 2] = r
        r -= 1

    ds = df[df[f"day{d}-1"] == 0]
    for n in ds["username"]:
        q = 0
        userrank[n][(d - 1) * 2] = r
    ds = df[df[f"day{d}-2"] > 0]
    ds = ds.sort_values(f"day{d}-2", ascending=True)
    r = 56
    for n in ds["username"]:
        userrank[n][(d - 1) * 2 + 1] = r
        r -= 1

    ds = df[df[f"day{d}-2"] == 0]
    for n in ds["username"]:
        q = 0
        userrank[n][(d - 1) * 2 + 1] = r


def intstr(i: int) -> str:
    if i == 0:
        return ""
    return str(i)


rankdata = []
for k, v in userrank.items():
    if sum(v) > 0:
        row = [k]
        [row.append(intstr(x)) for x in v]
        rankdata.append(row)
# print(rankdata)
cols = ["username"]
for d in days:
    cols.append(f"{d}-1")
    cols.append(f"{d}-2")
rf = pd.DataFrame(rankdata, columns=cols)
rf = rf.sort_values("username")
print(rf)
rf.to_excel("Advent-of-Code-Data/rankings.xlsx")

# print("Done")
