from datetime import datetime

def recurse(adapters, cur_jolts, count1, count3):
    #print('start', cur_jolts, adapters)
    if len(adapters) == 0:
        return (count1, count3 + 1)
    for a in adapters:
        #print('loop', a)
        if a - 3 == cur_jolts or a - 1 == cur_jolts:
            count1_delt = (1 if a - 1 == cur_jolts else 0)
            count3_delt = (1 if a - 3 == cur_jolts else 0)

            new_adapters = adapters.copy()
            new_adapters.remove(a)
            #print('recursing on adapter', cur_jolts, a, new_adapters)
            r = recurse(new_adapters, a, count1 + count1_delt, count3 + count3_delt)
            if r is not None:
                #print('found', r)
                return r

    #print('ret', cur_jolts, adapters)
    return None

def recurse2(adapters, cur_jolts, exp, depth):
    print(' ' * depth, 'start', cur_jolts)
    if cur_jolts + 3 == exp:
        #print('found!')
        return 1
    tot = 0
    for (i, a) in enumerate(adapters):
        if a <= cur_jolts + 3 and a >= cur_jolts + 1:
            #print('loop', a)
            new_adapters = adapters[i:]
            #print('recursing cj=', cur_jolts, 'a=', a, new_adapters)
            tot += recurse2(new_adapters, a, exp, depth + 1)

    if cur_jolts == 0:
        print(tot)
    return tot

def breadth2(adapters, cur_jolts, exp, depth):
    q = [cur_jolts]

    count = 0
    while len(q) > 0:
        c = q.pop()
        if c + 3 == exp:
            count += 1
            if count % 1000000 == 0:
                print(datetime.now(), count, len(q))
            continue
        for i in range(1, 4):
            if c + i in adapters:
                q.append(c + i)

    return count


with open("10.txt") as f:
    adapters = set(int(x) for x in f)

#print(adapters)

ret = recurse(adapters.copy(), 0, 0, 0)
print('part1', ret[0] * ret[1])

exp = max(adapters) + 3
print(exp)
tot = breadth2(adapters, 0, exp, 0)
print('part2', tot)