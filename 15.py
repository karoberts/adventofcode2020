numbers = [6,19,0,5,7,13,1]
#numbers = [0,3,6]

spoken = {k:i+1 for i,k in enumerate(numbers)}
prev_spoken = dict()

#print(spoken)

turn = len(spoken) + 1
last_spoken = numbers[-1]

while True:
    if turn == 2021: break

    #print('Turn {}: last = {}'.format(turn, last_spoken))

    if last_spoken not in spoken:
        spoken[0] = turn
        last_spoken = 0
    elif last_spoken not in prev_spoken:
        prev_spoken[0] = spoken[0]
        spoken[0] = turn
        last_spoken = 0
    else:
        prevprev = prev_spoken[last_spoken]
        prev = spoken[last_spoken]

        last_spoken = prev - prevprev
        if last_spoken not in spoken:
            spoken[last_spoken] = turn
        else:
            prev_spoken[last_spoken] = spoken[last_spoken]
            spoken[last_spoken] = turn

    #print('  spoke', last_spoken)

    turn += 1

print('part1', last_spoken)