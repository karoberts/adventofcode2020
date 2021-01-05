import re

rules = {}
texts = []
terminals = set()
rule_pat = re.compile(r'^(\d+): ([a-z"\d |]+)$')

with open("19.txt") as f:
    mode = 'RULES'
    for line in (l.strip() for l in f):
        if mode == 'RULES':
            if line == '':
                mode = 'TEXT'
                continue
            m = rule_pat.match(line)
            ms = m.group(2)
            o = ms.split(' ')
            os = [[], None]
            which = 0
            for t in o:
                if t.isdigit():
                    os[which].append(int(t))
                elif t[0] == '"':
                    os[which].append(t[1])
                    terminals.add(int(m.group(1)))
                else:
                    which += 1
                    os[which] = []

            rules[int(m.group(1))] = os
        else:
            texts.append(line)

#print(rules)
#print(terminals)

def process(rid, depth=0):
    if rid in terminals:
        return rules[rid][0][0]
    rulestr = ''
    rule = rules[rid]
    if rule[1] is not None:
        rulestr = '(?:'
    
    r = rule[0]

    #print(' ' * depth, r)
    for item in r:
        if isinstance(item, int):
            rulestr += process(item, depth + 1)

    if rule[1] is not None:
        rulestr += '|'
        r = rule[1]
        #print(' ' * depth, r)
        for item in r:
            if isinstance(item, int):
                rulestr += process(item, depth + 1)
        rulestr += ')'
    return rulestr

processed = set()
s = process(0)

pat = re.compile('^' + s + '$')
ans1 = sum(1 for t in texts if pat.match(t))

print('part1', ans1)

#for r, v in rules.items():
#    print('{}: {}'.format(r,v))

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

s42 = process(42)
s31 = process(31)
pattern = (
    f"^({s42})+"
    "("
    f"({s42}){{1}}({s31}){{1}}|"
    f"({s42}){{2}}({s31}){{2}}|"
    f"({s42}){{3}}({s31}){{3}}|"
    f"({s42}){{4}}({s31}){{4}}"
    ")$"
)
pat = re.compile(pattern)

ans2 = sum(1 for x in texts if pat.match(x))

print('part2', ans2)
