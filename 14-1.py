import re
from collections import defaultdict

mem_cmd = re.compile(r'^mem\[([0-9]+)\] = ([0-9]+)$')

def process_val(mask, val):
    thirty_six_bits = 0b111111111111111111111111111111111111
    factor = 0b1
    for c in reversed(mask):
        if c == '0':
            val &= (thirty_six_bits - factor)
        elif c == '1':
            val |= factor
        factor *= 2
    return val
    

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
            memory[addr] = process_val(cur_mask, val)

print('part1', sum(memory.values()))