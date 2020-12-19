import re

cmd_re = re.compile(r'^(acc|nop|jmp) ([+\-])(\d+)$')

program = []

with open('08.txt') as f:
    for line in (l.strip() for l in f):
        m = cmd_re.match(line)
        program.append( (m.groups()[0], int(m.groups()[2]) * (1 if m.groups()[1] == '+' else -1)) )

executed = set()
pc = 0
acc = 0

while True:
    if pc in executed:
        print('part1', acc)
        break
    executed.add(pc)
    cmd = program[pc]
    if cmd[0] == 'acc':
        acc += cmd[1]
    elif cmd[0] == 'nop':
        pass
    elif cmd[0] == 'jmp':
        pc += cmd[1]
        continue
    pc += 1