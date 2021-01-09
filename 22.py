import dllist

player1 = dllist.dllist()
player2 = dllist.dllist()

with open("22.txt") as f:
    cur_player = 1
    for line in (l.strip() for l in f):
        if line == "Player 1:" or line == "": continue
        if line == "Player 2:":
            cur_player = 2
            continue
        if cur_player == 1:
            player1.appendright(int(line))
        else:
            player2.appendright(int(line))

#print(f'Round 1')
#print(player1)
#print(player2)

round = 2
while len(player1) > 0 and len(player2) > 0:
    p1 = player1.popleft()
    p2 = player2.popleft()

    if p1 > p2:
        player1.appendright(p1)
        player1.appendright(p2)
    else:
        player2.appendright(p2)
        player2.appendright(p1)

    #print(f'Round {round}')
    #print(player1)
    #print(player2)
    round += 1

winner = player1 if len(player2) == 0 else player2

print('part1', sum(x * (i+1) for i, x in enumerate(reversed(winner))))

