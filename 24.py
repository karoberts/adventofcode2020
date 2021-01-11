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

i_limit = [0,0]
j_limit = [0,0]

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

        if pos[0] < i_limit[0]: i_limit[0] = pos[0]
        if pos[0] > i_limit[1]: i_limit[1] = pos[0]
        if pos[1] < j_limit[0]: j_limit[0] = pos[1]
        if pos[1] > j_limit[1]: j_limit[1] = pos[1]

    grid[pos] = not grid[pos]

print('part1', sum(1 for x in grid.values() if x))

def adj_count(g, p):
    return sum(1 for _, x in axial_directions.items() if g[(p[0] + x[0], p[1] + x[1])])

def fill_in(g):
    for i in range(i_limit[0] - 2, i_limit[1] + 3):
        for j in range(j_limit[0] - 2, j_limit[1] + 3):
            _ = g[(i, j)]

for day in range(0, 100):
    fill_in(grid)
    ng = grid.copy()
    for p in list(grid.keys()):
        bc = adj_count(grid, p)
        if grid[p]:
            if bc == 0 or bc > 2:
                ng[p] = False
        else:
            if bc == 2:
                ng[p] = True

        if p[0] < i_limit[0]: i_limit[0] = p[0]
        if p[0] > i_limit[1]: i_limit[1] = p[0]
        if p[1] < j_limit[0]: j_limit[0] = p[1]
        if p[1] > j_limit[1]: j_limit[1] = p[1]

    grid = ng
    #print(f'Day {day+1}: {sum(1 for x in grid.values() if x)}')

print('part2', sum(1 for x in grid.values() if x))