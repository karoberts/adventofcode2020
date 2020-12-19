import re

cmd_re = re.compile(r'^(acc|nop|jmp) ([+\-])(\d+)$')

program = []

with open('08.txt') as f:
    for line in (l.strip() for l in f):
        m = cmd_re.match(line)
        program.append( (m.groups()[0], int(m.groups()[2]) * (1 if m.groups()[1] == '+' else -1)) )

def run_program(prog):
    executed = set()
    pc = 0
    acc = 0

    while pc < len(prog):
        if pc in executed:
            return (True, acc)
        executed.add(pc)
        cmd = prog[pc]
        if cmd[0] == 'acc':
            acc += cmd[1]
        elif cmd[0] == 'nop':
            pass
        elif cmd[0] == 'jmp':
            pc += cmd[1]
            continue
        pc += 1

    return (False, acc)

r = run_program(program)
print('part1', r[1])

for (i, c) in enumerate(program):
    if c[0] == 'acc':
        continue

    new_p = program.copy()
    #print('trying line', i)

    if c[0] == 'nop':
        new_p[i] = ('jmp', c[1])
    elif c[0] == 'jmp':
        new_p[i] = ('nop', c[1])

    #print(new_p)

    r = run_program(new_p)
    if not r[0]:
        print('part2', r[1])
        break
