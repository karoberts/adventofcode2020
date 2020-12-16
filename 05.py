
def seat_id(bsp):
    row_min = 0
    row_max = 127
    for c in bsp[:7]:
        mid = (row_max - row_min + 1) // 2 - 1 + row_min
        #print('a', row_min, mid, row_max)
        if c == 'F':
            row_max = mid
        elif c == 'B':
            row_min = mid + 1

    if row_min != row_max:
        print('bad row', bsp, row_min, row_max)
        raise 1
    
    col_min = 0
    col_max = 7
    for c in bsp[7:]:
        mid = (col_max - col_min + 1) // 2 - 1 + col_min
        #print('b', col_min, mid, col_max)
        if c == 'R':
            col_min = mid + 1
        elif c == 'L':
            col_max = mid

    if col_min != col_max:
        print('bad col', bsp, col_min, col_max)
        raise 1

    #print(row_min, col_min, row_min * 8 + col_min)
    return (row_min * 8 + col_min, row_min, col_min)

#seat_id('FBFBBFFRLR')

with open('05.txt') as f:
    seats = [seat_id(l.strip()) for l in f]
    r = max((s[0] for s in seats))
    print('part1', r)

    seatset = set((s[0] for s in seats))
    for i in range(0, r + 1):
        if i in seatset: continue
        if i - 1 in seatset and i + 1 in seatset:
            print('part2', i)
            break
