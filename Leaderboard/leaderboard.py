import json
import matplotlib.pyplot as plt
import os
import sys
import numpy as np
import pandas as pd
from datetime import datetime
import time
import leaderboardapi

os.chdir(os.path.dirname(sys.argv[0]))
leaderboardapi.get_leaderboard()

PLOT_QUALITY = 240 * 1
markers = ['o', 'x', '+', 'v', '^', '<', '>', 's', 'd', 'p']

lastupdated = datetime.today().strftime('Last updated at %H:%M %d.%m.')
currentday = int(datetime.today().strftime('%d'))
currentday = 25

j = ""
with open("leaderboard.json") as f:
    l = f.read()
j = json.loads(l)
year = int(j['event'])

members = []
for i in j['members']:
    members.append(dict(j['members'][i]))

from datetime import datetime

days = range(1, 26)
usernames = []
data = dict()
for m in members:
    usernames.append(m["name"])
    time = dict()
    completion_day = dict(m["completion_day_level"])
    for d in completion_day:
        r = dict(completion_day[str(d)])
        star = "1"
        if "2" in r.keys():
            star = "2"
            st = datetime.utcfromtimestamp(r[star]["get_star_ts"]).strftime('%m:%d:%H:%M:%S')
            month, day, h, m, s = [int(y) for y in st.split(":")]
            if month == 12:
                h = h - 5
                day = day - int(d)
                t = s + m * 60 + h * 60 * 60 + day * 60 * 60 * 24
                time[int(d)] = t
    speed = []
    for day in days:
        if day in time.keys():
            speed.append(time[day])
        else:
            speed.append(0)

    if len(speed) > 0:
        data[usernames[-1]] = speed
    else:
        usernames.pop()

fig = plt.figure(figsize=(16, 12), dpi=PLOT_QUALITY)
ax = fig.add_subplot(111)
plt.grid(axis="y")
plt.title(f"Advent of Code {year} Time to solve")
cm = plt.get_cmap('tab20')
ax.set_prop_cycle(color=[cm(1. * i / 20) for i in range(20)])
maxtime = 0
m = 0
for un, speed in data.items():
    maxtime = max(maxtime, max(speed))
    if sum(speed) > 0:
        speedmasked = np.ma.array(speed)
        for i in range(len(speed)):
            if speed[i] == 0:
                speedmasked[i] = np.ma.masked
        ax.plot(days[:currentday], speedmasked[:currentday], f":{markers[m]}", label=un)
        m = (m + 1) % 9
# plt.legend(usernames)

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel("Day")
plt.ylabel("Time to Solve in s")
plt.xticks(days[:currentday])
plt.xlim(0, currentday + 1)
plt.yscale("log")
plt.savefig("Advent-of-Code-Data/leaderboardlog.png")
plt.yscale("linear")
plt.xticks(days[:currentday])
plt.xlim(0, currentday + 1)
plt.ylim(-20, maxtime + 600)
plt.savefig("Advent-of-Code-Data/leaderboard.png")

ylabel = ["Start", "10min", "30min"]
ylabelvalue = [0, 600, 60 * 30]
for i in range(11):
    ylabel.append(f"{i}h")
    ylabelvalue.append(i * 3600)
plt.yticks(ylabelvalue, ylabel)
plt.ylim(-20, 2 * 3600)
plt.savefig("Advent-of-Code-Data/leaderboard2h.png")
plt.ylim(-20, 3600)
plt.savefig("Advent-of-Code-Data/leaderboard1h.png")

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
        if "2" in r.keys():
            star = "2"
            st = datetime.utcfromtimestamp(r[star]["get_star_ts"]).strftime('%Y:%m:%d:%H:%M:%S')
            jahr, month, day, h, m, s = [int(y) for y in st.split(":")]
            if month == 12 and jahr == year:
                h = h - 5
                day = day - int(d)
                t = s + m * 60 + h * 60 * 60 + day * 60 * 60 * 24
                time[int(d)] = t
    usertimes[username] = time

table = []
cols = ["username"]
for d in days:
    cols.append(f"day{d}")
cols.append("localscore")
for k, time in usertimes.items():
    row = []
    row.append(k)
    for d in days:

        if d in time.keys():
            row.append(time[d])
        else:
            row.append(0)
    # Score
    row.append(userscore[k])
    table.append(row)

df = pd.DataFrame(table, columns=cols)
df = df.sort_values("localscore", ascending=False)
# print(df)
df.to_markdown("Advent-of-Code-Data/tts.md")
df.to_markdown("Advent-of-Code-Data/tts.md")
df.to_csv("Advent-of-Code-Data/tts.csv")
# df.to_excel("Advent-of-Code-Data/tts.xlsx")

# Rankings

userrank = dict()
for n in usertimes.keys():
    userrank[n] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for d in range(1, currentday + 1):
    ds = df[df[f"day{d}"] > 0]
    ds = ds.sort_values(f"day{d}", ascending=True)
    r = 1
    for n in ds["username"]:
        userrank[n][d - 1] = r
        r += 1

fig = plt.figure(figsize=(16, 12), dpi=PLOT_QUALITY)
ax = fig.add_subplot(111)
plt.grid(axis="y")
plt.title(f"Advent of Code {year} Rankings")
numofranks = sum([1 for x in list(userrank.values()) if sum(x) >= 1])
cm = plt.get_cmap('tab20')
ax.set_prop_cycle(color=[cm(1. * i / 20) for i in range(20)])

m = 0
for n, r in userrank.items():
    if sum(r) > 0:
        rmasked = np.ma.array(r)
        for i in range(len(r)):
            if r[i] == 0:
                rmasked[i] = np.ma.masked
        ax.plot(days[:currentday], rmasked[:currentday], f":{markers[m]}", label=n)
        m = (m + 1) % 9
        # plt.plot(days,r,":")

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel("Day")
plt.xlim(0, currentday + 1)
plt.ylabel("Rank")
plt.ylim(0, numofranks + 1)
plt.xticks(days[:currentday])
plt.yticks(range(1, numofranks + 1))
plt.savefig("Advent-of-Code-Data/rankings.png")


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
[cols.append(f"{d}") for d in days]
rf = pd.DataFrame(rankdata, columns=cols)
rf = rf.sort_values("username")
# print(rf)
rf.to_markdown("Advent-of-Code-Data/rankings.md")
rf.to_markdown("Advent-of-Code-Data/rankings.md")
rf.to_csv("Advent-of-Code-Data/rankings.csv")
# rf.to_excel("Advent-of-Code-Data/rankings.xlsx")

# print("Done")
