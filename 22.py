import dllist
from itertools import islice

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

player1_orig = dllist.dllist(player1)
player2_orig = dllist.dllist(player2)

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

def playgame(deck1, deck2, depth=0):

    if depth > 0 and  max(deck1) > max(deck2):
        return 1

    hands = set()
    while deck1.size > 0 and deck2.size > 0:
        s = (tuple(deck1), tuple(deck2))
        if s in hands:
            return 1

        hands.add(s)

        p1 = deck1.popleft()
        p2 = deck2.popleft()

        if deck1.size >= p1 and deck2.size >= p2:
            #print(' ' * depth, 'new game')
            if playgame(dllist.dllist(islice(deck1,p1)), dllist.dllist(islice(deck2,p2)), depth + 1) == 1:
                #print(' ' * depth, 'won by 1')
                deck1.appendright(p1)
                deck1.appendright(p2)
            else:
                #print(' ' * depth, 'won by 2')
                deck2.appendright(p2)
                deck2.appendright(p1)
        else:
            if p1 > p2:
                deck1.appendright(p1)
                deck1.appendright(p2)
            else:
                deck2.appendright(p2)
                deck2.appendright(p1)

    if depth > 0:
        return 1 if deck1.size > 0 else 2
    else:
        return deck1 if deck1.size > 0 else deck2
    
#player1_orig = dllist.dllist([9,2,6,3,1])
#player2_orig = dllist.dllist([5,8,4,7,10])

winner = playgame(player1_orig, player2_orig)
#print(winner)
print('part2', sum(x * (i+1) for i, x in enumerate(reversed(winner))))