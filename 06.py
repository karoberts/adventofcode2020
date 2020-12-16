
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

    print(count)