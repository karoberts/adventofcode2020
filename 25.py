
# test
card = 5764801
door = 17807724

# real
card = 9717666
door = 20089533

memo_card = {}
memo_door = {}

#tot_loops = 0

def xform(subj, ls, memo = None):
    #global tot_loops

    i_start = 0
    n = subj
    if memo is not None:
        for i in range(ls, 0, -1):
            #tot_loops += 1
            if i in memo:
                n = memo[i]
                i_start = i
                break

    for i in range(i_start, ls):
        n *= subj
        n %= 20201227

        if memo is not None:
            memo[i + 1] = n

    return n

def find_ls(pk, subj, memo=None):
    for loop_size in range(0, 20_000_000):
        """
        if loop_size % 1_000_000 == 0:
            print(loop_size, tot_loops)
        """
        n = xform(subj, loop_size, memo)
        #print(f'ls = {loop_size}, xform = {n}')
        if n == pk:
            return loop_size
    raise Exception(f'not found for {pk}')

card_ls = find_ls(card, 7, memo_card)
door_ls = find_ls(door, 7, memo_door)

print(f'card = {card_ls + 1}, door = {door_ls + 1}')

cipher1 = xform(card, door_ls)
cipher2 = xform(door, card_ls)

print('part1', cipher1)