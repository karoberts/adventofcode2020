
def manhat_dist(p):
    return abs(int(p.real)) + abs(int(p.imag))

instructions = []

with open("12.txt") as f:
    for line in (l.strip() for l in f):
        d = line[0]
        a = int(line[1:])
        instructions.append((d, a))

pos = 0 + 0j
waypoint = 10 - 1j

for i in instructions:
    #print(i, pos, waypoint)
    if i[0] == 'F':
        pos += waypoint * i[1]
    elif i[0] == 'N':
        waypoint += complex(0, -i[1])
    elif i[0] == 'S':
        waypoint += complex(0, i[1])
    elif i[0] == 'E':
        waypoint += complex(i[1], 0)
    elif i[0] == 'W':
        waypoint += complex(-i[1], 0)
    elif i[0] == 'L':
        deg = i[1]
        while deg > 0:
            waypoint *= -1j
            deg -= 90
    elif i[0] == 'R':
        deg = i[1]
        while deg > 0:
            waypoint *= 1j
            deg -= 90

print('part2', pos, manhat_dist(pos))
