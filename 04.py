import re

pat_cmd = re.compile(r'^(.{3}):(.+)$')

with open('04.txt') as f:
    valid = 0
    fields = dict()
    for line in (l.strip() for l in f.readlines()):
        if line == '':
            if len(fields) == 8:
                valid += 1
            elif len(fields) == 7 and 'cid' not in fields:
                valid += 1
            fields.clear()
            continue

        for val in line.split(' '):
            m = pat_cmd.match(val)
            if not m:
                print('err "{}" "{}"'.format(val, line))

            f = m.groups(1)[0]
            if f not in ['byr', 'iyr', 'eyr', 'hgt', 'hgt', 'hcl', 'ecl', 'pid', 'cid']:
                print('bad field:', f)
                continue

            fields[m.groups(1)[0]] = m.groups(1)[1]

    if len(fields) == 8:
        valid += 1
    elif len(fields) == 7 and 'cid' not in fields:
        valid += 1

    print('part1:', valid)
