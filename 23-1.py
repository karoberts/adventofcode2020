from dllist import dllist

istr = '389125467'
istr = '123487596'
inp = dllist((int(x) for x in istr))

inp_size = len(inp)
min_cup = min(inp)
max_cup = max(inp)
#inp_map = {v:i for i, v in enumerate(inp)}
inp_nmap = {v:inp.nodeat(i) for i, v in enumerate(inp)}

inp.last.setnext(inp.first)

def get_idx(idx):
    return idx % inp_size

def printit(p, n, c):
    print(f'{p} ', end='')
    for i in range(0, c):
        print(f'{n.value }', end='')
        n = n.next
    print()

cur_node = inp.first
for move in range(0, 100):

    cup1_node = cur_node.next

    cur_node.setnext(cup1_node.next.next.next)

    dest_val = cur_node.value
    while True:
        dest_val -= 1
        if dest_val < min_cup:
            dest_val = max_cup
        if dest_val in [cup1_node.value, cup1_node.next.value, cup1_node.next.next.value]:
            continue
        break

    dest_node = inp_nmap[dest_val]
    next_dest_node = dest_node.next
    dest_node.setnext(cup1_node)
    cup1_node.next.next.setnext(next_dest_node)

    cur_node = cur_node.next

printit('part1', inp_nmap[1].next, inp_size - 1)