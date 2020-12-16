
with open("06.txt") as f:
    yes_set = set()
    count = 0
    for line in (l.strip() for l in f):
        if line == '':
            count += len(yes_set)
            yes_set = set()
            continue

        for c in line:
            yes_set.add(c)

    count += len(yes_set)

    print('part1', count)

with open("06.txt") as f:
    yes_sets = []
    count = 0
    for line in (l.strip() for l in f):
        if line == '':
            if len(yes_sets) > 0:
                count += len(yes_sets[0].intersection(*yes_sets[1:]))
            yes_sets.clear()
            continue

        s = set()
        for c in line:
            s.add(c)
        yes_sets.append(s)

    if len(yes_sets) > 0:
        count += len(yes_sets[0].intersection(*yes_sets[1:]))

    print('part2', count)