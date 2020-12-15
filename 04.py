import re

h_cmd = re.compile(r'^([0-9]+)(cm|in)$')
c_cmd = re.compile(r'^#[0-9a-f]{6}$')
p_cmd = re.compile(r'^[0-9]{9}$')

def is_valid1(fields):
    return (len(fields) == 8) or (len(fields) == 7 and 'cid' not in fields)

def is_valid2(fields):
    y = int(fields['byr'])
    if y < 1920 or y > 2002: return False
    y = int(fields['iyr'])
    if y < 2010 or y > 2020: return False
    y = int(fields['eyr'])
    if y < 2020 or y > 2030: return False
    m = h_cmd.match(fields['hgt'])
    if m:
        h = int(m.groups(1)[0])
        if m.groups(1)[1] == 'cm' and (h < 150 or h > 193):
            return False
        elif m.groups(1)[1] == 'in' and (h < 59 or h > 76):
            return False
    else:
        return False
    m = c_cmd.match(fields['hcl'])
    if not m: return False
    if fields['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False
    m = p_cmd.match(fields['pid'])
    if not m: return False

    return True

pat_cmd = re.compile(r'^(.{3}):(.+)$')

with open('04.txt') as f:
    valid = 0
    valid2 = 0
    fields = dict()
    for line in (l.strip() for l in f.readlines()):
        if line == '':
            if is_valid1(fields):
                valid += 1
                if is_valid2(fields): valid2 += 1
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

    if is_valid1(fields):
        valid += 1
        if is_valid2(fields): valid2 += 1

    print('part1:', valid)
    print('part2:', valid2)

# 167 low