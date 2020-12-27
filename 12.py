
def manhat_dist(p):
    return abs(p[0]) + abs(p[1])

instructions = []

with open("12.txt") as f:
    for line in (l.strip() for l in f):
        d = line[0]
        a = int(line[1:])
        instructions.append((d, a))

N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

pos = (0, 0)
direc = E

for i in instructions:
    #print(i, pos, direc)
    if i[0] == 'F':
        pos = (pos[0] + direc[0] * i[1], pos[1] + direc[1] * i[1])
    elif i[0] == 'N':
        pos = (pos[0] + N[0] * i[1], pos[1] + N[1] * i[1])
    elif i[0] == 'S':
        pos = (pos[0] + S[0] * i[1], pos[1] + S[1] * i[1])
    elif i[0] == 'E':
        pos = (pos[0] + E[0] * i[1], pos[1] + E[1] * i[1])
    elif i[0] == 'W':
        pos = (pos[0] + W[0] * i[1], pos[1] + W[1] * i[1])
    elif i[0] == 'L':
        deg = i[1]
        while deg > 0:
            if direc == N:
                direc = W
            elif direc == S:
                direc = E
            elif direc == E:
                direc = N
            elif direc == W:
                direc = S
            deg -= 90
    elif i[0] == 'R':
        deg = i[1]
        while deg > 0:
            if direc == N:
                direc = E
            elif direc == S:
                direc = W
            elif direc == E:
                direc = S
            elif direc == W:
                direc = N
            deg -= 90

print('part1', pos, manhat_dist(pos))
