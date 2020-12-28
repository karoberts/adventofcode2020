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

with open("10.txt") as f:
    adapters = set(int(x) for x in f)

#print(adapters)

ret = recurse(adapters.copy(), 0, 0, 0)
print('part1', ret[0] * ret[1])
