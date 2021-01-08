import re
from collections import defaultdict
from typing import DefaultDict, Set, List

line_pat = re.compile(r'^([a-z ]+) \(contains ([a-z, ]+)\)$')

ings:Set[str] = set()
ings_lines:List[Set[str]] = list()
allergens = defaultdict(list)

with open("21.txt") as f:
    for line in (l.strip() for l in f):
        m = line_pat.match(line)

        i_as = m.group(2).split(', ')
        i_is = set(m.group(1).split(' '))

        for a in i_as:
            allergens[a].append(i_is)

        ings |= i_is
        ings_lines.append(i_is)

def search(allergens,assignments,results):
    if len(allergens) == 0:
        if not any(x == assignments for x in results):
            results.append(assignments)
        return
    for an, a in allergens.items():
        if len(a) == 0: continue
        for i in a:
            new_assignments = assignments.copy()
            new_assignments[an] = i

            new_allergens = dict()
            for k, v in allergens.items():
                if k == an: continue
                if i in v:
                    new_s = v.copy()
                    new_s.remove(i)
                    new_allergens[k] = new_s
                else:
                    new_allergens[k] = v

            search(new_allergens, new_assignments, results)

            
new_allergens = dict()
for an, a in allergens.items():
    #print(an)
    s = set.intersection(*a)
    #print(f'  ! {s}')
    new_allergens[an] = s

rs = list()
search(new_allergens, dict(), rs)
#print(rs)
if len(rs) > 1:
    raise Exception('too many results')

#print(ings)
possibles = ings.copy()
for assi in rs[0].values():
    possibles.remove(assi)

#print(possibles)
c = 0
for ing_line in ings_lines:
    for p in possibles:
        if p in ing_line:
            c += 1

print('part1', c)

vals = list()
for an in sorted(rs[0].keys()):
    vals.append(rs[0][an])

print('part2', ','.join(vals))
