import re

pat_cmd = re.compile(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)$')

with open('02.txt') as f:
    valid = 0
    valid2 = 0
    for line in (l.strip() for l in f):
        m = pat_cmd.match(line)

        min = int(m.group(1))
        max = int(m.group(2))
        let = m.group(3)[0]
        passw = m.group(4)

        #print(min, max, let, passw)

        count_of_let = sum(1 if c == let else 0 for c in passw)
        if count_of_let >= min and count_of_let <= max:
            valid += 1

        first = min
        second = max

        count_of_let2 = (1 if passw[first - 1] == let else 0) + (1 if passw[second - 1] == let else 0)

        if count_of_let2 == 1:
            valid2 += 1

    print('part1:', valid)
    print('part2:', valid2)
