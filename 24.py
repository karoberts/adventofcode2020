from collections import defaultdict

with open('24.txt') as f:
    dirs = [l.strip() for l in f]

"""
https://www.redblobgames.com/grids/hexagons/  <- axial coordinates
https://gamedevelopment.tutsplus.com/tutorials/hexagonal-character-movement-using-axial-coordinates--cms-29035   <- axial manhattan dist
       \ n  /       \0,-1/
     nw +--+ ne -1,0 +--+ 1,-1
       /    \       /    \
     -+      +-   -+      +-
       \    /       \    /
     sw +--+ se -1,1 +--+ 1,0
       / s  \       /0,1 \
"""

def axial_manhat(i,j):
    di=i-0
    dj=j-0
    j -= (i//2)
    si=-1 if di < 0 else 1
    sj=-1 if dj < 0 else 1
    absi=di*si
    absj=dj*sj
    return max(absi, absj) if si != sj else absi + absj

direction_map = {
    'e': 'n', 'w': 's', 'ne': 'nw', 'nw': 'sw', 'se': 'ne', 'sw': 'se'
}

axial_directions = {
    'se':(+1, 0), 'ne':(+1, -1), 'n':(0, -1),
    'nw':(-1, 0), 'sw':(-1, +1), 's':(0, +1)
}

grid = defaultdict(lambda:False)

for seq in dirs:
    pos = (0,0)
    i = 0
    while i < len(seq):
        d = seq[i:i+2]
        if d not in direction_map:
            d = seq[i]

        mapped_dir = direction_map[d]
        delt = axial_directions[mapped_dir]

        i += len(d)

        pos = (pos[0] + delt[0], pos[1] + delt[1])

    grid[pos] = not grid[pos]

print('part1', sum(1 for x in grid.values() if x))