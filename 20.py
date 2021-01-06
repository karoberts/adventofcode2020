from collections import defaultdict
from itertools import product
from math import sqrt

TILE_W = 10
TILE_H = 10

tiles = defaultdict(dict)

def print_tile(tile,w=TILE_W,h=TILE_H):
    for y in range(0, h):
        for x in range(0, w):
            print(tile[(x,y)], end='')
        print()
    print()

def vflip(tile,w=TILE_W,h=TILE_H):
    new_tile = dict()
    for y in range(0, h):
        for x in range(0, w):
            new_tile[(x, h - y - 1)] = tile[(x,y)]
    return new_tile

def hflip(tile,w=TILE_W,h=TILE_H):
    new_tile = dict()
    for y in range(0, h):
        for x in range(0, w):
            new_tile[(w - x - 1, y)] = tile[(x,y)]
    return new_tile

def rot_left(tile,w=TILE_W,h=TILE_H):
    new_tile = dict()
    for y in range(0, h):
        for x in range(0, w):
            new_tile[(y, -x + w - 1)] = tile[(x,y)]
    return new_tile

def rot_right(tile,w=TILE_W,h=TILE_H):
    new_tile = dict()
    for y in range(0, h):
        for x in range(0, w):
            new_tile[(-y + h - 1, x)] = tile[(x,y)]
    return new_tile

def rot_180(tile,w=TILE_W,h=TILE_H):
    new_tile = dict()
    for y in range(0, h):
        for x in range(0, w):
            new_tile[(-x + w - 1, -y + h - 1)] = tile[(x,y)]
    return new_tile

def match_v_edge(tile1, x, tile2):
    anti_x = TILE_W - x - 1
    for i in range(0, TILE_H):
        if tile1[(x, i)] != tile2[(anti_x, i)]:
            return False
    return True

def match_h_edge(tile1, y, tile2):
    anti_y = TILE_H - y - 1
    for i in range(0, TILE_W):
        if tile1[(i, y)] != tile2[(i, anti_y)]:
            return False
    return True

with open("20.txt") as f:
    tile_id = None
    tile_y = 0
    for line in (l.strip() for l in f):
        if line.startswith('Tile '):
            tile_id = int(line[5:-1])
            tile_y = 0
            continue
        if line == '':
            continue
        tile_x = 0
        for c in line:
            tiles[tile_id][(tile_x, tile_y)] = c
            tile_x += 1
        tile_y += 1


#print( match_h_edge(vflip(tiles[1951]), TILE_H - 1, vflip(tiles[2729])) )
#print( match_v_edge(vflip(tiles[1951]), TILE_W - 1, vflip(tiles[2311])) )

ADJS = [
    (-1, 0, match_v_edge, 0),
    (1, 0, match_v_edge, TILE_W - 1), 
    (0, -1, match_h_edge, 0), 
    (0, 1, match_h_edge, TILE_H - 9)
]

def find_positions(dim, px, py, matches, id_matches):
    for tid, t in tiles.items():
        if tid in id_matches:
            continue
        for orient in range(0, 8):
            try_tile = t
            if orient == 0:
                pass
            elif orient == 1:
                try_tile = vflip(t)
            elif orient == 2:
                try_tile = hflip(t)
            elif orient == 3:
                try_tile = rot_right(t)
            elif orient == 4:
                try_tile = rot_left(t)
            elif orient == 5:
                try_tile = rot_180(t)
            elif orient == 6:
                try_tile = rot_left(vflip(t))
            elif orient == 7:
                try_tile = rot_right(vflip(t))
            
            bad = False
            for a in ADJS:
                c = (px + a[0], py + a[1])
                if c in matches:
                    if not a[2](try_tile, a[3], matches[c]):
                        bad = True
                        break

            if not bad:
                next_matches = matches.copy()
                next_matches[(px, py)] = try_tile
                next_id_matches = id_matches.copy()
                next_id_matches[tid] = (px, py)
                npx = px + 1
                npy = py
                if npx == dim:
                    npx = 0
                    npy = py + 1
                if npy == dim:
                    return (next_id_matches, next_matches)
                x = find_positions(dim, npx, npy, next_matches, next_id_matches)
                if x:
                    return x
    return None

def calc(dim, r):
    prod = 1
    for tid, p in r.items():
        if p in [(0,0), (dim - 1,0), (0,dim - 1), (dim - 1,dim - 1)]:
            prod *= tid
    return prod

dim = int(sqrt(len(tiles)))

r = find_positions(dim, 0, 0, dict(), dict())

#print(r[0])
print('part1', calc(dim, r[0]))

full_image = dict()
fi_y = 0
fi_w = 0
fi_h = 0
for py in range(0,dim):
    for y in range(1, TILE_H-1):
        fi_x = 0
        for px in range(0,dim):
            for x in range(1,TILE_W-1):
                full_image[(fi_x,fi_y)] = r[1][(px,py)][(x,y)]
                fi_x += 1
                fi_w = max(fi_x, fi_w)
        fi_y += 1
        fi_h = max(fi_y, fi_h)

monster = dict()
monster_w = 0
monster_h = 0
with open("20-monster.txt") as f:
    y = 0
    for line in f:
        x = 0
        for c in line[:-1]:
            monster[(x,y)] = c == '#'
            x += 1
            monster_w = max(x, monster_w)
        y += 1
        monster_h = max(y, monster_h)

#img = hflip(rot_right(full_image, fi_w, fi_h),fi_w,fi_h)
#print_tile(full_image,fi_w,fi_h)
#print_tile(img,fi_w,fi_h)

"""
print()
for y in range(0, monster_h):
    for x in range(0, monster_w):
        print('O' if monster[(x,y)] else ' ', end='')
    print()
"""

def match(mon, tile, w, h, mw, mh):
    monster_match = 0
    for y in range(0, h - mh):
        for x in range(0, w - mw):
            found = True
            for my in range(0, mh):
                for mx in range(0, mw):
                    if mon[(mx,my)]:
                        if tile[(x+mx,y+my)] != '#':
                            found = False
                            break
                if not found:
                    break
            if found:
                monster_match += 1
    return monster_match

monster_c = sum(1 for x in monster.values() if x)

roughness = sum(1 for x in full_image.values() if x == '#')

for orient in range(0, 8):
    try_tile = full_image
    if orient == 0:
        pass
    elif orient == 1:
        try_tile = vflip(full_image,fi_w,fi_h)
    elif orient == 2:
        try_tile = hflip(full_image,fi_w,fi_h)
    elif orient == 3:
        try_tile = rot_right(full_image,fi_w,fi_h)
    elif orient == 4:
        try_tile = rot_left(full_image,fi_w,fi_h)
    elif orient == 5:
        try_tile = rot_180(full_image,fi_w,fi_h)
    elif orient == 6:
        try_tile = rot_left(vflip(full_image,fi_w,fi_h),fi_w,fi_h)
    elif orient == 7:
        try_tile = rot_right(vflip(full_image,fi_w,fi_h), fi_w, fi_h)

    r = match(monster, try_tile, fi_w, fi_h, monster_w, monster_h)
    if r > 0:
        print('part2', roughness - r * monster_c)
        break