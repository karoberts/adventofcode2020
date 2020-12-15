from collections import defaultdict

grid = dict()

with open('03.txt') as f:
    x = 0
    y = 0
    end_x = 0
    for line in f.readlines():
        for col in line:
            grid[(x,y)] = col == '#'
            x += 1
        y += 1
        end_x = x - 1
        x = 0

    end_y = y - 1
    trees = 0
    pos = (0, 0) 

    print(end_x, end_y)

    while pos[1] < end_y:
        npos = ((pos[0] + 3) % end_x, pos[1] + 1)
        trees += 1 if grid[npos] else 0
        pos = npos

    print('part1', trees)