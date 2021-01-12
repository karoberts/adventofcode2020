
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
        if ls not in memo:
            memo[ls] = pow(subj, ls + 1, 20201227)
        i_start = ls
        n = memo[ls]

    for i in range(i_start, ls):
        n *= subj
        n %= 20201227

        if memo is not None:
            memo[i + 1] = n

    return n

def find_ls(pk, subj, memo=None, sthint=0):
    for loop_size in range(sthint, 20_000_000):
        """
        if loop_size % 1_000_000 == 0:
            print(loop_size, tot_loops)
        """
        n = xform(subj, loop_size, memo)
        # this works too, but is slower
        #n = pow(subj, loop_size + 1, 20201227)
        #print(f'ls = {loop_size}, xform = {n}')
        if n == pk:
            return loop_size
    raise Exception(f'not found for {pk}')

memo_card[17_100_000] = pow(7, 17_100_001, 20201227)
memo_door[19_800_000] = pow(7, 19_800_001, 20201227)
card_ls = find_ls(card, 7, memo_card, 17_100_000)
door_ls = find_ls(door, 7, memo_door, 19_800_000)

print(f'card = {card_ls + 1}, door = {door_ls + 1}')

cipher1 = xform(card, door_ls)
cipher2 = xform(door, card_ls)

print('part1', cipher1)