
class Token:
    def __init__(self, vint:int, vop:str):
        self.intval:int = vint
        self.opval:str = vop
        pass

    def __repr__(self):
        return str(self.intval) if self.intval is not None else self.opval

"""
class Node:
    def __init__(self, a:Element, op:str, b:Element):
        self.a = a
        self.op = op
        self.b = b

    def __repr__(self):
        return '{} {} {}'.format(self.a, self.oper, self.b)
"""

def parse(expr):
    cur_num = ''
    tokens:List[Token] = []
    for c in expr:
        if c.isdigit():
            cur_num += c
        else:
            if len(cur_num) != 0:
                tokens.append(Token(int(cur_num), None))
                cur_num = ''
            if c == ' ':
                continue
            if c in ['+', '*', '(', ')']:
                tokens.append(Token(None, c))
    if len(cur_num) != 0:
        tokens.append(Token(int(cur_num), None))
    return tokens

def eval(tokens,pos,depth=0):
    val = None
    oper = None
    tgt = 0
    p = pos
    while p < len(tokens):
        t = tokens[p]
        if t.intval is not None:
            if val is None:
                val = t.intval
            elif oper == '*':
                #print(depth * ' ', '{} * {}'.format(val, t.intval))
                val *= t.intval
            elif oper == '+':
                #print(depth * ' ', '{} + {}'.format(val, t.intval))
                val += t.intval
        elif t.opval in ['*', '+']:
            oper = t.opval
        elif t.opval == '(':
            #print(depth * ' ', '(')
            if val is None:
                (val, p) = eval(tokens, p + 1, depth + 1)
            elif oper == '*':
                (x, p) = eval(tokens, p + 1, depth + 1)
                #print(depth * ' ', '{} * {}'.format(val, x))
                val *= x
            elif oper == '+':
                (x, p) = eval(tokens, p + 1, depth + 1)
                #print(depth * ' ', '{} + {}'.format(val, x))
                val += x
            #print(depth * ' ', ')')
        elif t.opval == ')':
            return (val, p)
        p += 1
    return (val, len(tokens))
                

expr = '1 + 2 * 3 + 4 * 5 + 6'
expr = '2 * 3 + (4 * 5)'
expr = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
expr = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
expr = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

"""
tokens = parse(expr)
print(tokens)
v = eval(tokens, 0)
print('v', v[0])

quit()
"""

with open("18.txt") as f:
    val = 0
    for line in (l.strip() for l in f):
        val += eval(parse(line), 0)[0]
    print('part1', val)
