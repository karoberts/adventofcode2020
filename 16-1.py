import re

field_pat = re.compile(r'^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)$')

fields = {}
nearby = []

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

        elif mode == 'NEARBY':
            nearby.append( [int(x) for x in line.split(',')] )
            pass

tot = 0
for t in nearby:
    #print('t', t)
    for tf in t:
        #print('  tf', tf)
        for f in fields.values():
            if (tf >= f[0] and tf <= f[1]) or (tf >= f[2] and tf <= f[3]):
                break
        else:
            #print('NO', tf)
            tot += tf

print('part1', tot)
