from collections import defaultdict
import itertools

grid = defaultdict(lambda:False)

with open("17.txt") as f:
    z = 0
    y = 0
    for line in (l.strip() for l in f):
        x = 0
        for c in line:
            grid[(x,y,z)] = True if c == '#' else False
            x += 1
        y += 1

neighbors = set(itertools.product(range(-1,2), repeat=3))
neighbors.remove((0,0,0))

def print_g(g):
    for z in range(max_z[0], max_z[1] + 1):
        print('z={}'.format(z))
        for y in range(max_y[0], max_y[1] + 1):
            for x in range(max_x[0], max_x[1] + 1):
                print('#' if g[(x,y,z)] else '.', end='')
            print()
    print()

def count_neighbors(g, p):
    return sum( 1 for n in neighbors if g[ (n[0] + p[0], n[1] + p[1], n[2] + p[2]) ] )

max_z = (-1, 1) 
max_y = (-1, y) 
max_x = (-1, x) 

#print_g(grid)

for round in range(0, 6):
    new_grid = grid.copy()
    for z in range(max_z[0], max_z[1] + 1):
        for y in range(max_y[0], max_y[1] + 1):
            for x in range(max_x[0], max_x[1] + 1):
                p = (x,y,z)
                c = count_neighbors(grid, p)
                if grid[p] and c not in [2,3]:
                    new_grid[p] = False
                elif not grid[p] and c == 3:
                    new_grid[p] = True
    grid = new_grid
    max_z = (max_z[0] - 1, max_z[1] + 1)
    max_y = (max_y[0] - 1, max_y[1] + 1)
    max_x = (max_x[0] - 1, max_x[1] + 1)

    #print('round', round + 1)
    #print_g(grid)

tot = sum(1 for v in grid.values() if v)
print('part1', tot)

#204 low