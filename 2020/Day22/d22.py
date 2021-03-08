with open("Day22/input.txt", "r") as f:
    l = f.read().splitlines()

p1c = []
p2c = []
pc = p1c
for j in l:
    j = j.strip()
    if j == "Player 1:":
        pc = p1c
    elif j == "Player 2:":
        pc = p2c
    elif j != "":
        pc.append(int(j))

"""
xprint = print
def nothing(*val: object):
    zzz = 0
print = nothing
"""



def playgame(gameg: int,p1c: list,p2c: list):
    prevgames = []
    game = gameg
    #print(f"=== Game {game} ===")
    round = 0
    while len(p1c) > 0 and len(p2c) > 0:
        round += 1
        p1win, p2win = False,False
        """
        print(f"\n-- Round {round} (Game {game}) --")
        print(f"Player 1's deck: {str(p1c)[1:-1]}")
        print(f"Player 2's deck: {str(p2c)[1:-1]}")
        """
        h = str(p1c)+"::"+str(p2c)
        if h in prevgames:
            for c in p2c:
                p1c.append(c)
            p2c.clear()
            return [gameg,p1c,p2c]
        prevgames.append(h)
        c1 = p1c.pop(0)
        c2 = p2c.pop(0)
        """
        print(f"Player 1 plays: {c1}")
        print(f"Player 2 plays: {c2}")
        """
        if len(p1c) >= c1 and len(p2c) >= c2:
            # play recursive 
            #print("Playing a sub-game to determine the winner...\n")
            sub1 = p1c.copy()
            for i in range(len(sub1)-c1):
                sub1.pop()
            sub2 = p2c.copy()
            for i in range(len(sub2)-c2):
                sub2.pop()
            gameg += 1
            [g,a,b] = playgame(gameg,sub1,sub2)
            if len(a) == 0:
                p2win = True
                #print(f"The winner of game {gameg} is player 2!\n\n...anyway, back to game {game}.")
            else:
                p1win = True
                #print(f"The winner of game {gameg} is player 1!\n\n...anyway, back to game {game}.")
            gameg = g

        if p1win or (not p2win and c1 > c2):
            p1win = False
            #print(f"Player 1 wins round {round} of game {game}!")
            p1c.append(c1)
            p1c.append(c2)
        elif p2win or (not p1win and c2 > c1):
            p2win = False
            #print(f"Player 2 wins round {round} of game {game}!")
            p2c.append(c2)
            p2c.append(c1)
    return [gameg,p1c,p2c]


[x,p1c,p2c] = playgame(1,p1c,p2c)


if len(p1c) == 0:
    windeck = p2c
    print("The winner of game 1 is player 2!\n\n")
else:
    windeck = p1c
    print("The winner of game 1 is player 1!\n\n")

print(f"== Post-game results ==")
print(f"Player 1's deck: {str(p1c)[1:-1]}")
print(f"Player 2's deck: {str(p2c)[1:-1]}")
winscore = 0
for i in range(len(windeck)):
    winscore += windeck[i] * (len(windeck)-i)

print(f"Winscore: {winscore}")
