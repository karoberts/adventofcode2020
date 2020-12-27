
def manhat_dist(p):
    return abs(int(p.real)) + abs(int(p.imag))

instructions = []

with open("12.txt") as f:
    for line in (l.strip() for l in f):
        d = line[0]
        a = int(line[1:])
        instructions.append((d, a))

pos = 0 + 0j
direc = 1 + 0j # east

for i in instructions:
    #print(i, pos, direc)
    if i[0] == 'F':
        pos += (direc * i[1])
    elif i[0] == 'N':
        pos += complex(0, -i[1])
    elif i[0] == 'S':
        pos += complex(0, i[1])
    elif i[0] == 'E':
        pos += complex(i[1], 0)
    elif i[0] == 'W':
        pos += complex(-i[1], 0)
    elif i[0] == 'L':
        deg = i[1]
        while deg > 0:
            direc *= -1j
            deg -= 90
    elif i[0] == 'R':
        deg = i[1]
        while deg > 0:
            direc *= 1j
            deg -= 90

print('part1', pos, manhat_dist(pos))
