
preamble = 25

with open("09.txt") as f:
    nums = []
    for i in range(0, preamble):
        nums.append( int(f.readline()) )

    pos = preamble
    for line in (l.strip() for l in f):
        num = int(line)
        nums.append(num)
        num_set = set(i for i in nums[pos-preamble:pos])
        #print('checking', num_set, 'for', num)
        for i in range(pos - preamble, pos):
            if num - nums[i] in num_set and num != nums[i] * 2:
                #print('found', num - nums[i], '+', nums[i])
                break
        else:
            print('part1', num)
            quit()
        pos += 1
