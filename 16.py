import re
from collections import defaultdict

field_pat = re.compile(r'^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$')

fields = {}
nearby = []
yours = None

with open("16.txt") as f:
    mode = 'FIELDS'
    for line in (l.strip() for l in f.readlines()):
        if len(line) == 0: continue

        if mode == 'FIELDS':
            if line == 'your ticket:':
                mode = 'YOURS'
                continue
            
            m = field_pat.match(line)
            fields[m.group(1)] = [ int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)) ]

        elif mode == 'YOURS':
            if line == 'nearby tickets:':
                mode = 'NEARBY'
                continue
            yours = [int(x) for x in line.split(',')]
            continue

        elif mode == 'NEARBY':
            nearby.append( [int(x) for x in line.split(',')] )
            pass

good_tickets = []

tot = 0
for t in nearby:
    #print('t', t)
    good = True
    for tf in t:
        #print('  tf', tf)
        for f in fields.values():
            if (tf >= f[0] and tf <= f[1]) or (tf >= f[2] and tf <= f[3]):
                break
        else:
            good = False
            #print('NO', tf)
            tot += tf
    if good:
        good_tickets.append(t)

print('part1', tot)

good_tickets.append(yours)

field_match = defaultdict(set)

for pos in range(0, len(yours)):
    for name, rule in fields.items():
        if all((ticket[pos] >= rule[0] and ticket[pos] <= rule[1]) or (ticket[pos] >= rule[2] and ticket[pos] <= rule[3]) for ticket in good_tickets):
            #print('matched', name, 'to pos', pos)
            field_match[name].add(pos)

#print(field_match)

pos2field = {}
while len(pos2field) < len(field_match):
    for f, m in field_match.items():
        if f in pos2field:
            continue
        if len(m) == 1:
            p = m.pop()
            #print('confirmed', p, 'is', f)
            pos2field[f] = p
            for s in field_match.values():
                if p in s:
                    s.remove(p)

#print(pos2field)

tot = 1
for f in fields.keys():
    if not f.startswith('departure'): continue
    pos = pos2field[f]
    #print('val', yours[pos])
    tot *= yours[pos]

print('part2', tot)

# high 722862493693
        
