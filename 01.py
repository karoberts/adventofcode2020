

with open("01.txt") as f:
    nums = set([int(x) for x in f.readlines()])

    for i in nums:
        alt_i = 2020 - i
        if alt_i in nums:
            print('part1:', i, alt_i, i * alt_i)
            break

    for i in nums:
        for j in nums:
            alt_ij = 2020 - i - j
            if alt_ij in nums:
                print('part2:', i, j, alt_ij, i * j * alt_ij)
                quit()

