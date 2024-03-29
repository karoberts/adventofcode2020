from functools import reduce

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open("13.txt") as f:
    f.readline()
    inp = f.readline()
    #inp = '17,x,13,19'
    buses = [-1 if x == 'x' else int(x) for x in inp.split(',')]

    a = [v - i for i, v in enumerate(buses) if v != -1]
    n = [b for b in buses if b != -1]

    #print(a)
    #print(n)

    r = chinese_remainder(n, a)
    print('part2', r)

