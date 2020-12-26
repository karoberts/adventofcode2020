from collections import defaultdict

def outputgrid(g, xs, ys):
    for y in range(0, ys):
        for x in range(0, xs):
            print(g[(x,y)], end='')
        print()
    print()

def gridval(g, x, y, a, xs, ys):
    while True:
        x += a[0]
        y += a[1]
        if x == -1 or x >= x_size: return '.'
        if y == -1 or y >= y_size: return '.'
        nk = (x,y)
        if g[nk] != '.':
            return g[(x, y)]


grid = defaultdict(lambda:'.')
x_size = 0
y_size = 0

with open("11.txt") as f:
    y = 0
    for line in (l.strip() for l in f):
        x = 0
        for c in line:
            grid[(x,y)] = c
            x += 1
        y += 1

    x_size = x
    y_size = y

adj = [(-1, -1), (0, -1), (1, -1),  (-1, 0), (1, 0),  (-1, 1), (0, 1), (1, 1)]

while True:
    next_grid = grid.copy()
    mods = 0
    for y in range(0, y_size):
        for x in range(0, x_size):
            k = (x,y)
            if grid[k] == 'L':
                if sum(1 for a in adj if gridval(grid, x, y, a, x_size, y_size) == '#') == 0:
                    next_grid[k] = '#'
                    mods += 1
            elif grid[k] == '#':
                if sum(1 for a in adj if gridval(grid, x, y, a, x_size, y_size) == '#') >= 5:
                    next_grid[k] = 'L'
                    mods += 1
    if mods == 0:
        break
    grid = next_grid

occupied = sum(1 for s in grid.values() if s == '#')
print('part1', occupied)

#outputgrid(grid, x_size, y_size)

# 2960 too high