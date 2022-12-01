import os
import sys
import browser_cookie3
import requests
import time


def get_leaderboard():
    os.chdir(os.path.dirname(sys.argv[0]))

    delta = 0
    with open("last-request.txt", "r") as l:
        lastrequest = int(l.read())
        delta = int(time.time()) - lastrequest

    if delta > 15 * 60:
        # Get cookies from the browser
        cookies = browser_cookie3.firefox()

        r = requests.get("https://adventofcode.com/2022/leaderboard/private/view/1483124.json", allow_redirects=False,
                         cookies=cookies)

        open("leaderboard.json", 'wb').write(r.content)
        open("last-request.txt", "w").write(str(int(time.time())))


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    get_leaderboard()
