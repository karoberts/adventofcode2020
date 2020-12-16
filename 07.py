
import re

rules_re = re.compile(r'^([a-z]+ [a-z]+) bags contain (no other bags|(?:[0-9]+ [a-z]+ [a-z]+ bag[s]?[.,]?[ ]?)+)')
rule_re = re.compile(r'^(no other bags|(?:[0-9]+ [a-z]+ [a-z]+ bag[s]?))')

rules = dict()
gold_bag_carry = []

def recurse(bag, s):
    for carry_bag in rules.keys():
        if bag in rules[carry_bag]:
            #print(carry_bag, 'can hold', bag)
            s.add(carry_bag)
            recurse(carry_bag, s)

with open('07.txt') as f:
    for line in (l.strip() for l in f):
        m = rules_re.findall(line)
        if not m:
            raise 1
        rules[m[0][0]] = dict()
        for r in m[0][1].split(', '):
            m2 = rule_re.match(r)
            if not m2:
                raise 2
            if m2[0] == 'no other bags':
                continue
            sp = m2[0].split(' ')
            n = int(sp[0])
            color = sp[1] + ' ' + sp[2]
            if color == 'shiny gold':
                gold_bag_carry.append(m[0][0])
            rules[m[0][0]][color] = n

#print(rules)
#print(gold_bag_carry)

gbc_set = set()
for bag in gold_bag_carry:
    gbc_set.add(bag)
    recurse(bag, gbc_set)

print(len(gbc_set))