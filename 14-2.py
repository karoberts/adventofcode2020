import re
from collections import defaultdict

mem_cmd = re.compile(r'^mem\[([0-9]+)\] = ([0-9]+)$')

def process_val(mask, addr, memory, val):
    thirty_six_bits = 0b111111111111111111111111111111111111
    factor = 0b1
    for c in reversed(mask):
        if c == '1':
            addr |= factor
        elif c == 'X':
            pass
        factor *= 2

    floaters = sum(1 for x in mask if x == 'X')

    for i in range(0, 2**floaters):
        new_addr = addr
        factor = 0b1
        floater_factor = 0b1
        for c in reversed(mask):
            if c == 'X':
                #print('setting floater', bin(floater_factor), bin(factor), i, i & floater_factor)
                if i & floater_factor != 0:
                    new_addr |= factor
                else:
                    new_addr &= (thirty_six_bits - factor)
                floater_factor *= 2
            factor *= 2
    
        #print('writing', val, 'to @', new_addr, i, bin(new_addr))
        memory[new_addr] = val
    

with open('14.txt') as f:
    cur_mask = ''
    memory = defaultdict(lambda:0)
    for line in (l.strip() for l in f.readlines()):
        if line.startswith('mask = '):
            cur_mask = line[7:]
        else:
            m = mem_cmd.match(line)
            addr = int(m.group(1))
            val = int(m.group(2))
            process_val(cur_mask, addr, memory, val)

print('part2', sum(memory.values()))