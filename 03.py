from collections import defaultdict

def count_trees(right, down):
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

        while pos[1] < end_y:
            npos = ((pos[0] + right) % end_x, pos[1] + down)
            trees += 1 if grid[npos] else 0
            pos = npos

        return trees

a = count_trees(1, 1)
b = count_trees(3, 1)
c = count_trees(5, 1)
d = count_trees(7, 1)
e = count_trees(1, 2)
print('part1', b)
print('part1', a*b*c*d*e, [a,b,c,d,e])

# 602811400 low