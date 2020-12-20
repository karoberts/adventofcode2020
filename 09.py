
preamble = 25
invalid = -1

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
            invalid = num
            break

        if invalid > 0:
            break
        pos += 1

print('part1', invalid)

for i in range(0, len(nums)):
    i_sum = 0
    for j in range(i, len(nums)):
        i_sum += nums[j]
        if i_sum > invalid:
            break
        elif i_sum == invalid:
            #print('found', i, j, nums[i:j+1])
            min_n = min(nums[i:j+1])
            max_n = max(nums[i:j+1])
            print('part2', min_n + max_n)
            quit()